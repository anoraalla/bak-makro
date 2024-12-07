# Load necessary libraries
# install.packages("psych") # Uncomment this line if 'psych' package is not installed
library(psych)
library(ggplot2)

setwd("/home/anna/Documents/bak-makro/stat")
# Read the CSV file into a data frame
df <- read.csv("12-01.csv")  # Replace with your actual file path

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
selected_columns <- df[, c("Bias_Perception", "Bias_Family", "Bias_Traits", "Bias_Interventions", "Bias_Competence")]

# Compute Cronbach's Alpha
cronbach_alpha <- psych::alpha(selected_columns)


# Print the result
print(cronbach_alpha)

bias_by_exposure <- ggplot(df, aes(x = Exposure, y = Bias_Total)) +
  geom_point() +  # Add scatter plot points
  geom_smooth(method = "lm", se = FALSE, color = "blue") +  # Add regression line (lm = linear model)
  labs(title = "Exposure vs. Bias Total",
       x = "Exposure",
       y = "Bias Total") +
  theme_minimal()

ggsave(filename="bias_by_exposure.png", plot=bias_by_exposure, width=8, height=6, dpi=300)



columns_to_plot <- c("Gender", "Age", "Residence", "Education", "Income", "Religion", 
                     "Ideology", "Election", "Party", "Candidate_Pluses", "Candidate_Minuses", 
                     "Routine", "Feminism", "Sector", "NACE", "Communication", "International", "Female_Bosses")

df[columns_to_plot] <- lapply(df[columns_to_plot], as.factor)

output_dir = "boxplots"

if (!dir.exists(output_dir)) {
  dir.create(output_dir)
}

for (colname in columns_to_plot) {
    # plot_formula <- as.formula(paste(colname, "~ Bias_Total"))
  
    # if (colname == "Gender") {
    #  df[[colname]] <- factor(df[[colname]], levels = c(1, 2), labels = c("Female", "Male"))
    #}
    
    boxplot <- ggplot(df, aes_string(x = colname, y = "Bias_Total")) +
      geom_boxplot() +
      labs(title = paste("Bias Total by ", colname),
           x = colname,
           y = "Bias Total") +
      theme_minimal()
    
    ggsave(filename=paste0(output_dir, "/", colname, "_boxplot.png"), 
           plot=boxplot, width=8, height=6, dpi=300)
}    
