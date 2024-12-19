import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = "https://kakijun.com/kanji/kanken/10/"
# Send an HTTP GET request to the URL
response = requests.get(url)
response.raise_for_status()  # Check if the request was successful
# Parse the webpage content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')
# Find all the kanji elements
kanji_elements = soup.select("div.singlekanji a")
# Extract the href value and kanji for each element
kanji_data = {}
for element in kanji_elements:
    href = element['href']
    kanji = element.text.strip()
    # Extract the value between '/c/' and '.html'
    value = href.split("/")[2].split(".")[0]
    # Store the result
    kanji_data[value] = kanji
# Save the results to a text file
file_path = "Kanken_Kanji10.txt"  # Specify the desired file name and path
with open(file_path, "w", encoding="utf-8") as file:
    for value, kanji in kanji_data.items():
        file.write(f"{value} : {kanji}\n")

print(f"Kanji data saved to {file_path}")
