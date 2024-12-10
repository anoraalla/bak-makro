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

# Convert Bias_Perception to a factor, specify ordered levels
df$Bias_Perception <- factor(df$Bias_Perception, levels = c(1, 2, 3, 4, 5), ordered = TRUE)
df$Bias_Family <- factor(df$Bias_Family, levels = c(1, 2, 3, 4, 5), ordered = TRUE)
df$Bias_Traits <- factor(df$Bias_Traits, levels = c(1, 2, 3, 4, 5), ordered = TRUE)
df$Bias_Interventions <- factor(df$Bias_Interventions, levels = c(1, 2, 3, 4, 5), ordered = TRUE)
df$Bias_Competence <- factor(df$Bias_Competence, levels = c(1, 2, 3, 4, 5), ordered = TRUE)

#df$Gender <- factor(df$Gender)
# df$Gender <- factor(df$Gender, levels=c(1,2), ordered=TRUE)
# df$Residence <- factor(df$Residence)

# df$Communication <- factor(df$Communication, levels = c(1, 2, 3, 4, 5), ordered = TRUE)
# df$International <- factor(df$International, levels = c(1, 2, 3, 4, 5), ordered = TRUE)
# df$Female_Bosses <- factor(df$Female_Bosses, levels = c(1, 2, 3, 4, 5), ordered = TRUE)
# df$Age <- factor(df$Age, levels = c(1, 2, 3, 4, 5, 6), ordered = TRUE)
# df$Education <- factor(df$Education, levels = c(1, 2, 3, 4, 5), ordered = TRUE)
# df$Income <- factor(df$Income, levels = c(1, 2, 3, 4, 5, 6, 7), ordered = TRUE)
# df$Ideology <- factor(df$Ideology, levels = c(1, 2, 3, 4, 5), ordered = TRUE)
# df$Feminism <- factor(df$Feminism, levels = c(1, 2, 3, 4, 5), ordered = TRUE)
# df$Election <- factor(df$Election, levels = c(1, 2), ordered = TRUE)
# df$Religion <- factor(df$Religion, levels = c(1, 2, 3), ordered = TRUE)



# df$Party_Affiliation <- factor(df$Party_Affiliation)


print("This is Bias_Perception")
# Ordered Logistic Regression using the polr (proportional odds logistic regression) in MASS package
ordered_model <- polr(Bias_Perception ~ Gender + Communication + International + Female_Bosses + Age + Education + Income + Ideology + Election + Feminism + Religion, data = df, Hess = TRUE)
# Summary of the ordered logit model
# summary(ordered_model)
# Brant test for the proportional odds assumption
brant_test <- brant(ordered_model)
# Check if the proportional odds assumption holds
print(brant_test)
# < 0.05 for Gender (0.0013) and Female_Bosses (0.0377)
print("\n\n")

print("This is Bias_Family")
# Ordered Logistic Regression using the polr (proportional odds logistic regression) in MASS package
ordered_model <- polr(Bias_Family ~ Gender + Communication + International + Female_Bosses + Age + Education + Income + Ideology + Feminism + Religion, data = df, Hess = TRUE)
# Summary of the ordered logit model
# summary(ordered_model)
# Brant test for the proportional odds assumption
brant_test <- brant(ordered_model)
# Check if the proportional odds assumption holds
print(brant_test)
# < 0.05 for Communication (0.0140) and Education (0.0411)
print("\n\n")



print("This is Bias_Traits")

# Ordered Logistic Regression using the polr (proportional odds logistic regression) in MASS package
ordered_model <- polr(Bias_Traits ~ Gender + Communication + International + Female_Bosses + Age + Education + Income + Ideology + Feminism + Religion, data = df, Hess = TRUE)
# Summary of the ordered logit model
# summary(ordered_model)
# Brant test for the proportional odds assumption
brant_test <- brant(ordered_model)
# Check if the proportional odds assumption holds
print(brant_test)
# < 0.05 for Ideology 0.0084
print("\n\n")

print("This is Bias_Interventions")
# Ordered Logistic Regression using the polr (proportional odds logistic regression) in MASS package
ordered_model <- polr(Bias_Interventions ~ Gender + Communication + International + Female_Bosses + Age + Education + Income + Ideology + Feminism + Religion, data = df, Hess = TRUE)
# Summary of the ordered logit model
# summary(ordered_model)
# Brant test for the proportional odds assumption
brant_test <- brant(ordered_model)
# Check if the proportional odds assumption holds
print(brant_test)
# < 0.05 for Gender (0.0170)
print("\n\n")



print("This is Bias_Competence")
# Ordered Logistic Regression using the polr (proportional odds logistic regression) in MASS package
ordered_model <- polr(Bias_Competence ~ Gender + Communication + International + Female_Bosses + Age + Education + Income + Ideology + Feminism + Religion, data = df, Hess = TRUE)
# Summary of the ordered logit model
# summary(ordered_model)
# Brant test for the proportional odds assumption
brant_test <- brant(ordered_model)
# Check if the proportional odds assumption holds
print(brant_test)
# < 0.05 - never. Low for Communication (0.0586)







# If the Brant test shows significant p-values (usually p < 0.05), consider multinomial logit
# if (any(brant_test$p.table[,5] < 0.05)) {
#   cat("The proportional odds assumption is violated.\n")
#   cat("Consider using a multinomial logistic regression model.\n")
#   # Multinomial Logistic Regression using multinom from nnet package
#   multinom_model <- multinom(Bias_Perception ~ Age + Income + LiberalViews, data = df)
#   # Summary of the multinomial logit model
#   summary(multinom_model)
# } else {
#   cat("The proportional odds assumption holds. The ordered logistic regression model is appropriate.\n")
# }