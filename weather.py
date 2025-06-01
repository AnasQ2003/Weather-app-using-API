import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from datetime import datetime
from geopy.geocoders import Nominatim
from io import BytesIO
import folium
import webbrowser

API_KEY = "679775c156dd419ec68e970a7fbfb006"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    if not city:
        weather_label.config(text="⚠ Please enter the city name!", fg="red", bg=root.cget("bg"))
        return

    try:
        response = requests.get(BASE_URL, params={"q": city, "appid": API_KEY, "units": "metric"})
        data = response.json()

        if data["cod"] != 200:
            weather_label.config(text="❌ City not found!", fg="red", bg=root.cget("bg"))
            return

        temp_c = data["main"]["temp"]
        temp_f = (temp_c * 9 / 5) + 32
        weather_desc = data["weather"][0]["description"].capitalize()
        wind_speed = data["wind"]["speed"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        time = datetime.now().strftime("%I:%M %p")

        weather_label.config(
            text=f"\U0001F321 Temperature: {temp_c:.2f}°C / {temp_f:.2f}°F\n"
                 f"\u2601 Weather: {weather_desc}\n"
                 f"\U0001F4A8 Wind: {wind_speed} m/s\n"
                 f"\U0001F4A7 Humidity: {humidity}%\n"
                 f"⚙ Pressure: {pressure} hPa\n"
                 f"⏰ Time: {time}",
            fg="black",
            bg=root.cget("bg")
        )

        update_background(weather_desc.lower())
        update_map(city)

    except Exception as e:
        weather_label.config(text=f"⚠ Something went wrong!\n{e}", fg="red", bg=root.cget("bg"))

def detect_location():
    try:
        geolocator = Nominatim(user_agent="geoapi")
        location = requests.get("https://ipinfo.io/json").json()
        city = location.get("city", "Unknown")

        if city:
            entry.delete(0, tk.END)
            entry.insert(0, city)
            get_weather(city)
        else:
            weather_label.config(text="❌ Could not detect location.", fg="red", bg=root.cget("bg"))
    except Exception as e:
        weather_label.config(text=f"⚠ Location detection failed: {e}", fg="red", bg=root.cget("bg"))

def update_background(weather_condition):
    if "clear" in weather_condition:
        bg_image = "clearsky.jpg"
    elif "cloud" in weather_condition:
        bg_image = "cloudy.jpeg"
    elif "rain" in weather_condition or "drizzle" in weather_condition:
        bg_image = "rainy.jpeg"
    elif "haze" in weather_condition or "fog" in weather_condition:
        bg_image = "haze.jpeg"
    else:
        bg_image = "background.jpeg"

    image = Image.open(bg_image)
    image = image.resize((400, 500), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(image)
    background_label.config(image=bg_photo)
    background_label.image = bg_photo

def update_map(city):
    try:
        geolocator = Nominatim(user_agent="geoapi")
        location = geolocator.geocode(city)
        if location:
            lat, lon = location.latitude, location.longitude
            map = folium.Map(location=[lat, lon], zoom_start=10)
            folium.Marker([lat, lon], popup=city).add_to(map)
            map.save("city_map.html")
            webbrowser.open("city_map.html")
    except Exception as e:
        weather_label.config(text=f"⚠ Failed to load map: {e}", fg="red", bg=root.cget("bg"))

root = tk.Tk()
root.title("Weather App")
root.geometry("400x600")
root.configure(bg="white")

default_bg = Image.open("background.jpeg")
default_bg = default_bg.resize((400, 500), Image.LANCZOS)
bg_photo = ImageTk.PhotoImage(default_bg)

background_label = tk.Label(root, image=bg_photo)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg="", bd=3, highlightthickness=0)
frame.pack(pady=10)

entry = tk.Entry(frame, font=("Arial", 14), bd=2, relief="solid", width=20)
entry.pack(pady=10)

button = tk.Button(frame, text="Get Weather", font=("Arial", 12, "bold"), bg="#3498db", fg="white",
                   relief="flat", bd=2, padx=10, pady=5, activebackground="#2980b9",
                   command=lambda: get_weather(entry.get()))
button.pack(pady=5)

detect_button = tk.Button(frame, text="Auto Detect Location", font=("Arial", 12, "bold"), bg="#2ecc71", fg="white",
                          relief="flat", bd=2, padx=10, pady=5, activebackground="#27ae60",
                          command=detect_location)
detect_button.pack(pady=5)

weather_label = tk.Label(frame, font=("Arial", 12), fg="black", justify="left", bg=root.cget("bg"))
weather_label.pack(pady=20)

root.mainloop()
