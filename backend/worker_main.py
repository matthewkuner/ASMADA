# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import time
from PyQt5 import QtCore
import backend.read_file
import backend.pre_processing
import backend.analyze_data
import backend.make_plots
import backend.export_files

# WorkerThread manages all aspects of analysis.
class WorkerThread(QtCore.QThread, 
                   backend.read_file.read_file_class, 
                   backend.pre_processing.pre_processing_class, 
                   backend.analyze_data.analyze_data_class,
                   backend.make_plots.make_plots_class,
                   backend.export_files.export_files_class):
    """
    Creates worker thread that can run the analysis in parallel to the GUI
    processes. This is done so that the GUI does not freeze while the analysis
    is running.
    """

    # Create a signal/slot pair that allows this worker thread to interact
    # with the GUI. This is used for receiving user inputs; it is also used
    # to display progress updates/errors during the analysis on the GUI.
    notifyProgress = QtCore.pyqtSignal(object)
    notifyError = QtCore.pyqtSignal(object)
    finished = QtCore.pyqtSignal()




    def __init__(self, GUI_inputs, parent=None):
        
        super(WorkerThread, self).__init__(parent)
        self.GUI_inputs = GUI_inputs




    def run(self):
        """
        Analyzes inputted isobaric thermal cycling data.
        """

        print('Analysis Start')

        # For those who wish to edit the source code, an analysis timer is used.
        start = time.perf_counter()            


        GUI_inputs = self.GUI_inputs


        # Initialize list to capture error messages.
        error = []
        
        # Perform each step of the analysis, one-by-one. If an error is
        # encountered during a particular step, all remaining steps are not
        # executed.
        
        # Read file.
        if len(error) == 0:
            try:
                df_raw_data = self.read_file(GUI_inputs)
            except Exception as e:     # Write error message to GUI.
                self.notifyError.emit('error reading file selected for analysis')
                error.append(e)

        # Pre-processing.
        if len(error) == 0:
            try:
                df_raw_data, cycles_to_analyze, tot_num_cyc = self.pre_processing(GUI_inputs, df_raw_data)
            except Exception as e:     # Write error message to GUI.
                self.notifyError.emit('error pre-procesing')
                error.append(e)

        # Analyze data.
        if len(error) == 0:
            try:
                df_material_parameters, df_smoothed_data, im_animation = self.analyze_data(GUI_inputs, df_raw_data, tot_num_cyc, cycles_to_analyze)
            except Exception as e:     # Write error message to GUI.
                self.notifyError.emit('error analyzing data')
                error.append(e)

        # Make plots.
        if len(error) == 0:
            try:
                fig_all_cycle, fig_temps_separate, fig_temps_all, fig_strains_separate, fig_strains_all, fig_transform_strain, fig_hysteresis, fig_UCT_LCT, fig_coef_thermal_expan = self.make_plots(GUI_inputs, df_material_parameters, df_smoothed_data, cycles_to_analyze, tot_num_cyc)
            except Exception as e:     # Write error message to GUI.
                self.notifyError.emit('error plotting evolution of material properties')
                error.append(e)

        # Export files.
        if len(error) == 0:
            try:
                self.export_files(GUI_inputs, cycles_to_analyze, df_material_parameters, im_animation, fig_all_cycle, fig_temps_separate, fig_temps_all, fig_strains_separate, fig_strains_all, fig_transform_strain, fig_hysteresis, fig_UCT_LCT, fig_coef_thermal_expan)
            except Exception as e:     # Write error message to GUI.
                self.notifyError.emit('error exporting files')
                error.append(e)


        # Print out the first error encountered. Helpful for those who wish to
        # edit the code.
        if len(error) > 0:
            print(error[0])
        else:
            # Write progress update to GUI.
            self.notifyProgress.emit('complete')

        # Close all plots.
        plt.close('all')
        
        
        # Helpful for those who wish to edit the code.
        finish = time.perf_counter()
        print('true cycles analyzed per second: ' + str(len(cycles_to_analyze)/(finish-start)))
        print('Complete')
        
        
        self.finished.emit()
        
        
        
        
    def stop(self):
        """
        Terminates WorkerThread.
        """
        
        self.terminate()