from os import system
import psutil
import datetime

system('say Welcome Blesson!')

current_time = datetime.datetime.now()
battery = psutil.sensors_battery()

if battery:
    print(f"Battery Percentage Remaining: {battery.percent}%")
    print(f"Power plugged in: {'Yes' if battery.power_plugged else 'No'}")
else:
    print("No battery information available.")

string = current_time.strftime("%A, %B %d, %Y %H:%M")
print(string)
system(f'say Todays date and time is {string}')
system(f'say Battery percentage is {battery.percent}%')

if battery.power_plugged:
    system(f'say Laptop is plugged in and charging.')
else:
    system(f'say Laptop is not plugged in. Please plug in the charger.')