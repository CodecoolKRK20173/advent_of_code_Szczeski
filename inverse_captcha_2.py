def inverse_captcha(number_to_check):
    length_of_string = len(number_to_check)
    next_to_check = length_of_string // 2
    summary = 0

    for i, number in enumerate(number_to_check):
        idx_next = i + next_to_check
        if idx_next >= length_of_string:
            idx_next -= length_of_string
        if number == number_to_check[idx_next]:
            summary += int(number)

    return summary


def main():
    number_to_check = input("Type the number to check: ")

    if int(number_to_check) % 2 != 0:
        raise ValueError('Type number with even number of elements')
    
    summary = inverse_captcha(number_to_check)

    print("Final sum of matches halfway around the given number is : {}".format(summary))

main()