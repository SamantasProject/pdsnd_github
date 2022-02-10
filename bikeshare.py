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
    
    # TO DO: get user input for city (chicago, new york city, washington).
    while True:
        city = input("Would you like to see data for Chicago, New York City or Washington? ").lower()
        if city in ('chicago', 'new york city', 'washington'):
            break
        else:
            print("Sorry, but your input doesn\'t seem right. Please try again.")
    
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Would you like to see data for January, February, March, April, May, June or all? ").lower()
        if month in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            break
        else:
            print("Sorry, but your input doesn\'t seem right. Please try again.")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Would you like to see data for Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all? ").lower()
        if day in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all'):
            break
        else:
            print("Sorry, but your input doesn\'t seem right. Please try again.")

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
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month, day of week, hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
        
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('Most common month:', common_month)

    # TO DO: display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    print('Most common day:', common_day_of_week)

    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]
    print('Most common start hour:', common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].value_counts().idxmax()
    print('Most common start station:', start_station)

    # TO DO: display most commonly used end station
    end_station = df['End Station'].value_counts().idxmax()
    print('Most common end station:', end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['stations'] = df['Start Station'] + ' and ' + df['End Station']
    combination = df['stations'].mode()[0]
    print('Most common combination of start and end stations:', combination)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_trip = df['Trip Duration'].sum()
    print('Total travel time in days:', total_trip/86400)

    # TO DO: display mean travel time
    mean_trip = df['Trip Duration'].mean()
    print('Average travel time in minutes:', mean_trip/60)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print('User Type:\n', user_type, '\n')

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        counts_gender = df['Gender'].value_counts()
        print('Gender Split:\n', counts_gender, '\n')
    else:
        print("Gender: No data available.")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_yob = df['Birth Year'].min()
        print('Earliest year of birth:', earliest_yob)
    except KeyError:
        print("Earliest year of birth: No data available.")
    
    try:
        recent_yob = df['Birth Year'].max()
        print('Latest year of birth:', recent_yob)
    except KeyError:
        print("Latest year of birth: No data available.")
    
    try:
        common_yob = df['Birth Year'].value_counts().idxmax()
        print('Most common year of birth:', common_yob)
    except KeyError:
        print("Most common year of birth: No data available.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    # TO DO: Add "show raw data" functionality
def raw(df):
    """Asking users if they want to see raw data"""
    
    raw_data = 0
    
    while True:
        answer = input("Would you like to see the raw data? Please say yes or no: ").lower()
        if answer not in ['yes', 'no']:
            answer = input("Please say yes or no: ").lower()
        elif answer == 'yes':
            raw_data += 5
            print(df.iloc[raw_data : raw_data + 5])
            again = input("Would you like to see more data? Please say yes or no ").lower()
            if again == 'no':
                break
        elif answer == 'no':
            return


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
