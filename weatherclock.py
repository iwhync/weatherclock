from tkinter import *
from datetime import datetime
import requests
import json

# OpenWeatherMap API key and location information
api_key = "your_key_here"  # replace with your actual API key
lat = "your_lat_here"  # replace with your actual latitude
lon = "-your_lon_here"  # replace with your actual longitude

# Call the OpenWeatherMap API to get the current weather data
url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
response = requests.get(url)
data = json.loads(response.text)

# Extract the relevant weather data
location = data["name"] + ", " + data["sys"]["country"]
temp = data["main"]["temp"]
humidity = data["main"]["humidity"]
pressure = data["main"]["pressure"]
windspeed = data["wind"]["speed"]
weather = data["weather"][0]["main"]

def update_time():
    # Get the current time and update the label
    time_now = datetime.now().strftime("%H:%M:%S.%f")[:-3] # remove the last 3 digits (microseconds)
    lbl1.configure(text=time_now)

    # Get the current date and update the label
    date_now = datetime.now().strftime("%A, %B %d, %Y")
    lbl2.configure(text=date_now)

    # Update the location and weather information on the label
    lbl3.configure(text=f"{location} \nTemperature: {temp} °C \nHumidity: {humidity}% \nPressure: {pressure} hPa \nWind Speed: {windspeed} m/s \nWeather: {weather}")
        
    # Schedule the function to be called again in 10 milliseconds
    root.after(10, update_time)

root = Tk()
root.title("Clock And Weather") # title bar
root.configure(background="white") # background
root.geometry("300x300") # size

lbl1 = Label(root, text="", font=("Arial Bold", 30)) # where time will appear
lbl1.configure(background="White") # Making the text colour fit
lbl1.place(relx=.5, rely=.2, anchor="center") # in the middle

lbl2 = Label(root, text="", font=("Arial", 16)) # where date will appear
lbl2.configure(background="White") # Making the text colour fit
lbl2.place(relx=.5, rely=.3, anchor="center") # below the time label

lbl3 = Label(root, text="", font=("Arial", 14)) # where location and weather will appear
lbl3.configure(background="White") # Making the text colour fit
lbl3.place(relx=.5, rely=.6, anchor="center") # below the date label



# Call the update_time function to start updating the label
update_time()

root.mainloop()
