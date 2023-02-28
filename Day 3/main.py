f = open('input.txt','r')
rucksackHalf1, rucksackHalf2, duplicates, duplicatesValues, rucksackList = [], [], [], [], []
for each in f:
  rucksackList.append(each.rstrip())
f.close()
for each in rucksackList:
  rucksackHalf1.append(each[0:int(len(each)/2)])
  rucksackHalf2.append(each[int(len(each)/2):int(len(each))])
counter = 0
for each in rucksackHalf1:
  for letter in each:
    if letter in rucksackHalf2[counter]:
      duplicates.append(letter)
      break
    else:
      pass
  counter += 1
for each in duplicates:
  if each.isupper():
    duplicatesValues.append(ord(each)-38)
  else:
    duplicatesValues.append(ord(each)-96)
print(f'p1 sum is {sum(duplicatesValues)}')
f.close()
rucksacksToCheck, everyThirdRucksack, duplicates, duplicatesValues, counter1, counter2 = open('input.txt','r').readlines(), [], [], [], -2, -1
for each in range(0,len(rucksacksToCheck), 3):
  everyThirdRucksack.append(rucksacksToCheck[each])
for each in rucksacksToCheck:
  if each in everyThirdRucksack:
    rucksacksToCheck.pop(rucksacksToCheck.index(each))
for each in everyThirdRucksack:
  counter1 += 2
  counter2 += 2
  for letter in each:
    if letter in rucksacksToCheck[counter1] and letter in rucksacksToCheck[counter2]:
      duplicates.append(letter)
      break
    else:
      pass
for each in duplicates:
  if each.isupper():
    duplicatesValues.append(ord(each)-38)
  else:
    duplicatesValues.append(ord(each)-96)
print(f'p2 sum is {sum(duplicatesValues)}')