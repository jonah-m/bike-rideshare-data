import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs.
    while True:
        city = input("Please enter the city you would like to get data on. (Chicago, New York City, Washington)\n").lower()
        if city.lower() not in ("chicago", "new york city", "washington"):
            print("That was an invalid entry. Please try again.")
        else:
            print("You selected " + city.title())
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("Please enter the month: \n" ).lower()
        if month not in ("all", "january", "february", "march", "april", "may", "june"):
            print("Invalid entry PLease try again.")
        else:
            print("You selected " + month.title())
            break
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Please select the day: all, Monday, Tueday, Wednesday, Thursday, Friday, Saturday, Sunday: \n").lower()
        if day not in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
            print("Invalid entry. Please try again.")
        else:
            print("You selected :" + day.title())
            break

        

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july','august', 'september', 'october', 'november', 'decemeber']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].value_counts().index.to_list()[0]
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    print("What is the most frequent month in the time frame you selected?")
    print(months[common_month - 1])
    # display the most common day of week
    common_day = df['day_of_week'].value_counts().index.to_list()[0]
    print("What is the most common day in the time frame you selected?")
    print(common_day)
    # display the most common start hour
    common_hour = df['Start Time'].dt.hour.value_counts().index.to_list()[0]
    print("What is the most common hour of the day(s) selected?")
    print(common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    frequent_start_station = df['Start Station'].value_counts().index.to_list()[0]
    print("What is the most commonly used start station?")
    print(frequent_start_station)

    # display most commonly used end station
    frequent_end_station = df['End Station'].value_counts().index.to_list()[0]
    print("What is the most commonly used end station?")
    print(frequent_end_station)

    # display most frequent combination of start station and end station trip
    #create a new column to easily pick up the most common value in the list
    df['route'] = df['Start Station'] + df['End Station']
    common_route = df['route'].value_counts().index.to_list()[0]
    print("What is the most common route?")
    print(common_route)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel = sum(df['Trip Duration'])
    print("What is the total travel time for the time period selected in minutes?")
    print(str(int(total_travel / 60)) + " minutes.")

    # display mean travel time
    travel_list = df['Trip Duration'].value_counts().index.to_list()
    mean_travel = sum(travel_list) / len(travel_list)

    print("What is the average travel time for this period in minutes?")
    print(str(int(mean_travel / 60)) + " minutes.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('What is the count for Customers and Subscribers?')
    print(df['User Type'].value_counts())

    # Display counts of gender
    if 'Gender' in df:
        print(df['Gender'].value_counts())
    else:
        print("There is no data regarding Genders")
    

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        birth_year = df['Birth Year'].value_counts().index.to_list()
        print('What is the Earliest Birth Year?')
        print( min(birth_year))
        print('What is the most recent birth year?')
        print(max(birth_year))
        print("What is the most common birth year?")
        print(df['Birth Year'].value_counts().index.to_list()[0])
    else:
        print("There is no data about birth years in the current date selection.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        while True:
            n = 1
            i = 6
            raw_data = input("Would you like to take a look at the raw data? Yes/No").lower()
            if raw_data not in ('yes', 'no'):
                print("You entered an invalid answer. Try Again.")
            elif raw_data == 'yes':
                while True:
                    pd.set_option('display.max_columns', None)
                    print(df[n:i])
                    new_input = input("Would you like to see the next set of data?").lower()
                    if new_input == 'yes':
                        n += 5
                        i +=5
                    
                    else:
                        break
            else:
                break
                           
                    
            
            



        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()


