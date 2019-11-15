import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_DATA = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

DAY_DATA = ['all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Would you like to see data for Chicago, New York City, or Washington? ").lower()

    while city not in ['chicago', 'new york city', 'washington']:
        city = input("Invalid Input! Please select Chicago, New York City, or Washington: ").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Would you like to filter by month? If no, type All: ").lower()

    while month not in MONTH_DATA:
        month = input("Invalid Input! Please select January, February, March, April, May, June, or All: ").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Would you like to filter by day of the week? If no, type All: ").lower()

    while day not in DAY_DATA:
        day = input("Invalid Input! Please select Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or All: ").lower()

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

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

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
    print("The most popular month is: {}".format(
        str(df['month'].mode()[0]))
    )

    # TO DO: display the most common day of week
    print("The most popular day of the week: {}".format(
        str(df['day_of_week'].mode()[0]))
    )

    # TO DO: display the most common start hour
    df['start_hour'] = df['Start Time'].dt.hour
    print("The most popular start hour: {}".format(
        str(df['start_hour'].mode()[0]))
    )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most popular start station is: {} ".format(
        df['Start Station'].mode()[0])
    )


    # TO DO: display most commonly used end station
    print("The most popular end station is: {}".format(
        df['End Station'].mode()[0])
    )

    # TO DO: display most frequent combination of start station and end station trip
    df['trips'] = df['Start Station']+ " " + df['End Station']
    print("The most popular trip start to end is: {}".format(
        df['trips'].mode()[0])
    )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    print("The total travel time is: {} seconds".format(
        str(int(df['Trip Duration'].sum())))
    )

    # TO DO: display mean travel time
    print("The average travel time is: {} seconds".format(
        str(int(df['Trip Duration'].mean())))
    )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()

    print("Here is a breakdown of user types:")
    print(user_types)

    # TO DO: Display counts of gender
    if city != 'washington':
        genders = df['Gender'].value_counts()
        print("Here is a breakdown by gender:")
        print(genders)

    # TO DO: Display earliest, most recent, and most common year of birth
        print("The earliest birth year is: {}".format(
            str(int(df['Birth Year'].min())))
        )
        print("The latest birth year is: {}".format(
            str(int(df['Birth Year'].max())))
        )
        print("The most common birth year is: {}".format(
            str(int(df['Birth Year'].mode()[0])))
        )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def show_ten_rows(df):
    """Displays raw data in increments of 10 rows on user command."""

    #Declare prompt and parameters for iloc
    start_row = 0
    end_row = 10
    prompt = input("Do you want to see 10 rows of raw data? 'Yes' or 'No': ").lower()

    #while loop to validate input
    while prompt not in ['yes', 'no']:
        prompt = input("Invalid Input! Please type 'Yes' or 'No': ").lower()
    if prompt == 'yes':
        #while loop through the last row of data to view increments of 5 rows
        while end_row <= df.shape[0]-1:
            print(df.iloc[start_row:end_row])
            start_row += 10
            end_row += 10

            answer = input("Would you like to see 10 more rows? Type 'Yes' or 'No': ").lower()
            #while loop to validate input
            while answer not in ['yes', 'no']:
                answer = input("Invalid Input! Please type 'Yes' or 'No': ").lower()
            if answer == 'yes':
                continue
            else:
                break
    else:
        return

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        show_ten_rows(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
