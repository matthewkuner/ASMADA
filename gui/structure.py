# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Automatic_Fatigue_Analysis_GUI_4_19_2021.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1135, 940)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1135, 940))
        MainWindow.setMaximumSize(QtCore.QSize(1135, 940))
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("TAM-LogoBox.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, -1, 1135, 940))
        self.tabWidget.setMaximumSize(QtCore.QSize(16777213, 16777215))
        self.tabWidget.setObjectName("tabWidget")
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(30, 530, 141, 31))
        self.label_7.setToolTip("")
        self.label_7.setStatusTip("")
        self.label_7.setObjectName("label_7")
        self.label_34 = QtWidgets.QLabel(self.widget)
        self.label_34.setGeometry(QtCore.QRect(30, 470, 1071, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.label_29 = QtWidgets.QLabel(self.widget)
        self.label_29.setGeometry(QtCore.QRect(30, 650, 511, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.open_file_button = QtWidgets.QPushButton(self.widget)
        self.open_file_button.setGeometry(QtCore.QRect(240, 70, 211, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.open_file_button.setFont(font)
        self.open_file_button.setObjectName("open_file_button")
        self.reset_inputs = QtWidgets.QPushButton(self.widget)
        self.reset_inputs.setGeometry(QtCore.QRect(940, 680, 141, 81))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.reset_inputs.setFont(font)
        self.reset_inputs.setObjectName("reset_inputs")
        self.cycles_to_analyze = QtWidgets.QComboBox(self.widget)
        self.cycles_to_analyze.setGeometry(QtCore.QRect(170, 530, 151, 31))
        self.cycles_to_analyze.setToolTip("")
        self.cycles_to_analyze.setStatusTip("")
        self.cycles_to_analyze.setObjectName("cycles_to_analyze")
        self.cycles_to_analyze.addItem("")
        self.cycles_to_analyze.addItem("")
        self.line_3 = QtWidgets.QFrame(self.widget)
        self.line_3.setGeometry(QtCore.QRect(10, 440, 1110, 21))
        self.line_3.setLineWidth(2)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_30 = QtWidgets.QLabel(self.widget)
        self.label_30.setGeometry(QtCore.QRect(420, 530, 341, 31))
        self.label_30.setObjectName("label_30")
        self.custom_cycles_to_analyze = QtWidgets.QLineEdit(self.widget)
        self.custom_cycles_to_analyze.setEnabled(False)
        self.custom_cycles_to_analyze.setGeometry(QtCore.QRect(770, 530, 331, 31))
        self.custom_cycles_to_analyze.setToolTip("")
        self.custom_cycles_to_analyze.setStatusTip("")
        self.custom_cycles_to_analyze.setText("")
        self.custom_cycles_to_analyze.setObjectName("custom_cycles_to_analyze")
        self.label_35 = QtWidgets.QLabel(self.widget)
        self.label_35.setGeometry(QtCore.QRect(30, 10, 1071, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_35.setFont(font)
        self.label_35.setObjectName("label_35")
        self.run_analysis = QtWidgets.QPushButton(self.widget)
        self.run_analysis.setGeometry(QtCore.QRect(620, 680, 141, 81))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.run_analysis.setFont(font)
        self.run_analysis.setObjectName("run_analysis")
        self.label_33 = QtWidgets.QLabel(self.widget)
        self.label_33.setGeometry(QtCore.QRect(40, 598, 1061, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_33.setFont(font)
        self.label_33.setAcceptDrops(False)
        self.label_33.setWordWrap(True)
        self.label_33.setObjectName("label_33")
        self.label_32 = QtWidgets.QLabel(self.widget)
        self.label_32.setGeometry(QtCore.QRect(30, 580, 1071, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_32.setFont(font)
        self.label_32.setAcceptDrops(False)
        self.label_32.setWordWrap(True)
        self.label_32.setObjectName("label_32")
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setGeometry(QtCore.QRect(560, 628, 20, 263))
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_11 = QtWidgets.QLabel(self.widget)
        self.label_11.setGeometry(QtCore.QRect(30, 710, 181, 31))
        self.label_11.setToolTip("")
        self.label_11.setStatusTip("")
        self.label_11.setObjectName("label_11")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(30, 220, 231, 31))
        self.label_5.setObjectName("label_5")
        self.line_2 = QtWidgets.QFrame(self.widget)
        self.line_2.setGeometry(QtCore.QRect(10, 620, 1110, 21))
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(30, 70, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setStatusTip("")
        self.label_3.setObjectName("label_3")
        self.display_file_name_label = QtWidgets.QLabel(self.widget)
        self.display_file_name_label.setGeometry(QtCore.QRect(520, 70, 581, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.display_file_name_label.setFont(font)
        self.display_file_name_label.setStatusTip("")
        self.display_file_name_label.setAutoFillBackground(True)
        self.display_file_name_label.setText("")
        self.display_file_name_label.setIndent(5)
        self.display_file_name_label.setObjectName("display_file_name_label")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(30, 270, 231, 31))
        self.label_6.setObjectName("label_6")
        self.export_file_name = QtWidgets.QLineEdit(self.widget)
        self.export_file_name.setGeometry(QtCore.QRect(220, 710, 311, 31))
        self.export_file_name.setStatusTip("")
        self.export_file_name.setObjectName("export_file_name")
        self.label_37 = QtWidgets.QLabel(self.widget)
        self.label_37.setGeometry(QtCore.QRect(20, 810, 511, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_37.setFont(font)
        self.label_37.setAcceptDrops(False)
        self.label_37.setWordWrap(True)
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.widget)
        self.label_38.setGeometry(QtCore.QRect(30, 830, 501, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_38.setFont(font)
        self.label_38.setAcceptDrops(False)
        self.label_38.setWordWrap(True)
        self.label_38.setObjectName("label_38")
        self.analysis_status_progress_label_2 = QtWidgets.QLabel(self.widget)
        self.analysis_status_progress_label_2.setGeometry(QtCore.QRect(750, 780, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.analysis_status_progress_label_2.setFont(font)
        self.analysis_status_progress_label_2.setStatusTip("")
        self.analysis_status_progress_label_2.setAutoFillBackground(True)
        self.analysis_status_progress_label_2.setText("")
        self.analysis_status_progress_label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.analysis_status_progress_label_2.setObjectName("analysis_status_progress_label_2")
        self.analysis_status_progress_label_1 = QtWidgets.QLabel(self.widget)
        self.analysis_status_progress_label_1.setGeometry(QtCore.QRect(620, 780, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.analysis_status_progress_label_1.setFont(font)
        self.analysis_status_progress_label_1.setStatusTip("")
        self.analysis_status_progress_label_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.analysis_status_progress_label_1.setAutoFillBackground(True)
        self.analysis_status_progress_label_1.setText("")
        self.analysis_status_progress_label_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.analysis_status_progress_label_1.setObjectName("analysis_status_progress_label_1")
        self.preview_table = QtWidgets.QTableWidget(self.widget)
        self.preview_table.setEnabled(True)
        self.preview_table.setGeometry(QtCore.QRect(520, 125, 581, 277))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preview_table.sizePolicy().hasHeightForWidth())
        self.preview_table.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.preview_table.setFont(font)
        self.preview_table.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.preview_table.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.preview_table.setFrameShadow(QtWidgets.QFrame.Plain)
        self.preview_table.setLineWidth(1)
        self.preview_table.setMidLineWidth(0)
        self.preview_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.preview_table.setAutoScrollMargin(16)
        self.preview_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.preview_table.setTabKeyNavigation(False)
        self.preview_table.setProperty("showDropIndicator", False)
        self.preview_table.setDragDropOverwriteMode(False)
        self.preview_table.setAlternatingRowColors(False)
        self.preview_table.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.preview_table.setShowGrid(True)
        self.preview_table.setGridStyle(QtCore.Qt.SolidLine)
        self.preview_table.setWordWrap(False)
        self.preview_table.setCornerButtonEnabled(True)
        self.preview_table.setRowCount(500)
        self.preview_table.setColumnCount(2)
        self.preview_table.setObjectName("preview_table")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.preview_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.preview_table.setHorizontalHeaderItem(1, item)
        self.preview_table.horizontalHeader().setCascadingSectionResizes(False)
        self.preview_table.horizontalHeader().setDefaultSectionSize(125)
        self.preview_table.horizontalHeader().setHighlightSections(False)
        self.preview_table.horizontalHeader().setMinimumSectionSize(125)
        self.preview_table.horizontalHeader().setSortIndicatorShown(False)
        self.preview_table.horizontalHeader().setStretchLastSection(False)
        self.preview_table.verticalHeader().setVisible(True)
        self.preview_table.verticalHeader().setDefaultSectionSize(25)
        self.preview_table.verticalHeader().setHighlightSections(False)
        self.preview_table.verticalHeader().setMinimumSectionSize(20)
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setGeometry(QtCore.QRect(30, 760, 401, 31))
        self.label_9.setObjectName("label_9")
        self.export_file_type = QtWidgets.QComboBox(self.widget)
        self.export_file_type.setGeometry(QtCore.QRect(440, 760, 91, 31))
        self.export_file_type.setObjectName("export_file_type")
        self.export_file_type.addItem("")
        self.export_file_type.addItem("")
        self.export_file_type.addItem("")
        self.strain_col = QtWidgets.QSpinBox(self.widget)
        self.strain_col.setEnabled(True)
        self.strain_col.setGeometry(QtCore.QRect(290, 270, 61, 31))
        self.strain_col.setPrefix("")
        self.strain_col.setMinimum(1)
        self.strain_col.setMaximum(999)
        self.strain_col.setObjectName("strain_col")
        self.temp_col = QtWidgets.QSpinBox(self.widget)
        self.temp_col.setGeometry(QtCore.QRect(290, 220, 61, 31))
        self.temp_col.setPrefix("")
        self.temp_col.setMinimum(1)
        self.temp_col.setMaximum(999)
        self.temp_col.setObjectName("temp_col")
        self.error_message_label = QtWidgets.QLabel(self.widget)
        self.error_message_label.setGeometry(QtCore.QRect(620, 820, 461, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.error_message_label.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.error_message_label.setFont(font)
        self.error_message_label.setToolTip("")
        self.error_message_label.setStatusTip("")
        self.error_message_label.setAutoFillBackground(False)
        self.error_message_label.setText("")
        self.error_message_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.error_message_label.setWordWrap(True)
        self.error_message_label.setObjectName("error_message_label")
        self.open_file_button_error = QtWidgets.QLabel(self.widget)
        self.open_file_button_error.setGeometry(QtCore.QRect(450, 70, 31, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.open_file_button_error.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.open_file_button_error.setFont(font)
        self.open_file_button_error.setToolTip("")
        self.open_file_button_error.setStatusTip("")
        self.open_file_button_error.setAutoFillBackground(False)
        self.open_file_button_error.setText("")
        self.open_file_button_error.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.open_file_button_error.setWordWrap(True)
        self.open_file_button_error.setObjectName("open_file_button_error")
        self.custom_cycles_to_analyze_error = QtWidgets.QLabel(self.widget)
        self.custom_cycles_to_analyze_error.setGeometry(QtCore.QRect(1100, 530, 31, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.custom_cycles_to_analyze_error.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.custom_cycles_to_analyze_error.setFont(font)
        self.custom_cycles_to_analyze_error.setToolTip("")
        self.custom_cycles_to_analyze_error.setStatusTip("")
        self.custom_cycles_to_analyze_error.setAutoFillBackground(False)
        self.custom_cycles_to_analyze_error.setText("")
        self.custom_cycles_to_analyze_error.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.custom_cycles_to_analyze_error.setWordWrap(True)
        self.custom_cycles_to_analyze_error.setObjectName("custom_cycles_to_analyze_error")
        self.export_file_name_error = QtWidgets.QLabel(self.widget)
        self.export_file_name_error.setGeometry(QtCore.QRect(530, 710, 31, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.export_file_name_error.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.export_file_name_error.setFont(font)
        self.export_file_name_error.setAcceptDrops(False)
        self.export_file_name_error.setToolTip("")
        self.export_file_name_error.setStatusTip("")
        self.export_file_name_error.setAutoFillBackground(False)
        self.export_file_name_error.setText("")
        self.export_file_name_error.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.export_file_name_error.setWordWrap(True)
        self.export_file_name_error.setObjectName("export_file_name_error")
        self.display_file_name_label_error = QtWidgets.QLabel(self.widget)
        self.display_file_name_label_error.setGeometry(QtCore.QRect(1100, 70, 31, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.display_file_name_label_error.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.display_file_name_label_error.setFont(font)
        self.display_file_name_label_error.setToolTip("")
        self.display_file_name_label_error.setStatusTip("")
        self.display_file_name_label_error.setAutoFillBackground(False)
        self.display_file_name_label_error.setText("")
        self.display_file_name_label_error.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.display_file_name_label_error.setWordWrap(True)
        self.display_file_name_label_error.setObjectName("display_file_name_label_error")
        self.temp_col_error = QtWidgets.QLabel(self.widget)
        self.temp_col_error.setGeometry(QtCore.QRect(350, 220, 21, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.temp_col_error.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.temp_col_error.setFont(font)
        self.temp_col_error.setToolTip("")
        self.temp_col_error.setStatusTip("")
        self.temp_col_error.setAutoFillBackground(False)
        self.temp_col_error.setText("")
        self.temp_col_error.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.temp_col_error.setWordWrap(True)
        self.temp_col_error.setObjectName("temp_col_error")
        self.strain_col_error = QtWidgets.QLabel(self.widget)
        self.strain_col_error.setGeometry(QtCore.QRect(350, 270, 21, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.strain_col_error.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.strain_col_error.setFont(font)
        self.strain_col_error.setToolTip("")
        self.strain_col_error.setStatusTip("")
        self.strain_col_error.setAutoFillBackground(False)
        self.strain_col_error.setText("")
        self.strain_col_error.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.strain_col_error.setWordWrap(True)
        self.strain_col_error.setObjectName("strain_col_error")
        self.label_47 = QtWidgets.QLabel(self.widget)
        self.label_47.setGeometry(QtCore.QRect(330, 520, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_47.setFont(font)
        self.label_47.setObjectName("label_47")
        self.label_44 = QtWidgets.QLabel(self.widget)
        self.label_44.setGeometry(QtCore.QRect(20, 400, 431, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_44.setFont(font)
        self.label_44.setAcceptDrops(False)
        self.label_44.setWordWrap(True)
        self.label_44.setObjectName("label_44")
        self.label_36 = QtWidgets.QLabel(self.widget)
        self.label_36.setGeometry(QtCore.QRect(30, 418, 391, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_36.setFont(font)
        self.label_36.setAcceptDrops(False)
        self.label_36.setWordWrap(True)
        self.label_36.setObjectName("label_36")
        self.label_39 = QtWidgets.QLabel(self.widget)
        self.label_39.setGeometry(QtCore.QRect(30, 368, 421, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_39.setFont(font)
        self.label_39.setAcceptDrops(False)
        self.label_39.setWordWrap(True)
        self.label_39.setObjectName("label_39")
        self.label_45 = QtWidgets.QLabel(self.widget)
        self.label_45.setGeometry(QtCore.QRect(20, 350, 431, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_45.setFont(font)
        self.label_45.setAcceptDrops(False)
        self.label_45.setWordWrap(True)
        self.label_45.setObjectName("label_45")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(920, 413, 26, 26))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("background-color:rgb(0, 185, 80)")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(630, 413, 26, 26))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 16777210))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("background-color:rgb(240, 228, 50)")
        self.label_2.setObjectName("label_2")
        self.label_17 = QtWidgets.QLabel(self.widget)
        self.label_17.setGeometry(QtCore.QRect(800, 413, 26, 26))
        self.label_17.setAutoFillBackground(False)
        self.label_17.setStyleSheet("background-color:rgb(86, 200, 233)")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.widget)
        self.label_18.setGeometry(QtCore.QRect(660, 409, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.widget)
        self.label_19.setGeometry(QtCore.QRect(830, 409, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.widget)
        self.label_20.setGeometry(QtCore.QRect(950, 409, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.stop_analysis = QtWidgets.QPushButton(self.widget)
        self.stop_analysis.setEnabled(False)
        self.stop_analysis.setGeometry(QtCore.QRect(780, 680, 141, 81))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.stop_analysis.setFont(font)
        self.stop_analysis.setObjectName("stop_analysis")
        self.skip_rows = QtWidgets.QSpinBox(self.widget)
        self.skip_rows.setGeometry(QtCore.QRect(290, 170, 61, 31))
        self.skip_rows.setPrefix("")
        self.skip_rows.setMinimum(0)
        self.skip_rows.setMaximum(999)
        self.skip_rows.setProperty("value", 0)
        self.skip_rows.setObjectName("skip_rows")
        self.label_10 = QtWidgets.QLabel(self.widget)
        self.label_10.setGeometry(QtCore.QRect(30, 170, 231, 31))
        self.label_10.setObjectName("label_10")
        self.temp_unit = QtWidgets.QComboBox(self.widget)
        self.temp_unit.setGeometry(QtCore.QRect(380, 220, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.temp_unit.setFont(font)
        self.temp_unit.setToolTip("")
        self.temp_unit.setStatusTip("")
        self.temp_unit.setObjectName("temp_unit")
        self.temp_unit.addItem("")
        self.temp_unit.addItem("")
        self.temp_unit.addItem("")
        self.strain_unit = QtWidgets.QComboBox(self.widget)
        self.strain_unit.setGeometry(QtCore.QRect(380, 270, 61, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.strain_unit.sizePolicy().hasHeightForWidth())
        self.strain_unit.setSizePolicy(sizePolicy)
        self.strain_unit.setToolTip("")
        self.strain_unit.setStatusTip("")
        self.strain_unit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.strain_unit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.strain_unit.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.strain_unit.setObjectName("strain_unit")
        self.strain_unit.addItem("")
        self.strain_unit.addItem("")
        self.label_13 = QtWidgets.QLabel(self.widget)
        self.label_13.setGeometry(QtCore.QRect(380, 170, 61, 31))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.widget)
        self.label_14.setGeometry(QtCore.QRect(28, 92, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.label_7.raise_()
        self.label_34.raise_()
        self.label_29.raise_()
        self.open_file_button.raise_()
        self.reset_inputs.raise_()
        self.cycles_to_analyze.raise_()
        self.line_3.raise_()
        self.label_30.raise_()
        self.custom_cycles_to_analyze.raise_()
        self.label_35.raise_()
        self.run_analysis.raise_()
        self.label_33.raise_()
        self.label_32.raise_()
        self.label_11.raise_()
        self.label_5.raise_()
        self.line_2.raise_()
        self.label_3.raise_()
        self.display_file_name_label.raise_()
        self.label_6.raise_()
        self.export_file_name.raise_()
        self.label_37.raise_()
        self.label_38.raise_()
        self.analysis_status_progress_label_2.raise_()
        self.analysis_status_progress_label_1.raise_()
        self.preview_table.raise_()
        self.label_9.raise_()
        self.export_file_type.raise_()
        self.strain_col.raise_()
        self.temp_col.raise_()
        self.error_message_label.raise_()
        self.open_file_button_error.raise_()
        self.custom_cycles_to_analyze_error.raise_()
        self.export_file_name_error.raise_()
        self.display_file_name_label_error.raise_()
        self.temp_col_error.raise_()
        self.strain_col_error.raise_()
        self.label_47.raise_()
        self.label_44.raise_()
        self.label_36.raise_()
        self.label_39.raise_()
        self.label_45.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_17.raise_()
        self.label_18.raise_()
        self.label_19.raise_()
        self.label_20.raise_()
        self.stop_analysis.raise_()
        self.skip_rows.raise_()
        self.label_10.raise_()
        self.temp_unit.raise_()
        self.strain_unit.raise_()
        self.label_13.raise_()
        self.line.raise_()
        self.label_14.raise_()
        self.tabWidget.addTab(self.widget, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Automatic Shape Memory Alloy Data Analyzer (ASMADA)"))
        self.label_7.setText(_translate("MainWindow", "Cycles to analyze:"))
        self.label_34.setText(_translate("MainWindow", "Data Processing"))
        self.label_29.setText(_translate("MainWindow", "Exporting Analyzed Data"))
        self.open_file_button.setText(_translate("MainWindow", "Open File"))
        self.reset_inputs.setText(_translate("MainWindow", "Reset Inputs"))
        self.cycles_to_analyze.setItemText(0, _translate("MainWindow", "all cycles"))
        self.cycles_to_analyze.setItemText(1, _translate("MainWindow", "[custom]"))
        self.label_30.setText(_translate("MainWindow", "<html><head/><body><p>if &quot;[custom]&quot; is chosen, enter desired cycles<span style=\" font-weight:600; vertical-align:super;\">3</span>:</p></body></html>"))
        self.custom_cycles_to_analyze.setPlaceholderText(_translate("MainWindow", "1-25,100,1000,5000"))
        self.label_35.setText(_translate("MainWindow", "Interpreting Raw Data"))
        self.run_analysis.setText(_translate("MainWindow", "Run Analysis"))
        self.label_33.setText(_translate("MainWindow", " \"1-25,100,1000,5000\"     will make the program analyze cycles 1 through 25, cycle 100, cycle 1000, and cycle 5000."))
        self.label_32.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; vertical-align:super;\">3</span> Enter a list of individual cycles or cycles ranges to analyze. Separate each item in the list with a comma. Ranges can be specified using a hyphen. For example, entering</p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p>(optional) File name<span style=\" font-weight:600; vertical-align:super;\">4</span>:</p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p>Column for Temperature data:</p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p>Select a file to analyze:</p></body></html>"))
        self.display_file_name_label.setToolTip(_translate("MainWindow", "The name of the selected file will appear here"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p>Column for Strain data<span style=\" font-weight:600; vertical-align:super;\">2</span>:</p></body></html>"))
        self.export_file_name.setToolTip(_translate("MainWindow", "Insert a valid file name. Do not include a file extension (e.g. \'.csv\')"))
        self.label_37.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; vertical-align:super;\">4</span> If nothing is entered, files will be exported using the file name of the inputted raw data</p></body></html>"))
        self.label_38.setText(_translate("MainWindow", "raw data file with descriptors appended after it (e.g. if the file \"my_raw_data\" is inputted, one of the outputted files will be \"my_raw_data_analyzed\")."))
        self.analysis_status_progress_label_2.setToolTip(_translate("MainWindow", "Shows status of in-progress analysis"))
        self.analysis_status_progress_label_1.setToolTip(_translate("MainWindow", "Shows status of in-progress analysis"))
        self.preview_table.setToolTip(_translate("MainWindow", "Useful for visualizing which columns contain the appropriate data"))
        self.preview_table.setSortingEnabled(False)
        item = self.preview_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Temperature"))
        item = self.preview_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Strain"))
        self.label_9.setText(_translate("MainWindow", "File type for exported material parameters:"))
        self.export_file_type.setItemText(0, _translate("MainWindow", ".csv"))
        self.export_file_type.setItemText(1, _translate("MainWindow", ".txt"))
        self.export_file_type.setItemText(2, _translate("MainWindow", ".xlsx"))
        self.label_47.setText(_translate("MainWindow", "  →"))
        self.label_44.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; vertical-align:super;\">2</span> If selected file contains displacement values, these must be converted to</p></body></html>"))
        self.label_36.setText(_translate("MainWindow", "strain externally."))
        self.label_39.setText(_translate("MainWindow", "using this input, consider converting the file to another format."))
        self.label_45.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; vertical-align:super;\">1</span> If selected file does not display properly after removing the header rows</p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_18.setText(_translate("MainWindow", "Temperature"))
        self.label_19.setText(_translate("MainWindow", "Strain"))
        self.label_20.setText(_translate("MainWindow", "Both"))
        self.stop_analysis.setText(_translate("MainWindow", "Stop Analysis"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p>Header rows to skip<span style=\" font-weight:600; vertical-align:super;\">1</span>:</p></body></html>"))
        self.temp_unit.setItemText(0, _translate("MainWindow", "[°C]"))
        self.temp_unit.setItemText(1, _translate("MainWindow", "[K]"))
        self.temp_unit.setItemText(2, _translate("MainWindow", "[°F]"))
        self.strain_unit.setItemText(0, _translate("MainWindow", "[%]"))
        self.strain_unit.setItemText(1, _translate("MainWindow", "[fraction]"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p>row(s)</p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p>(.csv or .txt only)</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), _translate("MainWindow", "Main"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Read Me / Help"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
