# i used code cell from forum to print them
import pandas as pd
import matplotlib.pyplot as plt


# Define colors for sorting and searching
colors = {
    "iterative": 'blue',
    "recursive": 'blue',
    "sort_by_weight": 'green',
    "sort_by_price": 'green',
    "search_by_weight": 'red',
    "search_by_price": 'red'
}

# Plot each row as a separate graph with specified colors
fig, axes = plt.subplots(nrows=6, ncols=1, figsize=(10, 20))

for i, column in enumerate(df.columns):
    df[column].plot(ax=axes[i], title=column.replace('_', ' ').capitalize(), marker='o', color=colors[column])
    axes[i].set_xlabel('Number of Students (n)')
    axes[i].set_ylabel('Time (seconds)')
    axes[i].grid(True)

# Adjust layout to prevent overlap
plt.tight_layout()

# Save the figure to a file
plt.savefig('/mnt/data/performance_graphs_colored.png')

# Display the figure inline
plt.show()
