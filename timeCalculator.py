#Skye Panaligan
def convert_seconds(seconds):
        
    #Constants
    SECONDS_IN_MINUTE = 60
    SECONDS_IN_HOUR = 3600
    SECONDS_IN_DAY = 86400

    # Calculate days
    days = seconds // SECONDS_IN_DAY
    day_remainder = seconds % SECONDS_IN_DAY

    # Calculate hours
    hours = day_remainder // SECONDS_IN_HOUR
    hour_remainder = day_remainder % SECONDS_IN_HOUR

    # Calculate minutes
    minutes = hour_remainder // SECONDS_IN_MINUTE
    seconds_remainder = hour_remainder % SECONDS_IN_MINUTE

    return days, hours, minutes, seconds_remainder


# Get input from user
try:
    seconds = int(input("Enter the number of seconds: "))
except ValueError:
    print("Please enter a valid integer for seconds.")


if seconds >= 60:
    print(str(seconds) + " seconds are equal to:")
    minutes = seconds//60
    remainderSeconds = seconds - (minutes * 60)

    print(str(minutes) + " full minute(s) and " + str(remainderSeconds) + " seconds.")
if seconds >=3600:
    hours = seconds//3600
    remainderSeconds = seconds - (hours * 3600)

    print(str(hours) + " full hours(s) and " + str(remainderSeconds) + " seconds.")
if seconds >= 86400:
    days = seconds//86400
    remainderSeconds = seconds - (days * 86400)

    print(str(days) + " full day(s) and " + str(remainderSeconds) + " seconds")