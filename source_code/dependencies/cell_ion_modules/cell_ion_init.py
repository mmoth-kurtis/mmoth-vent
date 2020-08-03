# So far these are only needed to test standalone
import sys
import numpy as np
sys.path.append("/home/fenics/shared/source_code/dependencies/cell_ion_modules")
#sys.path.append("/Users/charlesmann/Academic/UK/fenics/source_code/dependencies/cell_ion_module")

## Class for cell ion schemes
#
#calculate calcium concentration (and other concentrations depending on the model) and ion voltage
class cell_ion_init():

    def __init__(self,params):

        # Specify model to be ran
        model_name = params["model"][0]
        model_params = params["model_inputs"]

        #base_dir = "cell_ion_module"
        #model_name = base_dir + temp
        #model_name = "three_state_calcium"

        #print model_name

        # Import the model
        self.model = __import__(model_name)
        self.model_class = self.model.init(model_params)


        #self.model.init(model_params)
        #help(self.model)
