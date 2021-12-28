import requests
import json

import pandas as pd

BASE_URL = "https://vitescan.io/"

class ViteScanHoldersScrape:
    HOLDERS_URL = "vs-api/token?tokenId=tti_f370fadb275bc2a1a839c753&tabFlag=holders"

    def holders_updater(self):
        url = f"{BASE_URL}{self.HOLDERS_URL}"
        data = requests.get(url)

        if data.status_code == 200:
            holders = json.loads(data.content)['data']['accountsResults']
            with open('holders.json', 'w') as f:
                f.write(json.dumps(holders))

    @staticmethod
    def get_holders_stats():
        with open('holders.json', 'r') as f:
            data = json.load(f)

        df = pd.DataFrame(data)
        balance_mean = df['totalBalance'].mean() / 10 ** 8
        dex_mean = df['dexAvailableBalance'].mean() / 10 ** 8
        dex_locked_mean = df['dexLockedBalance'].mean() / 10 ** 8

        response = {
            'balance_mean': balance_mean,
            'dex_mean': dex_mean,
            'dex_locked_mean': dex_locked_mean
            }

        return response

    def get_holders_summary(self, page=1):
        url = f"{BASE_URL}{self.HOLDERS_URL}&pageNo={page}"
        data = requests.get(url)

        if data.status_code == 200:
            data = json.loads(data.content)['data']
            response = {
                'total': data['total'],
                'top_10': [{
                    'rank': acc['rank'],
                    'address': acc['address'],
                    'balance': acc['totalBalance'],
                    'txs_count': acc['txnCount'],
                    'percentage': acc['percentage'],
                    } for acc in data['accountsResults'][:10]],
                'page_count': data['pageCount']
                }
            return response

        else:
            print(data)
