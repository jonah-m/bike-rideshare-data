# bike-rideshare-data
<b><h2>Library details</h2></b>
* Python Version 3.9.7
* Numpy Version 1.20.3
* Pandas Version 1.3.4

<b><h2>Project Details</h2></b>
This project explores bike sharing data in three cities:
* Chicago
* New York City
* Washington 

The data is from the first 6 months of the year 2017.
Using user Input, we ask the user which city they would like to look at data for, as well as:
* The specific month or all
* The specific day of the week or all
* This will pull in data from a csv file, and then extract just the data we were looking for into a dataframe.

With that information, a function called time_stats calculates the following in terms of start times in a given data set:
*The most common month
* The most common Day
* The most common hour

The function station_stats calculates:
* The most common start station
* The most common end Station
* The most common route with the same start and end station

trip_duration_stats function calculates the following:
* Total travel time in the given timeframe selected by the user
* The average trip in the same given time frame based on user input

2 of the cities has information on gender and date of birth of the riders. With that information given, the function user_stats calculates:
* The number of subscribers and customers in the time frame given
* Counts each gender using the bike share service at that time
* Displays the earliest, latest, and most common birth year of riders

At the end, the script then asks the user if they would like to see the raw data. If requested, the script will run 5 lines of data from the dataframe and will ask the user if they would like to see any more data, and stops the script when the user does not want to see any more data, and does not want to restart the program.
