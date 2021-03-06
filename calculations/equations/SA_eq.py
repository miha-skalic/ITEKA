import lmfit
from calculations.equations import FitParam


def my_fiteq(params, subs_c, rate, *_):
    """
    Mixed inhibition (irr) equation for optimization
    """
    kms = params['kms'].value
    v_max = params['v_max'].value
    ka = params['ka'].value
    act = params['act'].value

    rate_calc = v_max * subs_c * act / (kms * ka + (kms + subs_c) * act)
    return rate_calc - rate


def create_my_eq(kms, v_max, ka, act, *_):
    """
    Mixed inhibition (irr) equation
    """
    def eq(subs_c, *_):
        return v_max * subs_c * act / (kms * ka + (kms + subs_c) * act)
    return eq


class SAparams(FitParam):
    """
    Mixed inhibition (irr) parameter class for fitting.
    """
    def __init__(self, kms=(1, 0, 100), v_max=(1, 0, 100),
                 ka=(1, 0, 100), act=(1, 0, 100)):
        FitParam.__int__(self)
        self.add('kms', value=kms[0], min=kms[1], max=kms[2])
        self.add('v_max', value=v_max[0], min=v_max[1], max=v_max[2])
        self.add('ka', value=ka[0], min=ka[1], max=ka[2])
        self.add('act', value=act[0], min=act[1], max=act[2])

        self.param_order = ['kms', 'v_max', 'ka', 'act']
        self.fitf = my_fiteq
        self.eq = create_my_eq
        self.name = 'Specific activation (irrev)'
        self.units = ['c', 'r', 'c', 'c']