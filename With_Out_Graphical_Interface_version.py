#Step 1 : Import the necessary librairies
import time

###################################################################################
#Step 2 : define the functions 
def up_date_time(hours, minutes, seconds): #up date the time
    seconds += 1 
    if seconds == 60: 
        seconds = 0
        minutes += 1
    if minutes == 60:
        minutes = 0
        hours += 1
    if hours == 24:
        hours = 0
    return hours, minutes, seconds


def format_time(hours, minutes, seconds, format_choice): #choose the format 
    struct_time = time.struct_time((2025, 1, 6, hours, minutes, seconds, 0, 0, -1))
    if format_choice == '12h':
        return time.strftime("%I:%M:%S %p", struct_time) #for the 12h format, we have to add the %p options to destinguish between morning and afternoon
    elif format_choice == '24h':
        return time.strftime("%H:%M:%S", struct_time)  
    else:
        raise ValueError("Invalid format choice! Please choose '12h' or '24h'.")


def alarm_setting(current_h, current_m, current_s, alarm_h, alarm_m, alarm_s): #Check if the alarm time matches the current time
    return (current_h == alarm_h and current_m == alarm_m and current_s == alarm_s)


def print_time(formatted_time): #Print the formated time
    print(f"The current time is: {formatted_time}", end="\r")




####################################################################################################################
#Step 3 : Enter the values
try:
    hours = int(input("Enter current hour (0 - 23): "))
    minutes = int(input("Enter current minute (0 - 59): "))
    seconds = int(input("Enter current second (0 - 59): "))
    
    if not (0 <= hours < 24 and 0 <= minutes < 60 and 0 <= seconds < 60):
        raise ValueError("Time values out of range")

except ValueError :
    print(f"Error")
    exit()


#####################################################################################################################
#Step 4 : Choose the adequated format 
try:
    format_choice = input("Choose the adequate format (12h / 24h): ").strip().lower()
    if format_choice not in ['12h', '24h']:
        raise ValueError("Invalid format choice! Please choose '12h' or '24h'.")

except ValueError as e:
    print(f"Error: {e}")
    exit()
##########################################################################################################################
########################################################################################################################
#Step 5 : Set the alarm
try :
    print (f"Please, set the alarm")

    alarm_hour = int(input("Choose the alarm hour (0 - 23) : "))
    alarm_minute = int(input("Choose the alarm minute (0 - 23) : "))
    alarm_second = int(input("Choose the alarm second (0 - 23) : "))

    if not (0 <= alarm_hour < 24 and 0 <= alarm_minute < 60 and 0 <= alarm_second < 60):
            raise ValueError("Time values out of range")

except ValueError :
    print(f"Error")
    exit()

####################################################################################################################
#Step 6 : Call the different functions (the main loop)
print("To exit, press Ctrl + C")

try:
    while True:
        formatted_time = format_time(hours, minutes, seconds, format_choice)
        print_time(formatted_time)

        if alarm_setting(hours, minutes, seconds, alarm_hour, alarm_minute, alarm_second):
            ALARM = format_time(alarm_hour, alarm_minute, alarm_second, format_choice)
            print(f"\nIt's {ALARM}. It's wake-up time!")
            

        time.sleep(1) # This function introduces a 1 second delay (in this case) between each update.
        hours, minutes, seconds = up_date_time(hours, minutes, seconds) 
except KeyboardInterrupt:
    print("\nClock interrupted!")