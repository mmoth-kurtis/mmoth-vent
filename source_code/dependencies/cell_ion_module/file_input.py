import numpy as np

def init(params):
    print "inside init function"
    model_class = calcium_file_input(params)
    return model_class


class calcium_file_input():

    def __init__(self,params):

        #params is a dictionary defined in the json input files
        # we can be specific here because this module is customizable to user needs
        self.file_path = params["path_to_calcium"][0]
        self.ca = np.load(self.file_path)
        #print np.shape(self.ca)
        #print self.ca[0,0]


    def calculate_concentrations(self,cycle,time,file):
        #print time
        #if time < 0.6:
        #    calcium_value = 3e-7
        #else:
        counter = int(2*time)
        print "counter is " + str(counter)
        calcium_value = self.ca[counter-1,0]
        return calcium_value
