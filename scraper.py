try:

    import requests
    from bs4 import BeautifulSoup
    import random

except:
    print(" Library Not Found !")


class Random_Proxy(object):

    def __init__(self):
        self.__url = 'https://www.sslproxies.org/'
        self.__headers = {
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-US,en;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Referer': 'http://www.wikipedia.org/',
            'Connection': 'keep-alive',
            }
        self.random_ip = []
        self.random_port = []

    def random_proxy(self):

        r = requests.get(url=self.__url, headers=self.__headers)
        soup = BeautifulSoup(r.text, 'html.parser')

        for x in soup.findAll('td')[::8]:
            self.random_ip.append(x.get_text())

        for y in soup.findAll('td')[1::8]:
            self.random_port.append(y.get_text())

        z = list(zip(self.random_ip, self.random_port))

        number = random.randint(0, len(z)-50)
        ip_random = z[number]

        ip_random_string = "{}:{}".format(ip_random[0],ip_random[1])
        proxy = {'http':'http://' + ip_random_string, 'https':'http://' + ip_random_string}

        return proxy

    def Proxy_Request(self,request_type='get',urls='',**kwargs):
        while True:
            try:
                proxy = self.random_proxy()
                print("Checking Proxy {}".format(proxy['http'].replace('http://', '')))
                for url in urls:
                    r = requests.request(request_type,url,proxies=proxy,headers=self.__headers ,timeout=8, **kwargs)
                    if r.ok:
                        print("--> " + url + " " + str(r))
                        continue
                    else:
                        raise keyError
                print("\n")
                print(proxy['http'].replace('http://', '') + ' --working')
                break
            except:
                pass

if __name__=="__main__":
    s = Random_Proxy()
    s.Proxy_Request(urls=['http://httpbin.org/ip', 'https://www.instagram.com/'])