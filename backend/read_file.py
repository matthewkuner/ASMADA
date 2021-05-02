# -*- coding: utf-8 -*-
import pandas as pd

class read_file_class:

    def read_file(self):
        """
        Reads the user's file according to four user inputs below:
            1) the selected filepath;
            2) the number of header rows to skip;
            3) the column number for the temperature data; and
            4) the column number for the strain data.


        Parameters
        ----------
        self.GUI_inputs : pandas DataFrame
            Contains all user inputs.
        self.filepath : Pathlib object
            Contains path to user-selected file.

        Returns
        -------
        df_raw_data : pandas DataFrame
            Contains raw temperature and strain data from the file.
        """

        # Write progress update to GUI.
        self.notifyProgress.emit('reading raw data')    

        # Extract user inputs defining how to read file.
        skip_rows = self.GUI_inputs.skip_rows.values[0]
        temp_data_col = self.GUI_inputs.temp_col.values[0] - 1
        strain_data_col = self.GUI_inputs.strain_col.values[0] - 1

        # Assign temperature/strain column names appropriately.
        if temp_data_col < strain_data_col:
            raw_data_col_names = ['temp', 'strain']
        else:
            raw_data_col_names = ['strain', 'temp']

        # Read in the full file using the user's inputs.
        df_raw_data = pd.read_csv(self.filepath,
                                  sep=None,
                                  header=None,
                                  skiprows=skip_rows,
                                  usecols=[temp_data_col, strain_data_col],
                                  names=raw_data_col_names,
                                  skip_blank_lines=True,
                                  encoding='utf-8',
                                  engine='python')


        # Convert all values into numeric values--convert strings into NaN.
        df_raw_data[df_raw_data.columns] = df_raw_data[df_raw_data.columns].apply(pd.to_numeric, errors='coerce', axis = 0)
        # Drop NaN values.
        df_raw_data = df_raw_data.dropna(axis='rows')


        # Rearrange columns to have 'temp' column first and 'strain' column
        # second.
        if raw_data_col_names == ['strain', 'temp']:
            df_raw_data = df_raw_data[['temp','strain']]




        return df_raw_data


