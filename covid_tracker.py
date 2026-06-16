import json
import requests
import csv
from bs4 import BeautifulSoup

def covid_stats(country):
    url = f"https://disease.sh/v3/covid-19/countries/{country}"

    response = requests.get(url)

    if response.status_code != 200:
        return

    data = response.json()

    print("\nCOVID Stats for", data["country"])
    print("Total Cases:", data["cases"])
    print("Today's Cases:", data["todayCases"])
    print("Deaths:", data["deaths"])
    print("Recovered:", data["recovered"])

    # Save to CSV
    with open("covid_stats.csv", "a", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            data["country"],
            data["cases"],
            data["todayCases"],
            data["deaths"],
            data["recovered"]
        ])

country = input("Enter country: ").lower()
covid_stats(country)