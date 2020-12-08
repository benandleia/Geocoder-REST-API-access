require(dplyr)
require(readr)

#Set the working directory, the file path where the files of interest are located. Almost always the first step.

setwd("C:/Users/SnowBe/Desktop/")

#Import the well .csv data

input_data <- read_csv("well.csv")

#############################################################SOME WORK TO EXAMINE THE DATA ##############################################################################

#Get a seperate data frame that shows all the unique locality values. YIKES!!!

localities_unique <- summarize(group_by(input_data, city), location_count = n())

#Figure out how many wells have a parcel ID. Same process as above, but if the PID is classed as "NA" that means there is no Parcel ID associated with the record

PID_unique <- summarize(group_by(input_data, legal_pid), PID_count = n())

#Same as above, but check to see if any sites are missing latitude coordinates

lat_unique <- summarize(group_by(input_data, latitude), lat_unique = n())

#Same as above, but check to see if any sites are missing longitude coordinates

long_unique <- summarize(group_by(input_data, longitude), long_unique = n())

#Dec 8, 2020 -- Looks like 2461 missing lat/long values. They are extracted and saved below.

missing_coords <- filter(input_data, is.na(latitude))

#Within the subset of missing lat/long values, find ones that are also missing location information

really_missing <- filter(missing_coords, is.na(city))

#Find stuff with no legal township

no_townships <- filter(really_missing, is.na(legal_township))