import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('data.csv')

# Display unique values for 'pathogen'
unique_pathogens = data['pathogen'].unique()
print("Select a pathogen by number:")
for i, pathogen in enumerate(unique_pathogens):
    print(f"{i+1}. {pathogen}")

# User selects a pathogen
selected_pathogen_index = int(input("Enter the number of the selected pathogen: ")) - 1
selected_pathogen = unique_pathogens[selected_pathogen_index]

# Filter data by selected pathogen
filtered_data = data[data['pathogen'] == selected_pathogen]

# Display unique values for 'demographics_type'
unique_demographics_types = filtered_data['demographics_type'].unique()
print("Select demographics types by number (space-separated):")
for i, demo_type in enumerate(unique_demographics_types):
    print(f"{i+1}. {demo_type}")

# User selects demographics types
selected_demo_indices = list(map(int, input("Enter the numbers of the selected demographics types: ").split()))
selected_demo_types = [unique_demographics_types[i-1] for i in selected_demo_indices]

# Filter data by selected demographics types
filtered_data = filtered_data[filtered_data['demographics_type'].isin(selected_demo_types)]

# Define demographics values
demo_values_dict = {
    "Sex": ["Male", "Female"],
    "Age Group": ["65+ years", "18-64 years", "5-17 years", "0-4 years"],
    "Race/Ethnicity": ["Hispanic", "White, NH", "Asian/NHOPI, NH", "Black, NH"]
}

# Automatically select demo values based on selected demo types
selected_demo_values = []
for demo_type in selected_demo_types:
    if demo_type in demo_values_dict:
        selected_demo_values.extend(demo_values_dict[demo_type])

# Filter data by selected demographics values
filtered_data = filtered_data[filtered_data['demographics_values'].isin(selected_demo_values)]

filtered_data['week_end'] = pd.to_datetime(filtered_data['week_end'])
filtered_data = filtered_data.sort_values(by='week_end')

# Plot the data
plt.figure(figsize=(10, 6))
linestyles = ['-', '--', '-.', ':']
for i, demo_value in enumerate(selected_demo_values):
    demo_data = filtered_data[filtered_data['demographics_values'] == demo_value]
    plt.plot(demo_data['week_end'], demo_data['percent_visits'], label=demo_value, color='black', linestyle=linestyles[i % len(linestyles)])

plt.xlabel('Week End')
plt.ylabel('Percent Visits')
plt.title(f'Percent Visits for {selected_pathogen}')
plt.legend()

selected_demo_types = [item.replace("/", "_") for item in selected_demo_types]
selected_demo_types_str = "_".join(selected_demo_types)

# Show up to 15 xticks on X-axis and rotate them by 90 degrees
plt.xticks(ticks=plt.gca().get_xticks()[::max(1, len(plt.gca().get_xticks()) // 15)], rotation=90)
plt.tight_layout()
plt.savefig(f'{selected_pathogen}_{selected_demo_types}.png',dpi=300)
plt.show()

