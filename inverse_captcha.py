given_number = input("Type a number: ")

number_length = len(given_number)

summary = 0

is_game_on = True
while is_game_on:

    for i, el in enumerate(given_number):
        if i+1 == number_length:
            if given_number[0] == given_number[-1]:
                summary += int(given_number[0])
                is_game_on = False
                break
            else:
                is_game_on = False
                break
        if int(given_number[i]) == int(given_number[i+1]):
            summary += int(given_number[i])

print("Summarize of all digitis matching the next one is : {}".format(summary))