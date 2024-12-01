left = []
right = []
for line in open('day1/data.txt'):
    l, r = line.strip().split()
    left.append(int(l))
    right.append(int(r))
    
left.sort()
right.sort()

distance = 0
for i in range(len(left)):
    distance += abs(left[i] - right[i])

print("answer:", distance)
