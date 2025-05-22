#Python program to Drawing Line and bar chart using matplotlib. 
import matplotlib.pyplot as plt 
## Data for line chart 
x_values = [1, 2, 3, 4, 5, 6] 
y_values = [5, 8, 12, 20, 15, 30] 
# Data for bar chart 
categories = ['X', 'Y', 'Z', 'P', 'Q'] 
values = [12, 7, 15, 10, 8] 
# Creating line chart 
plt.subplot(2, 1, 1)  # 2 rows, 1 column, chart position 1 
plt.plot(x_values, y_values, marker='o', color='blue') 
plt.title('Line Chart') 
plt.xlabel('X-axis') 
plt.ylabel('Y-axis') 
# Creating bar chart 
plt.subplot(2, 1, 2)  # 2 rows, 1 column, chart position 2 
plt.bar(categories, values, color='green') 
plt.title('Bar Chart') 
plt.xlabel('Categories') 
plt.ylabel('Values') 
# Adjust layout to prevent overlapping 
plt.tight_layout() 
# Displaying the charts 
plt.show()