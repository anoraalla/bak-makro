# Assuming df is your dataframe and it includes Bias_Perception as the dependent variable
library(MASS)         # For ordered logistic regression
library(nnet)         # For multinomial logistic regression
library(brant)        # For the Brant test

# Load necessary libraries
# install.packages("psych") # Uncomment this line if 'psych' package is not installed
library(psych)
library(ggplot2)

setwd("/home/anna/Documents/bak-makro/stat")
# Read the CSV file into a data frame
df <- read.csv("12-01.csv")  # Replace with your actual file path

# Convert Bias_Perception to a factor, specify ordered levels
df$Bias_Perception <- factor(df$Bias_Perception, levels = c(1, 2, 3, 4, 5), ordered = TRUE)

# Ordered Logistic Regression using the polr (proportional odds logistic regression) in MASS package
ordered_model <- polr(Bias_Perception ~ Communication + Gender + Age + Residence + Education + Income + Ideology + Feminism, data = df, Hess = TRUE)

# Summary of the ordered logit model
summary(ordered_model)

# Brant test for the proportional odds assumption
brant_test <- brant(ordered_model)
# Check if the proportional odds assumption holds
print(brant_test)

# If the Brant test shows significant p-values (usually p < 0.05), consider multinomial logit
if (any(brant_test$p.table[,5] < 0.05)) {
  cat("The proportional odds assumption is violated.\n")
  cat("Consider using a multinomial logistic regression model.\n")
  # Multinomial Logistic Regression using multinom from nnet package
  multinom_model <- multinom(Bias_Perception ~ Age + Income + LiberalViews, data = df)
  # Summary of the multinomial logit model
  summary(multinom_model)
} else {
  cat("The proportional odds assumption holds. The ordered logistic regression model is appropriate.\n")
}