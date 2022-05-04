import requests
import tkinter as tk
import time 
import json


def city_cords(city: str) -> tuple:
    response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city},&appid=86cbb748f03b1437917ce4f9e2169e8f")

    lat = response.json()[0]["lat"]
    lon = response.json()[0]["lon"]

    return (lat, lon)


# def jprint(obj):
#     # create a formatted string of the Python JSON object
#     text = json.dumps(obj, sort_keys=True, indent=4)
#     print(text)



def get_weather(canvas):
    city = textfield.get()
    lat, lon = city_cords(city)
    api = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=imperial&appid=86cbb748f03b1437917ce4f9e2169e8f"
    json_data = requests.get(api).json()
    condition = json_data["weather"][0]["main"]
    temp = str(json_data["main"]["temp"]) + "ºF"
    temp_max = str(json_data["main"]["temp_max"]) + "ºF"
    temp_min = str(json_data["main"]["temp_min"]) + "ºF"
    humidity = str(json_data["main"]["humidity"]) + " %"
    pressure = str(json_data["main"]["pressure"]// 68.948) + " Psi"
    wind_speed = str(json_data["wind"]["speed"]) + " Mph"
    sunrise = str(time.strftime("%I:%M:%S", time.gmtime(json_data["sys"]["sunrise"]-14400))) + " EST"
    sunset = str(time.strftime("%I:%M:%S", time.gmtime(json_data["sys"]["sunset"]-14400))) + " EST"


    final_info = condition + "\n" + temp
    final_data = "\n" + "Max temp: " + temp_max + "\n" + "Min temp: " + temp_min + "\n" + "Pressure: " + pressure + "\n" + "Humidity: " + humidity + "\n" + "Wind speed: " + wind_speed + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset 
    label1.config(text = final_info)
    label2.config(text = final_data)


    
# lat, lon = city_cords("London")
# api = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=imperial&appid=86cbb748f03b1437917ce4f9e2169e8f"
# jprint(requests.get(api).json())


canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")


f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textfield = tk.Entry(canvas, font = t)
textfield.pack(pady = 20)
textfield.focus()
textfield.bind("<Return>", get_weather)

label1 = tk.Label(canvas, font = t)
label1.pack()
label2 = tk.Label(canvas, font = f)
label2.pack()


if __name__ == "__main__":
    canvas.mainloop()
