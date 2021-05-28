# -*- coding: utf-8 -*-

class reset_error_messages_class:

    def reset_error_messages_command(self):
        """
        Resets all error messages.
        """

        self.open_file_button_error.setText('')
        self.display_file_name_label_error.setText('')
        self.temp_col_error.setText('')
        self.strain_col_error.setText('')
        self.custom_cycles_to_analyze_error.setText('')
        self.export_file_name_error.setText('')
        self.error_message_label.setText('')
        self.analysis_status_progress_label_1.setText('')
        self.analysis_status_progress_label_2.setText('')