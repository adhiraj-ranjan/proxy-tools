from requests import get

import sys, getopt

def main(argv):
   proxy = ''
   try:
      opts, args = getopt.getopt(argv,"p:",["proxy=",])
   except getopt.GetoptError:
      print('proxy_check.py -p <proxy>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('proxy_check.py -p <proxy>')
         sys.exit()
      elif opt in ("-p", "--proxy"):
         proxy = arg
         return proxy



def check(proxy):
    proxies = {'http':'http://' + proxy, 'https':'http://' + proxy}
    print(proxies)
    try:
        r = get('http://httpbin.org/ip', proxies=proxies, timeout=8)
        response = get('https://www.youtube.com/', proxies=proxies, timeout=8)
        print(r.text + " - working")
    except Exception as e:
        print(e)
        print(proxy + ' - not working')
    return proxy

if __name__ == "__main__":
   proxy = main(sys.argv[1:])
   check(proxy)