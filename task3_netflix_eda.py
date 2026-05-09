# Task 3 - Exploratory Data Analysis (EDA)
# Dataset  - Netflix Dataset
# Language - Python
# Run      - python task3_netflix_eda.py

import matplotlib.pyplot as plt

import pandas as pd



# define data
data = {
    "title"        : ["Stranger Things", "Money Heist", "Dark", "Ozark",
                      "The Crown", "Bridgerton", "Squid Game", "Narcos",
                      "Emily in Paris", "The Witcher", "Wednesday",
                      "Lupin", "Mindhunter", "Peaky Blinders", "Black Mirror"],
    "type"         : ["TV Show", "TV Show", "TV Show", "TV Show", "TV Show",
                      "TV Show", "TV Show", "TV Show", "TV Show", "TV Show",
                      "TV Show", "TV Show", "TV Show", "TV Show", "TV Show"],
    "country"      : ["United States", "Spain", "Germany", "United States",
                      "United Kingdom", "United States", "South Korea",
                      "United States", "United States", "United States",
                      "United States", "France", "United States",
                      "United Kingdom", "United Kingdom"],
    "release_year" : [2016, 2017, 2017, 2017, 2016, 2020, 2021, 2015,
                      2019, 2019, 2022, 2021, 2017, 2013, 2011],
    "rating"       : ["TV-14", "TV-MA", "TV-MA", "TV-MA", "TV-14",
                      "TV-14", "TV-MA", "TV-MA", "TV-14", "TV-MA",
                      "TV-14", "TV-MA", "TV-MA", "TV-MA", "TV-MA"],
    "seasons"      : [4, 5, 3, 4, 6, 3, 1, 3, 3, 3, 1, 3, 2, 6, 6],
    "imdb_score"   : [8.7, 8.2, 8.8, 8.4, 8.6, 7.3, 8.0, 8.8,
                      6.9, 8.2, 8.1, 7.5, 8.6, 8.8, 8.8]
}

# create dataframe
df = pd.DataFrame(data)

# show data
print("==============================")
print("      NETFLIX DATASET")
print("==============================")
print(df)
print()

# summary statistics
print("==============================")
print("    SUMMARY STATISTICS")
print("==============================")
print(df.describe())
print()

# trend - content by release year
print("==============================")
print("    CONTENT BY YEAR")
print("==============================")
year_count = df["release_year"].value_counts().sort_index()
print(year_count)
print()

# correlation analysis
print("==============================")
print("    CORRELATION ANALYSIS")
print("==============================")
print(df[["release_year", "seasons", "imdb_score"]].corr())
print()

# country count
country_count = df["country"].value_counts()

# rating count
rating_count = df["rating"].value_counts()

# setup figure and subplots
plt.figure(figsize=(14, 10))

# bar chart - shows by country
plt.subplot(2, 2, 1)
plt.bar(country_count.index, country_count.values,
        color="skyblue", edgecolor="black")
plt.xlabel("Country")
plt.ylabel("Number of Shows")
plt.title("Shows by Country")
plt.xticks(rotation=45)

# bar chart - rating distribution
plt.subplot(2, 2, 2)
plt.bar(rating_count.index, rating_count.values,
        color="lightgreen", edgecolor="black")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.title("Rating Distribution")
plt.xticks(rotation=45)

# histogram - imdb score
plt.subplot(2, 2, 3)
plt.hist(df["imdb_score"], bins=6,
         color="lightpink", edgecolor="black")
plt.xlabel("IMDB Score")
plt.ylabel("Frequency")
plt.title("IMDB Score Distribution")

# scatter plot - release year vs imdb score
plt.subplot(2, 2, 4)
plt.scatter(df["release_year"], df["imdb_score"],
            color="orange", edgecolor="black", s=100)
plt.xlabel("Release Year")
plt.ylabel("IMDB Score")
plt.title("Release Year vs IMDB Score")

# display
plt.tight_layout()
plt.savefig("task3_output.png")
plt.show()
print("Saved : task3_output.png")
