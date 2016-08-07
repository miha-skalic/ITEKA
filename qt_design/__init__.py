"""
Main window and functions for ITEKA
"""

# windows
from qt_design.main_ui import *
from qt_design.widget_windows import *

import calculations
import qt_design.reaction_plots as reaction_plots
from qt_design.calc_functions import *

import pickle
import sys
import os

import PyQt4.QtCore as qc
QtCore.QLocale.setDefault(QtCore.QLocale('en_US'))


class DefaultWindow(Ui_MainWindow, DsMethods, SsMethods):
    def preload_2subs_data(self, pname):
        """
        Sets up naming and reaction rates
        """
        dlg = PreloadTwoSubs()
        if not (dlg.SetBName.text() and dlg.SetAName.text()):
            WarningMessage(message="You need to name your substrates.")
            return -1
        self.reaction_data = calculations.TwoSubstrates(pname, dlg.SetAName.text(),
                                                        dlg.SetBName.text(),
                                                        is_itc=dlg.IsITC.isChecked(),
                                                        arate=dlg.ASpBox.value(),
                                                        brate=dlg.BSpBox.value())

    def batch_run(self):
        """
        Creates fitting and saves the results
        """

        dlg = BatchRun(self.reaction_data)
        dlg.exec_()

    def load_data(self):
        """
        Choose to load for single or multiple substrates
        """
        if self.reaction_data.is_single():
            self.load_data_ss()

        else:
            self.load_data_ds()
        self.post_load()

    def post_load(self):
        """
        Post data loding changes
        """
        for button in self.GraphBG2.buttons():
            button.show()
        for button in self.GraphBG1.buttons():
                button.show()
        self.Leg1Box.show()
        self.label.show()
        self.label_2.show()
        self.Extrap1.show()
        self.Extrap2.show()

        if self.reaction_data.is_single():
            self.Leg2Box.show()

        MainWindow.setWindowTitle("{} - ITEKA".format(self.reaction_data.name))
        self.changegraph_layout()
        self.BatchButton.setEnabled(True)
        self.SolExpButton.setEnabled(True)
        self.actionSave_input_data.setEnabled(True)
        self.actionExport_data_xls.setEnabled(True)
        self.NewProButton.setEnabled(False)
        self.LoadButton.setEnabled(True)
        self.RewBut.setEnabled(True)

    def start_project(self):
        """
        Project setup
        """
        dlg = StartProject()
        if dlg.exec_() == QtGui.QDialog.Accepted:
            # check for name
            if not dlg.ProjectName.text().strip():
                WarningMessage(message='You need a title for your project.')
                return

            # check for 2 substrates
            if dlg.radioButton_2.isChecked():
                if self.preload_2subs_data(dlg.ProjectName.text().strip()) == -1:
                    return
            else:
                self.reaction_data = calculations.OneSubstrate(dlg.ProjectName.text().strip(),
                                                               cunit=dlg.ConcVal.text(),
                                                               tunit=dlg.TimeVal.text())

            # enable new options
            self.LoadButton.setEnabled(True)
            self.NewProButton.setEnabled(False)

            # setup data object
            self.project_name = dlg.ProjectName.text().strip()
            MainWindow.setWindowTitle("{} - ITEKA".format(self.project_name))

    def reset_project(self):
        """
        Clears current work in project
        """
        if self.reaction_data is None:
            return
        message = 'Your unsaved data will be lost. Continue?'

        msgd = QtGui.QMessageBox
        if msgd.question(None, 'Warning!', message, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No) \
                == QtGui.QMessageBox.No:
            return -1

        MainWindow.setWindowTitle("ITEKA")
        self.fitparams = None
        self.reaction_data = None
        self.project_name = None
        self.NewProButton.setEnabled(True)
        self.LoadButton.setEnabled(False)
        self.BatchButton.setEnabled(False)
        self.SolExpButton.setEnabled(False)

        self.actionSave_input_data.setEnabled(False)
        self.actionExport_data_xls.setEnabled(False)
        self.RewBut.setEnabled(False)

        # flush graphs
        for button in self.GraphBG1.buttons():
            button.hide()
        for button in self.GraphBG2.buttons():
            button.hide()

        self.Leg1Box.hide()
        self.Leg2Box.hide()
        self.label.hide()
        self.label_2.hide()
        self.Extrap1.hide()
        self.Extrap2.hide()
        self.Graph1Sel.setCurrentIndex(0)
        self.Graph2Sel.setCurrentIndex(1)
        self.fig.clear()
        self.canvas.hide()
        self.mpl_toolbar.hide()
        self.Graph1Sel.hide()
        self.Graph2Sel.hide()

    def changegraph_layout(self):
        """
        Change plot buttons display and replot graphs
        """

        # Display
        if (not self.reaction_data.is_single()) and (self.Graph1Sel.currentIndex() in [1, 2]):
            for button in self.GraphBG1.buttons():
                button.setEnabled(True)
            for button in self.GraphBG2.buttons():
                button.setEnabled(True)
        elif not self.reaction_data.is_single():
            for button in self.GraphBG1.buttons():
                button.setEnabled(False)
            for button in self.GraphBG2.buttons():
                button.setEnabled(False)
        else:
            for button in self.GraphBG1.buttons():
                button.setEnabled(self.Graph1Sel.currentIndex() in [1, 2])
            for button in self.GraphBG2.buttons():
                button.setEnabled(self.Graph2Sel.currentIndex() in [1, 2])

        # unchecking
        if self.RepParab1.isChecked():
            self.RepLin1.setChecked(False)
        if self.RepParab2.isChecked():
            self.RepLin2.setChecked(False)
        if self.GlobParab1.isChecked():
            self.GlobLin1.setChecked(False)
        if self.GlobParab2.isChecked():
            self.GlobLin2.setChecked(False)

        # SS and DS difference
        if self.reaction_data.is_single():
            self.plot_basicgraphs()
        else:
            self.plot_basicgraphs2()

    def plot_basicgraphs(self):
        """
        Plots the graphs to be displayed in main window.
        """
        self.fig.clear()

        self.axes = self.fig.add_subplot(121)
        self.axes2 = self.fig.add_subplot(122)

        repfit1 = 1 if self.RepLin1.isChecked() else 2 if self.RepParab1.isChecked() else 0
        repfit2 = 1 if self.RepLin2.isChecked() else 2 if self.RepParab2.isChecked() else 0
        globfit1 = 1 if self.GlobLin1.isChecked() else 2 if self.GlobParab1.isChecked() else 0
        globfit2 = 1 if self.GlobLin2.isChecked() else 2 if self.GlobParab2.isChecked() else 0

        reaction_plots.plot_singlegraph(self.reaction_data, self.axes, self.Graph1Sel.currentIndex(),
                                        legend='Replicate ' if self.Leg1Box.isChecked() else '',
                                        rep_fit=repfit1,
                                        global_fit=globfit1,
                                        extrapolation = self.Extrap1.value())
        reaction_plots.plot_singlegraph(self.reaction_data, self.axes2, self.Graph2Sel.currentIndex(),
                                        legend='Replicate ' if self.Leg2Box.isChecked() else '',
                                        rep_fit=repfit2,
                                        global_fit=globfit2,
                                        extrapolation = self.Extrap2.value())

        # New options
        self.Graph1Sel.show()
        self.Graph2Sel.show()

        # Draw the plots
        self.canvas.draw()
        self.canvas.show()
        self.mpl_toolbar.show()

    def plot_basicgraphs2(self):
        """
        Plotting for two substrates examples!
        """

        self.Graph1Sel.show()
        self.fig.clear()

        repfit1 = 1 if self.RepLin1.isChecked() else 2 if self.RepParab1.isChecked() else 0
        repfit2 = 1 if self.RepLin2.isChecked() else 2 if self.RepParab2.isChecked() else 0
        globfit1 = 1 if self.GlobLin1.isChecked() else 2 if self.GlobParab1.isChecked() else 0
        globfit2 = 1 if self.GlobLin2.isChecked() else 2 if self.GlobParab2.isChecked() else 0

        self.axes = self.fig.add_subplot(121)
        self.axes2 = self.fig.add_subplot(122)
        reaction_plots.plot_singlegraph(self.reaction_data.get_repres(True), self.axes, self.Graph1Sel.currentIndex(),
                                        legend='Set ' if self.Leg1Box.isChecked() else '', rep_fit=repfit1,
                                        global_fit=globfit1, sname=self.reaction_data.nameA,
                                        extrapolation = self.Extrap1.value())

        reaction_plots.plot_singlegraph(self.reaction_data.get_repres(False), self.axes2, self.Graph1Sel.currentIndex(),
                                        legend='Set ' if self.Leg1Box.isChecked() else '', rep_fit=repfit2,
                                        global_fit=globfit2, sname=self.reaction_data.nameB,
                                        extrapolation = self.Extrap2.value())

        # Draw the plots
        self.canvas.draw()
        self.canvas.show()
        self.mpl_toolbar.show()

    def add_ds_dataset(self, vals, name, ds_objc, suba=True):
        vals = [' '.join(nvals) for nvals in vals]
        start = True
        for i in range(0, len(vals), 3):
            if start:
                ds_objc.add_set(vals[i], vals[i + 1], vals[i + 2], setname=name)
                start = False
            else:
                ds_objc.add_rep(vals[i], vals[i + 1], vals[i + 2])
        ds_objc.next_set()

    def read_reaction_data(self, handle):
        name = handle.readline()
        if name == '\n':
            return 'SWITCHSETTO2', None
        name = name.strip()
        if name == '':  # Stream depleted
            return None, None

        vals = []

        for line in handle:
            line = line.strip().split()
            if line == []:
                break  # Handle
            vals.append(line)

        vals = list(map(list, zip(*vals)))
        assert (len(vals) % 3 == 0)

        return vals, name

    def load_from_table(self, load_file):

        with open(load_file, 'r') as hanlde:
            pname = hanlde.readline().strip()
            aname = hanlde.readline().strip()
            bname = hanlde.readline().strip()
            cunit = hanlde.readline().strip()
            tunit = hanlde.readline().strip()

            ds_objc = calculations.TwoSubstrates(pname, aname, bname, tunit=tunit, cunit=cunit)
            if hanlde.readline().strip() != '':
                print("Error, Missformat")

            while True:
                set_vals, set_name = self.read_reaction_data(hanlde)
                if set_vals == None and set_name == None:  # depleted iter
                    break
                elif set_vals == 'SWITCHSETTO2':  # switch substrate roles
                    ds_objc.change_varible()
                    continue
                self.add_ds_dataset(set_vals, set_name, ds_objc)
        self.reaction_data = ds_objc


    def loadtable(self):
        dialog = QtGui.QFileDialog()
        filename = QtGui.QFileDialog.getOpenFileName(dialog, 'Select table file', os.getenv('HOME'))
        if filename:
            self.reset_project()
            self.load_from_table(filename)
            self.post_load()

    def load_from_file(self):
        """
        Loads pickle file
        """
        if self.reset_project() == -1:
            return
        dialog = QtGui.QFileDialog()
        filename = QtGui.QFileDialog.getOpenFileName(dialog, 'Open File', os.getenv('HOME'), 'Pickle (*.pkl)')
        if filename:
            self.reset_project()
            self.reaction_data = pickle.load(open(filename, 'rb'))
            self.post_load()

    def save_to_file(self):
        """
        Saves data pickle
        """
        dialog = QtGui.QFileDialog()
        filename = QtGui.QFileDialog.getSaveFileName(dialog, 'Save File', os.getenv('HOME'), 'Pickle (*.pkl)')
        if filename:
            pickle.dump(self.reaction_data, open(filename, 'wb'))

    def save_to_excel(self):
        """
        Saves data to excel spreadsheet
        """
        if self.reaction_data.is_single():
            if self.reaction_data.get_replicates() == 0:
                WarningMessage(message="You need to imput some data first.")
        dialog = QtGui.QFileDialog()
        filename = QtGui.QFileDialog.getSaveFileName(dialog, 'Save File', os.getenv('HOME'), 'Excel Workbook (*.xlsx)')
        if filename:
            calculations.data_to_xls(self.reaction_data, filename)

    def change_selection(self):
        """
        Switch for button combobox
        """
        if self.RepLin1.isChecked():
            self.RepParab1.setChecked(False)
        if self.RepLin2.isChecked():
            self.RepParab2.setChecked(False)
        if self.GlobLin1.isChecked():
            self.GlobParab1.setChecked(False)
        if self.GlobLin2.isChecked():
            self.GlobParab2.setChecked(False)

    def viewdata(self):
        """
        Window for viewing and delating data points
        """
        dlg = PointsView(self.reaction_data)
        if dlg.exec_():
            self.reaction_data = dlg.reac_data
            self.changegraph_layout()

    def __init__(self):
        Ui_MainWindow.__init__(self)
        self.setupUi(MainWindow)

        # data object inicialization
        self.reaction_data = None
        self.fitparams = None
        self.axes = None
        self.axes2 = None
        self.fitresults = None
        self.project_name = None
        self.savefolder = None

        # matplotlib canvas
        self.fig = Figure()
        self.canvas = FigureCanvas(self.fig)
        self.mpl_toolbar = NavigationToolbar(self.canvas, self.centralwidget)

        self.verticalLayout_2.addWidget(self.canvas)
        self.verticalLayout_2.addWidget(self.mpl_toolbar)
        self.verticalLayout_2.addWidget(self.mpl_toolbar)

        # Hide widgets
        for button in self.GraphBG1.buttons():
            button.hide()
        for button in self.GraphBG2.buttons():
            button.hide()

        self.Leg1Box.hide()
        self.Leg2Box.hide()
        self.Graph1Sel.hide()
        self.Graph2Sel.hide()
        self.mpl_toolbar.hide()
        self.label.hide()
        self.label_2.hide()
        self.Extrap1.hide()
        self.Extrap2.hide()
        self.canvas.hide()
        self.StatusLab.hide()

        # gray out the buttons
        self.LoadButton.setEnabled(False)
        self.SolExpButton.setEnabled(False)
        self.BatchButton.setEnabled(False)
        self.actionSave_input_data.setEnabled(False)
        self.actionExport_data_xls.setEnabled(False)
        self.RewBut.setEnabled(False)

        # connect buttons to process
        self.NewProButton.clicked.connect(self.start_project)
        self.LoadButton.clicked.connect(self.load_data)
        self.BatchButton.clicked.connect(self.batch_run)
        self.SolExpButton.clicked.connect(self.exploresol)
        self.RewBut.clicked.connect(self.viewdata)

        # connect combobox to changes
        self.Graph1Sel.activated.connect(self.changegraph_layout)
        self.Graph2Sel.setCurrentIndex(1)
        self.Graph2Sel.activated.connect(self.changegraph_layout)
        self.GraphBG1.buttonClicked.connect(self.changegraph_layout)
        self.GraphBG2.buttonClicked.connect(self.changegraph_layout)
        for button in [self.RepLin1, self.RepLin2, self.GlobLin1, self.GlobLin2]:
            button.stateChanged.connect(self.change_selection)

        self.Leg1Box.stateChanged.connect(self.changegraph_layout)
        self.Leg2Box.stateChanged.connect(self.changegraph_layout)

        self.Extrap1.valueChanged.connect(self.changegraph_layout)
        self.Extrap2.valueChanged.connect(self.changegraph_layout)

        # Menu triggers
        self.actionNew_project.triggered.connect(self.reset_project)
        self.actionLoad_input_data.triggered.connect(self.load_from_file)
        self.actionSave_input_data.triggered.connect(self.save_to_file)
        self.actionExport_data_xls.triggered.connect(self.save_to_excel)
        self.actionImport_table.triggered.connect(self.loadtable)

app = QtGui.QApplication(sys.argv)
MainWindow = QtGui.QMainWindow()
ui = DefaultWindow()

MainWindow.show()
sys.exit(app.exec_())
