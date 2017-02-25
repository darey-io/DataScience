import stats

data2 = [23,56,44,20,17,34,19,35,15,45, 67, 84, 33, 78, 93, 23,44,20,17,34,19,35,15,45]

b = stats.frequencyDistribution(data2)
print (b.distributeClassWidth())
midpoint = b.classMidPoint()

print(midpoint)
#for n in midpoint:
 #   print midpoint[1]
