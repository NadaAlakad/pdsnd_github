import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York': 'new_york_city.csv',
              'Washington': 'washington.csv'}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, "none" or "all" to apply no month filter
        (str) day - name of the day of week to filter by, "none" or "all" to apply no day filter
    """
    print('Hello dear! exploring data is so much fun, Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
      city = input("Which city would you like to see data for: Chicago, New York, or Washington?\n").title()
      if city not in ('Chicago', 'New York', 'Washington'):
        print("Not an appropriate choice. Make sure you pick one of the choices (Chicago, New York, or Washington)")
        continue
      else:
        break
    # TO DO: get user input for filter preference
    while True:
      filters = input("Would you like to filter the date by day, month or both? or type 'none' if you don't want to apply filter. \n").title()
      if filters not in ('Day', 'Month', 'Both', 'None'):
        print("Not an appropriate choice. Make sure you pick one of the choices (day, month, both, none).")
        continue
      else:
        break

    #Skip user input if none picked
    if filters != 'None':

      #Apply condition for date filter preference
      if filters != 'Day':
        # TO DO: get user input for month (all, january, february, ... , june)
        while True:
          month = input("\nWhich month would you like to filter by? months available (January, February, March, April, May, June) or type 'all' to see all or type 'none' if you don't want to apply filter. \n").title()
          if month not in ('January', 'February', 'March', 'April', 'May', 'June', 'All', 'None'):
            print("Not an appropriate choice. Make sure you pick one of the choices (January, February, March, April, May, June, all, none).")
            continue
          else:
            break
      else:
          month = 'All'



      #Apply condition for date filter preference
      if filters != 'Month':
      # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        while True:
          day = input("\nWhich day would you like to filter by? Type on of these days (Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday) or type 'all' if you want all or type 'none' if you don't want to apply filter. \n").title()
          if day not in ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'All', 'None'):
            print("Not an appropriate choice. Make sure you pick one of the choices (Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, all, none). ")
            continue
          else:
            break
      else:
          day = 'All'
    else:
        day = 'All'
        month = 'All'



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
    if month != 'All' and month != 'None':
        # use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1

      # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'All' and day != 'None':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    # extract month from the Start Time column to create an month column
    df['month'] = df['Start Time'].dt.month

    # find the most common month
    popular_month = df['month'].value_counts().idxmax()
    print('Most common month: ', popular_month)

    # TO DO: display the most common day of week
    # extract day of week from the Start Time column to create an day column
    df['day'] = df['Start Time'].dt.month

    # find the most common day
    popular_day = df['day'].value_counts().idxmax()
    print('Most common day of the week: ', popular_day)

    # TO DO: display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most common hour (from 0 to 23)
    popular_hour = df['hour'].value_counts().idxmax()
    print('Most common start hour: ', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most used start station
    # find the most common start station
    popular_start_station = df['Start Station'].value_counts().idxmax()
    print('Most common start station: ', popular_start_station)

    # TO DO: display most used end station
    # find the most common end station
    popular_end_station = df['End Station'].value_counts().idxmax()
    print('Most common used end station: ', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    combine_stations = df.groupby(['Start Station','End Station']).count()
    print('Most frequent start station and end station trips are: ', popular_start_station, " & ", popular_end_station)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = sum(df['Trip Duration'])
    print('Total travil time: ', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travil time: ', mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of user types: ',user_types)


    # TO DO: Display counts of gender
    try:
      gender = df['Gender'].value_counts()
      print('Counts of gender: ',gender)
    except KeyError:
      print("Counts of gender: No data available.")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
      earliest_year = df['Birth Year'].min()
      print('Earliest year:', earliest_year)
    except KeyError:
      print("Earliest Year: No data available.")

    try:
      recent_year = df['Birth Year'].max()
      print('Recent year: ', recent_year)
    except KeyError:
      print("Recent year: No data available.")

    try:
      common_year = df['Birth Year'].value_counts().idxmax()
      print('Common year: ', common_year)
    except KeyError:
      print("Common year: No data available.")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
  """Display 5 of raw data a time if the user wants and keep going 5 by 5 until the user stop it. """
  count = 0
  answer = input('\nWould you like to see 5 lines of raw data? Enter yes or no.\n')
  while True:
     # Check if response is yes, print the raw data and increment count by 5
    if answer.lower() == 'yes':
      print(df[count:count+5])
      count = count+5
      answer = input('\nWould you like to see 5 lines more of raw data? Enter yes or no.\n')
    # otherwise break
    else:
      break


def main():
    """Displays data depend on user choices of filtration and it restart the program if the user pick to restart."""
    while True:
        #Set all user filters into the variables then load data as per filters
        city, month, day = get_filters()
        df = load_data(city, month, day)

        #Run all functions to show filtered data
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        #Find out if user want to restart the program or stop it then do the action
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
