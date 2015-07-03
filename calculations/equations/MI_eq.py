import lmfit
from calculations.equations import FitParam


def my_fiteq(params, subs_c, rate, *_):
    """
    Mixed inhibition (irr) equation for optimization
    """
    km = params['km'].value
    v_max = params['v_max'].value
    inh = params['inh'].value
    kis = params['kis'].value
    kic = params['kic'].value

    rate_calc = v_max * subs_c / (km * (1 + inh / kis) + subs_c * (1 + inh / kic))
    return rate_calc - rate


def create_my_eq(km, v_max, inh, kis, kic, *_):
    """
    Mixed inhibition (irr) equation
    """
    def eq(subs_c, *_):
        return v_max * subs_c / (km * (1 + inh / kis) + subs_c * (1 + inh / kic))
    return eq


class MIparams(FitParam):
    """
    Mixed inhibition (irr) parameter class for fitting.
    """
    def __init__(self, km=(1, 0, 100), v_max=(1, 0, 100),
                 inh=(1, 0, 100), kis=(1, 0, 100), kic=(1, 0, 100)):
        FitParam.__int__(self)
        self.add('km', value=km[0], min=km[1], max=km[2])
        self.add('v_max', value=v_max[0], min=v_max[1], max=v_max[2])
        self.add('inh', value=inh[0], min=inh[1], max=inh[2])
        self.add('kis', value=kis[0], min=kis[1], max=kis[2])
        self.add('kic', value=kic[0], min=kic[1], max=kic[2])

        self.param_order = ['km', 'v_max', 'inh', 'kis', 'kic']
        self.units = ['c', 'r', 'c', 'c', 'c']
        self.fitf = my_fiteq
        self.eq = create_my_eq
        self.name = 'Mixed inhibition (irr)'
