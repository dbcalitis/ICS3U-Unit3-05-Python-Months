#!/usr/bin/env python3

# Created by: Daria Bernice Calitis
# Created on: Sept 2021
# This program prints the name of a month based on user input


def main():
    # This function prints the name of a month based on user input

    # input
    month_number = int(input("Enter the number of a month (ex:January = 1): "))

    # process & output
    if month_number == 1:
        print("January")
    elif month_number == 2:
        print("February")
    elif month_number == 3:
        print("March")
    elif month_number == 4:
        print("April")
    elif month_number == 5:
        print("May")
    elif month_number == 6:
        print("June")
    elif month_number == 7:
        print("July")
    elif month_number == 8:
        print("August")
    elif month_number == 9:
        print("September")
    elif month_number == 10:
        print("October")
    elif month_number == 11:
        print("November")
    elif month_number == 12:
        print("December")
    else:
        print("Invalid number")

    print("\nDone.")


if __name__ == "__main__":
    main()
