"""
Functions to create reaction plots
"""
from matplotlib.pyplot import get_cmap
from matplotlib.pyplot import figure
import numpy as np
import os
import statistics


def plotoutput(reac_obj, sfolder, grid=False, plot_fun=None):
    """
    saves basic graphs to sfolder
    """
    plot_pairs = {0: 'Michaelis-Menten',
                  1: 'Lineweaver-Buck',
                  2: 'Hans-Woolf',
                  3: 'Eadue-Hofstee'}

    my_figure = figure()
    xsubplot = my_figure.add_subplot(111)
    for singnal in plot_pairs:
        # SS plots
        if reac_obj.is_single():
            plot_singlegraph(reac_obj, xsubplot, singnal, grid, equation=plot_fun)
            fig_name = os.path.join(sfolder, plot_pairs[singnal] + '_plot.pdf')
            my_figure.savefig(fig_name)
            xsubplot.clear()

        # DS plots
        else:
            plot_dsegraph(reac_obj, xsubplot, singnal, grid, equations=[eq.function for eq in plot_fun[True]],
                          a_isvar=True)
            fig_name = os.path.join(sfolder, '{}_{}_plot.pdf'.format(reac_obj.nameA, plot_pairs[singnal]))
            my_figure.savefig(fig_name)
            xsubplot.clear()

            plot_dsegraph(reac_obj, xsubplot, singnal, grid, equations=[eq.function for eq in plot_fun[False]],
                          a_isvar=False)
            fig_name = os.path.join(sfolder, '{}_{}_plot.pdf'.format(reac_obj.nameB, plot_pairs[singnal]))
            my_figure.savefig(fig_name)
            xsubplot.clear()

    # add plots with Legend
    if reac_obj.is_single():
        plot_singlegraph(reac_obj, xsubplot, 0, grid, equation=plot_fun, legend='Replicate ')
        fig_name = os.path.join(sfolder, plot_pairs[0] + '_plot_LEGEND.pdf')
        my_figure.savefig(fig_name)
        xsubplot.clear()
    else:
        plot_dsegraph(reac_obj, xsubplot, 0, grid, equations=[eq.function for eq in plot_fun[True]],
              a_isvar=True, legend='Set ')
        fig_name = os.path.join(sfolder, '{}_{}_plot_LEGEND.pdf'.format(reac_obj.nameA, plot_pairs[0]))
        my_figure.savefig(fig_name)
        xsubplot.clear()

        plot_dsegraph(reac_obj, xsubplot, 0, grid, equations=[eq.function for eq in plot_fun[False]],
                      a_isvar=False, legend='Set ')
        fig_name = os.path.join(sfolder, '{}_{}_plot_LEGEND.pdf'.format(reac_obj.nameB, plot_pairs[0]))
        my_figure.savefig(fig_name)
        xsubplot.clear()


def resi_to_file(reac_obj, sfolder, equation=None, equations=None):
    """
    Makes residuals plot file
    """
    my_figure = figure()
    xsubplot = my_figure.add_subplot(111)

    # SS
    if reac_obj.is_single():
        plot_res(reac_obj, xsubplot, equation=equation, grid=False)
        fig_name = os.path.join(sfolder, 'residuals_plot.pdf')
        my_figure.savefig(fig_name)

    # DS
    else:
        plot_res(reac_obj, xsubplot, equations=[eq.function for eq in equations[True]],
                 a_isvar=True)
        fig_name = os.path.join(sfolder, '{}_residuals_plot.pdf'.format(reac_obj.nameA))
        my_figure.savefig(fig_name)
        xsubplot.clear()

        plot_res(reac_obj, xsubplot, equations=[eq.function for eq in equations[False]],
                 a_isvar=False)
        fig_name = os.path.join(sfolder, '{}_residuals_plot.pdf'.format(reac_obj.nameB))
        my_figure.savefig(fig_name)


def plot_eq_n_point(fit_results, reac_obj, sfolder, grid=False):
    for equat in fit_results.results_c:
        my_figure = figure()
        xsubplot = my_figure.add_subplot(111)
        plot_singlegraph(reac_obj, xsubplot, 0, grid=grid, equation=fit_results.eqs[equat])
        fig_name = os.path.join(sfolder, equat + '_plot.pdf')
        my_figure.savefig(fig_name)
        xsubplot.clear()


def plot_singlegraph(reac_obj, plot_obj, signal=0, grid=False, equation=None, legend='', global_fit=False,
                     rep_fit=False, pick=-1, errorbars=False, alpha0=0.15, alpha1=1, sname='Substrate',
                     extrapolation=0):
    """
    Plots designated plot based on signal and reaction object to plot_object.
    If equation is given it will be ploted with the points
    """

    # If there is nothing to do do nothing
    if reac_obj.get_replicates() == 0:
        return

    # color setup
    cm = get_cmap('gist_ncar')
    cols = [cm(1.*i/reac_obj.get_replicates()) for i in range(reac_obj.get_replicates())]

    #grid settings
    plot_obj.grid(b=grid)

    plot_obj.axhline(0, color='black')
    plot_obj.axvline(0, color='black')

    # setup for proper graph
    if signal == 1:
        x_name = "1 / {} concentration [1 / {}]".format(sname, reac_obj.cunit)
        y_name = "1 / Reaction rate [{}]".format(reac_obj.runit)
        x_vals = [1 / tfset for tfset in reac_obj.concentrations]
        y_vals = [1 / tfset for tfset in reac_obj.rates]

    elif signal == 2:
        x_name = "{} concentration [{}]".format(sname, reac_obj.cunit)
        y_name = "{} concentration / Reaction rate [{}]".format(sname, reac_obj.tunit)
        x_vals = reac_obj.concentrations
        y_vals = [tfset1 / tfset2 for tfset1, tfset2 in
                  zip(reac_obj.concentrations, reac_obj.rates)]

    elif signal == 3:
        x_name = "Reaction rate / {} concentration [1 / {}]".format(sname, reac_obj.tunit)
        y_name = "Reaction rate [{}]".format(reac_obj.runit)
        x_vals = [tfset1 / tfset2 for tfset1, tfset2 in
                  zip(reac_obj.rates, reac_obj.concentrations)]
        y_vals = reac_obj.rates
    else:
        x_name = "{} concentration [{}]".format(sname, reac_obj.cunit)
        y_name = "Reaction rate [{}]".format(reac_obj.runit)
        x_vals = reac_obj.concentrations
        y_vals = reac_obj.rates

    # plot the objects
    for x_rep, y_rep, count in zip(x_vals, y_vals, range(len(y_vals))):
        alp = alpha1 if (count == pick or pick == -1) else alpha0
        sel_col = cols.pop()

        # plot errors
        if errorbars and signal == 0:
            plot_obj.errorbar(list(errorbars[count][0]), errorbars[count][1],
                              yerr=[errorbars[count][2], errorbars[count][3]],
                              fmt='o', alpha=alp, color=sel_col)

        # plot points
        else:
            plot_obj.plot(x_rep, y_rep, 'o', ms=4, color=sel_col, label=reac_obj.setnames[count],
                          alpha=alp)

        # Plot linear fits
        extrap_val = (max(x_rep) - min(x_rep)) * extrapolation / 100
        line_vals = np.linspace(min(x_rep) - extrap_val, max(x_rep) + extrap_val, 100)
        if (signal == 1 or signal == 2) and rep_fit:
            fit = np.polyfit(x_rep, y_rep, rep_fit)
            fit_fn = np.poly1d(fit)
            plot_obj.plot(line_vals, fit_fn(line_vals),
                          ms=4,
                          color=sel_col)

    # plot given equation if it is specified
    if equation is not None:
        plot_fit(plot_obj, reac_obj.concentrations, equation=equation, signal=signal, alp=1)

    # plot global fit
    if (signal == 1 or signal == 2) and global_fit:
        x_globs = np.hstack(tuple(x_vals))
        y_globs = np.hstack(tuple(y_vals))
        fit = np.polyfit(x_globs, y_globs, global_fit)
        fit_fn = np.poly1d(fit)
        extrap_val = (max(x_rep) - min(x_rep)) * extrapolation / 100
        line_vals = np.linspace(min(x_globs) - extrap_val, max(x_globs) + extrap_val, 100)
        plot_obj.plot(line_vals, fit_fn(line_vals),
                      ms=4,
                      color='b',
                      label="Global fit")

    # Plot legend
    if legend:
        plot_obj.legend(loc=0)

    # set limits
    x_min = min([min(d_set) for d_set in x_vals])
    x_max = max([max(d_set) for d_set in x_vals])
    y_min = min([min(d_set) for d_set in y_vals])
    y_max = max([max(d_set) for d_set in y_vals])

    extrap_val = (x_max - x_min) * extrapolation / 100
    x_max = x_max + extrap_val
    x_min = x_min - extrap_val
    x_space = (x_max - x_min) * 0.05
    y_space = (y_max - y_min) * 0.05
    plot_obj.set_xlim(x_min - x_space, x_max + x_space)
    plot_obj.set_ylim(y_min - y_space, y_max + y_space)
    plot_obj.set_xlabel(x_name)
    plot_obj.set_ylabel(y_name)


def plot_res(reac_obj, plot_obj, equation=None, equations=None, grid=False, a_isvar=True, pick=-1):
    """
    Makes residual plot
    """

    # color setup
    cm = get_cmap('gist_ncar')
    if reac_obj.is_single():
        cols = [cm(1.*i/reac_obj.get_replicates()) for i in range(reac_obj.get_replicates())]
        x_vals = reac_obj.concentrations
        y_vals = [true_rate - equation(true_conc) for (true_conc, true_rate)
                  in zip(reac_obj.concentrations, reac_obj.rates)]

    else:
        x_vals = [x for x, _, _ in reac_obj.get_points(a_isvar)]
        if equations is not None:
            y_vals = [true_rate - eq(true_conc, x_2) for ((true_conc, true_rate, x_2), eq)
                      in zip(reac_obj.get_points(a_isvar), equations)]
        else:
            y_vals = [true_rate - equation(true_conc, x_2) for (true_conc, true_rate, x_2)
                      in reac_obj.get_points(a_isvar)]

        cols = [cm(1.*i/len(x_vals)) for i in range(len(x_vals))]

    # break if no data is present
    if not cols:
        return

    #grid settings
    plot_obj.grid(b=grid)

    # naming
    x_name = "Substrate concentration"
    y_name = "Fit residuals"
    plot_obj.set_xlabel(x_name)
    plot_obj.set_ylabel(y_name)

    x_max = max([max(d_set) for d_set in x_vals])
    x_min = min([min(d_set) for d_set in x_vals])
    y_min = min([min(d_set) for d_set in y_vals])
    y_max = max([max(d_set) for d_set in y_vals])

    x_space = (x_max - x_min) * 0.05
    y_space = (y_max - y_min) * 0.05
    plot_obj.set_xlim(x_min - x_space, x_max + x_space)
    plot_obj.set_ylim(y_min - y_space, y_max + y_space)

    for x_rep, y_rep, count in zip(x_vals, y_vals, range(len(y_vals))):
        alp = 1 if (count == pick or pick == -1) else 0.15
        sel_col = cols.pop()
        plot_obj.plot(x_rep, y_rep, 'o',
                      ms=4,
                      color=sel_col,
                      alpha=alp)
    # plot line
    plot_obj.plot([x_min, x_max], [0, 0], '--', color='#000000')


def plot_fit(plot_obj, x_vals, equation, signal=0, subs2=None, col='black', alp=1):
    """
    Adds fit to current graph
    """

    x_fit = np.array(np.hstack([x for x in x_vals]))

    x_fit = x_fit.ravel()
    x_fit = np.array(sorted(list(set(x_fit))))
    if subs2 is not None:
        y_pred = equation(x_fit, subs2)
    else:
        y_pred = equation(x_fit)
    if signal == 1:
        x_fit = 1 / x_fit
        y_pred = 1 / y_pred
    if signal == 2:
        y_pred = x_fit / y_pred
    if signal == 3:
        x_fit = y_pred / x_fit
    plot_obj.plot(x_fit, y_pred, color=col, alpha=alp)


def calc_ebars(mdata, subset):
    """
    Calculates and returns error bars for DS data
    """
    sets = mdata.AllRates[subset]
    x_vals = mdata.AllVar[subset]
    ebars = []
    for xset, set_x in zip(sets, x_vals):
        set_min = []
        set_mean = []
        set_max = []
        for count in range(len(xset[0])):
            vals = [x[count] for x in xset]
            set_min.append(statistics.mean(vals) - min(vals))
            set_max.append(max(vals) - statistics.mean(vals))
            set_mean.append(statistics.mean(vals))
        ebars.append([set_x[0], set_mean, set_min, set_max])
    return ebars


def plot_dsegraph(reac_obj, plot_obj, signal=0, grid=False, equation=None, equations=None, legend='', a_isvar=True,
                  pick=-1, errors=False):
    """
    Plots points and additional fits
    """
    ebars = calc_ebars(reac_obj, a_isvar)
    sname = reac_obj.nameA if a_isvar else reac_obj.nameB
    plot_singlegraph(reac_obj=reac_obj.get_repres(a_isvar), plot_obj=plot_obj, signal=signal, grid=grid, legend=legend,
                     pick=pick, errorbars=ebars if errors else False, sname=sname)
    s2_means = reac_obj.get_const_mean(a_isvar)
    x_all = [x[0] for x in reac_obj.AllVar[a_isvar]]

    cm = get_cmap('gist_ncar')
    cols = [cm(1.*i/len(x_all)) for i in range(len(x_all))]
    # plot for multiple equations
    if equations is not None:
        for x_vals, x2_vals, eq, count in zip(x_all, s2_means, equations, range(len(equations))):
            alp = 1 if (count == pick or pick == -1) else 0.15
            sel_col = cols.pop()
            plot_fit(plot_obj, x_vals, equation=eq, signal=signal, subs2=x2_vals, col=sel_col, alp=alp)
    # plot for single equations
    else:
        for x_vals, x2_vals in zip(x_all, s2_means):
            sel_col = cols.pop()
            plot_fit(plot_obj, x_vals, equation=equation, signal=signal, subs2=x2_vals, col=sel_col)
