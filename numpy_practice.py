import csv
import numpy as np

insta_list = []
study_time = []

with open("digital_behaviour.csv", "r", encoding="utf-8") as f:

    reader = csv.DictReader(f)

    for row in reader:
        insta_list.append(int(row["Instagram_Minutes"]))
        study_time.append(int(row["Study_Minutes"]))

# Convert lists into NumPy arrays
instagram = np.array(insta_list)
studytime = np.array(study_time)

# Basic calculations
total = instagram.sum()
average = instagram.mean()
minimum = instagram.min()
maximum = instagram.max()

# First 7 elements
insta_list = insta_list[:7]
study_time = study_time[:7]

total_instagram = sum(insta_list)

# Indexing
instagram[0]
instagram[-1]

# Slicing
instagram[-2:]
instagram[1:4]

# Vectorized operations
hours = instagram / 60

diff = instagram - studytime
greater_than_100 = instagram > 100 # Vectorized comparison
greater = instagram[instagram > 100]   # Vectorized filtering
count = (instagram > 100).sum() # Count values greater than 100
greater = instagram[instagram > 100].size()  # Vectorized filtering
# Instagram usage greater than average
days = instagram[instagram > average]