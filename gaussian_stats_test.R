

# Read delimited text file
data <- read.table("C:/Users/Filomena Mendes/Desktop/noisR Resistor/data_gauss_05_fev_ii.txt", sep = "\n", header = FALSE) # import data

# Extract values from data frame
values <- data$V1  # Assuming there's only one column in the data frame

# Initialize Gaussian data vector
gaussian_data <- numeric(0)

# Filter values based on condition
for (value in values) {
  if (value > 6893 & value < 6909) {
    gaussian_data <- c(gaussian_data, value)
  }
}


## Attach the "nortest" library that contains the chi-square test.
library(nortest)
#The test
pearson.test(gaussian_data)