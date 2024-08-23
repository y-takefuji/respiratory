import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('data.csv')

# Filter the data
filtered_data = data[(data['demographics_type'] == 'Age Group') & (data['demographics_values'] == '65+ years')]

# Convert 'week_end' to datetime
filtered_data['week_end'] = pd.to_datetime(filtered_data['week_end'], format='%Y-%m-%d')

# Sort the data by date
filtered_data = filtered_data.sort_values(by='week_end')

# Plot the data
plt.figure(figsize=(10, 6))

# Get unique pathogens
pathogens = filtered_data['pathogen'].unique()

# Define linestyles
linestyles = ['-', '--', '-.', ':']

# Plot each pathogen with a different linestyle and black color
for i, pathogen in enumerate(pathogens):
    pathogen_data = filtered_data[filtered_data['pathogen'] == pathogen]
    plt.plot(pathogen_data['week_end'], pathogen_data['percent_visits'], label=pathogen, linestyle=linestyles[i % len(linestyles)], color='black')

# Rotate date labels
plt.xticks(rotation=90)

# Add legend
plt.legend()

# Add labels and title
plt.xlabel('Week End')
plt.ylabel('Percent Visits')
plt.title('Percent Visits by Pathogen for Age Group 65+ years')

# Show the plot
plt.tight_layout()
plt.savefig('result.png',dpi=300)
plt.show()

