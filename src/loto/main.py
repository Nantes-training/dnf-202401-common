import random

if __name__ == '__main__':
    values = input("Enter 5 number separate by a comma between 1 and 50\n")
    while len(values.split(",")) != 5:
        values = input("Enter 5 number separate by a comma between 1 and 50, retard\n")
    values = values.replace(" ", "")
    loto_values = []
    for _ in range(0, 5):
        loto_values.append(random.randint(1, 50))
    if values.strip().split(",")[0] == loto_values[0] and values.strip().split(",")[1] == loto_values[1] and values.strip().split(",")[2] == loto_values[2] and \
            values.strip().split(",")[3] == loto_values[3] and values.strip().split(",")[4] == loto_values[4]:
        print("YOU WIN 1.000.000 $ !!!")
    else:
        print(f"You're shit\n Winner's number was: {loto_values}")
