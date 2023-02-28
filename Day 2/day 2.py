input = open('input.txt','r')
scores = 0

# x lose, y draw, z win
# 1 rock, 2 paper, 3 scissors
# 0 loss, 3 draw, 6 win
for each in input:
  if each.startswith('A'):   # rock
    if each[2] == 'X':       # scissors
      scores += 3
    elif each[2] == 'Y':     # rock
      scores += 4
    else:                    # paper
      scores += 8

    
  elif each.startswith('B'): # paper
    if each[2] == 'X':       # rock
      scores += 1
    elif each[2] == 'Y':     # paper
      scores += 5
    else:                    # scissors
      scores += 9

  
  else:                      # scissors
    if each[2] == 'X':       # paper
      scores += 2
    elif each[2] == 'Y':     # scissors
      scores += 6
    else:                    # rock
      scores += 7


print(scores)