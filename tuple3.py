import random
weather = input("Enter the weather (Sunny, Rainy, Cloudy, Random): ").lower()
weather = random.choice(["sunny", "rainy", "cloudy"]) if weather == "random" else weather

sunny = "sunny"
rainy = "rainy"
cloudy = "cloudy"

if weather == sunny:
    print("Its sunny. Wear a T-shirt and shorts. Good weather")
elif weather == rainy:
    print("Its rainy. Wear a raincoat and carry an umbrella. Bad weather")
elif weather == cloudy:
    print("Its cloudy. Wear a light jacket. Moderate weather")
else:
    print("Invalid input. Please enter Sunny, Rainy or Cloudy.")
