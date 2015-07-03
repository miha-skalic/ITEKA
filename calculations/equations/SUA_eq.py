import lmfit
from calculations.equations import FitParam


def my_fiteq(params, subs_c, rate, *_):
    """
    Substrate activation (irr) equation for optimization
    """
    ksa = params['ksa'].value
    v_max = params['v_max'].value
    ksc = params['ksc'].value

    rate_calc = v_max * (subs_c / ksa) ** 2 / (1 + subs_c / ksc + subs_c / ksa + (subs_c / ksa) ** 2)
    return rate_calc - rate


def create_my_eq(ksa, v_max, ksc, *_):
    """
    Substrate activation (irr) equation
    """
    def eq(subs_c, *_):
        return v_max * (subs_c / ksa) ** 2 / (1 + subs_c / ksc + subs_c / ksa + (subs_c / ksa) ** 2)
    return eq


class SUAparams(FitParam):
    """
    Mixed activation (irrev) parameter class for fitting.
    """
    def __init__(self, ksa=(1, 0, 100), v_max=(1, 0, 100),
                 ksc=(1, 0, 100)):
        FitParam.__int__(self)
        self.add('ksa', value=ksa[0], min=ksa[1], max=ksa[2])
        self.add('v_max', value=v_max[0], min=v_max[1], max=v_max[2])
        self.add('ksc', value=ksc[0], min=ksc[1], max=ksc[2])

        self.param_order = ['ksa', 'v_max', 'ksc']
        self.fitf = my_fiteq
        self.eq = create_my_eq
        self.name = 'Substrate activation (irr)'
        self.units = ['c', 'r', 'c']