""" The dataset I am working with contains data from the game show Jeopardy!. Each row in the dataset represents a question (or “clue”) from the show, along with various attributes related to that question. Here’s a breakdown of what the dataset includes:
Dataset Components:
Show Number: The episode number of the show.
Air Date: The date the episode aired.
Round: The round of the game (e.g., Jeopardy, Double Jeopardy, Final Jeopardy).
Category: The category under which the question falls.
Value: The monetary value of the question, indicating its difficulty level.
Question: The actual text of the question or clue.
Answer: The correct response to the question. """

import pandas as pd
import re

# Set the option to display the full contents of a column
pd.set_option('display.max_colwidth', -1)

# Load the Jeopardy dataset into a DataFrame
jeopardy = pd.read_csv('jeopardy.csv')

# Display the first 5 rows of the DataFrame to understand its structure
print(jeopardy.head(5))

# Remove leading spaces from column names for easier access
jeopardy.columns = jeopardy.columns.str.strip()
print(jeopardy.columns)

# Rename columns for easier access and consistency
new_column_names = {
    'Show Number': 'show_number',
    'Air Date': 'air_date',
    'Round': 'round',
    'Category': 'category',
    'Value': 'value',
    'Question': 'question',
    'Answer': 'answer'
}
jeopardy.rename(columns=new_column_names, inplace=True)

# Check for any missing values in the DataFrame
print(jeopardy.isnull().sum())

# Display information about the DataFrame, including data types
print(jeopardy.info())

# Display basic statistics for numerical columns
print(jeopardy.describe())

# Function to filter questions containing all specified words
def filter_questions(dataframe, words):
    # Convert the list of words to lowercase for case-insensitive matching
    words = [word.lower() for word in words]
    
    # Define a lambda function to check if all words are in the question as whole words
    filter_func = lambda question: all(re.search(r'\b' + re.escape(word) + r'\b', question.lower()) for word in words)
    
    # Apply the filter function to the 'question' column
    filtered_data = dataframe[dataframe['question'].apply(filter_func)]
    
    return filtered_data

# Example usage of the filter_questions function
words_to_search = ["King", "England"]
filtered_questions = filter_questions(jeopardy, words_to_search)

# Print the questions from the filtered DataFrame
for question in filtered_questions['question']:
    print(question)

# Function to convert the 'value' column to floats
def convert_value(value):
    # Handle non-numeric entries by returning 0.0
    if value in ['None', 'no value']:
        return 0.0
    # Remove dollar sign and commas, then convert to float
    return float(value.replace('$', '').replace(',', ''))

# Apply the conversion function to the 'value' column and create a new column 'value_float'
jeopardy['value_float'] = jeopardy['value'].apply(convert_value)

# Function to filter questions containing all specified words
def filter_questions(dataframe, words):
    # Convert the list of words to lowercase for case-insensitive matching
    words = [word.lower() for word in words]
    
    # Define a lambda function to check if all words are in the question
    filter_func = lambda question: all(word in question.lower() for word in words)
    
    # Apply the filter function to the 'question' column
    filtered_data = dataframe[dataframe['question'].apply(filter_func)]
    
    return filtered_data

# Example usage of the filter_questions function
words_to_search = ["King"]
filtered_questions = filter_questions(jeopardy, words_to_search)

# Print the entire filtered DataFrame
print(filtered_questions)

# Print only the 'question' column from the filtered DataFrame
print(filtered_questions['question'])

# Calculate the average value of the filtered questions using the 'value_float' column
average_value = filtered_questions['value_float'].mean()

# Print the average value, rounded to two decimal places
print(average_value.round(2))

# Function to count unique answers in the DataFrame
def count_unique_answers(dataframe):
    # Use value_counts to count unique answers
    return dataframe['answer'].value_counts()

# Example usage of the count_unique_answers function
words_to_search = ["King"]
filtered_questions = filter_questions(jeopardy, words_to_search)

# Get the count of unique answers in the filtered questions
unique_answer_counts = count_unique_answers(filtered_questions)

# Print the unique answer counts
print("Unique answer counts:")
print(unique_answer_counts)
