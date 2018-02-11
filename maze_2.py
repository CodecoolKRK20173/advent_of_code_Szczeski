def open_file(filename):
    with open(filename, 'r') as data:
        numbers = [int(n) for n in data]
        return numbers


def jump_on_list(numbers):
    steps = 0
    i = 0
    while i < len(numbers):
        steps += 1
        if numbers[i] >= 3:
            numbers[i] -= 1
            i += numbers[i] + 1
        else:
            numbers[i] += 1
            i += numbers[i] - 1
            
    return steps


def main():
    numbers = open_file('maze_input.txt')
    steps = jump_on_list(numbers)

    print(steps)

main()
