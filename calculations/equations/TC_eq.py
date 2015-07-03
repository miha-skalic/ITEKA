import lmfit
from calculations.equations import FitParam


def tc_function(params, subsa, rate, subsb, *_):
    """
    Ternary complex mechanism equation for optimization
    """
    v_max = params['v_max'].value
    kda = params['kda'].value
    kma = params['kma'].value
    kmb = params['kmb'].value

    rate_calc = v_max * subsb * subsa / (kda * kmb + kmb * subsa + kma * subsb + subsb * subsa)
    return rate_calc - rate


def create_tc(v_max, kda, kma, kmb, *_):
    """
    Ternary complex mechanism equation
    """
    def eq(subsa, subsb):
        return v_max * subsb * subsa / (kda * kmb + kmb * subsa + kma * subsb + subsb * subsa)
    return eq


class TCparams(FitParam):
    """
    lmfit parameter class ternary complex mechanism fitting.
    """
    def __init__(self, v_max=(1, 0, 100), kda=(1, 0, 100), kma=(1, 0, 100), kmb=(1, 0, 100)):
        FitParam.__int__(self)
        lmfit.Parameters.__init__(self)
        self.add('v_max', value=v_max[0], min=v_max[1], max=v_max[2])
        self.add('kda', value=kda[0], min=kda[1], max=kda[2])
        self.add('kma', value=kma[0], min=kma[1], max=kma[2])
        self.add('kmb', value=kmb[0], min=kmb[1], max=kmb[2])
        self.fitf = tc_function
        self.eq = create_tc
        self.name = 'Ternary complex'
        self.param_order = ['v_max', 'kda', 'kma', 'kmb']
        self.units = ['r', 'c', 'c', 'c']

def tcsi_function(params, subsa, rate, subsb, *_):
    """
    Substrate inhibited ternary complex mechanism equation for optimization
    """
    v_max = params['v_max'].value
    kma = params['kma'].value
    kmb = params['kmb'].value
    kda = params['kda'].value
    ksib = params['ksib'].value

    rate_calc = v_max * subsb * subsa / (kda * kmb + kmb * subsa + kma * subsb + subsa * subsb * (1 + (subsb / ksib)))
    return rate_calc - rate


def create_tcsi(v_max, kma, kmb, kda, ksib, *_):
    """
    Substrate inhibited ternary complex equation
    """
    def eq(subsa, subsb):
        return v_max * subsb * subsa / (kda * kmb + kmb * subsa + kma * subsb + subsa * subsb * (1 + (subsb / ksib)))
    return eq


class TCSIparams(FitParam):
    """
    lmfit parameter class for Substrate inhibited ternary complex mechanism fitting.
    """
    def __init__(self, v_max=(1, 0, 100), kma=(1, 0, 100), kmb=(1, 0, 100), kda=(1, 0, 100), ksib=(1, 0, 100)):
        FitParam.__int__(self)
        lmfit.Parameters.__init__(self)
        self.add('v_max', value=v_max[0], min=v_max[1], max=v_max[2])
        self.add('kma', value=kma[0], min=kma[1], max=kma[2])
        self.add('kmb', value=kmb[0], min=kmb[1], max=kmb[2])
        self.add('kda', value=kda[0], min=kda[1], max=kda[2])
        self.add('ksib', value=ksib[0], min=ksib[1], max=ksib[2])
        self.fitf = tcsi_function
        self.eq = create_tcsi
        self.name = 'Ternary complex (substrate inhibition)'
        self.param_order = ['v_max', 'kma', 'kmb', 'kda', 'ksib']
        self.units = ['r', 'c', 'c', 'c', 'c']
