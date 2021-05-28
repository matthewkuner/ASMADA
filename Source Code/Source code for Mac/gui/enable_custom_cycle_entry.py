# -*- coding: utf-8 -*-


# MainDialog manages all functions of Graphical User Interface (GUI).
class enable_custom_cycle_entry_class:

    def enable_custom_cycle_entry_command(self, index):
        """
        Enables entry of custom cycles if '[custom]' is chosen in the
        'cycles to analyze' combobox. Otherwise text box is disabled.
        """
        
        if index == 1:
            self.custom_cycles_to_analyze.setEnabled(True)
        else:
            self.custom_cycles_to_analyze.setEnabled(False)
            self.custom_cycles_to_analyze.setText('')