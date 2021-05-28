# -*- coding: utf-8 -*-
import pandas as pd
from PyQt5 import QtWidgets, QtGui

# MainDialog manages all functions of Graphical User Interface (GUI).
class preview_data_class:

    def preview_data_command(self):
        """
        Displays preview of how the user's file is read by this code.
        """

        self.reset_error_messages_command()

        try:
            # Extract user inputs regarding how to read the selected file.
            skip_rows = self.skip_rows.value()
            temp_data_col = self.temp_col.value() - 1
            strain_data_col = self.strain_col.value() - 1

            # Read in the first 500 rows of the selected file.
            df_raw_data = pd.read_csv(self.filepath,
                                      sep=None,
                                      header=None,
                                      skiprows=skip_rows,
                                      nrows=500,
                                      encoding='utf-8',
                                      engine='python')

            # Create column names for preview table (default name is 
            # 'ignored').
            raw_data_col_names = ['[ignored ' + str(x) + ']' for x in range(len(df_raw_data.columns) + 1)][1:]

            # Identify if the entered temp/strain column numbers exceed
            # the size of the selected file. If this is the case, an error
            # is raised.
            if temp_data_col >= len(df_raw_data.columns) or strain_data_col >= len(df_raw_data.columns):
                if temp_data_col >= len(df_raw_data.columns):
                    self.temp_col_error.setText(' *')    
                if strain_data_col >= len(df_raw_data.columns):
                    self.strain_col_error.setText(' *')
                raise Exception('column number inputted exceeds number of columns in file')
                

            # Assign header labels to the temperature and strain columns 
            # (if column numbers are different).
            if temp_data_col != strain_data_col:
                raw_data_col_names[temp_data_col] = 'Temperature' + ' ' + str(self.temp_unit.currentText())
                raw_data_col_names[strain_data_col] = 'Strain' + ' ' + str(self.strain_unit.currentText())

            # Set column count of the preview table to match size of file.
            self.preview_table.setColumnCount(len(df_raw_data.columns))
            
            # Set column headers of the preview table.
            self.preview_table.setHorizontalHeaderLabels(raw_data_col_names)
            # Set all column headers bold.
            boldfont = QtGui.QFont()
            boldfont.setFamily("MS Shell Dlg 2")
            boldfont.setPointSize(8)
            boldfont.setBold(True)
            for col_num in range(len(df_raw_data.columns)):
                self.preview_table.horizontalHeaderItem(col_num).setFont(boldfont)
                

            # Input the first 500 rows of data into preview_table.
            for i in range(len(df_raw_data.index)):
                for j in range(len(df_raw_data.columns)):
                    # Convert numeric value to string (where applicable).
                    try:
                        item = QtWidgets.QTableWidgetItem('{:.3f}'.format(df_raw_data.iloc[i, j]))
                    except:
                        # If no item is present in the cell, simply create a blank item.
                        item = QtWidgets.QTableWidgetItem(df_raw_data.iloc[i, j])

                    # Highlight temperature and strain columns. If the same
                    # column number is entered for both, that column is
                    # highlighted in green. If not, Temperature is yellow,
                    # and Strain is blue.
                    if j in [temp_data_col, strain_data_col]:
                        if temp_data_col == strain_data_col:
                            item.setBackground(QtGui.QColor(0, 185, 80))
                        elif j == temp_data_col:
                            item.setBackground(QtGui.QColor(240, 228, 50))
                        elif j == strain_data_col:
                            item.setBackground(QtGui.QColor(86, 200, 233))

                    # Insert item object into cell.
                    self.preview_table.setItem(i, j, item)

        except Exception as e:
            # If error was raised, assign appropriate error to display.
            invalid_input_error_message = ''
            if str(e) == 'column number inputted exceeds number of columns in file':
                invalid_input_error_message = '• Column number inputted exceeds number of columns in file.'
            else:
                invalid_input_error_message = '• Unknown error'
            QtWidgets.QMessageBox.warning(self,
                                           "User Input Error",
                                           invalid_input_error_message)
            self.error_message_label.setText('user input error')