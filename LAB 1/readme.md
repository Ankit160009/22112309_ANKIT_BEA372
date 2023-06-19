# Lab 1- 19th June, 2023

This code repository includes Python scripts for analyzing a bank dataset. The scripts offer functionality to access the dataset, extract headers, calculate customer counts based on marital categories, and generate a histogram illustrating the distribution of ages.

## Functions

### `open_dataset()`

This function is responsible for accessing the content of the bank dataset file. It reads the file and stores its content as a list, which is then returned as the output of the function.

### `headers(data)`

This function accepts the dataset content as an input and displays the headers that are present in the file.

### `count_of_customers_by_marital_category(data)`

This function accepts the dataset content as input and calculates the count of customers in each marital category. It then displays the count for each category.

### `age_histogram(data)`

This function accepts the dataset content as an input and creates a histogram to visualize the age distribution. It groups the ages into intervals of 10 and calculates the count of ages within each interval. The resulting histogram displays the age intervals along with the corresponding age counts in a visual representation.

## Usage

To use this code, follow these steps:

1. Make sure you have the bank.csv file in the directory where you want to run the script.

2. Open the Python script that contains the code.

3. Use the functions in the desired order to analyze the dataset. For example:

    ```python
    dataset = open_dataset()
    headers(dataset)
    count_of_customers_by_marital_category(dataset)
    age_histogram(dataset)
    ```

4. Run the Python script and observe the results printed in the console.

These instructions will ensure the presence of the dataset file, open the script, call the functions in the desired sequence, and view the analysis results.



