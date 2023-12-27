# Data Cleaning Projects

## Table of Contents
- Introduction
- Datasets
- Tools Used
- Installation
- Data Cleaning Tasks
  - Chipotle Dataset
  - Data-cleaning-for-beginners-using-pandas Dataset
- Acknowledgments
- Conclusion

## Introduction
Welcome to the Data Cleaning Projects repository! This repository is dedicated to showcasing data cleaning and manipulation tasks executed on two distinct datasets. The primary objective behind these tasks is to enhance the quality, reliability, and consistency of the data, ensuring it's primed for deeper analysis.

## Datasets
Two datasets have been meticulously analyzed and cleaned:
1. **chipotle.tsv**: This dataset encapsulates information related to Chipotle orders, spanning various attributes such as order IDs, item names, quantities, choice descriptions, and corresponding prices.
2. **Data-cleaning-for-beginners-using-pandas.csv**: A diverse dataset focusing on individual attributes like age, salary, ratings, location details, establishment dates, and an indicator for easy application processes.

## Tools Used
The cleaning and manipulation tasks were predominantly executed using:
- Python
- Pandas library

## Installation
To replicate or extend the work presented in this repository, it's imperative to have Python and the Pandas library installed. If not already set up, you can swiftly install the Pandas library via pip:

```bash
pip install pandas
```

## Data Cleaning Tasks

### Chipotle Dataset
The Chipotle dataset, housed in the `chipotle.tsv` file, presented several challenges and tasks:

- **Columns Overview**:
  - Order Id: Represents unique order identifiers.
  - Quantity: Denotes the number of items ordered.
  - Item Name: Specifies the name of the item ordered.
  - Choice Description: Describes the specific choices or modifications to the ordered item.
  - Item Price: Captures the price associated with each item.

Various data cleaning and validation tasks were executed, including but not limited to:
- Handling missing values across columns.
- Verifying and adjusting data types to align with the intended usage.
- Identifying and managing duplicated entries.
- Standardizing item names and descriptions for consistency.
- Ensuring data integrity across related columns like order IDs.

For a detailed walkthrough of the cleaning tasks, please refer to the [chipotle_cleaning.ipynb](https://github.com/rupakbera21/Data-Cleaning/blob/main/Week3_2_Rupak.ipynb) Jupyter notebook.

### Pandas Dataset
The Pandas dataset, while diverse, required a meticulous approach to cleaning and preparation:

- **Columns Overview**:
  - Age: Captures the age of the individual.
  - Salary: Specifies the salary associated with each individual.
  - Rating: Represents a rating assigned to individuals.
  - Location: Details the geographical location of each individual.
  - Established: Indicates the establishment or joining date.
  - Easy Apply: An indicator suggesting the ease of application.

Tasks executed on this dataset encompassed:
- Identifying and handling missing values.
- Ensuring appropriate data type assignments for each column.
- Detecting and addressing potential outliers.
- Standardizing location details for uniformity.
- Transforming categorical data for analytical purposes.

For a deeper dive into the cleaning processes, consult the [pandas_cleaning.ipynb](https://github.com/rupakbera21/Data-Cleaning/blob/main/Week3_1_Rupak.ipynb) Jupyter notebook.

OR 

You can also take a look on the .ipynb files in the drive link -> [Drive Link](https://drive.google.com/drive/folders/1VX0OJwwyp9p05-vK8p9NItdU4J250GRi?usp=sharing) 

## Acknowledgments
Gratitude is extended to [Rushikesh Konapure](https://github.com/rishikonapure), my mentor, for invaluable guidance and insights throughout this project. Additionally, a special acknowledgment to **PrepInsta** for presenting this enriching winter internship opportunity in the realm of data analytics.

## Conclusion
Data cleaning stands as a cornerstone in the data analysis pipeline, ensuring that subsequent analyses are built on a foundation of quality and reliability. Through meticulous examination and transformations, both datasets have been primed for insightful analyses, paving the way for deeper exploration and understanding.
