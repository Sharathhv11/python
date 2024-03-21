import requests as req


# this is sample live weather app made using python requests

def weather(city):
    """ this module returns the weather of the given city"""

    try:

        # api key for making api call
        api_key = '30d4741c779ba94c470ca1f63045390a'

        params = {
            "q": city,
            "units": "imperial",
            "APPID": api_key

        }

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
        }

        response = req.get(f"https://api.openweathermap.org/data/2.5/weather", params=params, headers=headers)

        if (response.status_code == req.codes.not_found):
            return f"The city {city} is not exists please enter the valid city name "
        else:
            res_json = response.json()
            return_dict = {"City": city,
                           "weather": res_json["weather"][0]["description"],
                           "Temprature": "{} °c".format(int(((res_json["main"]["temp"] - 32) * 5 / 9))),
                           "Humidity": "{}%".format(res_json["main"]["humidity"]),
                           "Wind Speed ": "{} km/h".format(res_json["wind"]["speed"])
                           }
            return return_dict

    except Exception as e:
        return "please connect to internet"


if (__name__== "__main__"):
    city = input("Enter the city : ").capitalize().strip()
    w_res = weather(city)
    if (type(w_res) != str):
        for x, y in w_res.items():
            print("{:<12} : {} ".format(x, y))
    else:
        print(w_res)