
# We are going to define a model class for each city we model.
# Santa cruz is going to have it's own class
import json
import os
import pandas as pd
import wrtools as wt

class SantaCruz:
    def __init__(self,config):
        print("initializing santa cruz ")

        # set all the parameters by reading the config file
        for key in config:
            setattr(self, key, config[key])

    def run_opt(self,params,policy,verbose=False):
        print("running optimization")

        # So now we are running. Verbose is the other running parameter

        # write the parameter options to the outputfile,
        self.write_params(params,"params.json")

        # initialize our sources
        north_coast = wt.Inflow(self.drought_path+"/north_coast.csv")
        felton_diversion = wt.Inflow(self.drought_path+"/felton_diversion.csv")
        newell_inflow = wt.Inflow(self.drought_path+"/newell_inflow.csv")
        tait_street = wt.Inflow(self.drought_path+"/tait_street.csv")
        #TODO: add groundwater

        #TODO: check they all have the same number of droughts as a little doublecheck-a-roo

        # initialize our City
        city = wt.City( self.income_elasticity, self.MHI)
        city.set_bins(self.household_counts,self.income_bins,self.household_sizes,self.leaks)

        # initialize utility object
        ut = wt.Utility(self.discount_rate)

        # set rates. (see readme for how these work)
        ut.set_fixed_charge(self.base_charge)
        ut.set_baseline_fixed_charge(self.base_charge)
        ut.set_tier_prices(self.tier_prices)
        ut.set_tiers(self.tiers)


        #

        # initialize demand
        res_demand

        non_res_demand








    def write_params(self,params,name):
        #write parameters
        with open(os.path.join(params['output_path'],name), "w+") as outfile:
            json.dump(params, outfile)
        print("writing parameters to ",os.path.join(params['output_path'],name))
