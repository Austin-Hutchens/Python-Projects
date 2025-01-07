import matplotlib.pyplot as plt

# Data for each week
weeks = ['Week 1', 'Week 2', 'Week 3']

# Repetitions for each set in each week
week1_reps = [8, 5, 4]
week2_reps = [9, 7, 5]
week3_reps = [12, 10, 7]

# Weight used (constant in this case)
weight = 225  # pounds



# Plotting the data
plt.figure(figsize=(10, 6))  # Optional: Adjust the figure size

# Set positions and width for bars
bar_width = 0.2
bar_positions = [1, 2, 3]  # Positions for each set (1, 2, 3)

# Plot bars for each week
plt.bar([p - bar_width for p in bar_positions], week1_reps, width=bar_width, color='b', align='center', label='Week 1')
plt.bar(bar_positions, week2_reps, width=bar_width, color='g', align='center', label='Week 2')
plt.bar([p + bar_width for p in bar_positions], week3_reps, width=bar_width, color='r', align='center', label='Week 3')

# Add labels and title
plt.title('Bench Press Progress')
plt.xlabel('Set')
plt.ylabel('Repetitions')
plt.xticks(bar_positions, ['Set 1', 'Set 2', 'Set 3'])
plt.grid(True)
plt.legend()

plt.tight_layout()  # Optional: Adjust layout to prevent clipping of labels
plt.show()
