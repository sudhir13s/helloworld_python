# Python program to find current
# weather details of any city
# using openweathermap api

# import required modules
import requests, json
import os


def hello_world(city_name):
    # Enter your API key here
    api_key = os.environ.get('SECRET_KEY')

    # base_url variable to store url
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    # complete_url variable to store
    # complete url address
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name

    # get method of requests module
    # return response object
    response = requests.get(complete_url)

    # json method of response object
    # convert json format data into
    # python format data
    x = response.json()

    # Now x contains list of nested dictionaries
    # Check the value of "cod" key is equal to
    # "404", means city is found otherwise,
    # city is not found
    msg = "City Not Found"
    print("status code: ", response.status_code)
    if response.status_code in [200, 201]:
        # store the value of "main"
        # key in variable y
        y = x["main"]

        # store the value corresponding
        # to the "temp" key of y
        current_temperature = y["temp"]

        # store the value corresponding
        # to the "pressure" key of y
        current_pressure = y["pressure"]

        # store the value corresponding
        # to the "humidity" key of y
        current_humidiy = y["humidity"]

        # store the value of "weather"
        # key in variable z
        z = x["weather"]

        # store the value corresponding
        # to the "description" key at
        # the 0th index of z
        weather_description = z[0]["description"]

        # print following values
        msg = "Temperature = " + str(current_temperature)
        print(msg)
        return msg

    else:
        print("City Not Found")
        return msg


if __name__ == '__main__':
    city_name = input("Enter city name : ")
    hello_world(city_name)
