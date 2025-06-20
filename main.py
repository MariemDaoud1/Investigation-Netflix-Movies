# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

# Select the 'release_year' column
net90 = netflix_df["release_year"]

# Filter the DataFrame for release years between 1990 and 1999
is90 = net90.between(1990, 1999)
net90=netflix_df[is90]
duration = int(net90['duration'].mode()[0])
short_movie_count = len(net90[(net90['duration'] <= 90)&( net90["genre"]=="Action") & (net90["type"]=="Movie")])
