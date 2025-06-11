from ai import *

# This script fetches the win-loss record of the Seattle Seahawks for the last 5 seasons
import requests
from bs4 import BeautifulSoup

team_abbr = "sea"
years = [2023, 2022, 2021, 2020, 2019]
history = []
seahawks_records = []

for year in years:
    url = f"https://www.pro-football-reference.com/teams/{team_abbr}/{year}.htm"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    record_tag = soup.find("strong", text="Record:")
    if record_tag:
        record = record_tag.next_sibling.strip().split(",")[0]  # Just "9-8-0"
        seahawks_records.append((year, record))
    else:
        seahawks_records.append((year, "Record not found"))

history.append(seahawks_records)
prompt = """
You are an expert NFL analyst and data-driven AI.

Below is the Seattle Seahawks' win-loss record for the past 5 seasons.
Use this data to analyze recent performance trends, and predict how the team is likely to perform in the upcoming season. 
Focus on patterns such as consistency, improvement or decline over the years.

Return a brief analysis followed by a predicted win-loss record for the next season.
"""

##ai part
response = promptLLM(prompt, history)
print(response)