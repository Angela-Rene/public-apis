# a3df82eb4be065f64b3f087259d501a7 weatherstack API access key

import pandas as pd
import requests

API_KEY = "a3df82eb4be065f64b3f087259d501a7"  
BASE_URL = "http://api.weatherstack.com/current"

#params = {"access_key": API_KEY, "query": city}


def current_weather(city):
    params = {"access_key": API_KEY, "query": city}
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        print("Success! Data retrieved.")
        weather_data = response.json()
        #weather_df = pd.DataFrame(weather_data)
        
        location = weather_data["location"] ["name"]
        temp = weather_data["current"]["temperature"]
        temp_fahr = (temp * 9/5) + 32
        feel_like = weather_data["current"]["feelslike"]
        feel_like_fahr = (feel_like * 9/5) + 32
        condition = weather_data["current"]["weather_descriptions"]
        time = weather_data["location"]["localtime"]
        
        return f"The weather in {location} is {temp_fahr} degrees fahrenheit(feels like {feel_like_fahr}). \nIt is {condition}, at {time}. "
        # return weather_data
        
    else:
        print(f"Failed to retrieve data. Error code: {response.status_code}")
      
city_name = input("Enter a city for weather details: ")
print(current_weather(city_name))



# city = "New York"
# params = {"access_key": API_KEY, "query": city}
# response = requests.get(BASE_URL, params= params)
# print(response.json())







    