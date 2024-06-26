from os import system
import psutil
import datetime

system('say Welcome User. Your system information is as follows:')

#Read the date and time
current_time = datetime.datetime.now()
battery = psutil.sensors_battery()

#Convert date and time to string and speak it
string = current_time.strftime("%A, %B %d, %Y %H:%M")
print(string)
system(f'say today is {string}')

#Read the battery percentage and speak it
system(f'say Battery percentage is {battery.percent}%')

#Print battery information in the termainal
if battery:
    print(f"Battery Percentage Remaining: {battery.percent}%")
    print(f"Power plugged in: {'Yes' if battery.power_plugged else 'No'}")
else:
    print("No battery information available.")

#Speak the battery charging status
if battery.power_plugged:
    system(f'say Laptop is plugged in and charging.')
else:
    system(f'say Laptop is not plugged in. Please plug in the charger.')