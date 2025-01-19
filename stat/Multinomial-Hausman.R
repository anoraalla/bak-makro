library(mlogit)

# Assuming df is your dataframe and it includes Bias_Perception as the dependent variable
library(MASS)         # For ordered logistic regression
library(nnet)         # For multinomial logistic regression
library(brant)        # For the Brant test

# Load necessary libraries
# install.packages("psych") # Uncomment this line if 'psych' package is not installed
library(psych)
library(ggplot2)

setwd("/Users/kapsitis/workspace-public/bak-makro/stat")
# setwd("/home/anna/Documents/bak-makro/stat")
# Read the CSV file into a data frame
df <- read.csv("Survey-Clean.08.csv")  # Replace with your actual file path

df$Bias_Perception <- factor(df$Bias_Perception, levels = c(1, 2, 3, 4, 5), ordered = TRUE)
df$Bias_Family <- factor(df$Bias_Family, levels = c(1, 2, 3, 4, 5), ordered = TRUE)
df$Bias_Traits <- factor(df$Bias_Traits, levels = c(1, 2, 3, 4, 5), ordered = TRUE)
df$Bias_Interventions <- factor(df$Bias_Interventions, levels = c(1, 2, 3, 4, 5), ordered = TRUE)
df$Bias_Competence <- factor(df$Bias_Competence, levels = c(1, 2, 3, 4, 5), ordered = TRUE)


df$Gender <- factor(df$Gender, levels=c(1,2), ordered=TRUE)
df$Communication <- factor(df$Communication, levels = c(1, 2, 3, 4, 5), ordered = TRUE)
df$International <- factor(df$International, levels = c(1, 2, 3, 4, 5), ordered = TRUE)
df$Female_Bosses <- factor(df$Female_Bosses, levels = c(1, 2, 3, 4, 5), ordered = TRUE)
df$Age <- factor(df$Age, levels = c(1, 2, 3, 4, 5, 6), ordered = TRUE)
df$Education <- factor(df$Education, levels = c(1, 2, 3, 4, 5), ordered = TRUE)
df$Income <- factor(df$Income, levels = c(1, 2, 3, 4, 5, 6, 7), ordered = TRUE)
df$Ideology <- factor(df$Ideology, levels = c(1, 2, 3, 4, 5), ordered = TRUE)
df$Feminism <- factor(df$Feminism, levels = c(1, 2, 3, 4, 5), ordered = TRUE)
df$Religion <- factor(df$Religion, levels = c(1, 2, 3), ordered = TRUE)


# Prepare your data for mlogit (re-shape the dataset)
# Assuming 'Bias_Family' is your response variable and is multinominal for the context
df_mlogit <- mlogit.data(df, choice = "Bias_Perception", shape = "wide", varying = NULL)

# Fit a multinomial logit model
#multinom_model <- mlogit(Bias_Perception ~ Gender + Communication + International + Female_Bosses +
#                           Age + Education + Income + Ideology + Feminism + Religion, data = df_mlogit)
multinom_model <- mlogit(Bias_Perception ~ Gender + Communication, data = df_mlogit)


# Perform the Hausman test
# Note: This tests specific alternatives, you would need to specify a reduced and a full model
hausman_test <- hmftest(multinom_model, altnote = "Relative MacFadden")

# Check results
print(hausman_test)

# library(car)
# ordered_model <- polr(Bias_Perception ~ Gender + Communication + International + Female_Bosses + 
#                         Age + Education + Income + Ideology + Feminism + Religion, data = df, Hess = TRUE)
# 
# multicollinearity_check <- vif(ordered_model)  # Replace 'your_model' with the actual model object
# print(multicollinearity_check)

