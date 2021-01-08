"""
Calculator for Old School Runescape's Managing Miscellania if not doing any actions for a number of days.
Assumes Royal Trouble is complete.
"""
import sys

if len(sys.argv) > 2:
    best_profit = int(sys.argv[1])
    second_best_profit = int(sys.argv[2])
    try:
        num_days = int(sys.argv[3])
    except IndexError:
        num_days = 100
else:
    print("Enter the best max profit for 10 workers:")
    best_profit = int(input())
    print("\nEnter the second best max profit for 10 workers:")
    second_best_profit = int(input())
    print("\nEnter the number of days:\nNote: the max is 100 days.")
    num_days = min(100, int(input()))

MAX_COINS_TAKEN_DAILY = 75000
MAX_REVENUE = MAX_COINS_TAKEN_DAILY + best_profit + second_best_profit / 2


def calculate(initial_amount, days=100):
    if initial_amount >= MAX_COINS_TAKEN_DAILY * (10 + days):
        return days * (1 + days) / 2 * MAX_REVENUE / 100  # sum from 1-n as a percentage
    resources_value = 0
    for approval_rate in range(100, 100 - days, -1):
        coins_taken = min(initial_amount / 10, MAX_COINS_TAKEN_DAILY)
        initial_amount -= coins_taken
        resources_value += approval_rate / 100 * MAX_REVENUE * coins_taken / MAX_COINS_TAKEN_DAILY
    return resources_value


# find the best amount in multiples of 75000
best_initial_amount = 0
best_profit = 0
for multiple in range(1, 10 + num_days):
    amount = multiple * 75000
    profit = calculate(amount, num_days) - amount
    if profit > best_profit:
        best_profit = profit
        best_initial_amount = amount

print(
    "For Miscellania over %d days, the best profit is:\nInvest %d for %d in profit."
    % (num_days, best_initial_amount, best_profit)
)
