# Read delimited text file
data <- read.table("C:/Users/Filomena Mendes/Desktop/noisR Resistor/data_gauss_05_fev_ii.txt", sep = "\n", header = FALSE) # import data

# Extract values from data frame
values <- data$V1  # Assuming there's only one column in the data frame

# Initialize Gaussian data vector
gaussian_data <- numeric(0)

# Filter values based on condition
for (value in values) {
  if (value > 6897 & value < 6909) {
    gaussian_data <- c(gaussian_data, value)
  }
}


## Attach the "nortest" library that contains the chi-square test.
library(nortest)

pearson.test(gaussian_data) #The Pearson test
ad.test(gaussian_data)
cvm.test(gaussian_data)
lillie.test(gaussian_data)

gaussian_data <- gaussian_data[1:5000]
#Under 5000 tests
shapiro.test(gaussian_data)
sf.test(gaussian_data)
