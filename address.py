#!/usr/bin/env python3

# Created by : Kent
# Created on : December 2022
# This program prints out your name and address using default function parameters


def full_name(first_name, last_name, middle_name=None):

    # return the full formal name
    full_name = first_name
    if middle_name != None:
        full_name = full_name + " " + middle_name[0]
    full_name = full_name + " " + last_name

    return full_name


def address(post, address, city, province, apt=None):

    # return the full formal
    full_address = address
    if apt != None:
        full_address = "Unit :" + apt + " " + full_address
    full_address = full_address + ", " + city + ", " + province + "\n" + post

    return full_address


def main():
    # gets a users name and prints out their formal name
    middle_name = None
    apt_num = None

    first_name = input("Enter your first name: ")
    question = input("Do you have a middle name? (y/n): ")
    if question.upper() == "Y" or question.upper() == "YES":
        middle_name = input("Enter your middle name: ")
    last_name = input("Enter your last name: ")

    # Checking if the user has a middle name.
    if middle_name != None:
        name = full_name(first_name, last_name, middle_name)
        name = name.upper()
    else:
        name = full_name(first_name, last_name)
        name = name.upper()

    # Second question to ask the if the user has an apt number.
    question_2 = input("Do you live in an apartment? (y/n): ")
    if question_2.upper() == "Y" or question_2.upper() == "YES":
        apt_num = input("Enter your apartment number: ")
    user_address = input("Enter the address (Street number, Street name): ")
    user_city = input("Enter the city: ")
    user_province = input("Enter the province: ")
    post_code = input("What is your residence post code?: ")

    # Checking if the user lives in an apt.
    if apt_num != None:
        final_address = address(
            post=post_code, address=user_address, city=user_city, province=user_province
        )
        final_address = final_address.upper()
    else:
        final_address = address(
            post=post_code,
            address=user_address,
            city=user_city,
            province=user_province,
            apt=apt_num,
        )
        final_address = final_address.upper()
    print(name + "\n" + final_address)


if __name__ == "__main__":
    main()
