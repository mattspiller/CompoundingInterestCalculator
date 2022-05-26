# Author: Matthew Spiller
# Date Modified: February 7, 2022

# CompoundingInterestCalculator
# Description: Calculates compound interest on a monthly basis by taking an Annualized Percentage Rate as input from the user. User determines the number of months to calculate for.

print("Please enter the annual interest rate: ", end='')
apr = float(input())  # Annual Percentage Rate
apr += 6
mpr_multiplier = (1 + (apr / 100) / 12)  # monthly percentage rate multiplier

print("Please enter the initial balance: ", end='')
balance = float(input())

print("Please enter the number of months to know the balance: ", end='')
months = int(input())

print("Initial Balance: " + str(balance))
print("Annual Interest Rate: " + str(apr))

for i in range(months):
    balance *= mpr_multiplier
    print("After " + str(i+1) + " month(s): " + str(round(balance, 2)))
