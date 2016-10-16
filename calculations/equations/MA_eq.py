import lmfit
from calculations.equations import FitParam
import os

def my_fiteq(params, subs_c, rate, *_):
    """
    Mixed activation (irrev) equation for optimization
    """
    kms = params['kms'].value
    v_max = params['v_max'].value
    act = params['act'].value
    kac = params['kac'].value
    kas = params['kas'].value
    E = float(os.environ['Eval'])
    rate_calc = v_max * E * subs_c * act / (kms * (kas + act) + subs_c * (kac + act))
    return rate_calc - rate


def create_my_eq(kms, v_max, act, kac, kas, *_):
    """
    Mixed activation (irrev) equation
    """
    def eq(subs_c, *_):
        E = float(os.environ['Eval'])
        return v_max * E * subs_c * act / (kms * (kas + act) + subs_c * (kac + act))
    return eq


class MAparams(FitParam):
    """
    Mixed activation (irrev) parameter class for fitting.
    """
    def __init__(self, kms=(1, 0, 100), v_max=(1, 0, 100),
                 act=(1, 0, 100), kac=(1, 0, 100), kas=(1, 0, 100)):
        FitParam.__int__(self)
        self.add('kms', value=kms[0], min=kms[1], max=kms[2])
        self.add('v_max', value=v_max[0], min=v_max[1], max=v_max[2])
        self.add('act', value=act[0], min=act[1], max=act[2])
        self.add('kac', value=kac[0], min=kac[1], max=kac[2])
        self.add('kas', value=kas[0], min=kas[1], max=kas[2])

        self.param_order = ['kms', 'v_max', 'act', 'kac', 'kas']
        self.units = ['c', 'r', 'c', 'c', 'c']
        self.fitf = my_fiteq
        self.eq = create_my_eq
        self.name = 'Mixed activation (irrev)'
