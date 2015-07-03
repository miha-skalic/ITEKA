"""
Holds methods for single and Double substrate reactions
"""

import calculations
from qt_design.add_data import *
from qt_design.widget_windows import *
import copy


class LoadData(QtGui.QDialog, Ui_AddData):
    """
    Single substrate load data window
    """

    def __init__(self, data_store, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.setWindowTitle('Data input')

        self.temp_storage = copy.deepcopy(data_store)
        self.pushButton.clicked.connect(self.add_submisions)
        self.pushButton_2.clicked.connect(self.accept)
        self.CancelButton.clicked.connect(self.reject)
        self.rep_count.setText(str(self.temp_storage.replicates))

        self.label.setText('Substrate concentrations (in {}):'.format(self.temp_storage.cunit))
        self.label_2.setText('Reaction Rates (in {}):'.format(self.temp_storage.runit))

    def add_submisions(self):
        """
        Read fields and append replicates
        """
        concentrations = self.plainTextEdit.toPlainText()
        rates = self.plainTextEdit_2.toPlainText()

        self.plainTextEdit_2.setPlainText('')

        try:
            self.temp_storage.add_replicate(concentrations, rates)
        except AssertionError:
            WarningMessage("Dimension mismatch. Can't add the replicate.")
        except ValueError:
            WarningMessage("Import failed. Make sure points are represented by"
                           " numbers separated by space, comma or tab.")
        self.rep_count.setText(str(self.temp_storage.replicates))


class DsMethods(object):
    """
    Methods for double substrate
    """
    def __init__(self):
        self.reaction_data = None

    def load_data_ds(self):
        """
        Load data for two substrates
        """
        dlg = LoadDataDs(self.reaction_data)
        if dlg.exec_():
            self.reaction_data = dlg.subdata


class SsMethods(object):
    def __init__(self):
        self.reaction_data = None

    def load_data_ss(self):
        """
        Load the data to project
        """
        dlg = LoadData(self.reaction_data)
        if dlg.exec_():
            self.reaction_data = dlg.temp_storage

        else:
            print('Loading data canceled')
        print('You have {} replicates in your project'.format(self.reaction_data.replicates))

    def exploresol(self):
        """
        Explore possible solutions of your equation
        """
        dlg = ExploreSolutions(self.reaction_data, self.fitresults)
        dlg.exec_()