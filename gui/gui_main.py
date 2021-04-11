# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, QtGui
import gui.structure
import gui.open_dialog_box
import gui.preview_data
import gui.enable_custom_cycle_entry
import gui.run_analysis
import gui.lock_inputs
import gui.update_progress
import gui.error_message
import gui.reset_error_messages
import gui.reset_inputs
import gui.terminate_worker

# MainDialog manages all functions of Graphical User Interface (GUI).
class MainDialog(QtWidgets.QMainWindow, 
                 QtGui.QFont, 
                 gui.structure.Ui_MainWindow,
                 gui.open_dialog_box.open_dialog_box_class,
                 gui.preview_data.preview_data_class,
                 gui.enable_custom_cycle_entry.enable_custom_cycle_entry_class,
                 gui.run_analysis.run_analysis_class,
                 gui.lock_inputs.lock_inputs_class,
                 gui.update_progress.update_progress_class,
                 gui.error_message.error_message_class,
                 gui.reset_error_messages.reset_error_messages_class,
                 gui.reset_inputs.reset_inputs_class,
                 gui.terminate_worker.terminate_worker_class):
    """
    Interact with Graphical User Interface (GUI), providing it with
    functionality.

    This allows the user to*:
        1) select a file for analysis,
        2) input which columns contain the temperature and strain data,
        3) specify the temperature and strain units used,
        4) specify which cycles they want analyzed,
        5) input a custom file name for the exported files,
        6) initiate the analysis,
        7) display progress of the analysis, and
        8) display errors in the user inputs/other miscellaneous errors/
           pop-ups.
    * these functions do not (necessarily) correspond to individual functions
    within the "MainDialog" class.
    """

    def __init__(self, parent=None):
        """
        Creates connection between buttons/spinboxes/textboxes/etc. to the
        functions within the MainDialog class.
        """
        
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)

        self.open_file_button.clicked.connect(lambda: self.open_dialog_box_command())
        self.skip_rows.valueChanged.connect(self.preview_data_command)
        self.temp_col.valueChanged.connect(self.preview_data_command)
        self.strain_col.valueChanged.connect(self.preview_data_command)
        self.temp_unit.currentIndexChanged.connect(self.preview_data_command)
        self.strain_unit.currentIndexChanged.connect(self.preview_data_command)
        # Adjust the appearance of the dropdown menu for strain units (this 
        # saves space on the GUI).
        combo_view = QtWidgets.QListView()
        combo_view.setFixedWidth(81)        
        self.strain_unit.setView(combo_view)
        font = QtGui.QFont('MS Shell Dlg 2', 10)
        self.strain_unit.setFont(font)
        self.cycles_to_analyze.currentIndexChanged.connect(self.enable_custom_cycle_entry_command)
        self.reset_inputs.clicked.connect(self.reset_inputs_command)
        self.run_analysis.clicked.connect(self.run_analysis_command)
        self.stop_analysis.clicked.connect(self.terminate_worker_command)
        self.stop_analysis.clicked.connect(self.analysis_terminated_message_command)
        self.stop_analysis.setEnabled(False)


    def closeEvent(self, event):
        self.terminate_worker_command()