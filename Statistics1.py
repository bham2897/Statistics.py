import pandas as pd
import numpy as np
from scipy.stats import binom

# Load the dataset
file_path = '/Users/divya/Desktop/Stroke prediction data set.csv'  # Replace with your actual file path
data = pd.read_csv(file_path)

# Calculate mean, median, and quartiles for 'Age'
age_mean = data['Age'].mean()
age_median = data['Age'].median()
age_quartiles = np.percentile(data['Age'], [25, 50, 75])

# Calculate mean, median, and quartiles for 'Average Glucose Level'
glucose_mean = data['Average Glucose Level'].mean()
glucose_median = data['Average Glucose Level'].median()
glucose_quartiles = np.percentile(data['Average Glucose Level'], [25, 50, 75])

# Calculate the probability of having a stroke (p)
p_stroke = data['Stroke History'].mean()

# Number of trials
n_trials = 10

# Calculate the probability of exactly 3 strokes in 10 trials
prob_exactly_3 = binom.pmf(3, n_trials, p_stroke)

# Print results
print("Age - Mean:", age_mean, "Median:", age_median, "Quartiles:", age_quartiles)
print("Average Glucose Level - Mean:", glucose_mean, "Median:", glucose_median, "Quartiles:", glucose_quartiles)
print("Probability of exactly 3 strokes in 10 patients:", prob_exactly_3)



