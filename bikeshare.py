import time
import pandas as pd
import numpy as np

<<<<<<< HEAD
#python is fun
#numpy is fun too
||||||| merged common ancestors
=======
#Ride Bikes Eh

>>>>>>> documentation
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

    cities = ['chicago', 'new york city', 'washington']
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    days = ['All', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    city = ''
    month = ''
    day = ''
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while city not in cities:
       city = input('chicago, new york city, or washington: ').strip().lower()


    # TO DO: get user input for month (all, january, february, ... , june)
    while month not in months:
        month = input('pick a month: ').strip().lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while day not in days:
        day = input('pick a day of the week: ').strip().capitalize()

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

    # acceptable responses for month and days to be used later in if statements.
    months = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'july': 7, 'august':8, 'september': 9, 'october': 10, 'november': 11, 'december': 12}
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

    # get appropriate csv file and put in dataframe
    df = pd.read_csv(CITY_DATA[city])

    #convert start time to_datetime and extract month and day of week
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    #drop rows that arent in month or day
    if month in months:
        df = df[df.month == months[month]]
    if day in days:
        df = df[df.day_of_week == day]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('most popular month: ', popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('most popular day: ', popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    # find the most popular hour
    popular_hour = df['hour'].mode()[0]
    print('most popular time: ', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('most popular start station: ', popular_start_station)


    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('most popular end station: ', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Start_End'] = df['Start Station'] + ' TO ' + df['End Station']
    popular_start_end = df['Start_End'].mode()[0]
    print('most popular journey is: ', popular_start_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = sum(df['Trip Duration'])
    print('Total travel second: ', total_time)
    # TO DO: display mean travel time
    mean_trip = df.loc[:,'Trip Duration'].mean()
    print('Average trip in seconds: ', mean_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    cust_count = df['User Type'].value_counts()
    print(cust_count)
    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender_count = df['Gender'].value_counts()
        print(gender_count)



    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        most_frequent = df['Birth Year'].mode()[0]
        youngest = df['Birth Year'].max()
        oldest = df['Birth Year'].min()
        print('The oldest user was born in: ', oldest)
        print('The youngest user was born in: ', youngest)
        print('The most common year for a user to be born is: ', most_frequent)
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)

def raw_data(df):
    a=0
    """print 5 lines of raw data at a time"""
    print_lines = input('\nWould you like to print some raw data? Enter yes or no.\n')
    if print_lines.lower() == 'yes':
        print(df.loc[[a,a+1,a+2,a+3,a+4]])
        while True:
            print_again = input('\nWould you like to some MORE raw data? Enter yes or no.\n')
            if print_again.lower() == 'yes':
                a += 5
                print(df.loc[[a,a+1,a+2,a+3,a+4]])
            else:
                break






def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
