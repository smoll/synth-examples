import requests

headers = {
    'pragma': 'no-cache',
    'accept-encoding': 'gzip, deflate, sdch, br',
    'x-csrf-token': '76aa0ba9221e321e699c2cb3e16094188dd70dcb',
    'x-requested-with': 'XMLHttpRequest',
    'accept-language': 'en-US,en;q=0.8',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    'accept': '*/*',
    'cache-control': 'no-cache',
    'authority': 'www.maxmind.com',
    'referer': 'https://www.maxmind.com/en/locate-my-ip-address',
}

# Converted from 'Copy as curl' output
resp = requests.get('https://www.maxmind.com/geoip/v2.1/city/me?', headers=headers)

assert 'traits' in resp.json()
isp = resp.json()['traits']['isp']
ip = resp.json()['traits']['ip_address']

# Print a few values in JSON response
print('isp={}'.format(isp))
print('ip={}'.format(ip))
