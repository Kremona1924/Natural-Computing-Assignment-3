import numpy as np
import math
import os

def get_score_per_line(filename):
    data = np.loadtxt(filename, encoding='utf-16', dtype='float')

    scores_per_line = []

    curr_line_score = 0
    nr_of_datapoints = 0

    for i, d in enumerate(data):
        if math.isnan(d):
            if nr_of_datapoints > 0:  # No division by zero
                curr_line_score /= nr_of_datapoints
            scores_per_line.append(curr_line_score)
            curr_line_score = 0
            nr_of_datapoints = 0
        else:
            curr_line_score += d
            nr_of_datapoints += 1
    
    return scores_per_line

# Path to the directory containing the results files
results_directory = r"C:\Users\31613\OneDrive\Documenten\Artificial Intelligence\Semester 2\Natural Computing\Assignment 3\results_r2to6"
output_directory = results_directory  

# List of file bases and r values
file_bases = ['results_0', 'results_1']
r_values = ['r2', 'r3', 'r4', 'r5', 'r6']

# Walk through all files
for base in file_bases:
    for r in r_values:
        input_filename = os.path.join(results_directory, f"{base}_{r}.txt")
        output_filename = os.path.join(output_directory, f"average_{base}_{r}.txt")
        
        # Calculate average scores
        average_scores = get_score_per_line(input_filename)
        
        # Write average scores to file
        with open(output_filename, 'w') as f:
            for avg in average_scores:
                f.write(str(avg) + '\n')
        
        print(f"Verwerkt {output_filename}: {len(average_scores)} gemiddelde scores geschreven.")
