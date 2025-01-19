# We need to create a script in language R to compare votes for male and female candidates. 
# Read 248 lines from file "kandidatiZemgaleFinal.csv" (including a single header line). 
# The column names (given on the 1st line) will be the following: 
# (Apgabals,Struktūrvienība,Party,Name,Gender,Number,Pluses,Minuses)
# For every value of "Party" you can count the number of lines having Gender equal to value "Male" 
# and also the number of lines having Gender equal to value "Female". 
# The script needs to output a list of all values "Party" followed by two numbers (the count of "Male" and "Female" 
# values in the Gender column). 
# Here are some initial values in the CSV file:

library(dplyr)
library(ggplot2)

setwd("/Users/kapsitis/workspace-public/bak-makro/velesanas2")

candFiles <- c("kandidatiRigaFinal.csv", 
               "kandidatiVidzemeFinal.csv", 
               "kandidatiLatgaleFinal.csv", 
               "kandidatiKurzemeFinal.csv", 
               "kandidatiZemgaleFinal.csv")
candCounts <- c(650, 440, 265, 230, 247)
titles <- c("Riga", "Vidzeme", "Latgale", "Kurzeme", "Zemgale")

pVotesDf <- read.csv("partyVotesByDistrict.csv", stringsAsFactors = FALSE)

votesByRegion <- data.frame(Region = character(), 
                            PartyNum = integer(), 
                            Votes = integer(), 
                            MaleCand = integer(),
                            MalePluses = integer(),
                            MaleMinuses = integer(),
                            FemaleCand = integer(),
                            FemalePluses = integer(), 
                            FemaleMinuses = integer(),
                            stringsAsFactors = FALSE)
filteredVotes <- pVotesDf[pVotesDf$Struktūrvienība=="Rīga" & pVotesDf$Balsstiesīgie=="565297",]
for (party in 1:19) {
  votesByRegion <- rbind(votesByRegion, 
                         data.frame(Region = "Riga", 
                                    PartyNum = party, 
                                    Votes = as.numeric(filteredVotes[1, party+5]), 
                                    MaleCand=0, 
                                    MalePluses=0, 
                                    MaleMinuses=0, 
                                    FemaleCand=0, 
                                    FemalePluses=0, 
                                    FemaleMinuses=0))
}

for (theRegion in c("Vidzeme", "Latgale", "Kurzeme", "Zemgale")) {
  filteredVotes <- pVotesDf[pVotesDf$Struktūrvienība==theRegion,]
  for (party in 1:19) {
    votesByRegion <- rbind(votesByRegion, 
                           data.frame(Region = theRegion, 
                                      PartyNum = party, 
                                      Votes = as.numeric(filteredVotes[1, party+5]), 
                                      MaleCand=0, 
                                      MalePluses=0, 
                                      MaleMinuses=0, 
                                      FemaleCand=0, 
                                      FemalePluses=0, 
                                      FemaleMinuses=0))
  }  
}






for (i in 1:5) {
  # print(titles[i])
  df <- read.csv(candFiles[i], stringsAsFactors = FALSE)
  df <- head(df, candCounts[i])  # Only extract the total counts

  # If pivot_wider is causing issues due to package version or availability, you can use:
  # gender_counts <- table(df$Party, df$Gender)
  # print(gender_counts)
  
  partyValues <- df$Party
  genderValues <- df$Gender
  plusesValues <- df$Pluses
  minusesValues <- df$Minuses
  
  for (j in 1:length(partyValues)) {
    number_string <- gsub("^([0-9]+).*", "\\1", partyValues[j])
    partyNumber <- as.numeric(number_string)
    theGender <- genderValues[j]
    thePluses <- as.numeric(plusesValues[j])
    theMinuses <- as.numeric(minusesValues[j])
    condition <- votesByRegion$Region == titles[i] & votesByRegion$PartyNum == partyNumber
    num_rows_updated <- sum(condition)
    if (num_rows_updated != 1) {
      print(sprintf("Bad values for region %s, partyr %d", titles[i], partyNumber))
    }    
    if (theGender == "Male") {
      votesByRegion$MaleCand[condition] <- votesByRegion$MaleCand[condition] + 1
      votesByRegion$MalePluses[condition] <- votesByRegion$MalePluses[condition] + thePluses
      votesByRegion$MaleMinuses[condition] <- votesByRegion$MaleMinuses[condition] + theMinuses
    }
    if (theGender == "Female") {
      votesByRegion$FemaleCand[condition] <- votesByRegion$FemaleCand[condition] + 1
      votesByRegion$FemalePluses[condition] <- votesByRegion$FemalePluses[condition] + thePluses
      votesByRegion$FemaleMinuses[condition] <- votesByRegion$FemaleMinuses[condition] + theMinuses 
    }
  }
}

votesByRegion$bias <- (votesByRegion$MalePluses - votesByRegion$MaleMinuses)/(votesByRegion$MaleCand * votesByRegion$Votes) - 
  (votesByRegion$FemalePluses - votesByRegion$FemaleMinuses)/(votesByRegion$FemaleCand * votesByRegion$Votes)


# Compute weighted bias for each PartyNum
weighted_bias <- votesByRegion %>%
  group_by(PartyNum) %>%
  summarise(
    weightedBias = sum(bias * Votes) / sum(Votes)
  )

# Print the computed weighted bias values
print(weighted_bias)

# Plot the weighted bias using ggplot2
# ggplot(weighted_bias, aes(x = as.factor(PartyNum), y = weightedBias)) +
#   geom_bar(stat = "identity") +
#   coord_flip() +  # To make horizontal bars
#   labs(title = "Weighted Bias by PartyNum", x = "PartyNum", y = "Weighted Bias") +
#   theme_minimal()


shortnames <- c("Unity", "Russian Union", 
                "Greens and Farmers", "Folk Servants", 
                "Sovereign Power", "Christian Party", 
                "Harmony" ,"For Stability",
                "People's Might", "United for Latvia", 
                "National Union", "Latvia First", 
                "Conservatives", "For Everyone", 
                "Progressives", "Development/Pro!", 
                "Union for Latvia", "Unified List", 
                "Republic")

weighted_bias$PartyName <- shortnames[weighted_bias$PartyNum]

# weighted_bias$Elected <- c(1,0,1,0,0,0,0,1,0,0,1,1,0,0,1,0,0,1,0)
weighted_bias$Elected <- c("1","0","1","0","0","0","0","1","0","0",
                           "1","1","0","0","1","0","0","1","0")


weighted_bias <- weighted_bias %>%
  arrange(weightedBias)

p <- ggplot(weighted_bias, aes(x = reorder(PartyName, weightedBias), y = weightedBias, fill = as.factor(Elected))) +
  geom_bar(stat = "identity") +
  coord_flip() +  # Flip to make horizontal bars
  labs(
    title = "Weighted Bias by Party",
    x = "Party",
    y = "Weighted Bias",
    fill = "Elected Status"  # Legend title
  ) +
  theme_minimal() +
  theme(
    plot.title = element_text(family = "Times New Roman", face = "bold", size = 14),
    axis.title.x = element_text(family = "Times New Roman", size = 12),
    axis.title.y = element_text(family = "Times New Roman", size = 12),
    axis.text.x = element_text(family = "Times New Roman", size = 12),
    axis.text.y = element_text(family = "Times New Roman", size = 12)
  ) + 
  scale_fill_manual(values = c("0" = "lightgray", "1" = "skyblue"), labels = c("Not Elected", "Elected"))

ggsave("gender_bias.png", plot = p, width = 10, height = 6, dpi = 300)
