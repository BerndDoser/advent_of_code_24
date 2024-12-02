nb_safe = 0
for line in open('day2/data.txt'):
    code = line.strip().split()
    code = list(map(int, code))
    
    # First check if the code ist sorted
    if code != sorted(code) and code != sorted(code, reverse=True):
        print("unsafe")
        continue 
    
    # Then check if the differences are between 1 and 3
    code.sort()
    differences = [i-j for i, j in zip(code[1:], code[:-1])]
    print(code)
    print(differences)
    if min(differences) > 0 and max(differences) < 4:
        print("safe")
        nb_safe += 1
    else:
        print("unsafe")

print("answer:", nb_safe)
