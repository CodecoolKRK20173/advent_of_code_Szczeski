number_to_check = int(input('Type number you want to check steps for : '))

# which layer and basically a wheel radius of a wheel written in square with side of length 2n
n = 1
i = 1
if number_to_check == 1:
    steps = 0
else:
    while i < number_to_check:
        # 2 for corner of the next layer
        n += 2
# n**2 number representing bottom right corner of the layer
        i = n**2
# list of corners,k in range(5) because for first wall of layer it couldn't find number for given condition
    corners = [i - k*(n - 1) for k in range(5)]

    for c in corners:
        # distance from corner to the number to check (absolute value)
        distance = abs(c - number_to_check)

        if distance <= (n-1)//2:
            steps = n - 1 - distance
            break

print(steps)