# -*- coding: utf-8 -*-
"""nullity_matrix.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XD62YHyeArnoby57VWYAYdfv8sFjt3E2

#MISSING GROUNDWATER DATA
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your data into a pandas DataFrame (replace 'data.csv' with your file)
data_groundwater = pd.read_excel("https://raw.githubusercontent.com/Ricardo8932/ProyectoConagua/main/Database/Groundwater/groundwater_contaminants_with_sign.xlsx")

# Select the columns you want to include in the heatmap
selected_columns_groundwater = data_groundwater.columns[14:28]  # Replace with the range of column names you want

# Create a heatmap of missing values ​​for only the selected columns
plt.figure(figsize=(10, 6))  # Adjust the size of the figure

# Generates a heat map showing the presence of missing values ​​in selected columns
heatmap = sns.heatmap(data_groundwater[selected_columns_groundwater].isnull(), cbar=False, cmap='Blues_r')

# Rotate the x-axis labels by 90 degrees so they are vertical and increase the font size
heatmap.set_xticklabels(heatmap.get_xticklabels(), rotation=90, fontsize=17)

# Set a step on the y-axis to show only some labels and increase the font size
step = 6  # Adjust this value depending on how many labels you want to display
y_labels = [label if i % step == 0 else '' for i, label in enumerate(heatmap.get_yticklabels())]
heatmap.set_yticklabels(y_labels, fontsize=14)

plt.title('a)', loc='left', fontsize=20)
plt.show()

"""#MISSING LOTIC DATA

"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your data into a pandas DataFrame (replace 'data.csv' with your file)
data_lotic = pd.read_excel("https://raw.githubusercontent.com/Ricardo8932/ProyectoConagua/main/Database/Lotic/lotic_contaminants_with_sign.xlsx")

# Select the columns you want to include in the heatmap
selected_columns_lotic = data_lotic.columns[13:21]  # Replace with the range of column names you want

# Create a heatmap of missing values ​​for only the selected columns
plt.figure(figsize=(10, 6))  # Adjust the size of the figure

# Generates a heat map showing the presence of missing values ​​in selected columns
heatmap = sns.heatmap(data_lotic[selected_columns_lotic].isnull(), cbar=False, cmap='Blues_r')

# Rotate the x-axis labels by 90 degrees so they are vertical and increase the font size
heatmap.set_xticklabels(heatmap.get_xticklabels(), rotation=90, fontsize=17)

# Set a step on the y-axis to show only some labels and increase the font size
step = 6  # Adjust this value depending on how many labels you want to display
y_labels = [label if i % step == 0 else '' for i, label in enumerate(heatmap.get_yticklabels())]
heatmap.set_yticklabels(y_labels, fontsize=14)

plt.title('b)', loc='left', fontsize=20)
plt.show()

"""#MISSING LENTIC DATA"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your data into a pandas DataFrame (replace 'data.csv' with your file)
data_lentic = pd.read_excel("https://raw.githubusercontent.com/Ricardo8932/ProyectoConagua/main/Database/Lentic/lentic_contaminants_with_sign.xlsx")

# Select the columns you want to include in the heatmap
selected_columns_lentic = data_lentic.columns[13:25]  # Replace with the range of column names you want

# Create a heatmap of missing values ​​for only the selected columns
plt.figure(figsize=(10, 6))  # Adjust the size of the figure

# Generates a heat map showing the presence of missing values ​​in selected columns
heatmap = sns.heatmap(data_lentic[selected_columns_lentic].isnull(), cbar=False, cmap='Blues_r')

# Rotate the x-axis labels by 90 degrees so they are vertical and increase the font size
heatmap.set_xticklabels(heatmap.get_xticklabels(), rotation=90, fontsize=17)

# Set a step on the y-axis to show only some labels and increase the font size
step = 6  # Adjust this value depending on how many labels you want to display
y_labels = [label if i % step == 0 else '' for i, label in enumerate(heatmap.get_yticklabels())]
heatmap.set_yticklabels(y_labels, fontsize=14)

plt.title('c)', loc='left', fontsize=20)
plt.show()

"""#MISSING COASTAL DATA"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your data into a pandas DataFrame (replace 'data.csv' with your file)
data_coastal = pd.read_excel("https://raw.githubusercontent.com/Ricardo8932/ProyectoConagua/main/Database/Coastal/coastal_contaminants_with_sign.xlsx")

# Select the columns you want to include in the heatmap
selected_columns_coastal = data_coastal.columns[13:21]  # Replace with the range of column names you want

# Create a heatmap of missing values ​​for only the selected columns
plt.figure(figsize=(10, 6))  # Adjust the size of the figure

# Generates a heat map showing the presence of missing values ​​in selected columns
heatmap = sns.heatmap(data_coastal[selected_columns_coastal].isnull(), cbar=False, cmap='Blues_r')

# Rotate the x-axis labels by 90 degrees so they are vertical and increase the font size
heatmap.set_xticklabels(heatmap.get_xticklabels(), rotation=90, fontsize=17)

# Set a step on the y-axis to show only some labels and increase the font size
step = 6  # Adjust this value depending on how many labels you want to display
y_labels = [label if i % step == 0 else '' for i, label in enumerate(heatmap.get_yticklabels())]
heatmap.set_yticklabels(y_labels, fontsize=14)

plt.title('d)', loc='left', fontsize=20)
plt.show()