import requests
#city = input("Enter the city you are from: ")
#gender = input("Please enter your gender: ").lower()[0]
response = requests.get("http://api.weatherstack.com/forecast?access_key=909ed8fe5608fd96dc5c6602fcff3224&query=mecca")#.format(city))
allresponse = response.json()
forecast = allresponse["forecast"]['2020-10-20']
current = allresponse["current"]

# HOT to COLD
clothes_dict = {"0": ["Swimsuit"],
                "1": ["Dress", "Flip-flops", "Cap"],
                "2": ["Hat"],
                "3": ["Skirt", "Shorts", "High heels", "Sunglasses"],
                "4": ["T-shirt"],
                "5": ["Shirt", "Jeans", "Tracksuit"],
                "6": ["Sweater", "Leather jackets"],
                "7": ["Hoodies", "Jacket", "Polo shirt"],
                "8": ["Long coat", "Boots"],
                "9": ["Shoes", "Coat", "Socks", "Scarf", "Gloves"]}

max_index = 9
min_index = 0

points = 0

# greater the multiplier the more significant

if forecast["avgtemp"] > 0:
    if forecast["avgtemp"] > 20 and current["humidity"] > 60: # high temp and high humidity isnt good
        points += forecast["avgtemp"] * 4
    else:
        points -= forecast["avgtemp"] * 4
else:
    points -= forecast["avgtemp"] * 4
points -= forecast["uv_index"] * 2
points += current["wind_speed"]
points += current["precip"] * 5
points += forecast["totalsnow"] * 10
points += current["cloudcover"] // 2
if current["is_day"] == "yes":
    points -= 10
else:
    points += 10

print(points)
index = 0
for i in str(points):
    index += str(i)
print(index)
        
