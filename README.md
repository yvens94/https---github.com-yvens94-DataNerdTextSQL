

# DataNerdTextSQL

DataNerdTextSQL is a Text to SQL Application designed to allow users to query a dataset extracted from the site datanerd.tech 'Created by Luke Barousse to track job posting in the data field' using natural language. This README provides an overview of the project structure, data cleaning process, database creation, and prompt engineering details.

## Data Cleaning Process

The data cleaning process involves the following steps:

1. **Data collection**: Luke allow acces to an Extract a subset of data from datanerd.tech with a direct link to Kaggle
2. **Exploration**: Explore the extracted data to understand its structure, features, and any inconsistencies or missing values, and assess the kind necessary transformation that would be need to be done.
3. **Cleaning**: a thourough cleaning process was realized correcting inconsistencies, and ensuring data consistency. transforming columns, renaming columns, creating new bins and categories extracting important part of data from text, correcting format, to make sure it would be possible to use SQL queries on it.


## Database Creation

DataNerdTextSQL utilizes a SQLite database to store the cleaned. The database creation process involves:

1. **Database Setup**: Initialize a SQLite database using the sqlite3 libraries.
2. **Table Creation**: Define the database schema and create table to store different entities within the dataset.
3. **Data Loading**: Load the cleaned data into the SQLite database by inserting records .

## Prompt Engineering

Prompt engineering is a crucial aspect of DataNerdTextSQL, enabling effective communication between the user and the SQL database using natural language with an LLM as translator. The prompt engineering process involves:

1. **Prompt Design**: Design prompts that effectively capture user queries in natural language while ensuring clarity and specificity.
2. **Prompt Optimization**: Optimize prompts to enhance the performance of the Language Model (LLM) in understanding and generating accurate SQL queries.
3. **Prompt Evaluation**: Evaluate the effectiveness of prompts through experimentation with one-shot and few-shot inference techniques to generate correct SQL queries.

## Implementation

### Environment Setup

1. **Create Environment**: Set up a virtual environment for the project using appropriate tools like `Gemini_venv`.
2. **Install Requirements**: Install project dependencies specified in the `requirements.txt` file.
3. **Environment Variables**: Configure environment variables required for the application to setup the api.

### Data Processing

1. **Data Extraction**: Extract a subset of data from datanerd.tech using web scraping or API requests.
2. **Data Cleaning**: Clean and normalize the extracted data to ensure consistency and accuracy.
3. **Database Creation**: Set up a SQLite database and load the cleaned data into corresponding tables.

### Prompt Engineering

1. **Prompt Design**: Design natural language prompts to capture user queries effectively. 
2. **Prompt Optimization**: Optimize prompts to improve LLM performance in generating accurate SQL queries. One word can change everything
3. **Prompt Evaluation**: Experiment with different prompts and inference techniques to achieve correct SQL query generation. One shot and few shot inference

### Application Development

1. **LLM Integration**: Integrate the Language Model into the application to process user queries.
2. **Streamlit App**: Develop a Streamlit web application to provide a user-friendly interface for interacting with the SQL database.
3. **GeminiPro Integration**: Incorporate GeminiPro for SQL query creation and access to the SQLite database.

### Deployment

 **Deployment**: Deploy the DataNerdTextSQL application on Streamlit ensuring accessibility to users.


## Conclusion

DataNerdTextSQL is a powerful Text to SQL Application designed to facilitate seamless querying of a dataset using natural language. By following the outlined implementation steps and leveraging prompt engineering techniques, users can efficiently interact with the dataset and retrieve relevant information using simple natural language queries.

