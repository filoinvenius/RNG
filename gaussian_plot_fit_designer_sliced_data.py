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

sliced_data = np.array([i for i in data if i > 6893 and i < 6925])
print(len(sliced_data))

#Print min and max values
diff = max_v-min_v
print(min_v, max_v, diff)

# Define the Gaussian function
def gaussian(x, amplitude, mean, stddev):
    return amplitude * np.exp(-(x - mean)**2 / (2 * stddev**2))

# Fit the sliced_data to the Gaussian function
n_bins = 31
hist, bin_edges = np.histogram(sliced_data, bins=n_bins, density=True)
bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
params, covariance = curve_fit(gaussian, bin_centers, hist, p0=[1, np.mean(sliced_data), np.std(sliced_data)])

# Plot the histogram
plt.hist(sliced_data, bins=n_bins, density=True, alpha=0.6, color='turquoise', label=f"Histogram ({n_bins} bins)" )

# Plot the fitted Gaussian curve
plt.plot(bin_centers, gaussian(bin_centers, *params), 'r--', label='Fit: A=%5.3f, $\mu$=%5.3f, $\sigma$=%5.3f' % tuple(params))

# Set x-axis limits based on the sliced_data
plt.xlim(min(sliced_data), max(sliced_data))

# Display the plot
plt.xlabel('Voltage Values')
plt.ylabel('Density')
plt.legend()
plt.title('Voltage (Sliced) Data and Gaussian Fit')
plt.show()
