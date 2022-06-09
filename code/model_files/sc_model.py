
# We are going to define a model class for each city we model.
# Santa cruz is going to have it's own class

from optparse import OptionParser


class SantaCruz:
    def __init__(self,config):
        print("initializing santa cruz ")

        # set all the parameters by reading the config file
        parser = OptionParser()
        parser.



    def run_opt(self,params):
        print("running optimization")
        # this just runs verbose and silences the outputs

        self.run_verbose(params,verb=False)

    def run_verbose(self, params,verb=True):
        # this is the actual model running
        print("running one")


