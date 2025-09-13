# Programming-Assignment_3
This repository shows the use and purpose of Pandas Library. It aims to develop the ability to apply and use these functions to create Python programs for data manipulation and analysis.

## Learning Outcomes
* To identify the codes and functions incorporated in the Pandas library
* To be able to apply and use the different codes and functions in creating a Python program using a
Pandas library

## Table of Contents
* Problem 1
* Problem 2
-----------------------------------

## Problem 1
This problem focuses on extracting and analyzing data from a given file — in this case, cars.csv. The file contains information about multiple car models, including various specifications and details for each vehicle. The problem requires using the Pandas library to read the set of data, filter specific rows or columns, and display the relevant information in a clear and organized way.

### Step-by-Step
#### 1. CSV File 
   First step in doing the experiment is placing the file cars.csv in the same folder as the jupyter notebook.
#### 2. Reading CSV File
   Followed by reading the CSV file. To load the data from the file, call the read_csv function from the pandas library. The result is then stored in a variable named "cars" so you can use it later to access and manipulate the data.
```python
cars = pd.read_csv('cars.csv')
cars
```
#### 3. Display first five rows
  To display the first five rows of the DataFrame named cars, first call the DataFrame (cars), then use the function head to specify that you want the first rows. Finally, provide the number of rows to display inside the parentheses — in this case, 5.
```python
cars.head(5)
```
#### 4. Display the last five rows
Just like in displaying the first five rows, call the DataFrame cars, but this time use the function tail to specify that you want the last rows. Then, provide the number of rows to display inside the parentheses — in this case, 5.
```python
cars.tail(5)
```
---------------------------------
### Problem 2
In this problem, it involves working with the cars DataFrame created in Problem 1 and applying subsetting, slicing, and indexing operations to extract specific pieces of information. The problem focuses on selecting particular rows, columns, or combinations of both to retrieve the required data efficiently.

### Step-by-Step
#### 1. First five rows with odd columns
  First step is to display only the odd-numbered columns, use the iloc indexer on the cars DataFrame. The iloc tells pandas to select all row but only columns starting at index 1 and skipping to the next column (1::2). This is followed by printing the first five rows along with their respective columns.
```python
odd = cars.iloc[:, 1::2]
print(odd.head(5))
```
#### 2. Display row of Mazda RX4
  To display the row of that contains the Model value "Mazda RX4", use a condition inside square brackets to filter the cars DataFrame. The syntax tells pandas to check the Model column and return only the rows where the value is exactly "Mazda RX4".
```python
cars.loc[(cars['Model'] == 'Mazda RX4'), ['Model']]
```
#### 3. Cylinders of CamaroZ28

