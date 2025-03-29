import time

# Get current time
timestamp = time.strftime('%H:%M:%S')
print("Current time:", timestamp)

# Extract hours, minutes, and seconds
hour = int(time.strftime('%H'))
minute = int(time.strftime('%M'))
second = int(time.strftime('%S'))

# Print greetings based on the current time
if 0 <= hour < 12:
    print("Good Morning.")
elif 12 <= hour < 18:
    print("Good Afternoon.")
else:
    print("Good Night.")
