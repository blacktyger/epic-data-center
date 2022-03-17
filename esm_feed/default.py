
keybase = {

    }

tor = {

    }

core_software = {
    'server': {
        'last_version': '2.17',
        'versions': ['2', '2.13', '2.15', '2.17'],
        'binary_url': {
            'windows': 'https://dl.epic.tech/epic_v2.17-win.zip',
            'linux': 'https://dl.epic.tech/epic_v2.17-ubuntu.zip',
            'macos': 'https://dl.epic.tech/epic_v2.17-mac.zip'
            }
        },
    'wallet_cli': {
        'last_version': '2.6.1',
        'versions': ['2', '2.6', '2.6.1'],
        'binary_url': {
            'windows': 'https://epic.tech/wp-content/downloads/epic-wallet-cli/epic-wallet-2.6.1.zip',
            'linux': 'https://d1ftoepmu0es39.cloudfront.net/epic-wallet_2.6.0-1_amd64.deb',
            'macos': ''
            }
        },
    'miner_randomx': {
        'last_version': '2.3.1-1',
        'versions': ['2', '2.3', '2.3.1-1'],
        'binary_url': {
            'windows': 'https://d1ftoepmu0es39.cloudfront.net/epic-miner_2.3.1-1.zip',
            'linux': 'https://d1ftoepmu0es39.cloudfront.net/epic-miner_2.3.1-1_amd64.deb',
            'macos': ''
            }
        },
    'miner_progpow': {
        'last_version': '2.3.1-1',
        'versions': ['2', '2.3', '2.3.1-1'],
        'binary_url': {
            'windows': 'https://d1ftoepmu0es39.cloudfront.net/epic-miner-opencl_2.3.1-1.zip',
            'linux': 'https://d1ftoepmu0es39.cloudfront.net/epic-miner-opencl_2.3.1-1_amd64.deb',
            'macos': ''
            }
        },
    'blockchain_data': {
        'snapshots': [
            {'name': 'tar.gz',
             'timestamp': '',
             'url': 'https://51pool.online/downloads/epic_chain_data.tar.gz'},
            {'name': 'zip',
             'timestamp': '',
             'url': 'https://www.dropbox.com/s/xont7xmp6en82v4/chain_data.zip'}
             ]
        },
    'dependencies': {
        'librandomx': {
            'version': '1.0.0-3',
            'binary_url': {
                'windows': '',
                'linux': 'https://d1ftoepmu0es39.cloudfront.net/librandomx_1.0.0-3_amd64.deb',
                'macos': ''
                }
            }
        }
    }