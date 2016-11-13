import lmfit
from calculations.equations import FitParam
import os

def ppmsi_function(params, subsa, rate, subsb, erate, *_):
    """
    Ping pong mechanism equation for optimization
    """
    v_max = params['v_max'].value
    kdb = params['kdb'].value
    kma = params['kma'].value
    kmb = params['kmb'].value
    # E = float(os.environ['Eval'])
    E = erate
    rate_calc = v_max * E * subsb * subsa / (kmb * subsa + (kma * subsb) * (1 + (subsb / kdb)) + subsa * subsb)
    return rate_calc - rate


def create_ppmsi(v_max, kdb, kma, kmb, *_):
    """
    Create Ping pong mechanism equation
    """
    def eq(subsa, subsb, erate):
        # E = float(os.environ['Eval'])
        return v_max * erate * subsb * subsa / (kmb * subsa + (kma * subsb) * (1 + (subsb / kdb)) + subsa * subsb)
    return eq


class PPMSIparams(FitParam):
    """
    lmfit parameter class  for Ping pong mechanism fitting.
    """
    def __init__(self, v_max=(1, 0, 100), kdb=(1, 0, 100), kma=(1, 0, 100), kmb=(1, 0, 100)):
        FitParam.__int__(self)
        lmfit.Parameters.__init__(self)
        self.add('v_max', value=v_max[0], min=v_max[1], max=v_max[2])
        self.add('kdb', value=kdb[0], min=kdb[1], max=kdb[2])
        self.add('kma', value=kma[0], min=kma[1], max=kma[2])
        self.add('kmb', value=kmb[0], min=kmb[1], max=kmb[2])
        self.fitf = ppmsi_function
        self.eq = create_ppmsi
        self.name = 'Ping-pong (substrate inhibition)'
        self.param_order = ['v_max', 'kdb', 'kma', 'kmb']
        self.units = ['r', 'c', 'c', 'c']

def ppm_function(params, subsa, rate, subsb, erate, *_):
    """
    Ping pong mechanism equation for optimization
    """
    v_max = params['v_max'].value
    kma = params['kma'].value
    kmb = params['kmb'].value
    E = erate
    rate_calc = v_max * E  * subsb * subsa / (kmb * subsa + (kma * subsb) + subsa * subsb)
    return rate_calc - rate


def create_ppm(v_max, kma, kmb, *_):
    """
    Create Ping pong mechanism equation
    """
    def eq(subsa, subsb, erate):
        return v_max * erate * subsb * subsa / ((kmb * subsa) + (kma * subsb) + (subsa * subsb))
    return eq


class PPMparams(FitParam):
    """
    lmfit parameter class  for Ping pong mechanism fitting.
    """
    def __init__(self, v_max=(1, 0, 100), kma=(1, 0, 100), kmb=(1, 0, 100)):
        FitParam.__int__(self)
        lmfit.Parameters.__init__(self)
        self.add('v_max', value=v_max[0], min=v_max[1], max=v_max[2])
        self.add('kma', value=kma[0], min=kma[1], max=kma[2])
        self.add('kmb', value=kmb[0], min=kmb[1], max=kmb[2])
        self.fitf = ppm_function
        self.eq = create_ppm
        self.name = 'Ping-pong mechanism'
        self.param_order = ['v_max', 'kma', 'kmb']
        self.units = ['r', 'c', 'c']
