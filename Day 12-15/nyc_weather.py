#!/usr/bin/python3
"""
More exercises on hash maps:

Using nyc_weather.csv, answer the following:
- What was the average temperature in first week of Jan
- What was the maximum temperature in first 10 days of Jan
- What was the temperature on Jan 9?
- What was the temperature on Jan 4?
"""

# get the avg and max temps
temps = []

with open("nyc_weather.csv", "r") as f:
    for line in f:
        # get the temperature
        temp = line.split(",")
        try:
            temps.append(int(temp[1]))
        except:
            print("Invalid temperature")

print("List of temperatures:",temps)

# get the average
avg = sum(temps[:7])/len(temps[:7])
print(f"Average temperature: {avg}")

# get the max
max_temp = max(temps[:10])
print(f"Max temp: {max_temp}")


# get the temperature on Jan 4 and 9
data = {}

with open("nyc_weather.csv", "r") as f:
    for line in f:
        record = line.split(",")
        day = record[0]
        try:
            temp = int(record[1])
            data[day] = temp
        except:
            print("Invalid temperature")

print("Weather data: ", data)

# get the temperature on Jan 4
print(f"Temperature on Jan 4: {data['Jan 4']}")

# get the temperature on Jan 9
print(f"Temperature on Jan 9: {data['Jan 9']}")
