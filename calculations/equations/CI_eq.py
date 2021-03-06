import lmfit
from calculations.equations import FitParam


def my_fiteq(params, subs_c, rate, *_):
    """
    Competitive inhibition (irr) equation for optimization
    """
    km = params['km'].value
    v_max = params['v_max'].value
    inh = params['Inh'].value
    ki = params['ki'].value

    rate_calc = v_max * subs_c / (km + subs_c + km * inh / ki)
    return rate_calc - rate


def create_my_eq(km, v_max, inh, ki, *_):
    """
    Competitive inhibition (irr) equation
    """
    def eq(subs_c, *_):
        return v_max * subs_c / (km + subs_c + km * inh / ki)
    return eq


class CIparams(FitParam):
    """
    Allosteric inhibition parameter class for fitting.
    """
    def __init__(self, km=(1, 0, 100), v_max=(1, 0, 100),
                 inh=(1, 0, 100), ki=(1, 0, 100)):
        FitParam.__int__(self)
        self.add('km', value=km[0], min=km[1], max=km[2])
        self.add('v_max', value=v_max[0], min=v_max[1], max=v_max[2])
        self.add('Inh', value=inh[0], min=inh[1], max=inh[2])
        self.add('ki', value=ki[0], min=ki[1], max=ki[2])

        self.param_order = ['km', 'v_max', 'Inh', 'ki']
        self.units = ['c', 'r', 'c', 'c']
        self.fitf = my_fiteq
        self.eq = create_my_eq
        self.name = 'Competitive inhibition (irr)'
