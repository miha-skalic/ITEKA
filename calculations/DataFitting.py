"""
Functions and classes for data fitting
"""
import lmfit
import random
from calculations.equations import *
import numpy as np
from copy import deepcopy


def random_start(in_params):
    """
    Creates random starting points
    """
    params = in_params
    for param in params:
        params[param].value = random.uniform(params[param].min, params[param].max)
    return params


def get_scaling_factor(x_val, y_val):
    """
    return scaling factor, given values
    """
    for i in range(1, 15):
        if y_val * 10 ** i > x_val:
            # print('scailed to {}'.format(10**(i - 1)))
            return 10**(i - 1)
    # print('Failed to scale')
    return 1


def find_fit(param_object, inicializations, *fitpoints):
    """
    Returns best fit for a given function
    """
    # # scale up rates
    # scaling_factor = get_scaling_factor(np.mean(fitpoints[0]), np.mean(fitpoints[1]))
    # fitpoints = list(fitpoints)
    # fitpoints[1] *= scaling_factor
    # param_object['v_max'].value *= scaling_factor
    # param_object['v_max'].max *= scaling_factor
    # param_object['v_max'].min *= scaling_factor

    # # Multiple Reruns
    param_object = deepcopy(param_object)
    best_fit = param_object.get_solution(*fitpoints)
    # rerun i times
    #for i in range(5):
    #    best_fit.minimize()

    # search for random inicialization fits
    if inicializations > 0:
        alt_fits = [random_start(param_object).get_solution(*fitpoints) for _ in range(inicializations)]
        best_fit = min(alt_fits + [best_fit], key=lambda sol: sum(sol.residual**2))

    # # scale down
    # best_fit.params['v_max'].value /= scaling_factor
    # best_fit.params['v_max'].max /= scaling_factor
    # best_fit.params['v_max'].min /= scaling_factor
    # best_fit.residual /= scaling_factor

    # append the equation
    best_fit.function = param_object.eq(*[best_fit.values[idx] for idx in param_object.param_order])
    best_fit.units = param_object.units
    best_fit.get_units = param_object.get_units
    return best_fit
