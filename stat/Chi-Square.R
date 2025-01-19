# Load necessary libraries
# install.packages("psych") # Uncomment this line if 'psych' package is not installed
library(psych)
library(ggplot2)

# setwd("/home/anna/Documents/bak-makro/stat")
setwd("/Users/kapsitis/workspace-public/bak-makro/stat")
# Read the CSV file into a data frame
df <- read.csv("Survey-Clean.08.csv")  # Replace with your actual file path


# Optionally recode "Feminism" values to numeric
# df$Feminism_numeric <- as.numeric(factor(df$Feminism, levels = c("Not important", "Slightly important", "Moderately important", "Important", "Extremely important")))

# Create a contingency table
contingency_table <- table(df$Communication, df$Feminism)

# Perform the chi-square test
chi_square_test <- chisq.test(contingency_table)

# Check results
print(chi_square_test)


heatmap_data <- as.data.frame(as.table(contingency_table))

# Rename columns for clarity
colnames(heatmap_data) <- c("Communication", "Feminism", "Frequency")

# Plot the heatmap
heatmap <- ggplot(heatmap_data, aes(x = Feminism, y = Communication, fill = Frequency)) +
  geom_tile(color = "white") +  # Draw the heat map cells
  geom_text(aes(label = Frequency), color = "black", 
            vjust = 0.5, hjust = 0.5, size = 4, family = "Times New Roman") +  # Add text labels
  scale_fill_gradient(low = "#FFFFFF", high = "#0066CC") +  # Use a color gradient
  labs(title = "Response Count by Feminism Importance and Job Communication",
       x = "Feminism Importance",
       y = "Communication Level") +
  theme_minimal(base_family = "Times New Roman") +
  theme(
    plot.title = element_text(size = 14, face = "bold", hjust = 0.5),
    axis.title = element_text(size = 12, color = "#000000FF"),
    axis.text = element_text(size = 10, color = "#000000FF"),
    text = element_text(family = "Times New Roman"), 
    panel.background = element_rect(fill = "#FFFFFFFF", color = NA), # Set panel background to white
    plot.background = element_rect(fill = "#FFFFFFFF", color = NA) # Set plot background to white
  )
  
  #  theme_minimal() +
#  theme(axis.text.x = element_text(angle = 45, hjust = 1))  # Rotate x-axis labels for better readability
ggsave(filename = "heatmap.png", plot = heatmap, width = 8, height = 4, dpi = 300)
