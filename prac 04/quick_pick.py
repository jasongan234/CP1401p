"""https://github.com/jasongan234/CP1401p/blob/master/prac%2004/quick_pick.py"""
import random

def main():
    smallest_number = 1
    largest_number = 45
    maximum_numbers_on_line= 6
    quick_picks = int(input("Enter number of quick picks:"))

    for i in range(quick_picks):
        quick_picks_list = []
        for j in range(maximum_numbers_on_line):
            random_numbers = random.randint(smallest_number, largest_number)
            while random_numbers in quick_picks_list:
                random_numbers = random.randint(smallest_number, largest_number)
            quick_picks_list.append(random_numbers)
        quick_picks_list.sort()
        print(" ".join("{:2}".format(random_numbers) for random_numbers in quick_picks_list))

main()