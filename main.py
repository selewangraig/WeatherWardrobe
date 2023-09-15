#get weather data using open weather api
import requests

def get_weather_data(api_key, city_name):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city_name}&APPID={api_key}&units=metric"
    response = requests.get(complete_url)
    data = response.json()
    return data

#function to take weather data as input and return outfit recommendations based on conditions
def get_outfit_recommendations(weather_data):
    temperature = weather_data["main"]["temp"]
    humidity = weather_data["main"]["humidity"]
    description = weather_data["weather"][0]["description"]

    if temperature > 25 and humidity < 70:
        return "It's hot and not too humid. Consider wearing a t-shirt and shorts."
    elif 10 <= temperature <= 20 and "rain" in description:
        return "It's cool and rainy. Don't forget your waterproof jacket and an umbrella!"
    else:
        return "Sorry, I don't have specific recommendations for this weather"
    
#simple CLI for the user to input their location and see outfit recommendations
def main():
    api_key = "9125490bab64b6e39a2f3b83bd916a76"
    city_name = input("Enter your city: ")

    weather_data = get_weather_data(api_key, city_name)

    if weather_data["cod"] == 200:
        outfit_recommendation = get_outfit_recommendations(weather_data)
        print(outfit_recommendation)
    else:
        print("Sorry, couldn't fetch weather data for that location.")

if __name__ == "__main__":
    main()