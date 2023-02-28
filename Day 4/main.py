input = open('input.txt').readlines()
part_one, part_two = 0, 0
for line in input:
  first_pair, second_pair = line.split(',')
  start_one, end_one = first_pair.split('-')
  start_two, end_two = second_pair.split('-')
  start_one, start_two, end_one, end_two = int(start_one), int(start_two), int(end_one), int(end_two)
  if start_one >= start_two and end_two >= end_one or start_two >= start_one and end_one >= end_two:
    part_one += 1
  
  # p2
  if start_one >= start_two and start_one <= end_two:
    part_two += 1
    continue
  elif end_one >= start_two and start_one <= end_two:
    part_two += 1
    continue
  elif start_two >= start_one and start_two <= end_one:
    part_two += 1
    continue
  elif end_two >= start_one and start_two <= end_one:
    part_two += 1
    continue
  else:
    continue

print('p1: ',part_one)
print('p2: ',part_two)
  
