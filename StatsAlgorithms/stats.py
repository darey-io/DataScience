from __future__ import division
if __name__ == '__main__':
    print('Please import this module before using it')
else:

    class frequencyDistribution():

        def __init__(self, data):

            self.data = data
            self.upper = max(self.data)                 #Get the lower limit of the data
            self.lower = min(self.data)                 #Get the upper limit of the data
            self.classwidth = int(float(self.upper)/self.lower + (self.upper % self.lower > 0))     # Compute the classwidth and Always round up the result
#There is a bug here and we need to handle ZeroDivisionError for self.classwidth
#Define the function that distributes the data based on the classwidth

        def distributeClassWidth(self):
            self.iter = 0                                 # Use the iter variable to coordinate what code to run the first time and subsequent times
            self.tempdata = []                            #Get an empty List
            for self.n in range(self.upper):              #Start the loop here
                if self.iter == 0:                        #Check if this is the first loop
                    self.tup1 = self.lower                #Even though i am not using TUPLES, i am using the terminology to indicate that the sub-lists are in the form of a tuple
                    self.tup2 = self.tup1 + self.classwidth
                    self.tuple = [self.tup1, self.tup2]
                    self.tempdata.append(self.tuple)
                    self.tup1 = self.tup2 + 1
                    self.iter += 1
                else:
                    self.tup2 = self.tup1 + self.classwidth
                    self.tuple = [self.tup1, self.tup2]
                    self.tempdata.append(self.tuple)
                    if self.tup2 > self.upper:
                        break
                    self.tup1 = self.tup2 + 1
            return self.tempdata

# Improve this function later to be able to reference indexes of the returned data
        def classMidPoint(self):
            self.distributed_data = self.distributeClassWidth()
            self.midpoint = []
            for self.n in self.distributed_data:
                self.tmp_midpoint = [self.n, float(self.n[0] + self.n[1])/2]
                self.midpoint.append(self.tmp_midpoint)
            return self.midpoint

        def __str__(self):
            return self.tempdata
            return self.tmp_midpoint






