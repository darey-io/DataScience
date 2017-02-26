import stats

data2 = [2,5,4,11,10]

b = stats.frequencyDistribution(data2)
print (b.distributeClassWidth())
midpoint = b.classMidPoint()

print(midpoint)
#for n in midpoint:
 #   print midpoint[1]
