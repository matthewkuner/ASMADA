# -*- coding: utf-8 -*-
import os
from pathlib import Path
from PyQt5.QtWidgets import QFileDialog

class open_dialog_box_class:

    def open_dialog_box_command(self):
        """
        Allows user to go use the file directory to choose a file for analysis.
        """
        
        # Upon selecting a new file, reset the user inputs.
        self.reset_inputs_command()
    

        os.chdir(self.path_to_parent_dir)
    
        # Allow only .txt or .csv files to be selected.
        filt = "Text or CSV files (*.txt *.csv)"
        file_dlg_data = QFileDialog.getOpenFileName(None,
                                                    "Select file for analysis",
                                                    str(self.path_to_parent_dir),
                                                    filter = filt)
    
        # saves filepath for future use
        self.filepath = Path(file_dlg_data[0])
        
        # Extract just filename from filepath.
        file_name = self.filepath.name
        # Display filename on GUI.
        self.display_file_name_label.setText(file_name)
        
        # changes back to directory containing ASMADA_config.ini
        os.chdir(self.path_to_code)
        
        print(str(self.filepath)==".")
        
            
        # Load a preview of the file to the preview table.
        self.preview_data_command()