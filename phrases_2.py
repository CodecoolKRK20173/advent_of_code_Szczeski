def main():

    with open('phrases_4.txt', 'r') as data:
        valid = 0
        invalid = 0
        for line in data:
            if check_line(line):
                valid += 1
            else:
                invalid += 1
        print("Valid : {}\nInvalid: {}".format(valid, invalid))


def check_line(line):

    words = {}

    for el in line.split():
        el = sorted(el)
        word = ''.join(el)
        if word in words:
            return False
        words[word] = 1

    return True

main()