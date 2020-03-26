# Title: Assignment 8
# Author: Benjamin Lemery
# Date: 3/24/20

import time
import random
from Stack import Stack
from Queues import Queue

stack = Stack()
queue = Queue()

starting_balance = 1000
balance = starting_balance

current_stock_value = 20 # int(input("Enter the current stock price: $"))

accounting_system = int(input('Press 1 if you use FIFO accounting\n'
                              'Press 2 if you use LIFO account :'))

while True:
    user_selection = int(input("Press 1 to check profit or losses\n"
                               "Press 2 to check running stock\n"
                               "Press 3 to buy stock.\n"
                               "Press 4 to sell stock."))
    if user_selection == 1:
        if balance < starting_balance:
            print("You have lost: " + str(starting_balance - balance) + '\n' + "Your current balance is: $" + str(balance))

        elif balance ==  starting_balance:
            print("Your balance remains at : $" + str(starting_balance))
        elif balance > starting_balance:
            print("You have profited by : $" + str(starting_balance + balance) + "Your current balance is: $" + str(balance))

    # Check running stock
    elif user_selection == 2:
        print("Your starting balance was: $" + str(starting_balance))
        print("Your current balance is: $" +str(balance) +'\n')

    elif user_selection == 3:
        # Buy stock
        tomorrows_stock_value = random.randint(10, 30)
        print("The stock price is: $" + str(tomorrows_stock_value))
        print("Your current balance is: $" + str(balance))
        stock_quantity_to_buy = int(input("Enter how much stock you want to buy: "))
        stock_cost = tomorrows_stock_value

        stock_total_cost = stock_cost * stock_quantity_to_buy

        print("You paid: $" + str(stock_total_cost))
        print("Your old balance was: $" + str(balance))
        balance -=stock_total_cost
        print("Your new balance is: $" + str(balance))

        if accounting_system == 1:
            # FIFO CODE
            stock_quantity_to_buy_push = queue.push(stock_quantity_to_buy)
            stock_cost_push = queue.push(stock_cost)

        elif accounting_system == 2:
            # LIFO code
            stock_quantity_to_buy_push = stack.push(stock_quantity_to_buy)
            stock_cost_push = stack.push(stock_cost)

    # SELL STOCK
    elif user_selection == 4:
        tomorrows_stock_value = random.randint(10, 30)
        print("Getting tomorrows stock value..")
        time.sleep(1)
        print("Tomorrows stock value will be" + ": $"+str(tomorrows_stock_value))

        stock_quantity_to_sell = int(input("Enter how much stock you want to sell: "))
        stock_profit = tomorrows_stock_value * stock_quantity_to_sell
        print("The total value of the stock you sold was: $"+str(stock_profit))
        print("You had: $" + str(balance))
        balance += stock_profit
        print("Your new balance is : $" + str(balance))

        if accounting_system == 1:
            # FIFO code
            queue.pop(stock_quantity_to_sell)
            queue.pop(stock_profit)

        elif accounting_system == 2:
            # LIFO
            stack.pop(stock_quantity_to_sell)
            stack.pop(stock_profit)