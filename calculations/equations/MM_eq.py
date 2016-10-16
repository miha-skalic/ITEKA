import lmfit
from calculations.equations import FitParam
import os

def mm_function(params, subs_c, rate, *_):
    """
    Michaelis–Menten equation for optimization
    """
    km = params['km'].value
    v_max = params['v_max'].value
    E = float(os.environ['Eval'])

    rate_calc = v_max * E * subs_c / (km + subs_c)
    return rate_calc - rate


def create_mm(km, v_max, *_):
    """
    Create hills equation
    """
    def eq(x, *_):
        E = float(os.environ['Eval'])

        return v_max * E * x / (km + x)
    return eq


class MMparams(FitParam):
    """
    lmfit parameter class for MM fitting.
    """
    def __init__(self, km=(1, 0, 100), v_max=(1, 0, 100)):
        FitParam.__int__(self)
        self.add('km', value=km[0], min=km[1], max=km[2])
        self.add('v_max', value=v_max[0], min=v_max[1], max=v_max[2])
        self.param_order = ['km', 'v_max']
        self.units = ['c', 'r']
        self.fitf = mm_function
        self.eq = create_mm
        self.name = 'Michaelis-Menten equation'
