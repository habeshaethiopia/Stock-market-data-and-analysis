import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plot_histogram(data, column, bins=10):
    """
    Plots a histogram for a specified column in the DataFrame.

    Parameters:
    data (pd.DataFrame): The DataFrame containing the data.
    column (str): The column name to plot the histogram for.
    bins (int): The number of bins for the histogram.
    """
    plt.figure(figsize=(10, 6))
    plt.hist(data[column], bins=bins, edgecolor="k")
    plt.title(f"Histogram of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.show()


def plot_scatter(data, column1, column2):
    """
    Plots a scatter plot for two specified columns in the DataFrame.

    Parameters:
    data (pd.DataFrame): The DataFrame containing the data.
    column1 (str): The column name for the x-axis.
    column2 (str): The column name for the y-axis.
    """
    plt.figure(figsize=(10, 6))
    plt.scatter(data[column1], data[column2], alpha=0.5)
    plt.title(f"Scatter Plot of {column1} vs {column2}")
    plt.xlabel(column1)
    plt.ylabel(column2)
    plt.show()


def plot_time_series(data, date_column, value_column):
    """
    Plots a time series line chart for a specified date and value column in the DataFrame.

    Parameters:
    data (pd.DataFrame): The DataFrame containing the data.
    date_column (str): The column name for the dates.
    value_column (str): The column name for the values.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(data[date_column], data[value_column])
    plt.title(f"Time Series of {value_column}")
    plt.xlabel("Date")
    plt.ylabel(value_column)
    plt.xticks(rotation=45)
    plt.show()


def plot_boxplot(data, column):
    """
    Plots a box plot for a specified column in the DataFrame.

    Parameters:
    data (pd.DataFrame): The DataFrame containing the data.
    column (str): The column name to plot the box plot for.
    """
    plt.figure(figsize=(10, 6))
    plt.boxplot(data[column])
    plt.title(f"Box Plot of {column}")
    plt.ylabel(column)
    plt.show()


def plot_correlation_matrix(data):
    """
    Plots a correlation matrix heatmap for the DataFrame.

    Parameters:
    data (pd.DataFrame): The DataFrame containing the data.
    """
    plt.figure(figsize=(12, 8))
    correlation_matrix = data.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", linewidths=0.5)
    plt.title("Correlation Matrix Heatmap")
    plt.show()
