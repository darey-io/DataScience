import datetime
from collections import namedtuple

# accepts data range, get the top and lowwer values and calculate the class width
class frequencyDistribution():
    def __init__ (self, data):
        self.data = data
        self.upper = max(self.data)
        self.lower = min(self.data)
        self.classwidth = int(float(self.upper)/self.lower + (self.upper % self.lower > 0)) #Always round up the result

#Take care of capturing the last bit of the tuples

    def distributeClassWidth(self):
        self.iter = 0   #Use this to check the iteration is running the first time or not.
        self.count = 0  #Use this for the while loop
        self.tempdata = []
        self.data_distribution = range(self.lower, self.upper + 1, self.classwidth)
        for self.n in range(self.upper):
            if self.iter == 0:
                self.tup1 = self.lower
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
'''
    def classMidPoint(self):
        for self.tuple in self.tempdata:
            print (self.tuple)

    def __str__(self):
        return self.tempdata

'''


data = [23,44,20,17,34,19,35,15,45]
a = frequencyDistribution(data)
print(a.distributeClassWidth())[0][1]



print("\n")
print("********************************\n")

data2 = [23,56,44,20,17,34,19,35,15,45, 67, 84, 33, 78, 93]
b = frequencyDistribution(data2)
print(b.classMidPoint())

