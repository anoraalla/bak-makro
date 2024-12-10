# Load necessary libraries
# install.packages("psych") # Uncomment this line if 'psych' package is not installed
library(psych)
library(ggplot2)

# setwd("/home/anna/Documents/bak-makro/stat")
setwd("/Users/kapsitis/workspace-public/bak-makro/stat")

# Read the CSV file into a data frame
df <- read.csv("Survey-Clean.08.csv")  # Replace with your actual file path

#df$Bias_Total <- mean(df$Bias_Perception, df$Bias_Family, df$Bias_Traits, df$Bias_Interventions, df$Bias_Competence)
df$Bias_Total <- rowMeans(
  data.frame(
    replace(df$Bias_Perception, is.na(df$Bias_Perception), 3),
    replace(df$Bias_Family, is.na(df$Bias_Family), 3),
    replace(df$Bias_Traits, is.na(df$Bias_Traits), 3),
    replace(df$Bias_Interventions, is.na(df$Bias_Interventions), 3),
    replace(df$Bias_Competence, is.na(df$Bias_Competence), 3)
  ), 
  na.rm = TRUE
)

df$Exposure <- rowMeans(
  data.frame(
    replace(df$Communication, is.na(df$Communication), 3),
    replace(df$International, is.na(df$International), 3)), 
  na.rm = TRUE
)



# mean(df$Communication, df$International)

# Select the relevant columns for Cronbach's Alpha calculation
# selected_columns <- df[, c("Bias_Perception", "Bias_Family", "Bias_Traits", "Bias_Interventions", "Bias_Competence")]
selected_columns <- df[, c("Bias_Family", "Bias_Traits", "Bias_Interventions", "Bias_Competence")]

# Compute Cronbach's Alpha
cronbach_alpha <- psych::alpha(selected_columns)


# Print the result
print(cronbach_alpha)