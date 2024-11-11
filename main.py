import tkinter as tk
from weather import get_weather

def fetch_weather():
    city = city_entry.get()
    weather_data = get_weather(city)
    
    if weather_data:
        result_label.config(text=
            f"Temperature: {weather_data['temperature']}°C\n"
            f"Feels like: {weather_data['feels_like']}°C\n"
            f"Description: {weather_data['description']}\n"
            f"City: {weather_data['city']}, {weather_data['country']}\n"
            f"Humidity: {weather_data['humidity']}%\n"
            f"Wind speed: {weather_data['wind_speed']}m/s\n"
        )
    else:
        result_label.config(text="City not found")
        
        
root = tk.Tk()
root.title("Weather App")
root.geometry("400x400")

city_label = tk.Label(root, text="Enter the city: ")
city_label.pack()
city_entry = tk.Entry(root)
city_entry.pack()

fetch_button = tk.Button(root, text="Fetch Weather", command=fetch_weather)
fetch_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
        
