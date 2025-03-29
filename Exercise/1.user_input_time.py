# Function to convert time input to 24-hour format and extract hours and minutes
def convert_to_24hr(time_str):
    import datetime
    time_obj = datetime.datetime.strptime(time_str, '%I:%M %p')
    return time_obj.hour, time_obj.minute

# Input time from user
time = input('Enter time (in HH:MM AM/PM format): ')

# Convert time using the function
hour, minute = convert_to_24hr(time)

# Determine the period of the day
if 0 <= hour < 12:
    print("Good Morning.")
elif 12 <= hour < 18:
    print("Good Afternoon.")
else:
    print("Good Night.")
