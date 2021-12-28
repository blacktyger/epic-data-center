"""
ViteScan.io Scrape, mostly used to get all EPIC-002 holders stats
"""

import json
import time

import requests

from settings import Database
from vitescan_io_scrape import ViteScanScrape

SCRAPES = [ViteScanScrape]
DATABASE = Database
INTERVAL = 2*60


def main():
    print(f"STARTING VITESCAN SCRAPE...")
    while True:
        for scrape in SCRAPES:
            try:
                scrape().holders_updater()

                holders = {
                    'summary': scrape().get_holders_summary(),
                    'stats': scrape().get_holders_stats()
                    }

                response = {
                    'btc_price': 0,
                    'usd_price': 0,
                    'holders_count': holders['summary']['total'],
                    'holders_stats': holders['stats']
                    }

                url = f"{DATABASE.API_URL}{DATABASE.API_GET_VITEX}"
                response = requests.post(url=url, data=json.dumps(response), headers={'Content-Type': 'application/json'})

                if response.status_code in [200, 201]:
                    print(f'DB RESPONSE [{response.status_code}] - Added new VitexUpdate')
                else:
                    print(response.text)

            except Exception as e:
                print(e)
                continue

        time.sleep(INTERVAL)


if __name__ == '__main__':
    main()