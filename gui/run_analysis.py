# -*- coding: utf-8 -*-
from pathlib import Path
from pathvalidate import is_valid_filename
import pandas as pd
from PyQt5 import QtWidgets
from backend import worker_main




# MainDialog manages all functions of Graphical User Interface (GUI).
class run_analysis_class:

    def run_analysis_command(self):
        """
        Checks if analysis can be ran; runs the analysis if user inputs are valid.

        This method has three primary functions:
            1)  Check if the 'Exported_Files' folder exists. If not, this
                section creates the folder and emphasizes to the user that all
                future exported files will be found there;
            2)  Check if user inputs are valid;
            3a) Display appropriate error messages (if any); or
            3b) If no errors are found, runs the analysis by passing user
                inputs to a worker thread--this will perform the analysis in
                parellel with the GUI, so that the GUI does not freeze while 
                the analysis is running.
        """
        
        # Catch if column number input errors are present. This must be done
        # here, as errors are reset below.
        temp_col_error = self.temp_col_error.text()
        strain_col_error = self.strain_col_error.text()
        
        # Reset error messages.
        self.reset_error_messages_command()
        # Terminate any currently running worker threads as a precaution.
        self.terminate_worker_command()


        ## Check if any user input errors are present.
        # Check whether the 'Exported_Files' folder (which is used to save all 
        # files exported by this tool) exists or not. If it does not exist, it 
        # will be created and this will be displayed for the user.
        Exported_Files_folder_exists = Path.is_dir(self.path_to_Exported_Files_folder)
        
        # If the 'Exported_Files' folder had to be created, emphasize this to
        # the user and do *not* run the analysis.
        if Exported_Files_folder_exists == False: 
            # Attempt to make 'Exported_Files' folder if one does not exist
            Path.mkdir(self.path_to_Exported_Files_folder)
            # Write message to GUI and creates pop-up
            self.error_message_label.setText("* A new folder named 'Exported_Files' has been created in the same location as this analysis tool. All files exported using this tool will be saved in this folder.")
            QtWidgets.QMessageBox.information(self,
                                              "New folder created",
                                              "A new folder named 'Exported_Files' has been created in the same location as this analysis tool's files--all future files exported using this tool will be saved in this folder. Please run the analysis again.")
        
        
        # Create variable to hold all user input error messages.
        invalid_input_error_message = ''

        # Check for user input errors. If no errors are found, run the analysis.
        if Exported_Files_folder_exists == True:
            # Check if a file has been selected for analysis
            if str(self.filepath) == '.':
                invalid_input_error_message += '• No file selected for analysis.\n'
                self.open_file_button_error.setText(' *')
                self.display_file_name_label_error.setText(' *')

            # Check if different column numbers are entered for temperature and
            # strain data.
            if self.temp_col.value() == self.strain_col.value():
                invalid_input_error_message +=  '• Column numbers for temperature and strain data must be different.\n'
                self.temp_col_error.setText(' *')
                self.strain_col_error.setText(' *')
            # Check if column number inputs are valid (i.e. they do not exceed 
            # the number of columns in the selected file). This is where the 
            # two error messages (which were saved at the very start of this 
            # function) are used.
            else:
                if temp_col_error == ' *' and str(self.filepath) != '.':
                    invalid_input_error_message +=  '• Column number for temperature data exceeds number of (identified) columns in the chosen file.\n'
                    self.temp_col_error.setText(' *')
                if strain_col_error == ' *' and str(self.filepath) != '.':
                    invalid_input_error_message +=  '• Column number for strain data exceeds number of (identified) columns in the chosen file.\n'
                    self.strain_col_error.setText(' *')
    
            # If a custom list of cycles to analyze has been inputted, check 
            # if that list is valid.
            allowed_char = "0123456789,- "
            if self.cycles_to_analyze.currentText() == '[custom]':
                if not all(char in allowed_char for char in self.custom_cycles_to_analyze.text()):
                    invalid_input_error_message += '• Invalid characters entered in custom cycles to analyze.\n'
                    self.custom_cycles_to_analyze_error.setText(' *')
                if self.custom_cycles_to_analyze.text() == '':
                    invalid_input_error_message += '• No cycles entered in custom cycles to analyze.\n'
                    self.custom_cycles_to_analyze_error.setText(' *')
    
            # If a custom file name for exported files has been inputted,
            # check if the custom file name is valid.
            if self.export_file_name.text() != '':
                # Check if file name is valid
                if not(is_valid_filename(self.export_file_name.text())):
                    invalid_input_error_message += '• The file name for your exported data, "' + self.export_file_name.text() + '", is invalid.\n'
                # Check if file name contains a file extension (it should not).
                if '.' in self.export_file_name.text():
                    invalid_input_error_message += '• The file name for your exported data, "' + self.export_file_name.text() + '", contains at least one period ("."). Please remove all periods from the desired file name for exported files.'
                self.export_file_name_error.setText(' *')


            # If any errors are found in the user inputs, create an error
            # message and do *not* run the analysis.
            if invalid_input_error_message != '':
                    self.error_message_label.setText('user input error')
                    QtWidgets.QMessageBox.critical(self,
                                                   "User Input Error",
                                                   invalid_input_error_message)
            # Otherwise, run the analysis.
            else:
                # Upon initiation of the analysis, disable GUI inputs.
                self.lock_inputs_command(True)
                
                # Write progress update to GUI.
                self.analysis_status_progress_label_1.setText('Status:')
                
                # Create dataframe containing all user inputs.
                GUI_inputs = pd.DataFrame(
                                          [{'skip_rows':self.skip_rows.value(),
                                            'temp_col':self.temp_col.value(),
                                            'temp_unit':str(self.temp_unit.currentText()),
                                            'strain_col':self.strain_col.value(),
                                            'strain_unit':str(self.strain_unit.currentText()),
                                            'cycles_to_analyze':str(self.cycles_to_analyze.currentText()),
                                            'custom_cycles_to_analyze':self.custom_cycles_to_analyze.text(),
                                            'export_file_name':self.export_file_name.text(),
                                            'export_file_type':str(self.export_file_type.currentText())}]
                                          )
                
    
    
                # Create a workerThread, which receives the above dataframe of
                # user inputs and runs the analysis in parallel with GUI.
                self.workerThread = worker_main.WorkerThread(GUI_inputs=GUI_inputs,
                                                             path_to_code=self.path_to_code,
                                                             path_to_parent_dir=self.path_to_parent_dir,
                                                             path_to_Exported_Files_folder=self.path_to_Exported_Files_folder,
                                                             filepath=self.filepath)
                self.workerThread.notifyProgress.connect(self.update_progress_command)
                self.workerThread.notifyError.connect(self.error_message_command)
                self.workerThread.finished.connect(self.terminate_worker_command)
                self.workerThread.start()