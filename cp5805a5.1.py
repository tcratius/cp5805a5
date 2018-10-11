#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().run_line_magic('matplotlib', 'notebook')
import numpy as np
import pandas as pd

def display_plot_menu():
    print("""Please choose from the following options:
         1 – Line
         2 – Bar
         3 – Box plot
        """)

def display_main_menu():
    print("""Welcome to The DataFrame Statistician!
Please choose from the following options:
         1 – Load from a CSV file
         2 – Analyse
         3 – Visualise
         4 - Quit
        """)
    
def analysing_data(multi_sets):
    for val in multi_sets:
        print("-"*10)
        print("Number of values (n): {:^10.f0}".format(multi_sets.size))
        print("Mean: {:^10.f2}".format(multi_sets[val].mean()))
        print("Standard Deviation: {:^10.f2}".format(multi_sets[val].std()))
        print("Std.Err of Mean: {:^10.f2}".format(multi_sets[val].sem()))
        print("-"*20)

def select_plot_option():
    display_plot_menu()
    plot_option = get_int_value("\nPick the plot - <ENTER> [1-3]: ")
    
    while plot_option > 3 or plot_option <= 0: 
        print("That is not the correct option, choose number from 1 to 3")
        display_plot_menu()
        plot_option = get_int_value("\nPick the plot - <ENTER> [1-3]: ")
    
    return plot_option

def select_sub_plot_option():
    sub_option = get_int_value("\nEnter [0] <- 'Single' OR [1] <- 'Subplot'\n: ")
    
    while sub_option > 1 or sub_option < 0:
        print("There are only two numbers to choose from 0 or 1. Please Try again.")
        sub_option = get_int_value("\nEnter [0] <- 'Single' OR [1] <- 'Subplot'\n: ")
        
    return sub_option
    

def visualise_plot(multi_sets):
    plot_option, sub_option = 0, 0
    plot_option = select_plot_option()
    sub_option = select_sub_plot_option()
    
    if plot_option == 1 and sub_option == 0:
        print("plot 1")
    elif plot_option == 2 and sub_option == 0:
        print("plot2")
    elif plot_option == 3 and sub_option == 0:
        print("plot3")
    elif plot_option == 1 and sub_option == 1:
        print("plot4")
    elif plot_option == 2 and sub_option == 1:
        print("plot5")
    elif plot_option == 3 and sub_option == 1: 
        print("plot6")
    else:
        print("\nThat option is not available")
        plot_option, sub_plot = 0, 0


        
def get_int_value(prompt):
    try:
        value = int(input(prompt))
        return value
    except ValueError: 
        print("ValueError: An integer is required, please try again.")
        return 0 

def get_str_value(prompt):
    value = input(prompt)
    return value
    
def loading_file(multi_sets, file_name):
    try:
        file_name = get_str_value("\nType here the file you wish to open: ")
        file_contents = pd.read_csv(file_name)
        multi_sets = pd.DataFrame(file_contents)
        print("The file {} was succesfully opened and read".format(file_name))
    except IOError:
        print("file not found or not in current directory")
        
    return multi_sets, file_name

def main():
    number, file_name = 0, None
    multi_sets = pd.DataFrame()
    while number != 4:
        display_main_menu()
        number = get_int_value("Enter the menu option number [1 - 4]: ")
        if number == 1:
            multi_sets, file_name = loading_file(multi_sets, file_name)
        elif number == 2 and file_name != None:
            analysing_data(multi_sets)
        elif number == 3 and file_name != None:
            visualise_plot(multi_sets)
        elif number == 4:
            print("\n{:*^20}".format("Good bye!"))
        elif file_name == None:
            print("\nPlease load a file into memory via option [1]\n")
        else:
            print("Please ENTER a valid menu option")
            number = 0


main()


# #### file_name, number = 0, None
# print(file_name, number)

# In[4]:


get_ipython().run_line_magic('matplotlib', 'notebook')
import pandas as pd
import numpy as np
from numpy import nan as NA

for val in multi_sets:
    print(val)

file_contents = pd.read_csv("ld.csv")
multi_sets = pd.DataFrame(file_contents)
# df["weight"].mean()
print(list(multi_sets.columns.values))
print(list(multi_sets))
print(multi_sets["day"].mean())
print(multi_sets.describe())
print(multi_sets.size)
print(multi_sets["day"].std())
print(multi_sets["day"].sem())

# grouped.aggregate(lambda x: np.std(x, ddof=1)/np.sqrt(x.count()))


# In[ ]:


dir(pd.DataFrame)


# In[ ]:




