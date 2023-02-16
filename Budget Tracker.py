#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from datetime import date


# In[2]:


goods_or_services = []
prices = []
dates = []
expense_types = []


# In[3]:


def add_expense(good_or_service,price,date,expense_type):
    goods_or_services.append(good_or_service)
    prices.append(price)
    dates.append(date)
    expense_types.append(expense_type)


# In[4]:


# Main Program

option = -1 #Users option or choice or input

while(option != 0):
    
    print('Welcome to expense tracker:')
    print('1. Add Food Expense')
    print('2. Add Household Expense')
    print('3. Add Transportation Expense')
    print('4. Show and Save the Expense Report')
    print('0. Exit')
    option = int(input('Choose an option:\n'))
    
    print()
    if option == 0:
        print('Exiting the program')
        break
    elif option == 1:
        print('Adding Food')
        expense_type = 'Food'
    elif option == 2:
        print('Adding Household')
        expense_type = 'Household'
    elif option == 3:
        print('Adding Transportation')
        expense_type = 'Transportation'
    elif option == 4:
        expense_report = pd.DataFrame()
        expense_report['Goods_or_Services'] = goods_or_services
        expense_report['Prices'] = prices
        expense_report['Dates'] = dates
        expense_report['Expense_Types'] = expense_types
        
        expense_report.to_csv('expenses.csv')
        print(expense_report)
    else:
        print('Incorrect Choice. Please Choose (0-4)')
    
    if option == 1 or option == 2 or option == 3:
        good_or_service = input('Enter the good or service for the expense type '+expense_type+':\n')
        price = float(input('Enter the price of the good or service:\n'))
        today = date.today()
        add_expense(good_or_service,price,today,expense_type)
    
    print()


# In[ ]:





# In[ ]:




