import sqlite3
import matplotlib.pyplot as plt
import pandas as pd
from googletrans import Translator
import re


def open_database(path):
    """
    Function to open database and get dataset list

    :param path: String containing the path of database
    :return database: The connection to the database
    :return dataset_list: Dataframe containing all available dataset from the database
    """

    db = sqlite3.connect(path)

    # query to get all dataset from the database
    query = "SELECT * FROM sqlite_master WHERE type='table'"
    dataset_list = pd.read_sql_query(query, db)

    return db, dataset_list


def open_dataset(db, dataset_list):
    """
    Function to open all database for inspection purpose

    :param db: The connection to the database
    :param dataset_list: Dataframe containing all available dataset from the database
    :return dataset_name: List containing the name of all datasets
    :return dataset_data: Dictionary containing the name of dataset and its dataset
    """

    dataset_name = dataset_list['name'].tolist()
    dataset_data = dict()

    for i, dataset in enumerate(dataset_name):
        dataset_query = "SELECT * FROM " + dataset
        dataset_data[dataset] = pd.read_sql(dataset_query, db)

    return dataset_name, dataset_data


def read_query_dataset(query, db):
    """
    Function to extract and join relevant dataset from database

    :param query: SQL query to extract relevant dataset for selected objective
    :param db: The connection to the database
    :return df: Dataframe containing relevant dataset for objective analytics
    """

    df = pd.read_sql_query(query, db)

    return df


def translate_category_to_english(df, ori_col, en_col):
    """
    Function to manually translate the remaining original product categories which haven't had
    the english translation

    :param df: Dataframe containing relevant dataset for objective analytics
    :param ori_col: String containing the column name of original product category name
    :param en_col: String containing the column name of english translation of product category
    :return df: Dataframe after getting the english translation of the remaining categories
    """

    # Get all remaining product categories with NaN Value
    translator = Translator()

    # Get all remaining product categories with NaN Value
    unique_pcn_for_pcne = df.loc[df[en_col].isna(), ori_col].unique()

    # Set the translation result as english translation of product category
    for pcn in unique_pcn_for_pcne:
        pcn_str = pcn.replace('_', ' ')
        translated_pcn = translator.translate(pcn_str, src=translator.detect(pcn_str).lang, dest='en')
        translated_pcn = translated_pcn.text.lower().replace(' ', '_')
        df.loc[df[ori_col] == pcn, en_col] = translated_pcn

    return df


def text_normalization(string):
    """
    Function to do simple normalization in order to remove unrelated characters

    :param string: String containing the string to normalize
    :return: String after normalization
    """

    # Lower the string
    string = string.lower()
    # Change character '_' as space (' ')
    string = re.sub(r'_', ' ', string)
    # Set all characters except alphabetical characters and space as ' '
    string = re.sub(r'[^A-Za-z\s]', '', string)
    # Remove trailing space
    string = re.sub(r'^\s+|\s+$|\s+(?=\s)', ' ', string)

    return string


def compare_column_consistency(df, col_a, col_b, statement):
    """
    Function to compare the number of columns to check their consistency.
    Both features are equal if the numbers are equal.

    :param df: Dataframe containing relevant dataset for objective analyticsDataframe cons
    :param col_a: String containing the name of compared column A
    :param col_b: String containg the name of compared column B
    :param statement: String containing the statement of consistency
    :return: Show statement whether the
    """

    freq_col_a = df[col_a].value_counts().values.tolist()
    freq_col_b = df[col_b].value_counts().values.tolist()

    freq_equal = freq_col_a == freq_col_b

    print("{} = {}".format(statement, freq_equal))


def create_plot(res, plot_kind, legend_opt, title, x_label, y_label):
    """
    Function to create plot from the data

    :param res: Dataframe containing the result of data grouping or pivoting
    :param plot_kind: String containing the selected plot type
    :param legend_opt: Option for whether to show the legend or not
    :param title: String containing the title of the plot
    :param x_label: String containing the label text for x-axis
    :param y_label: String containing the label text for y-axis
    :return: Show the plot result
    """

    # Create plot
    res.plot(kind=plot_kind, legend=legend_opt)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    # Show plot
    plt.show()
