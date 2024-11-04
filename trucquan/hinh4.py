import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("7_OneCatOneNum.csv")

# Sort the dataset by the quantity of weapons exported
df_sorted = df.sort_values(by='Arms Exported', ascending=False)

# Generate bar chart
plt.figure(figsize=(12, 8))
plt.barh(df_sorted['Country'], df_sorted['Arms Exported'], color='skyblue')
plt.xlabel('Arms Exported')
plt.ylabel('Country')
plt.title('Arms Exported by the 50 Largest Exporters in 2017 (Bar Chart)')
plt.gca().invert_yaxis()  # Invert y-axis to have the country with the highest export at the top
plt.tight_layout()
plt.show()

# Generate lollipop chart
plt.figure(figsize=(12, 8))
plt.stem(df_sorted['Country'], df_sorted['Arms Exported'], basefmt=' ', use_line_collection=True)
plt.xlabel('Country')
plt.ylabel('Arms Exported')
plt.title('Arms Exported by the 50 Largest Exporters in 2017 (Lollipop Chart)')
plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
plt.tight_layout()
plt.show()
