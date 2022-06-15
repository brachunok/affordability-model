
# We are going to define a model class for each city we model.
# Santa cruz is going to have it's own class
import json
import os
import pandas as pd

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

        # initiaize the drought scenarios

        # where i'm at: restructure the drought files to be one file for each
        # source with n columns for n droughts
        # in WR tools, make a class for each source, and when we initialize the source,
        # read in the file to go along with it




    def write_params(self,params,name):
        #write parameters
        with open(os.path.join(params['output_path'],name), "w+") as outfile:
            json.dump(params, outfile)
        print("writing parameters to ",os.path.join(params['output_path'],name))
