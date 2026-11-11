
import requests
from bs4 import BeautifulSoup
import json

# Step 1: Website URL
url = "https://quotes.toscrape.com/"

try:
    # Step 2: Send HTTP request
    response = requests.get(url, timeout=10)

    # Check whether request was successful
    response.raise_for_status()

    # Step 3: Parse HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Step 4: Find all quote containers
    quotes = soup.find_all("div", class_="quote")

    # Step 5: Create an empty list
    data = []

    # Step 6: Extract quotes and authors
    for quote in quotes:

        text = quote.find(
            "span", class_="text"
        ).get_text(strip=True)

        author = quote.find(
            "small", class_="author"
        ).get_text(strip=True)

        data.append({
            "quote": text,
            "author": author
        })

    # Step 7: Save data into JSON file
    with open("quotes.json", "w", encoding="utf-8") as file:

        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False
        )

    # Step 8: Display success message
    print("Quotes successfully saved to quotes.json!")
    print("Total quotes extracted:", len(data))

except requests.exceptions.Timeout:
    print("Error: Website request timed out.")

except requests.exceptions.ConnectionError:
    print("Error: Unable to connect to the website.")

except requests.exceptions.HTTPError as e:
    print("HTTP Error:", e)

except requests.exceptions.RequestException as e:
    print("Request Error:", e)

except Exception as e:
    print("Unexpected Error:", e)
