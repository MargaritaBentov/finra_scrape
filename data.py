from os import path
import pandas as pd
import requests
import time
import random
from tenacity import retry, stop_after_attempt, wait_exponential
# from requests.exceptions import HTTPError

# Constants
BACKUP_INTERVAL = 100  # Backup after every 100 links
SLEEP_MIN = 0.05  # Minimum sleep time in seconds (100 milliseconds)
SLEEP_MAX = .5  # Maximum sleep time in seconds (1000 milliseconds)
SYMBOL = 'EIS'  # Symbol to filter
BACKUP_FILE = 'backup.csv'  # Backup file name

# Initialize DataFrame
columns = ['Date', 'Symbol', 'ShortVolume', 'ShortExemptVolume', 'TotalVolume', 'Market', 'Link']
if path.exists(BACKUP_FILE):
    df = pd.read_csv(BACKUP_FILE)
else:
    df = pd.DataFrame(columns=columns)


@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, max=10))
def process_link(link):
    response = requests.get(link)
    response.raise_for_status()  # Raise an exception for HTTP errors
    data = response.text.splitlines()
    for row in data[1:]:  # Skip header
        parts = row.split('|')
        if parts and len(parts) > 1 and parts[1] == SYMBOL:
            parts.append(link)
            df.loc[len(df)] = parts


def backup_data():
    df.to_csv(BACKUP_FILE, index=False)


def main():
    with open('links.txt', 'r') as file:
        links = [line.strip() for line in file]

    print(f'processing {len(links)} links...')
    for i, link in enumerate(links):
        if link in df['Link']:
            continue
        process_link(link)
        if not ((i + 1) % BACKUP_INTERVAL):
            backup_data()
            print(f'back up made on {i+1} link out of {len(links)}, df.shape: {df.shape}')
        time.sleep(random.uniform(SLEEP_MIN, SLEEP_MAX))  # Random sleep

    # Final backup
    backup_data()
    print("Processing complete.")


if __name__ == "__main__":
    main()
