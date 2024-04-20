library(readr)
library(MASS)
library(ISLR2)
attach(palm_ffb)
palm_ffb <- read_csv("C:/Users/User/Downloads/Ace/palm_ffb.csv")
print(head(palm_ffb))
summary(palm_ffb)
regression1 <- lm(FFB_Yield ~ SoilMoisture + . -Date, data = palm_ffb)
summary(regression1)

regression2 <- lm(FFB_Yield ~ SoilMoisture + . -HA_Harvested-Date, data = palm_ffb)
summary(regression2)

regression3 <- lm(FFB_Yield ~ SoilMoisture + . -Max_Temp-HA_Harvested-Date , data = palm_ffb)
summary(regression3)

regression4 <- lm(FFB_Yield ~ SoilMoisture + . -Average_Temp-Max_Temp-HA_Harvested-Date, data = palm_ffb)
summary(regression4)

regression5 <- lm(FFB_Yield ~ SoilMoisture + . -Min_Temp-Average_Temp-Max_Temp-HA_Harvested-Date, data = palm_ffb)
summary(regression5)

regression6 <- lm(FFB_Yield ~ SoilMoisture + . -Working_days-Min_Temp-Average_Temp-Max_Temp-HA_Harvested-Date, data = palm_ffb)
summary(regression6)
