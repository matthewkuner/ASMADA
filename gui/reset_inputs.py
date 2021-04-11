# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets


class reset_inputs_class:

    def reset_inputs_command(self):
        """
        Resets all inputs.
        """
        
        self.display_file_name_label.setText('')
        self.skip_rows.setValue(0)
        self.temp_col.setValue(1)
        self.temp_unit.setCurrentIndex(0)
        self.strain_col.setValue(1)
        self.strain_unit.setCurrentIndex(0)
        self.cycles_to_analyze.setCurrentIndex(0)
        self.custom_cycles_to_analyze.setText('')
        self.export_file_name.setText('')
        self.export_file_type.setCurrentIndex(0)
        self.display_file_name_label.setText('')
        self.analysis_status_progress_label_1.setText('')
        self.analysis_status_progress_label_2.setText('')

        # Reset table to only two columns.
        self.preview_table.setColumnCount(2)
        # Reset column header text.
        self.preview_table.setHorizontalHeaderLabels(['Temperature', 'Strain'])

        # Reset all values in the table.
        for i in range(999):
            for j in range(2):
                item = ''
                self.preview_table.setItem(i, j, QtWidgets.QTableWidgetItem(item))

        # Reset error messages as well.
        self.reset_error_messages_command()