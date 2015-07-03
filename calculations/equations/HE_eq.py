import lmfit
from calculations.equations.fitparam import FitParam


def he_function(params, subs_c, rate, *_):
    """
    Hills equation for optimization
    """
    # return (x[0] * sub_rate[:, 0] ** x[2] / (x[1] + sub_rate[:, 0] ** x[2])) - sub_rate[:, 1]
    kh = params['kh'].value
    v_max = params['v_max'].value
    n = params['n'].value

    rate_calc = (v_max * subs_c ** n) / (kh + subs_c ** n)
    return rate_calc - rate


def create_he(kh, v_max, n, *_):
    """
    Create hills equation
    """
    def eq(x, *_):
        return (v_max * x ** n) / (kh + x ** n)
    return eq


class HEparams(FitParam):
    """
    lmfit parameter class for Hills fitting.
    """
    def __init__(self, kh=(1, 0, 100), vmax=(1, 0, 100), n=(1, 0, 10)):
        FitParam.__int__(self)
        lmfit.Parameters.__init__(self)
        self.add('kh', value=kh[0], min=kh[1], max=kh[2])
        self.add('v_max', value=vmax[0], min=vmax[1], max=vmax[2])
        self.add('n', value=n[0], min=n[1], max=n[2])
        self.fitf = he_function
        self.eq = create_he
        self.name = 'Hills equation'
        self.param_order = ['kh', 'v_max', 'n']
        self.units = ['c', 'r', '']