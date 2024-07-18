import streamlit as st
from os import system
import psutil
import datetime


name = 'Blesson'
system(f'say Welcome {name}. Your system information is as follows:')
st.write(f"{name}")
#Read the date and time
current_time = datetime.datetime.now()
battery = psutil.sensors_battery()

#Convert date and time to string and speak it
string = current_time.strftime("%A, %B %d, %Y %H:%M")
print(string)
system(f'say today is {string}')
st.write(f"Today is: {string}")
#Read the battery percentage and speak it
system(f'say Battery percentage is {battery.percent}%')
st.write(f"Battery Percentage remaining is: {battery.percent}%")

#Print battery information in the termainal
if battery:
    print(f"Battery Percentage Remaining: {battery.percent}%")
    print(f"Power plugged in: {'Yes' if battery.power_plugged else 'No'}")
    st.write("Power Adapter is plugged in and system is charging.")
else:
    print("No battery information available.")

#Speak the battery charging status
if battery.power_plugged:
    system(f'say Laptop is plugged in and charging.')
else:
    system(f'say Laptop is not plugged in. Please plug in the charger.')