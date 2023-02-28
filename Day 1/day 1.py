fileHandler = open('input.txt', 'r')
tempList, allCals, tempNum, allCalsSum = [], [], 0, []
for each in fileHandler:
  if each.isnumeric() != True:
    allCals.append(sum(tempList))
    tempList = []
  else:
    tempList.append(int(each.rstrip('\n')))
for each in range(3):
  allCalsSum.append(max(allCals))
  allCals.pop(allCals.index(max(allCals)))
print(sum(allCalsSum))

  
