# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets


class error_message_class:

    def error_message_command(self, text):
        """
        Displays errors on GUI.
        """

        # Only write error message if it is the first error encountered
        if self.error_message_label.text() == '':
            
            self.analysis_status_progress_label_2.setText('error')            

            if text == 'error reading file selected for analysis':
                self.error_message_label.setText("* Unknown error encountered while reading file selected for analysis.")
                QtWidgets.QMessageBox.critical(self,
                                               "Error reading file selected for analysis",
                                               "Unknown error encountered while reading file selected for analysis. Please check that the correct file and temperature/strain columns were selected.")

            if text == 'error pre-procesing':
                self.error_message_label.setText("* Unknown error encountered during pre-processing.")
                QtWidgets.QMessageBox.critical(self,
                                               "Error during pre-processing",
                                               "Unknown error encountered while pre-processing the file selected for analysis. Please check that the correct file and temperature/strain columns were selected.")

            if text == 'error plotting of all cycles together':
                self.error_message_label.setText("* Unknown error encountered while plotting all cycles together.")
                QtWidgets.QMessageBox.critical(self,
                                               "Error while plotting all cycles together",
                                               "Unknown error encountered while plotting all cycles together in the temperature-strain domain. Please check that the correct file and temperature/strain columns were selected. Though unlikely, this may also be caused by the selected file being too large--if your file is over 1 GB in size, consider analyzing the file in sections.")

            if text == 'error analyzing data':
                self.error_message_label.setText("* Unknown error encountered during data analysis.")
                QtWidgets.QMessageBox.critical(self,
                                               "Error during data analysis",
                                               "Unknown error encountered while analyzing the selected file. Please check that the correct file and temperature/strain columns were selected.")

            if text == 'error plotting evolution of material properties':
                self.error_message_label.setText("* Unknown error encountered while plotting the evolution of material properties.")
                QtWidgets.QMessageBox.critical(self,
                                               "Error while plotting the evolution of material properties",
                                               "Unknown error encountered while plotting the evolution of material properties. Please check that the correct file and temperature/strain columns were selected.")
            
            if text == 'error exporting files':
                self.error_message_label.setText("* Unknown error encountered while exporting files.")
                QtWidgets.QMessageBox.critical(self,
                                               "Error while exporting files",
                                               "Unknown error encountered while exporting files. Please check that you have valid permissions to write files on this computer user/computer.")