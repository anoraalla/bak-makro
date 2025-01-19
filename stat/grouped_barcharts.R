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

# Load necessary libraries
library(ggplot2)
library(tidyr)
library(dplyr)
library(RColorBrewer)

# Sample data frame
# df <- data.frame(
#   Bias_Perception = sample(1:5, 100, replace = TRUE),
#   Bias_Family = sample(1:5, 100, replace = TRUE),
#   Bias_Traits = sample(1:5, 100, replace = TRUE),
#   Bias_Interventions = sample(1:5, 100, replace = TRUE),
#   Bias_Competence = sample(1:5, 100, replace = TRUE)
# )

# Reshape data to long format
df_long <- df %>%
  pivot_longer(cols = c("Bias_Perception", "Bias_Family", "Bias_Traits", "Bias_Interventions", "Bias_Competence"),
               names_to = "Bias_Type",
               values_to = "Likert_Score")

bar_width <- 0.8   # default width of each bar
dodge_width <- bar_width * 1

# Create the plot
grouped_barcharts <- ggplot(df_long, aes(x = factor(Likert_Score), fill = Bias_Type)) +
  # geom_bar(position = "dodge", stat = "count") +
  geom_bar(position = position_dodge(width = dodge_width), stat = "count", width = bar_width) +
  # scale_fill_manual(values = c("Bias_Perception" = "blue",
  #                              "Bias_Family" = "red",
  #                              "Bias_Traits" = "green",
  #                              "Bias_Interventions" = "purple",
  #                              "Bias_Competence" = "orange")) +
  scale_fill_brewer(palette = "Set1") +
  labs(x = "Answer on Likert Scale",
       y = "Answer Count",
       fill = "Bias Type") +
  ggtitle("Distribution of Bias Variables") +
  theme_minimal(base_family = "Times New Roman") +
  theme(
    plot.title = element_text(size = 14, face = "bold", hjust = 0.5),
    axis.title = element_text(size = 12),
    axis.text = element_text(size = 10),
    text = element_text(family = "Times New Roman"), 
    panel.background = element_rect(fill = "white", color = NA), # Set panel background to white
    plot.background = element_rect(fill = "white", color = NA) # Set plot background to white
  )

ggsave(filename = "grouped_barcharts.png", plot = grouped_barcharts, width = 8, height = 6, dpi = 300)
