from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from copy import deepcopy
import numpy as np

from qt_design.start_dial import *
from qt_design.fit_setup import *
from qt_design.dataview import *
from qt_design.twosubstr.preload2subs import *
from qt_design.twosubstr.load_data_ds import *
from qt_design.solutionexplorer import *
from qt_design.batch import *
import qt_design.reaction_plots as reaction_plots
import calculations
import os


class StartProject(QtGui.QDialog, Ui_start_dial):
    """
    Window for project setup
    """
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.setWindowTitle("Project information")
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)


class FitSetup(QtGui.QDialog, Ui_FitSetup):
    """
    Project setup window
    """
    def __init__(self, eq_params, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.setWindowTitle("{} - fitting settings".format(eq_params.name))
        self.LBSet.stateChanged.connect(self.setinterface)
        self.UBSet.stateChanged.connect(self.setinterface)
        self.InclRand.stateChanged.connect(self.setinterface)
        parameters = eq_params.param_order
        n_params = len(parameters)
        self.samelabels = [[self.lab11, self.lab21, self.lab31],
                           [self.lab12, self.lab22, self.lab32],
                           [self.lab13, self.lab23, self.lab33],
                           [self.lab14, self.lab24, self.lab34],
                           [self.lab15, self.lab25, self.lab35],
                           [self.lab16, self.lab26, self.lab36]]
        self.spboxes = [[self.SB11, self.SB21, self.SB31],
                        [self.SB12, self.SB22, self.SB32],
                        [self.SB13, self.SB23, self.SB33],
                        [self.SB14, self.SB24, self.SB34],
                        [self.SB15, self.SB25, self.SB35],
                        [self.SB16, self.SB26, self.SB36]]
        self.fixcbs = [self.CB1, self.CB2, self.CB3, self.CB4, self.CB5, self.CB6]

        # connect buttons
        for fixc in self.fixcbs:
            fixc.stateChanged.connect(self.setinterface)

        # label display
        for param_name, labels in zip(parameters, self.samelabels):
            for label in labels:
                label.setText(param_name)

        for sboxes, param in zip(self.spboxes, parameters):
            param_vals = eq_params[param]
            sboxes[0].setValue(param_vals.value)
            sboxes[1].setValue(param_vals.min)
            sboxes[2].setValue(param_vals.max)

        # hide redundant
        for labels, spboxes, fixbox in zip(self.samelabels[n_params:], self.spboxes[n_params:], self.fixcbs[n_params:]):
            fixbox.hide()
            for label, spbox in zip(labels, spboxes):
                label.hide()
                spbox.hide()

        # checkset
        if any([eq_params[par].min == - np.inf for par in eq_params]):
            self.LBSet.setChecked(False)
        if any([eq_params[par].max == np.inf for par in eq_params]):
            self.UBSet.setChecked(False)
        for par, fixcb in zip(eq_params, self.fixcbs):
            if not eq_params[par].vary:
                fixcb.setChecked(True)

        # inicialization setup
        self.InicN.setValue(eq_params.initializations)

    def setinterface(self):
        """
        Redraws the window interface
        """
        #Lower bound
        check = self.LBSet.isChecked()
        self.SB21.setEnabled(check)
        self.SB22.setEnabled(check)
        self.SB23.setEnabled(check)
        self.SB24.setEnabled(check)
        self.SB25.setEnabled(check)
        self.SB26.setEnabled(check)

        # Upper bound
        check = self.UBSet.isChecked()
        self.SB31.setEnabled(check)
        self.SB32.setEnabled(check)
        self.SB33.setEnabled(check)
        self.SB34.setEnabled(check)
        self.SB35.setEnabled(check)
        self.SB36.setEnabled(check)

        # fixed valu check
        for ((_, lbsb, ubsp), fixcb) in zip(self.spboxes, self.fixcbs):
            if fixcb.isChecked():
                lbsb.setEnabled(False)
                ubsp.setEnabled(False)

        # random inicialization
        check = self.LBSet.isChecked() and self.UBSet.isChecked()
        self.InclRand.setEnabled(check)
        self.InicN.setEnabled((check and self.InclRand.isChecked()))


class WarningMessage(QtGui.QDialog):
    def __init__(self, message="None message", parent=None):
        super(WarningMessage, self).__init__(parent)
        self.setWindowTitle('Warning')
        msgbox = QtGui.QMessageBox(self)
        msgbox.setText(message)
        msgbox.addButton(QtGui.QPushButton('Ok'), QtGui.QMessageBox.YesRole)
        msgbox.exec_()

##################
# TWO SUBSTRATES #
##################


class PreloadTwoSubs(QtGui.QDialog, Ui_PreloadTwoSubs):
    """
    Window to set up stoichometry and naming
    """
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.setWindowTitle('Reaction Information')
        self.SetAName.textChanged.connect(self.change_labels)
        self.SetBName.textEdited.connect(self.change_labels)
        self.IsITC.stateChanged.connect(self.enable_stoich)
        self.exec_()

    def change_labels(self):
        """
        Updates label display
        """
        self.SubALab.setText(self.SetAName.text())
        self.SubBLab.setText(self.SetBName.text())

    def enable_stoich(self):
        """
        Adjust for stoichiometry
        """
        self.ITCSettings.setEnabled(False)
        if self.IsITC.isChecked():
            self.ITCSettings.setEnabled(True)


class LoadDataDs(QtGui.QDialog, Ui_LoadDataDs):
    """
    Data loding window for two substrates
    """
    def __init__(self, reac_data):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.setWindowTitle('Data input')
        self.subdata = deepcopy(reac_data)

        self.SwitchRoles.clicked.connect(self.change_substr_role)
        self.SwitchSet.clicked.connect(self.change_set)
        self.AddRep.clicked.connect(self.append_data)

        self.OKButton.clicked.connect(self.accept)
        self.CancelButton.clicked.connect(self.reject)

        self.label_3.setText('Reaction rate (in {})'.format(self.subdata.runit))
        self.label_2.setText('Injection spacing (time; in {})'.format(self.subdata.tunit))
        self.label.setText('Concentration (in {})'.format(self.subdata.cunit))

        self.OKButton.setEnabled(False)
        self.display_name()
        self.select_type()

        self.change_set()

    def append_data(self):
        """
        Appends data to current set
        """
        rates = self.RateText.toPlainText()
        varvar = self.SubAText.toPlainText()

        # check and adjust for ITC
        if self.subdata.is_itc:
            constvar = self.make_const_conc()
        else:
            constvar = self.SubBText.value()
            temp_rates = rates.replace(',', ' ').split()
            constvar = ', '.join([str(constvar) for _ in temp_rates])

        if self.subdata.isnewset():
            try:
                self.subdata.add_set(varvar, constvar, rates)
            except AssertionError:
                WarningMessage("Dimension mismatch. Can't add the replicate.")
            except ValueError:
                WarningMessage("Load failed. Make sure points are represented by"
                               " numbers separated by space, comma or tab.")
        else:
            try:
                self.subdata.add_rep(varvar, constvar, rates)
            except AssertionError:
                WarningMessage("Dimension mismatch. Can't add the replicate.")
            except ValueError:
                WarningMessage("Load failed. Make sure points are represented by"
                               " numbers separated by space, comma or tab.")

        self.change_set(rep_add=True)
        self.OKButton.setEnabled(True)

    def change_set(self, rep_add=False):
        """
        Changes set you are appending to (or the display only)
        """

        # make everytging go away
        if not rep_add:
            self.subdata.next_set()

        self.SubAText.setPlainText('')
        self.RateText.setPlainText('')

        # # block out windows
        if self.subdata.isnewset():
            self.verticalWidget.setEnabled(True)
            self.SubBText.setEnabled(True)
            self.SubAText.setEnabled(True)

        else:
            self.verticalWidget.setEnabled(False)
            self.SubBText.setEnabled(False)
            self.SubBText.setValue(self.subdata.get_last_const()[0])
            self.SubAText.setPlainText(', '.join(str(num) for num in self.subdata.get_current_var()))
            self.SubAText.setEnabled(False)

        # # Set text
        self.SetNu.setText(str(self.subdata.setindex + 1))
        self.RepNu.setText(str(self.subdata.get_rep_cout()))

    def change_substr_role(self):
        """
        Make swith betwean variable and constant substrate
        """
        self.subdata.change_varible()
        self.change_set()
        self.display_name()

    def make_const_conc(self):
        """
        Calculates constant concentrations for ITC data.
        """
        rates = calculations.transform_data(self.RateText.toPlainText())

        # set constant variables
        const_var = [self.InitConc.value()]
        for i in range(1, len(rates)):
            const_var.append(const_var[-1] - (rates[i-1] * self.subdata.get_stoch_val() * self.TimeStep.value()))
        return ', '.join([str(tmp_name) for tmp_name in const_var])

    def display_name(self):
        """
        Creates and displays appropriate tags.
        """
        tags = [' (Variable Substrate; in {})'.format(self.subdata.cunit),
                ' (Constant Substrate; in {})'.format(self.subdata.cunit)]
        first_name = self.subdata.nameA
        second_name = self.subdata.nameB

        if self.subdata.a_is_var:
            self.SubAName.setText(first_name + tags[0])
            self.SubBName.setText(second_name + tags[1])
        else:
            self.SubAName.setText(second_name + tags[0])
            self.SubBName.setText(first_name + tags[1])

    def select_type(self):
        """
        Changes type data loding type
        """
        self.verticalWidget_2.setVisible(not self.subdata.is_itc)
        self.verticalWidget.setVisible(self.subdata.is_itc)


class ExploreSolutions(QtGui.QDialog, Ui_SolutionExplorer):
    """
    Class for exploring solutions
    """
    def __init__(self, reacs, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.setWindowTitle('Explore solutions')

        self.equation = None
        self.axes = None
        self.axes2 = None

        self.fig = Figure()
        self.canvas = FigureCanvas(self.fig)
        self.mpl_toolbar = NavigationToolbar(self.canvas, parent)
        self.verticalLayout.addWidget(self.canvas)
        self.verticalLayout.addWidget(self.mpl_toolbar)
        self.verticalLayout.addWidget(self.mpl_toolbar)

        # Default Load button
        self.AjdButVal.clicked.connect(self.adjustvals)
        self.AutoFitBut.clicked.connect(self.make_fit_all)
        self.ReFitSet.clicked.connect(self.make_fit_single)

        # hide fit results
        self.set_fit_widget.setVisible(False)

        # data setup
        self.alldata = reacs
        if reacs.is_single():
            self.data = reacs
            self.SetCB.hide()
            self.ErrLAb.hide()
            self.ErrCB.hide()
            self.SubLab.hide()
            self.EncLab.hide()
            self.EncCB.hide()
        else:
            self.SetCB.addItems([self.alldata.nameA, self.alldata.nameB])
            self.resetencview()
            # self.data = reacs.get_repres()

        # setup variables
        # order of variables (fields)
        self.sliders = [self.Slider1, self.Slider2, self.Slider3, self.Slider4, self.Slider5, self.Slider6]
        self.labs = [self.Param1, self.Param2, self.Param3, self.Param4, self.Param5, self.Param6]
        self.vals = [self.Val1, self.Val2, self.Val3, self.Val4, self.Val5, self.Val6]
        self.lines = [self.line_1, self.line_2, self.line_3, self.line_4, self.line_5, self.line_6]

        self.allfitlabs = [self.fitlab1, self.fitlab2, self.fitlab3, self.fitlab4, self.fitlab5, self.fitlab6]
        self.allvallabs = [self.vallab1, self.vallab2, self.vallab3, self.vallab4, self.vallab5, self.vallab6]
        self.ulabs = [self.ulab1, self.ulab2, self.ulab3, self.ulab4, self.ulab5, self.ulab6]

        # formula setup
        self.equations = [calculations.MMparams(), calculations.HEparams(), calculations.AInHparams(),
                          calculations.CIparams(), calculations.MAparams(), calculations.NCIparams(),
                          calculations.MIparams(), calculations.SAparams(), calculations.SUAparams(),
                          calculations.UCIparams()]
        if not self.alldata.is_single():
            self.equations += [calculations.PPMparams(), calculations.PPMSIparams(),
                               calculations.TCparams(), calculations.TCSIparams()]
        self.equations_formulas = [i.eq for i in self.equations]
        self.EqSel.addItems([eqparams.name for eqparams in self.equations])
        self.set_equations = []

        # redraw the plots
        self.PlotCB.currentIndexChanged.connect(self.change_graph_select)
        self.SetCB.currentIndexChanged.connect(self.change_set)
        self.EqSel.activated.connect(self.change_layout)
        self.EncCB.currentIndexChanged.connect(self.cached_make_plot)
        self.ErrCB.currentIndexChanged.connect(self.cached_make_plot)
        for val in self.vals:
            val.valueChanged.connect(self.change_equation)

        slider_changes = [self.slider1_change, self.slider2_change, self.slider3_change,
                          self.slider4_change, self.slider5_change, self.slider6_change]

        for slider, slider_c in zip(self.sliders, slider_changes):
            slider.setMaximum(1000)
            slider.valueChanged.connect(slider_c)

        # Import fits
        self.SetParams.clicked.connect(self.imp_fit_vals)

        # Legend toggle
        self.multi_cach = False
        self.LegendCB.clicked.connect(self.legend_display)

        # set up equation and make plot
        self.change_layout()

    def make_fit_all(self):
        """
        Fits all sets
        """
        self.make_fit(sel_set=-1)

    def make_fit_single(self):
        """
        Fits only selected set
        """
        self.make_fit(sel_set=self.setsel.currentIndex())

    def imp_fit_vals(self):
        """
        Import set fit values to global vals
        """
        n_params = range(len(self.equations[self.EqSel.currentIndex()].param_order))
        for parval, cbox, _ in zip(self.allvallabs, self.vals, n_params):
            cbox.setValue(float(parval.text()))
        self.change_equation()

    def legend_display(self):
        """
        Switch on and off legend display
        """
        self.make_plot(self.multi_cach)

    def change_set(self):
        """
        Change representation (for tow substrates only)
        """
        self.resetencview()
        self.change_layout()

    def resetencview(self):
        """
        Readjusts display values for fade view
        """
        a_isvar = False if self.SetCB.currentIndex() == 1 else True
        self.EncCB.clear()
        self.EncCB.addItem('All')
        self.EncCB.addItems(['Set {}'.format(i + 1) for i in range(len(self.alldata.AllVar[a_isvar]))])

    def make_slider_change(self, slider, val):
        """
        Make value changes based on slider
        """
        param_idx = self.sliders.index(slider)
        eq_idx = self.EqSel.currentIndex()
        param_name = self.equations[eq_idx].param_order[param_idx]
        param = self.equations[eq_idx][param_name]
        min_val = param.min
        max_val = param.max
        val.setValue((max_val - min_val) * slider.value() / 1000 + min_val)

    def slider1_change(self):
        self.make_slider_change(self.sliders[0], self.vals[0])

    def slider2_change(self):
        self.make_slider_change(self.sliders[1], self.vals[1])

    def slider3_change(self):
        self.make_slider_change(self.sliders[2], self.vals[2])

    def slider4_change(self):
        self.make_slider_change(self.sliders[3], self.vals[3])

    def slider5_change(self):
        self.make_slider_change(self.sliders[4], self.vals[4])

    def slider6_change(self):
        self.make_slider_change(self.sliders[5], self.vals[5])

    def adjustvals(self):
        """
        Adjusts values to the best found fit (ss) or
        only changes fitting parameters(ds)
        """
        sel_eq = self.equations[self.EqSel.currentIndex()]
        dlg = FitSetup(sel_eq)

        if dlg.exec_():
            if dlg.LBSet.isChecked() and dlg.UBSet.isChecked() and dlg.InclRand.isChecked():
                sel_eq.initializations = dlg.InicN.value()
            else:
                sel_eq.initializations = 0
            new_bounds = [[sbbox.value() for sbbox in bgroup] for bgroup in dlg.spboxes]
            if not dlg.LBSet.isChecked():
                for bound_g in new_bounds:
                    bound_g[1] = - np.inf
            if not dlg.UBSet.isChecked():
                for bound_g in new_bounds:
                    bound_g[2] = np.inf
            # margins check
            if any([bounds[1] >= bounds[2] and not useb.isChecked() for bounds, useb in zip(new_bounds, dlg.fixcbs)]):
                WarningMessage("Update failed. Make sure all lower bounds are bellow upper bounds")
                return
            sel_eq.change_all(new_bounds)

            params = [sel_eq[p_idx] for p_idx in sel_eq.param_order]

            # fix values
            for fixch, param, val in zip(dlg.fixcbs, params, new_bounds):
                if fixch.isChecked():
                    param.set(vary=False)
                    param.min = val[0] - 0.0000000000001
                    param.max = val[0] + 0.0000000000001
                    param.value = val[0]
                else:
                    param.set(vary=True)

        if self.alldata.is_single():
            self.change_layout()

    def make_fit(self, sel_set):
        sel_eq = self.equations[self.EqSel.currentIndex()]

        # SS fitting
        if self.alldata.is_single():
            calc_res = calculations.find_fit(sel_eq,
                                             sel_eq.initializations,
                                             np.hstack(self.data.concentrations),
                                             np.hstack(self.data.rates))
            for par_id, spbox in zip(sel_eq.param_order, self.vals):
                spbox.setValue(calc_res.params[par_id].value)

        # DS fitting
        else:
            a_isvar = False if self.SetCB.currentIndex() == 1 else True
            # fit all
            if sel_set == -1:
                self.EncCB.setCurrentIndex(0)
                self.set_equations = [calculations.find_fit(sel_eq,
                                      sel_eq.initializations, x, y, x2)
                                      for x, y, x2 in self.alldata.get_points(a_isvar)]
            # fit selected
            else:
                x, y, x2 = list(self.alldata.get_points(a_isvar))[sel_set]
                self.set_equations[sel_set] = calculations.find_fit(sel_eq, sel_eq.initializations, x, y, x2)

            self.make_plot(multiple=True)

            # display fit results
            if not self.alldata.is_single():
                sel_set = 0 if sel_set < 0 else sel_set
                self.show_best_fit(set_num=sel_set)

    def show_best_fit(self, set_num=0):
        """
        Disaplys new fit resuls
        """

        def fit_display_update():
            """
            Update fit label display
            """
            set_idx = self.setsel.currentIndex()
            fit_par_fun = self.set_equations[set_idx].params
            for dislab, vallab, fitparam in zip(self.allfitlabs, self.allvallabs, fit_par_fun):
                dislab.setVisible(True)
                vallab.setVisible(True)
                dislab.setText(fitparam)
                vallab.setText('{0:.5f}'.format(fit_par_fun[fitparam].value))

            # hide redundant
            for dislab, vallab in zip(self.allfitlabs[len(fit_par_fun):], self.allvallabs[len(fit_par_fun):]):
                dislab.setVisible(False)
                vallab.setVisible(False)

        def change_fitview():
            self.EncCB.setCurrentIndex(self.setsel.currentIndex() + 1)
            fit_display_update()

        self.set_fit_widget.setVisible(True)

        # combo box setup
        self.setsel.clear()
        self.setsel.addItems(['set {}'.format(i+1) for i in range(len(self.set_equations))])
        self.setsel.activated.connect(change_fitview)
        self.setsel.setCurrentIndex(set_num)
        fit_display_update()
        self.perfit_res()

    def perfit_res(self):
        """
        Calculate and change sum of residuals
        """
        group_index = True if self.SetCB.currentIndex() == 0 else False
        eqs = [fit.function for fit in self.set_equations]
        sem_sum = 0.
        for seta, setb, setr, equation in zip(self.alldata.AllVar[group_index],
                                              self.alldata.AllConst[group_index],
                                              self.alldata.AllRates[group_index],
                                              eqs):
            for apoints, bpoints, rpoints in zip(seta, setb, setr):
                sem_sum += sum((equation(apoints, bpoints) - rpoints)**2)
        self.ResLab.setText('{0:.8f}'.format(sem_sum))

    def change_graph_select(self):
        """
        Changes graph setup
        """
        if not self.alldata.is_single():
            if self.PlotCB.currentIndex() == 0:
                self.ErrCB.setEnabled(True)
            else:
                self.ErrCB.setCurrentIndex(0)
                self.ErrCB.setEnabled(False)
        self.change_layout()

    def change_layout(self):
        """
        Changes layout and equations
        """
        # Display options
        eq_idx = self.EqSel.currentIndex()
        sel_eq = self.equations[eq_idx]
        params = sel_eq.param_order
        # show
        for label, spbox, slider, line, param, ulab in zip(self.labs[:len(params)],
                                                           self.vals[:len(params)],
                                                           self.sliders[:len(params)],
                                                           self.lines[:len(params)],
                                                           params,
                                                           self.ulabs[:len(params)]):
            label.setText(param)
            label.show()
            ulab.setText(sel_eq.get_units(param, self.alldata))
            ulab.show()
            spbox.show()
            if self.alldata.is_single():
                spbox.setValue(sel_eq[param].value)
            line.show()
            slider.show()

        # hide
        for label, spbox, slider, line, ulab in zip(self.labs[len(params):],
                                                    self.vals[len(params):],
                                                    self.sliders[len(params):],
                                                    self.lines[len(params):],
                                                    self.ulabs[len(params):]):
            label.hide()
            spbox.hide()
            slider.hide()
            line.hide()
            ulab.hide()

        # lock sliders if not limited
        enable_sliders = True
        if any([sel_eq[param].max == np.inf for param in params]) or \
                any([sel_eq[param].min == -np.inf for param in params]):
            enable_sliders = False
        for slider in self.sliders:
            slider.setEnabled(enable_sliders)
        # lock sliders and values if not vary
        for param, slider, valfield in zip(params, self.sliders, self.vals):
            valfield.setEnabled(sel_eq[param].vary)
            slider.setEnabled(sel_eq[param].vary and enable_sliders)

        # change displayed equation
        self.EqPic.setPixmap(QtGui.QPixmap('./qt_design/eq_pic/{}.gif'.format(sel_eq.name)))

        self.change_equation()

    def change_equation(self):
        """
        Changes equation parameters and does replotting
        """
        all_vals = [val.value() for val in self.vals]

        # Hide fit widget
        self.set_fit_widget.setVisible(False)

        eq_idx = self.EqSel.currentIndex()
        self.equation = self.equations_formulas[eq_idx](*all_vals)
        self.make_plot()
        # make calculations i
        group_index = True if self.SetCB.currentIndex() == 0 else False
        self.ResLab.setText('{0:.6f}'.format(self.alldata.res_sum(self.equation, group_index)))

        # save new values
        for param, new_val in zip(self.equations[eq_idx].param_order, all_vals):
            self.equations[eq_idx].change_value(param, new_val)

    def cached_make_plot(self):
        """
        Wrapped plot with cached multiple
        """
        self.make_plot(multiple=self.multi_cach)

    def make_plot(self, multiple=False):
        """
        draws the plots
        """
        # legend setup
        if self.LegendCB.isChecked():
            legend = 'Replicate ' if self.alldata.is_single() else 'Set '
        else:
            legend = ''
        self.multi_cach = multiple

        self.fig.clear()
        self.axes = self.fig.add_subplot(121)
        self.axes2 = self.fig.add_subplot(122)
        a_isvar = False if self.SetCB.currentIndex() == 1 else True
        if self.alldata.is_single():
            # reaction plot
            reaction_plots.plot_singlegraph(self.data, self.axes, signal=self.PlotCB.currentIndex(),
                                            equation=self.equation, legend=legend)

            # residuals plot
            reaction_plots.plot_res(self.alldata, self.axes2, equation=self.equation, a_isvar=a_isvar)

        # plot for DS data
        else:
            ebars = True if self.ErrCB.currentIndex() == 1 else False
            # plot when finding fits
            if multiple:
                reaction_plots.plot_dsegraph(self.alldata, self.axes, signal=self.PlotCB.currentIndex(),
                                             equations=[eq.function for eq in self.set_equations],
                                             a_isvar=a_isvar, legend=legend, pick=self.EncCB.currentIndex() - 1,
                                             errors=ebars)
                reaction_plots.plot_res(self.alldata, self.axes2, equations=[eq.function for eq in self.set_equations],
                                        a_isvar=a_isvar, pick=self.EncCB.currentIndex() - 1)
            # plot when adusting values
            else:
                reaction_plots.plot_dsegraph(self.alldata, self.axes, signal=self.PlotCB.currentIndex(),
                                             equation=self.equation, a_isvar=a_isvar, legend=legend,
                                             pick=self.EncCB.currentIndex() - 1, errors=ebars)
                reaction_plots.plot_res(self.alldata, self.axes2, equation=self.equation, a_isvar=a_isvar,
                                        pick=self.EncCB.currentIndex() - 1)
        self.canvas.draw()


def make_file_path(path_list, filename=None):
    """
    Creates a path for your file and returns ful path
    """
    fullpath = os.path.join(*path_list)
    if not os.path.exists(fullpath):
        os.makedirs(fullpath)
    if filename is not None:
        return os.path.join(fullpath, filename)
    else:
        return fullpath


def adjustvals(sel_eq):
    """
    Set values for batch run
    """
    def make_change():
        dlg = FitSetup(sel_eq)
        if dlg.exec_():
            if dlg.LBSet.isChecked() and dlg.UBSet.isChecked() and dlg.InclRand.isChecked():
                sel_eq.initializations = dlg.InicN.value()
            else:
                sel_eq.initializations = 0
            new_bounds = [[sbbox.value() for sbbox in bgroup] for bgroup in dlg.spboxes]
            if not dlg.LBSet.isChecked():
                for bound_g in new_bounds:
                    bound_g[1] = - np.inf
            if not dlg.UBSet.isChecked():
                for bound_g in new_bounds:
                    bound_g[2] = np.inf
            # margins check
            if any([bounds[1] >= bounds[2] and not useb.isChecked()
                    for bounds, useb in zip(new_bounds, dlg.fixcbs)]):
                WarningMessage("Update failed. Make sure all lower bounds are bellow upper bounds")
                return
            sel_eq.change_all(new_bounds)

            params = [sel_eq[p_idx] for p_idx in sel_eq.param_order]

            # fix values
            for fixch, param, val in zip(dlg.fixcbs, params, new_bounds):
                if fixch.isChecked():
                    param.set(vary=False)
                    param.min = val[0] - 0.0000000000001
                    param.max = val[0] + 0.0000000000001
                    param.value = val[0]
                else:
                    param.set(vary=True)
    return make_change


class BatchRun(QtGui.QDialog, Ui_BatchDialog):
    """
    Window for fast multiple fitting
    """
    def __init__(self, in_data, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.setWindowTitle('Multiple equation fit')

        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.CDButton.clicked.connect(self.select_outputfolder)
        self.savepath = os.getenv('HOME')
        self.PathLabel.setText(self.savepath)

        self.alldata = in_data

        self.equations = [calculations.MMparams(), calculations.HEparams(), calculations.AInHparams(),
                          calculations.CIparams(), calculations.MAparams(), calculations.NCIparams(),
                          calculations.MIparams(), calculations.SAparams(), calculations.SUAparams(),
                          calculations.UCIparams()]
        if not self.alldata.is_single():
            self.equations += [calculations.PPMparams(), calculations.PPMSIparams(),
                               calculations.TCparams(), calculations.TCSIparams()]

        self.optbut = []
        self.optcb = []

        for equa in self.equations:
            self.add_options(equa)

        # button conections
        self.changes = [adjustvals(eq_fit) for eq_fit in self.equations]
        for button, change in zip(self.optbut, self.changes):
            button.clicked.connect(change)
        self.CalcBut.clicked.connect(self.run_analysis)

    def add_options(self, params):
        """
        Adds parametes to the display
        """
        posit = len(self.optbut)
        cbox = QtGui.QCheckBox()
        cbox.setChecked(False)
        self.gridLayout.addWidget(cbox, posit, 1, 1, 1)
        cbox.setText(params.name)
        setbut = QtGui.QPushButton()
        self.gridLayout.addWidget(setbut, posit, 2, 1, 1)
        setbut.setText("Settings")
        setbut.setEnabled(False)

        # Connect checkbox to settings
        cbox.stateChanged.connect(lambda x: setbut.setEnabled(cbox.isChecked()))
        self.optbut.append(setbut)
        self.optcb.append(cbox)

    def select_outputfolder(self):
        """
        Select default save path
        """
        dialog = QtGui.QFileDialog()
        temp_path = QtGui.QFileDialog.getExistingDirectory(dialog, 'Select a folder:',
                                                           self.savepath, QtGui.QFileDialog.ShowDirsOnly)
        if temp_path:
            self.savepath = temp_path
            self.PathLabel.setText(self.savepath)

    def create_valid_folder(self, path):
        """
        Creates returns directory to save results to
        """
        savepath_r = os.path.join(path, self.alldata.name)
        savepath = savepath_r

        n = 0
        while os.path.exists(savepath):
            n += 1
            savepath = savepath_r + '_' + str(n)
        os.mkdir(savepath)
        return savepath

    def make_ss_outpust(self, savefolder, sel_eq):
        """
        Creates outputs for single substrate
        """
        # calculate parameters
        calc_result = calculations.find_fit(sel_eq,
                                            sel_eq.initializations,
                                            np.hstack(self.alldata.concentrations),
                                            np.hstack(self.alldata.rates))
        plotfolder = make_file_path([savefolder, sel_eq.name])

        # make fit plots
        reaction_plots.plotoutput(self.alldata, plotfolder, plot_fun=calc_result.function)

        # make residuals plot
        reaction_plots.resi_to_file(self.alldata, plotfolder, equation=calc_result.function)

        # make excel report
        xls_file = make_file_path([plotfolder], '{} fit report.xlsx'.format(sel_eq.name))
        calculations.fit_to_xls(self.alldata, calc_result, xls_file)

    def make_ds_output(self, savefolder, sel_eq):
        """
        Creates outputs for double substrate
        """
        plotfolder = make_file_path([savefolder, sel_eq.name])

        # make fits
        sub_a_fits = [calculations.find_fit(sel_eq,
                      sel_eq.initializations, x, y, x2)
                      for x, y, x2 in self.alldata.get_points(True)]
        sub_b_fits = [calculations.find_fit(sel_eq,
                      sel_eq.initializations, x, y, x2)
                      for x, y, x2 in self.alldata.get_points(False)]
        fits = {True: sub_a_fits, False: sub_b_fits}

        # write xls
        xls_file = make_file_path([plotfolder], '{} fit report.xlsx'.format(sel_eq.name))
        calculations.fit_to_xls(self.alldata, fits, xls_file)

        # make fit plots
        plotfolder = make_file_path([savefolder, sel_eq.name])
        reaction_plots.plotoutput(self.alldata, plotfolder, plot_fun=fits)
        reaction_plots.resi_to_file(self.alldata, plotfolder, equations=fits)

    def run_analysis(self):

        # selet folder to save the results to
        if not self.savepath:
            WarningMessage(message="Please specify save folder")
            return
        savefolder = self.create_valid_folder(self.savepath)

        raw_data_xls = make_file_path([savefolder], 'input_data.xlsx')
        calculations.data_to_xls(self.alldata, raw_data_xls)

        for cbox, parameter in zip(self.optcb, self.equations):
            if cbox.isChecked():
                if self.alldata.is_single():
                    self.make_ss_outpust(savefolder, parameter)
                else:
                    self.make_ds_output(savefolder, parameter)
        WarningMessage(message="Results have been saved to {}".format(savefolder))


class PointsView(QtGui.QDialog, Ui_PointsView):
    """
    Window for exploring and delating points
    """
    def __init__(self, reac_data, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.setWindowTitle("Points view")
        self.reac_data = deepcopy(reac_data)
        self.axes = None
        self.axes2 = None
        self.fig = Figure()
        self.canvas = FigureCanvas(self.fig)
        self.mpl_toolbar = NavigationToolbar(self.canvas, parent)
        self.verticalLayout_3.addWidget(self.canvas)
        self.verticalLayout_3.addWidget(self.mpl_toolbar)

        # SS init
        if self.reac_data.is_single():
            self.label.hide()
            self.label_2.hide()
            self.VarBox.hide()
            self.SetBox.hide()
            self.qbox_level3()
        # DS init
        else:
            self.qbox_level1()

        # make change
        self.VarBox.activated.connect(self.qbox_level1)
        self.SetBox.activated.connect(self.qbox_level2)
        self.RepBox.activated.connect(self.qbox_level3)
        self.DelBut.clicked.connect(self.delete_points)

    def select_rep(self):
        """
        Returns you rep which should be bold
        """
        sel_set = self.SetBox.currentIndex()
        varsub = self.VarBox.currentIndex() == 0
        return [sel_set if varsub else -2, sel_set if not varsub else -2]

    def draw_plots(self):
        """
        Draw or re-draw plots
        """
        self.fig.clear()
        if self.reac_data.is_single():
            self.axes = self.fig.add_subplot(111)
            # Graph plot
            reaction_plots.plot_singlegraph(self.reac_data, self.axes, 0, pick=self.RepBox.currentIndex())
            self.canvas.draw()
            self.canvas.show()

        else:
            self.axes = self.fig.add_subplot(121)
            self.axes2 = self.fig.add_subplot(122)

            picks = self.select_rep()
            reaction_plots.plot_singlegraph(self.reac_data.get_repres(True), self.axes, 0, pick=picks[0], alpha1=0.75)
            reaction_plots.plot_singlegraph(self.reac_data.get_repres(False), self.axes2, 0, pick=picks[1], alpha1=0.75)

            # enhance single point
            sub_group = True if self.VarBox.currentIndex() == 0 else False
            plot_obj = self.axes if sub_group else self.axes2
            dat_set = self.SetBox.currentIndex()
            dat_rep = self.RepBox.currentIndex()
            # plot if possible
            try:
                plot_obj.plot(self.reac_data.AllVar[sub_group][dat_set][dat_rep],
                              self.reac_data.AllRates[sub_group][dat_set][dat_rep], 'o', color='red')
            except IndexError:
                pass
            self.canvas.draw()
            self.canvas.show()

    def qbox_level1(self):
        """
        Display changes stage 1
        """
        idx = self.VarBox.currentIndex()
        idx = 0 if idx == -1 else idx
        self.VarBox.clear()
        self.VarBox.addItems([self.reac_data.nameA, self.reac_data.nameB])
        self.VarBox.setCurrentIndex(idx)
        self.qbox_level2()

    def qbox_level2(self):
        """
        Display changes stage 2
        """
        idx = self.SetBox.currentIndex()
        idx = 0 if idx == -1 else idx
        self.SetBox.clear()
        subs_sel = True if self.VarBox.currentIndex() == 0 else False
        self.SetBox.addItems(['Set {}'.format(i + 1) for i in range(len(self.reac_data.AllVar[subs_sel]))])
        self.SetBox.setCurrentIndex(idx if idx < len(self.SetBox) else 0)
        self.qbox_level3()

    def qbox_level3(self):
        """
        Display changes stage 3
        """
        idx = self.RepBox.currentIndex()
        idx = 0 if idx == -1 else idx
        self.RepBox.clear()
        if self.reac_data.is_single():
            self.RepBox.addItems(['Replicate {}'.format(i + 1) for i in range(self.reac_data.replicates)])
            self.RepBox.setCurrentIndex(idx if idx < len(self.RepBox) else 0)
        else:
            subs_sel = True if self.VarBox.currentIndex() == 0 else False
            sub_set = self.SetBox.currentIndex()
            try:
                self.RepBox.addItems(['Replicate {}'.format(i + 1) for i in range(len(
                    self.reac_data.AllVar[subs_sel][sub_set]))])
                self.RepBox.setCurrentIndex(idx if idx < len(self.RepBox) else 0)
            except:
                WarningMessage('You have no replicates for selected substrate')
        self.draw_plots()

    def delete_points(self):
        """
        Deletes replicate points
        """
        # SS delete
        if self.reac_data.is_single():
            if self.reac_data.replicates > 0:
                posit = self.RepBox.currentIndex()
                self.reac_data.rates.pop(posit)
                self.reac_data.concentrations.pop(posit)
                self.reac_data.replicates -= 1
                self.qbox_level3()
            else:
                WarningMessage("No points to delete")
        # DS delete
        else:
            subs_sel = True if self.VarBox.currentIndex() == 0 else False
            set_pos = self.SetBox.currentIndex()
            rep_pos = self.RepBox.currentIndex()

            self.reac_data.AllVar[subs_sel][set_pos].pop(rep_pos)
            self.reac_data.AllRates[subs_sel][set_pos].pop(rep_pos)
            self.reac_data.AllConst[subs_sel][set_pos].pop(rep_pos)
            if not self.reac_data.AllVar[subs_sel][set_pos]:
                self.reac_data.AllVar[subs_sel].pop(set_pos)
                self.reac_data.AllRates[subs_sel].pop(set_pos)
                self.reac_data.AllConst[subs_sel].pop(set_pos)
            self.qbox_level1()
