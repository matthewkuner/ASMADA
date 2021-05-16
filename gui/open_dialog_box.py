# -*- coding: utf-8 -*-
import os
from pathlib import Path
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from configparser import ConfigParser

class open_dialog_box_class:

    def open_dialog_box_command(self):
        """
        Allows user to go use the file directory to choose a file for analysis.
        """
        
        # Upon selecting a new file, reset the user inputs.
        self.reset_inputs_command()
    

        #####os.chdir(self.path_to_parent_dir)
        
        config = ConfigParser()
        config.read('ASMADA_config.ini')
        path_to_last_file_selected = config['paths']['path_to_last_file_selected']
        if Path.is_dir(Path(path_to_last_file_selected)) == True:
            open_dialog_start_path = path_to_last_file_selected
        else:
            open_dialog_start_path = str(self.path_to_parent_dir)
        
    
        # Allow only .txt or .csv files to be selected.
        filt = "Text or CSV files (*.txt *.csv)"
        file_dlg_data = QFileDialog.getOpenFileName(None,
                                                    "Select file for analysis",
                                                    open_dialog_start_path,
                                                    filter = filt)
    
        # saves filepath for future use
        self.filepath = Path(file_dlg_data[0])
        
        # Extract just filename from filepath.
        file_name = self.filepath.name
        # Display filename on GUI.
        self.display_file_name_label.setText(file_name)
        
        print(self.filepath)
        print(self.filepath.parent)
        
        if str(self.filepath) != '.':
            # sets filepath within ASMADA_config.ini
            config.set('paths', 'path_to_last_file_selected', str(self.filepath.parent))
            # re-saves ASMADA_config.ini
            with open('ASMADA_config.ini', 'w') as configfile:
                config.write(configfile)
        
        
        
        
        # changes back to directory containing ASMADA_config.ini
        os.chdir(self.path_to_code)
        
        if str(self.filepath) == '.':
                self.open_file_button_error.setText(' *')
                self.display_file_name_label_error.setText(' *')
                self.error_message_label.setText('user input error')
                QtWidgets.QMessageBox.warning(self,
                                           "User Input Error",
                                           '• No file selected for analysis.\n')
        else:
            # Load a preview of the file to the preview table.
            self.preview_data_command()