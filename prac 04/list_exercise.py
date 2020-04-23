def main():
    numbers = []
    for x in range(5):
        input_numbers = int(input("Enter number here: "))
        numbers.append(input_numbers)

    print("The first number in the sequence is {}". format(numbers[0]))
    print("The last number in the sequence is {}".format(numbers[4]))
    print("The smallest number is {}".format(min(numbers)))
    print("The largest number in the sequence is {}".format(max(numbers)))

    total = sum(numbers)
    average = total/len(numbers)
    print("The average is {}".format(average))

    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    input_name = input("Enter your name: ")
    if input_name not in usernames:
        print("Access denied")
    else:
        print("Access Granted")

if __name__ == '__main__':
    main()