#python 3

#remaining = 8
#remaining = 6
#remaining = 2

last_assignment = 0

current = 1

prizes = []

remaining = int(input())
while current <= remaining:
    if current > last_assignment and (remaining - current) > current:
        prizes.append(current)
        remaining -= current
        current += 1
    else:
        prizes.append(remaining)
        break
print(len(prizes))

print(" ".join([str(i) for i in prizes]))
    