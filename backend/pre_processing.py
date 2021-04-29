# -*- coding: utf-8 -*-
import numpy as np
from scipy.signal import find_peaks

class pre_processing_class:
    
    def pre_processing(self, GUI_inputs, df_raw_data):
        """
        Performs the following functions:
            1)  Identify cycles in the file using the 'find_peaks' method
                from the 'scipy.signal' package;
            2)  Remove all cycles that were not specified by the user for
                analysis.


        Parameters
        ----------
        GUI_inputs : pandas DataFrame
            Contains all user inputs.
        df_raw_data : pandas DataFrame
            contains raw temperature and strain data (cycles are not yet
            identified).

        Returns
        -------
        df_raw_data : pandas DataFrame
            Now has cycle number appended as a new column.
        cycles_to_analyze : list
            Contains list of cycles to analyze as specified by the user.
        tot_num_cyc : int
            Total number of cycles in the file.
        """

        # Write progress update to GUI.
        self.notifyProgress.emit('pre-processing')


        # Initialize argument variables for find_peak function.
        min_peak_height = df_raw_data['temp'].mean()
        # Arbitrarily assume all fatigue files have at least 25 data 
        # points per cycle.
        min_dist_between_peaks = 25
        # The prominence variable is particularly crucial for identifying
        # cycles in the data--look up "peak prominence".
        min_peak_prominence = round(df_raw_data['temp'].std())
        # Use the 'find_peaks' method to find the indices of the peaks.
        new_cycle_inds = find_peaks(df_raw_data['temp'],
                                    height=min_peak_height,
                                    prominence=min_peak_prominence,
                                    distance=min_dist_between_peaks)
        new_cycle_inds = np.asarray(new_cycle_inds)[0]


        # If the file only contains one cycle, set 'new_cycle_inds'
        # variable to be a one-long numpy array containing the last point 
        # in the data file.
        if new_cycle_inds.size == 0:
            new_cycle_inds = np.array([len(df_raw_data.index) - 1])

        # If file is large, remove first 3 rows of data (as they are
        # likely remnants of the test setup).
        if new_cycle_inds.size > 20:
            new_cycle_inds[0] = new_cycle_inds[0] + 3


        num_rows_in_file = df_raw_data['temp'].to_numpy().size

        # Initialize array of cycle numbers that will eventually be 
        # appended to df_raw_data.
        cycle_numbers_to_append = np.empty([0, 0], dtype=int)

        # Initialize cur_cyc_num variable, which will be appended to the
        # necessary number of rows for each respective cycle.
        cur_cycle_num = 0

        for x in range(new_cycle_inds.size):
            # Mark rows of data that occur before the first identified 
            # peak as cycle '0'.
            if x == 0:
                cycle_numbers_to_append = np.append(cycle_numbers_to_append,
                                                    np.full((1, new_cycle_inds[x]),
                                                            cur_cycle_num,
                                                            dtype=int))

            # Increment the cur_cyc_num variable.
            cur_cycle_num = cur_cycle_num + 1
            # Mark all intermediate rows (e.g. after the first cycle, and
            # before the last cycle) of data appropriately.
            if x < new_cycle_inds.size - 1:
                cycle_numbers_to_append = np.append(cycle_numbers_to_append,
                                                    np.full((1,new_cycle_inds[x+1] - new_cycle_inds[x]),
                                                            cur_cycle_num,
                                                            dtype=int))

            # Mark all rows of data that occur after the final identified 
            # peak as cycle the number of the last cycle.
            elif x == new_cycle_inds.size - 1:
                cycle_numbers_to_append = np.append(cycle_numbers_to_append,
                                                    np.full((1,num_rows_in_file - new_cycle_inds[x]),
                                                            cur_cycle_num,
                                                            dtype=int))



        # Concatenate cycle dataframe with df_raw_data.
        df_raw_data.insert(0,'cycle', cycle_numbers_to_append)
        # Drop all rows with all NaN values.
        df_raw_data = df_raw_data.dropna(axis='rows')




        # Find total number of cycles
        tot_num_cyc = new_cycle_inds.size
        print('total cycles: ' + str(tot_num_cyc))

        # Create a list of cycles to analyze, dependent on both the user 
        # input and the total number of cycles in the file.
        if GUI_inputs.cycles_to_analyze.values[0] == 'all cycles':
            # If file contains only one cycle, analyze that single cycle.
            if tot_num_cyc == 1:
                cycles_to_analyze = [0]
            # If file contains a small number of cycles (but more than 
            # one), analyze the zeroth and final cycle as well.
            elif tot_num_cyc < 50:
                cycles_to_analyze = [*range(0,tot_num_cyc+1)]
            # If the file contains a large number of cycles, exclude the
            # zeroth and final cycle from the analysis.
            else:
                cycles_to_analyze = [*range(1,tot_num_cyc)]

        elif GUI_inputs.cycles_to_analyze.values[0] == '[custom]':
            custom_cycles_to_analyze = GUI_inputs.custom_cycles_to_analyze.values[0]
            # If a custom list of cycles are specified, all spaces are
            # removed from the list. Then, the list is split using commas
            # and each item is interpreted.
            custom_cycles_to_analyze = custom_cycles_to_analyze.replace(' ','')
            custom_cycles_to_analyze = custom_cycles_to_analyze.split(',')
            cycles_to_analyze = []
            for s in range(len(custom_cycles_to_analyze)):
                cur_vals = custom_cycles_to_analyze[s]
                # If a hyphen is included in the current item, the item is
                # split using the hyphen character, and a range is created
                # between the first and last value.
                if '-' in cur_vals:
                    cur_vals = cur_vals.split('-')
                    first_val = int(cur_vals[0])
                    last_val = int(cur_vals[-1])
                    cur_vals = [*range(first_val,last_val+1)]
                    cycles_to_analyze = cycles_to_analyze + cur_vals

                # Otherwise, the item list is a singular value and is
                # simply appended to the list of cycles to analyze.
                else:
                    cur_vals = [int(cur_vals)]
                    cycles_to_analyze = cycles_to_analyze + cur_vals


            # Sort the list of cycles to analyze, in case user inputted
            # cycles out of order.
            cycles_to_analyze.sort()

            # Remove any cycle numbers less than 0 or greater than the
            # total number of cycles.
            cycles_to_analyze = [i for i in cycles_to_analyze if i <= tot_num_cyc]
            cycles_to_analyze = [i for i in cycles_to_analyze if i >= 0]


        # Reduce size of df_raw_data to only include the cyles that the 
        # user specifies for analysis.
        df_raw_data = df_raw_data.loc[df_raw_data.cycle.isin(cycles_to_analyze)]

        print('total cycles being analyzed: ' + str(len(cycles_to_analyze)))




        return df_raw_data, cycles_to_analyze, tot_num_cyc