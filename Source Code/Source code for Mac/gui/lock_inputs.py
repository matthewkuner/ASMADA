# -*- coding: utf-8 -*-

class lock_inputs_class:

    def lock_inputs_command(self, bool_var):
        """
        Locks or unlocks inputs.
        """

        self.run_analysis.setEnabled(not bool_var)
        self.skip_rows.setEnabled(not bool_var)
        self.temp_col.setEnabled(not bool_var)
        self.temp_unit.setEnabled(not bool_var)
        self.strain_col.setEnabled(not bool_var)
        self.strain_unit.setEnabled(not bool_var)
        self.cycles_to_analyze.setEnabled(not bool_var)
        if self.cycles_to_analyze.currentText() == '[custom]':
            self.custom_cycles_to_analyze.setEnabled(not bool_var)
        self.export_file_name.setEnabled(not bool_var)
        self.export_file_type.setEnabled(not bool_var)
        self.display_file_name_label.setEnabled(not bool_var)
        self.open_file_button.setEnabled(not bool_var)
        self.reset_inputs.setEnabled(not bool_var)