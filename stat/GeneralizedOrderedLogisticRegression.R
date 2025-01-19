# Assuming df is your dataframe and it includes Bias_Perception as the dependent variable
library(MASS)         # For ordered logistic regression
library(nnet)         # For multinomial logistic regression
library(brant)        # For the Brant test

library(psych)
library(ggplot2)
library(VGAM)
library(dplyr)

setwd("/Users/kalvi/workspace-public/bak-makro/stat")
df <- read.csv("Survey-Clean.08.csv")  # Replace with your actual file path

# Convert Bias_Perception to a factor, specify ordered levels
df$Bias_Perception <- factor(df$Bias_Perception, levels = c(1, 2, 3, 4, 5), ordered = TRUE)
df$Bias_Family <- factor(df$Bias_Family, levels = c(1, 2, 3, 4, 5), ordered = TRUE)
df$Bias_Traits <- factor(df$Bias_Traits, levels = c(1, 2, 3, 4, 5), ordered = TRUE)
df$Bias_Interventions <- factor(df$Bias_Interventions, levels = c(1, 2, 3, 4, 5), ordered = TRUE)
df$Bias_Competence <- factor(df$Bias_Competence, levels = c(1, 2, 3, 4, 5), ordered = TRUE)


#df <- na.omit(df)  # Remove NA values
df <- df %>% mutate_all(~ifelse(is.na(.), 1, .))

# df$Gender <- factor(df$Gender, levels=c(1,2), ordered=TRUE)
# df$Communication <- factor(df$Communication, levels = c(1, 2, 3, 4, 5), ordered = TRUE)
# df$International <- factor(df$International, levels = c(1, 2, 3, 4, 5), ordered = TRUE)
# df$Female_Bosses <- factor(df$Female_Bosses, levels = c(1, 2, 3, 4, 5), ordered = TRUE)
# df$Age <- factor(df$Age, levels = c(1, 2, 3, 4, 5, 6), ordered = TRUE)
# df$Education <- factor(df$Education, levels = c(1, 2, 3, 4, 5), ordered = TRUE)
# df$Income <- factor(df$Income, levels = c(1, 2, 3, 4, 5, 6, 7), ordered = TRUE)
# df$Ideology <- factor(df$Ideology, levels = c(1, 2, 3, 4, 5), ordered = TRUE)
# df$Election <- factor(df$Election, levels = c(1, 2), ordered = TRUE)
# df$Feminism <- factor(df$Feminism, levels = c(1, 2, 3, 4, 5), ordered = TRUE)
# df$Religion <- factor(df$Religion, levels = c(1, 2, 3), ordered = TRUE)


library(ggplot2)
library(dplyr)

# Convert "Communication" column to a factor with ordered levels
df$Communication <- factor(df$Communication, levels = c(1, 2, 3, 4, 5))

df$Bias_Family <- ifelse(df$Bias_Family %in% c(3, 4, 5), 3, df$Bias_Family)

# Create the stacked bar chart
# p <- ggplot(df, aes(x = Bias_Family, fill = Communication)) +
#   geom_bar(position = "fill") +
#   labs(x = "Bias Family", y = "Proportion") +
#   scale_fill_manual(values = c("#F8766D", "#7CAE00", "#00BFC4", "#C77CFF", "#619CFF"),
#                     name = "Communication") +
#   theme_minimal()

p <- ggplot(df, aes(x = Bias_Family, fill = Communication)) +
  geom_bar(position = "stack") +
  labs(x = "Bias Family", y = "Count") +
  scale_fill_manual(values = c("#F8766D", "#7CAE00", "#00BFC4", "#C77CFF", "#619CFF"),
                    name = "Communication") +
  theme_minimal()


# Save the plot to a PNG file
ggsave("Bias_Family_per_Communication_after_rename.png", plot = p, width = 8, height = 6)


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



# 
# generalized_model <- vglm(Bias_Perception ~ Gender + Communication + 
#                             International + Female_Bosses + Age + 
#                             Education + Income + Ideology + 
#                             Election + Feminism + Religion, 
#                           family = cumulative(parallel=FALSE), data = df)

# summary(generalized_model)

# 
# lapply(df[, c("Gender", "Communication", "International", "Female_Bosses", 
#               "Age", "Education", "Income", "Ideology", 
#               "Election", "Feminism", "Religion")], function(x) {
#                 cat("Variable: ", deparse(substitute(x)), "\n")
#                 print(table(x))
#                 cat("Levels: ", levels(x), "\n\n")
#               })


