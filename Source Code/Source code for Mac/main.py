# -*- coding: utf-8 -*-
"""
Automatic Shape Memory Alloy Data Analyzer (ASMADA) source code v 1.0.

This code serves to automatically analyze isobaric thermal cycling tests of
Shape Memory Alloys (SMAs) in accordance with ASTM standard E3097-17.

Author and programmer: Matthew Kuner

       e-mails: matthewkuner@gatech.edu
                matthewkuner@gmail.com
                matthewkuner@yahoo.com
        
Main paper: Matthew C. Kuner, Anargyros A. Karakalas, and Dimitris C. Lagoudas
            "ASMADA – A Tool for Automatic Analysis of Shape Memory Alloy 
            Thermal Cycling Data under Constant Stress",
            !!!
            [JOURNAL NAME] (YEAR),
            DOI: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
            !!!


Developed in Python 3.7.3. All packages and versions used in developing this
application can be found in the "requirements.txt" file. These packages
can be easily downloaded by running the following in your command prompt (or
Terminal, etc.):
    $ pip install -r requirements.txt


The ASMADA program is structured as follows:
ASMADA_folder/
│
├── main.py
├── ASMADA_config.ini
├── gui/
│    ├── enable_custom_cycle_entry.py
│    ├── error_message.py
│    ├── lock_inputs.py
│    ├── open_dialog_box.py
│    ├── preview_data.py
│    ├── reset_error_messages.py
│    ├── reset_inputs.py
│    ├── run_analysis.py
│    ├── structure.py       
│    ├── structure.ui    # can be edited in Qt Designer to change GUI layout; not imported/used directly
│    ├── terminate_worker.py
│    └── update_progress.py
├── backend/
│    ├── analyze_data.py
│    ├── export_files.py
│    ├── find_nearest.py
│    ├── find_SPR_tangent_lines.py
│    ├── find_TRR_tangent_line.py
│    ├── initialize_analysis_variables.py
│    ├── initialize_animation.py
│    ├── line_intersection.py
│    ├── make_plot_labels.py
│    ├── make_plot_markers.py
│    ├── make_plots.py
│    ├── modified_sigmoid.py
│    ├── pre_processing.py
│    ├── read_file.py
│    ├── round_to_odd.py
│    └── worker_main.py
├── TAM-LogoBox.ico
├── requirements.txt
└── README
"""

import sys
from PyQt5 import QtWidgets
from gui import gui_main


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('fusion')
    form = gui_main.MainDialog()
    form.show()
    sys.exit(app.exec_())