import requests

print('[ - ] collecting proxies...')
r = requests.get('https://proxylist.geonode.com/api/proxy-list?limit=50&page=1&sort_by=lastChecked&sort_type=desc&country=IN')

proxylist = []

for proxies in r.json()['data']:
    proxy = str(proxies['ip'] + ':' + proxies['port'])
    proxylist.append(proxy)

headers = {
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-US,en;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Referer': 'http://www.wikipedia.org/',
            'Connection': 'keep-alive',
            }

epoint = input("Enter endpoint : ")
for proxy in proxylist:
    print('checking - ' + proxy)
    proxy_ = {'http': f'http://{proxy}', 'https': f'http://{proxy}'}
    try:
        response = requests.get(epoint, headers=headers, proxies=proxy_, timeout=4)
    except:
        continue
    if response.ok:
        print(proxy + ' - working')
        input('continue ? ')