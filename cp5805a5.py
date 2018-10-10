#!/usr/bin/env python
# coding: utf-8

# In[17]:


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
    pass

def visualise_plot(multi_sets):
    plot_option, sub_plot = 0, -1
    while plot_option == 0 
        display_plot_menu()
        plot_option = int_value("Pick the plot - <ENTER> [1-3]: ")
        sub_option = int_value("Now choose if the plot is be a\n single [0] or subplot [1]: "
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
            print("that option is not available")
            plot_option, sub_plot = 0, -1


def get_int_value(prompt):
    try:    
        value = int(input(prompt))
        return value
    except:
        print("An integer is required, please try again.")
        return 0 

def get_str_value(prompt):
    value = input(prompt)
    return value

def loading_file(multi_sets, file_name):
    try:
        file_name = get_str_value("Type here the file you wish to open: ")
        file_contents = pd.read_csv(file_name)
        multi_sets = pd.DataFrame(file_contents)       
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
            print("Good bye!")
        else:
            print("Please ENTER a valid menu option")
            number = 0


main()


# #### file_name, number = 0, None
# print(file_name, number)

# In[37]:


get_ipython().run_line_magic('matplotlib', 'notebook')
import pandas as pd
import numpy as np
from numpy import nan as NA



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


# In[32]:


dir(pd.DataFrame)


# In[ ]:




