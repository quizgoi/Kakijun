import requests
import os
# Function to download and save a file
def download_file(url, save_name):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise an error for bad status codes
        with open(save_name, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"Downloaded: {save_name}")
    except requests.RequestException as e:
        print(f"Failed to download {url}: {e}")

# Main function to process the text file and download files
def main(input_file):
    # Get the directory of the script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:
            # Skip empty or malformed lines
            if ':' not in line:
                continue

            # Extract the download link value and kanji
            left, right = line.split(':', 1)
            download_link_value = left.strip()
            kanji = right.strip()

            # Construct the URL and save file name
            url = f"https://kakijun.com/kanjiphoto/worksheet/2/kanji-kakijun-worksheet-2-{download_link_value}.png"
            save_name = os.path.join(script_dir, f"{kanji}.png")

            # Download the file
            download_file(url, save_name)

if __name__ == "__main__":
    # Specify the input file name
    input_file = "Kanji_link_Kakijun.txt"  # Replace with your file name
    main(input_file)