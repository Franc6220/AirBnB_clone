#!/usr/bin/python3
#This program calculates the variance of numbers
def calculate_variance(numbers):
    sum_numbers = 0
    for number in numbers:
        sum_numbers = sum_numbers + number
    mean = sum_numbers / len(numbers)

#Calculates the mean of squared numbers
    sum_squares = 0
    for number in numbers:
        sum_squares = sum_squares + number**2
    mean_squares = sum_squares / len(numbers)

    return mean_squares - mean**2
