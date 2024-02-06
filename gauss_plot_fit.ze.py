import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Load data from the file
file_path = 'data_gauss_05_fev_ii.txt'

# Read data as strings
data_strings = np.loadtxt(file_path, dtype=str)

# Convert data to float, handling non-numeric values
data = []
min_v=8000
max_v=0
for value in data_strings:
    try:
        data.append(float(value))
        if float(value) < min_v:
            min_v = float(value)
        if float(value) > max_v:
            max_v = float(value)
        
    except ValueError:
        print(f"Warning: Could not convert '{value}' to float. Skipping.")

data = np.array(data)

#Print min and max values
diff = max_v-min_v
print(min_v, max_v, )

# Define the Gaussian function
def gaussian(x, amplitude, mean, stddev):
    return amplitude * np.exp(-(x - mean)**2 / (2 * stddev**2))

# Fit the data to the Gaussian function
n_bins = 100
hist, bin_edges = np.histogram(data, bins=n_bins, density=True)
bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
params, covariance = curve_fit(gaussian, bin_centers, hist, p0=[1, np.mean(data), np.std(data)])

# Plot the histogram
plt.hist(data, bins=n_bins, density=True, alpha=0.6, color='turquoise', label=f"Histogram ({n_bins} bins)" )

# Plot the fitted Gaussian curve
plt.plot(bin_centers, gaussian(bin_centers, *params), 'r--', label='Fit: A=%5.3f, $\mu$=%5.3f, $\sigma$=%5.3f' % tuple(params))

# Set x-axis limits based on the data
plt.xlim(min(data), max(data))

# Display the plot
plt.xlabel('Voltage Values')
plt.ylabel('Density')
plt.legend()
plt.title('Voltage Data and Gaussian Fit')
plt.show()
