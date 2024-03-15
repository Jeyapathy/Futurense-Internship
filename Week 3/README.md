# Analysis of Data using netflix movie 

We delve into the world of Netflix and explore the vast collection of movies available on the platform.We have done analysing of data using netlflix csv file which contains of informations with rows and columns respectively,By leveraging data science techniques and visualization tools, we aim to gain insights into various aspects of Netflix movie content, including genres, release years, durations, and more.

# About the Dataset
The dataset used for this analysis is sourced from Netflix and contains information about movies available on the platform. It includes details such as the title, type (movie or TV show), release year, duration, country of production, genres, and ratings. This rich dataset provides a comprehensive overview of Netflix movie content and serves as the foundation for our analysis.

# Goals 
Our primary objectives in this are as follows:

* Exploratory Data Analysis (EDA): Conduct in-depth exploration of the Netflix movie dataset to understand its structure, distribution, and key attributes.
* Genre Analysis: Analyze the distribution of movies across different genres and identify the most popular genres on Netflix.
* Temporal Analysis: Investigate trends in movie releases over time by analyzing the distribution of movies across release years.
* Duration Analysis: Examine the distribution of movie durations and identify patterns or trends in movie lengths.
* Visualizations: Create insightful visualizations using popular libraries such as Matplotlib, Seaborn, and Plotly to represent findings effectively.

# repository Structure 
* Data: Contains the dataset file netflix_titles.csv used for analysis.
* Notebooks: Includes Jupyter notebooks documenting the data analysis process, code, and visualizations.

Data Preprocessing:
The dropna() function is used to remove rows with missing values from the DataFrame, creating a new DataFrame called netflix.
It displays the number of rows and columns in the cleaned dataset using string formatting.

Data Analysis:
The code filters the netflix DataFrame to select only rows where the 'type' column equals 'Movie', creating a new DataFrame called movie.
It removes the 'min' suffix from the 'duration' column and converts it to an integer data type to represent the duration of movies in minutes.
It checks the data type of the 'duration' column to confirm the conversion.

Data Visualization:
The code creates a scatter plot to visualize the relationship between the release year and duration of movies.
It uses matplotlib to generate the scatter plot, labeling the x-axis as 'Release Year' and the y-axis as 'Duration'.
It then creates a histogram using Plotly to visualize the distribution of movie durations.
The histogram bins the movie durations with a size of 0.5 minutes and uses a dark theme for visualization.

* Check the shape of the DataFrame df:
This task provides information about the dimensions of the dataset, showing the number of rows and columns.

* Check the data types of columns in the DataFrame df:
This task displays the data types of each column in the dataset, which helps in understanding the structure of the data.

* Check for missing values in the DataFrame df:
This task identifies any missing values present in the dataset, which is crucial for data cleaning and preprocessing.

* Plot a histogram of the distribution of movie and TV show counts:
This task visualizes the distribution of content types (movies and TV shows) in the dataset, providing insights into the content distribution.

* Plot the top 10 countries with the most content on Netflix:
This task visualizes the top 10 countries contributing the most content to Netflix, helping to identify the primary sources of content.

* Display the first 10 rows of the DataFrame df:
This task shows a preview of the dataset by displaying the first 10 rows, giving an overview of the data structure.

* Calculate and display basic statistics for the numerical columns in the DataFrame df:
This task computes basic statistical measures (such as mean, median, min, max, etc.) for numerical columns, providing insights into the data distribution.

* Check unique values in the 'rating' column of the DataFrame df:
This task lists unique values present in the 'rating' column, helping to understand the diversity of content ratings.

* Plot a pie chart showing the distribution of content ratings:
This task visualizes the distribution of content ratings using a pie chart, providing a clear representation of the proportion of each rating category.

* Display the columns in the DataFrame df:
This task lists all the columns present in the dataset, giving an overview of the available features.
