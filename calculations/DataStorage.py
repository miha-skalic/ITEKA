import numpy as np
import random
import os


def random_start(in_params):
    """
    Creates random starting points
    """
    params = in_params
    for param in params:
        params[param].value = random.uniform(params[param].min, params[param].max)
    return params


def transform_data(in_string):
    """
    Transfrom string to np array
    """
    proc_vals = in_string.replace(',', ' ')
    proc_vals = [float(data_point) for data_point in proc_vals.strip().split()]
    return np.array(proc_vals)


class OneSubstrate(object):
    """
    Holds experimental data for one enzyme
    """
    def __init__(self, name, enzymec, tunit='s', cunit='mM'):
        self.replicates = 0
        self.name = name
        self.concentrations = None
        self.rates = None
        self.single = True
        self.enzymec = enzymec
        self.cunit = cunit
        self.tunit = tunit
        self.runit = '({})/({})'.format(cunit, tunit)
        self.setnames = []

    def __len__(self):
        """
        Number of replicates in the set
        """
        return self.replicates

    def __iter__(self):
        for con_rep, rat_rep in zip(self.concentrations, self.rates):
            yield con_rep, rat_rep

    def add_replicate(self, n_concetration, n_rate, transform=True, setname=None):
        """
        Adds replicates
        """
        if transform:
            n_concetration = transform_data(n_concetration)
            n_rate = transform_data(n_rate)
        assert len(n_concetration) == len(n_rate)

        if self.replicates == 0:
            self.concentrations = [n_concetration]
            self.rates = [n_rate]
        else:
            self.concentrations.append(n_concetration)
            self.rates.append(n_rate)
        self.replicates += 1
        setname = 'Replicate ' + str(self.replicates) if setname is None else setname
        self.setnames.append(setname)

    def res_sum(self, fitfunc, *_):
        """
        Return sum of residuals squared based on give function
        """
        return sum((fitfunc(np.hstack(tuple(self.concentrations))) - np.hstack(tuple(self.rates))) ** 2)

    def get_replicates(self):
        return self.replicates

    def is_single(self):
        """
        States if given objects hold information for only one substrate
        """
        return self.single


class TwoSubstrates():
    """
    Stores data for two substrates
    """
    def __init__(self, p_name, aname, bname, is_itc=False, arate=1, brate=1, tunit='s', cunit='mM',
                 enzymec = 1):
        self.nameA = str(aname)
        self.nameB = str(bname)
        self.name = str(p_name)
        self.a_is_var = True
        self.setindex = 0
        self.is_itc = bool(is_itc)
        self.single = False
        self.enzymec = enzymec

        # storage objects
        self.Asets = []
        self.Bsets = []
        self.Aconst = []
        self.Bconst = []
        self.Arates = []
        self.Brates = []

        self.AEnzyme = []
        self.BEnzyme = []

        self.setnames = {True: [], False: []}

        self.AllVar = {True: self.Asets, False: self.Bsets}
        self.AllConst = {True: self.Aconst, False: self.Bconst}
        self.AllRates = {True: self.Arates, False: self.Brates}
        self.stoich = {True: float(brate), False: float(arate)}

        self.Econc = {True: self.AEnzyme, False: self.BEnzyme}

        # units
        self.cunit = cunit
        self.tunit = tunit
        self.runit = '({})/({})'.format(cunit, tunit)

    def change_varible(self):
        """
        Change if substrate A is variable
        """
        self.a_is_var = not self.a_is_var
        self.setindex = 0

    def add_rep(self, varvals, constvar, rates, setpos=None, vinint=1., vadd=0.1):
        """
        Adds replicate to specified set
        """
        if setpos is None:
            setpos = self.setindex

        rates = transform_data(rates)
        constvar = transform_data(constvar)
        varvals = transform_data(varvals)

        assert len(varvals) == len(constvar)
        assert len(constvar) == len(rates)

        self.AllVar[self.a_is_var][setpos].append(varvals)
        self.AllRates[self.a_is_var][setpos].append(rates)
        self.AllConst[self.a_is_var][setpos].append(constvar)

        # enzmy concentration
        econc = [vinint / (vadd * (i + 1.) + vinint) * float(os.environ['Eval']) for i in range(1, len(varvals) + 1)]
        self.Econc[self.a_is_var][setpos].append(econc)

    def add_set(self, varvals, constvals, rates, setname='Nameless_set', vinint=1., vadd=0.1):
        """
        Adds data to sets
        """
        varvals = transform_data(varvals)
        constvals = transform_data(constvals)
        rates = transform_data(rates)

        assert len(varvals) == len(constvals)
        assert len(varvals) == len(rates)

        self.AllVar[self.a_is_var].append([varvals])
        self.AllConst[self.a_is_var].append([constvals])
        self.AllRates[self.a_is_var].append([rates])

        self.setnames[self.a_is_var].append(setname)

        # enzmy concentration
        econc = [vinint / (vadd * (i + 1.) + vinint) * float(os.environ['Eval']) for i in range(1, len(varvals) + 1)]
        self.Econc[self.a_is_var].append([econc])

    def next_set(self):
        """
        Switch appending set to next avaliable
        """
        if self.setindex == len(self.AllConst[self.a_is_var]):
            self.setindex = 0
        else:
            self.setindex += 1

    def isnewset(self):
        """
        Return True if constant substrate needs to be defined
        """
        if self.setindex == len(self.AllConst[self.a_is_var]):
            return True
        elif self.setindex < len(self.AllConst[self.a_is_var]):
            return False
        else:
            raise ValueError('Apeenidng index is to high')

    def is_single(self):
        """
        States if given objects hold information for only one substrate
        """
        return self.single

    def get_last_const(self):
        """
        Returns current constant values
        """
        if self.isnewset():
            return None
        else:
            return self.AllConst[self.a_is_var][self.setindex][-1]

    def get_current_var(self):
        """
        Returns current variable values
        """
        if self.isnewset():
            return None
        else:
            return self.AllVar[self.a_is_var][self.setindex][-1]

    def get_rep_cout(self):
        """
        Returns the number of reps in working set
        """
        if not self.isnewset():
            return len(self.AllRates[self.a_is_var][self.setindex])
        return 0

    def get_stoch_val(self):
        """
        Fetch stoichometry value of current variable substrate
        """
        return self.stoich[self.a_is_var]

    def get_points(self, a_var=True):
        """
        Returns all points (subA, rate & sub2)
        if not a_var returns data for when a is not variable else when it is variable
        """
        varss = self.AllVar[a_var]
        consts = self.AllConst[a_var]
        rates = self.AllRates[a_var]
        enzyms = self.Econc[a_var]

        for i in range(len(varss)):
            var = np.concatenate(varss[i])
            const = np.concatenate(consts[i])
            rate = np.concatenate(rates[i])
            enzyms = np.concatenate(enzyms[i])
            yield var, rate, const, enzyms

    def get_repres(self, a_var=True):
        """
        Returns OneSubstrate objects that reprisents data.
        """
        new_class = OneSubstrate('temp', cunit=self.cunit, tunit=self.tunit, enzymec=self.enzymec)
        n = 0
        for concx, ratex, _, _ in self.get_points(a_var):
            new_class.add_replicate(concx, ratex, transform=False, setname=self.setnames[a_var][n])
            n += 1
        return new_class

    def get_allpoints(self, a_var=True):
        """
        Returs all data poits in a array
        """
        fvar = np.array([])
        fcost = np.array([])
        frate = np.array([])
        fenzym = np.array([])

        for concx, ratex, conccx, enzyx in self.get_points(a_var):
            fvar = np.append(fvar, concx)
            fcost = np.append(fcost, conccx)
            frate = np.append(frate, ratex)
            fenzym = np.append(fenzym, enzyx)

        return fvar, frate, fcost, fenzym

    def get_const_mean(self, a_isvar=True):
        """
        Returns list of means for second values
        """
        all_set_means = []
        for my_set in self.AllConst[a_isvar]:
            all_set_means.append(np.array(my_set).mean(axis=0))
        return all_set_means

    def res_sum(self, fitfunc, a_var):
        """
        Return sum of residuals squared based on give function
        """
        a_var, a_rate, a_const, a_enzyme = self.get_allpoints(a_var)
        return sum((fitfunc(a_var, a_const, a_enzyme) - a_rate) ** 2)
