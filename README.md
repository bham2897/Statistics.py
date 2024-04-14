# Statistics1.py

# Stroke Prediction Data Analysis

This repository contains a Python script for analyzing a dataset related to stroke prediction. The script computes statistical measures such as mean, median, and quartiles for certain health metrics and calculates the probability of stroke occurrences using the binomial distribution.

## Description

The Python script processes data from a CSV file containing individual health records and calculates the following:
- Mean, median, and quartiles for the 'Age' and 'Average Glucose Level' columns.
- Probability of observing a specified number of stroke cases in a sample of patients, using the binomial distribution.


### Required Libraries:
- `pandas`: For data manipulation and analysis.
- `numpy`: For numerical operations.
- `scipy`: Specifically, the `binom` function from `scipy.stats` to calculate binomial distribution probabilities.

 OUTPUT: Age - Mean: 54.035666666666664 Median: 54.0 Quartiles: [36. 54. 72.]
Average Glucose Level - Mean: 129.44520866666667 Median: 128.9 Quartiles: [ 94.5175 128.9    164.5925]
Probability of exactly 3 strokes in 10 patients: 0.11693760014208965



