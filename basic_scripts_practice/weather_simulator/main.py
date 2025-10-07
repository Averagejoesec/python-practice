import random

print("""
Weather Simulator
=================
Select a city:
1. New York
2. Los Angles
3. Chicago
4. Miami
5. Seattle
""")

city_choice = int(input("Enter your choice (1-5): "))
if city_choice == 1:
    city = "New York"
elif city_choice == 2:
    city = "Lost Angeles"
elif city_choice == 3:
    city = "Chicago"
elif city_choice == 4:
    city = "Miami"
elif city_choice == 5:
    city = "Seattle"
else:
    print("Incorrect choice, choose a valid listed city.")


print("""
Select season:
1. Winter
2. Spring
3. Summer
4. Fall
""")


season_choice = int(input("Enter your choice (1-4): "))

if season_choice == 1:
    season = "Winter"
elif season_choice == 2:
    season = "Spring"
elif season_choice == 3:
    season = "Summer"
elif season_choice == 4:
    season = "Fall"
else:
    print("Choose a valid listed season.")

winter_conditions = ["Partly Cloudy", "Rain", "Snow", "Sunny"]
weather_library = {"New York":
                            [{"Winter":
                                {"Temperature": random.randrange(35), "Humidity": random.randrange(50,60),
                                "Wind Speed": random.randrange(40), "Conditions": random.choice(winter_conditions)},
                            "Spring": {},
                            "Summer": {},
                            "Fall": {},
                            }
                            ],
                    "Los Angeles":
                            [{"Winter":
                                {"Temperature": random.randrange(35), "Humidity": random.randrange(50,60),
                                "Wind Speed": random.randrange(40), "Conditions": random.choice(winter_conditions)},
                            "Spring": {},
                            "Summer": {},
                            "Fall": {},
                            }
                            ],
                            }

# Generates random weather conditions (temperature, humidity, wind speed, conditions)
print(f"""
Weather for {city} ({season})
=============================

Current Weather:
Temperature: {weather_library[city][0][season]['Temperature']}
Humidity: {weather_library[city][0][season]['Humidity']}
Wind Speed: {weather_library[city][0][season]['Wind Speed']}
Conditions: {weather_library[city][0][season]['Conditions']}
""")


# Simulates different seasons (winter, spring, summer, fall)

# Provides daily weather forecasts for multiple days

# Shows weather statistics and trends

# Allows users to view weather for different cities

# Displays weather warnings for extreme conditions