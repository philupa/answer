import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)


#1 Import the sales dataset into your Notebook using your preferred Python method/library. Name it ‘raw_sales’. This must be done using a method that allows further analysis or manipulation of the data.
raw_data = pd.read_csv('sales (1).csv')
#2 Display the schema of the ‘raw_sales’ dataset.
print(raw_data.columns)
#3 Update or create a new working dataset, called ‘sales’, that does not contain duplicate values.
sales = raw_data.drop_duplicates()
#4 From the ‘sales’ dataset, calculate the total sales value of the ‘Furniture’ Category. Print your answer.
print(sales.loc[sales.Category == "Furniture"]['Sales'].sum())
#5 Return a separate dataset, called ‘category_sales’, that contains the total ‘Sales’ and ‘Profit’ for each Category. Order the dataset by ‘Profit’.
category_sales = sales.groupby('Category')[['Sales', 'Profit']].agg('sum').sort_values('Profit', ascending=False)
print(category_sales)
#6 Create a Python list containing distinct values for the ‘Category’ column of the ‘sales’ dataset. Print the resulting list.
category_list = sales['Category'].drop_duplicates().tolist()
print(category_list)
#7 Create a second column called ‘Sales2’ in the ‘sales’ dataset that contains half the value of the &#39;Sales&#39; column if the ‘Sales’ value is even and the full value of ‘Sales’ if the 'Sales' value is odd.
sales['Sales2'] = np.where(sales['Sales']%2==1, sales['Sales'], sales['Sales']/2)
#8 Using the ‘sales’ dataset and without creating a new dataset, display the 5th to the 10th row (indexing starts at 0) of the following columns; ‘Product Name’, ‘Discount’ and ‘Sales’.
print(sales.loc[4:9,['Product Name', 'Discount', 'Sales']])
#9 Plot the columns &#39;Sales&#39; and &#39;Profit&#39; of the ‘sales’ dataset against the index of the dataset on the same graph, colour coding 'Sales' red and 'Profit' blue. Make sure the plot has a title, legend and both axes are labelled accordingly.
sales.plot(y=['Sales','Profit'], kind='bar', color=['red','blue'], title='Sales and profit for each order', xlabel='Order', ylabel='Number of sales/profit')
#10 Write a Python function that takes in a list of strings. The output will be a list that contains the same number of strings with the following constraints and transformations applied:
# i. If the original string had an even number of characters, add an exclamation point (!).
# ii. Blank spaces have been removed
# iii. Vowels have been capitalised
#Test your function by passing in the list from the answer to question 6.
def stringtransformer(list_of_strings):
    transformed_list = []
    for string in list_of_strings:
        new_string = string
        if len(new_string) % 2 == 0:
            new_string += '!'
        new_string = new_string.replace(' ', '')
        new_string = new_string.replace('a','A')
        new_string = new_string.replace('e','E')
        new_string = new_string.replace('i','I')
        new_string = new_string.replace('o','O')
        new_string = new_string.replace('u','U')
        transformed_list.append(new_string)
    return transformed_list

stringtransformer(category_list)