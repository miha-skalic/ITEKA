import lmfit


class FitParam(lmfit.Parameters):
    """
    Parent class for fit equations
    """
    def __int__(self):
        lmfit.Parameters.__init__(self)
        self.initializations = 0

    def change_value(self, parameter, new_value):
        """
        Changes default value for parameters
        """
        self[parameter].set(value=new_value)

    def change_all(self, new_vals):
        """
        Sets new values for parameter
        """
        for param, nu in zip(self.param_order, range(6)):
            self[param].set(value=new_vals[nu][0], min=new_vals[nu][1], max=new_vals[nu][2])

    def get_solution(self, *fitpoints):
        """
        Uses lmfit to find optimal solution
        first point is concentration, followed by rate (and constant concentration)
        """
        return lmfit.minimize(self.fitf, self, args=fitpoints)

    def get_units(self, par, dat_obj):
        idx = self.param_order.index(par)
        simbl = self.units[idx]
        if simbl == 'c':
            return dat_obj.cunit
        elif simbl == 'r':
            return dat_obj.runit
        elif simbl == '':
            return ''
