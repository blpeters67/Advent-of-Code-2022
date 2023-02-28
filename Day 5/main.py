def main():
  
  part_1()
  part_2()

##############################################

def get_dict():
  
  dict = {}
  lineWithAmtOfStacks = 0

  with open('input.txt', 'r') as f:
   inputLines = f.readlines()

  for line in inputLines:
    if line[0] == " ":
      lineWithAmtOfStacks += inputLines.index(line)
      break

  nums = inputLines[lineWithAmtOfStacks].strip().replace(' ','')
  for num in nums:
    dict[int(num)] = []

  # loop however many times there are keys in the dict
  for i in range(int(min(dict.keys()))-1,int(max(dict.keys()))):
    # loop the same num of times as the stack with the most crates
    for i2 in range(0,lineWithAmtOfStacks):
      # finds the item by indexing the inputLines and lining it up with the number
      itemToAdd = inputLines[i2][inputLines[lineWithAmtOfStacks].index(str(i+1))]
      if itemToAdd != ' ':
        dict[i+1].extend(itemToAdd)
    # the items get put in backwards order, so we reverse it
    dict[i+1].reverse()
  
  return dict

##############################################

def part_1():
  
  dict = get_dict()

  instructions = get_instructions()
  
  for line in instructions:
    for each in range(line[0]): # move topmost item in dict list from one dict index to other, this many times
      item = dict[line[1]][len(dict[line[1]])-1]
      dict[line[2]].append(item)
      dict[line[1]].pop(len(dict[line[1]])-1)
  
  print('Part 1 answer:')
  for i in range(1,10):
    print(dict[i][len(dict[i])-1],end='')

##############################################

def part_2():

  dict2 = get_dict()

  instructions = get_instructions()

  def performMove(amount, moveFrom, moveTo):
    if amount > len(dict2[moveFrom]):
      amount = len(dict2[moveFrom])
    itemsToMove = dict2[moveFrom][len(dict2[moveFrom])-(amount):len(dict2[moveFrom])]
    [dict2[moveFrom].pop() for i in range(amount)]
    dict2[moveTo].extend(itemsToMove)

  for i in instructions:
    performMove(i[0],i[1],i[2])

  print('\n\nPart 2 answer:')
  for n in range(1,10):
    print(f'{dict2[n][len(dict2[n])-1]}',end='')

##############################################

def get_instructions():
  
  counter = 0
  f = open('input.txt','r').readlines()
  
  for line in f:
    if line.startswith("m") != True:
      counter += 1
    else:
      break
  
  for each in range(0,counter):
    f.pop(0)

  instructions = [line.strip().replace('move ','')
  .replace(' from ',' ').replace(' to ',' ') for line in f]
  instructions = [list(map(int, i.split())) for i in instructions]
  return instructions  

##############################################

main()