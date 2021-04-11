# -*- coding: utf-8 -*-
import os
from pathlib import Path
from configparser import ConfigParser
from PyQt5.QtWidgets import QFileDialog

class open_dialog_box_class:

    def open_dialog_box_command(self):
        """
        Allows user to go use the file directory to choose a file for analysis.
        """
        
        # Upon selecting a new file, reset the user inputs.
        self.reset_inputs_command()
    
        config = ConfigParser()
        config.read('ASMADA_config.ini')
        path_to_parent_dir = config['paths']['path_to_parent_dir']
        path_to_code = config['paths']['path_to_code']
        os.chdir(path_to_parent_dir)
    
        # Allow only .txt or .csv files to be selected.
        filt = "Text or CSV files (*.txt *.csv)"
        file_dlg_data = QFileDialog.getOpenFileName(None,
                                                    "Select file for analysis",
                                                    str(path_to_parent_dir),
                                                    filter = filt)
    
        filepath = Path(file_dlg_data[0])
        
        # Extract just filename from filepath.
        file_name = filepath.name
        # Display filename on GUI.
        self.display_file_name_label.setText(file_name)
        
        # changes back to directory containing ASMADA_config.ini
        os.chdir(path_to_code)
        
        # sets filepath within ASMADA_config.ini
        config.set('paths', 'filepath', str(filepath))
        
        # re-saves ASMADA_config.ini
        with open('ASMADA_config.ini', 'w') as configfile:
            config.write(configfile)
            
        # Load a preview of the file to the preview table.
        self.preview_data_command()