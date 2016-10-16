import lmfit
from calculations.equations import FitParam
import os

def ainh_function(params, subs_c, rate, *_):
    """
    Allosteric inhibition equation for optimization
    """
    ks = params['ks'].value
    v_max = params['v_max'].value
    n = params['n'].value
    l = params['L'].value
    inh = params['Inh'].value
    ki = params['ki'].value

    E = float(os.environ['Eval'])

    rate_calc = v_max * E * subs_c * (ks + subs_c) ** (n-1) / (l * (ks * (1 + inh / ki)) ** n + (ks + subs_c) ** n)
    return rate_calc - rate


def create_ainh(ks, v_max, n, l, inh, ki, *_):
    """
    Create Allosteric inhibition equation
    """
    def eq(subs_c, *_):
        E = float(os.environ['Eval'])
        return v_max * E * subs_c * (ks + subs_c) ** (n-1) / (l * (ks * (1 + inh / ki)) ** n + (ks + subs_c) ** n)
    return eq


class AInHparams(FitParam):
    """
    Allosteric inhibition parameter class for fitting.
    """
    def __init__(self, ks=(1, 0, 100), v_max=(1, 0, 100), n=(1, 0, 100),
                 l=(1, 0, 100), inh=(1, 0, 100), ki=(1, 0, 100)):
        FitParam.__int__(self)
        self.add('ks', value=ks[0], min=ks[1], max=ks[2])
        self.add('v_max', value=v_max[0], min=v_max[1], max=v_max[2])
        self.add('n', value=n[0], min=n[1], max=n[2])
        self.add('L', value=l[0], min=l[1], max=l[2])
        self.add('Inh', value=inh[0], min=inh[1], max=inh[2])
        self.add('ki', value=ki[0], min=ki[1], max=ki[2])

        self.param_order = ['ks', 'v_max', 'n', 'L', 'Inh', 'ki']
        self.units = ['c', 'r', 'c', '', 'c', 'c']
        self.fitf = ainh_function
        self.eq = create_ainh
        self.name = 'Allosteric inhibition (MWC)'
