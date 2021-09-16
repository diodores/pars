from pprint import pprint
import requests
session = requests.Session()
data = {}

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0',
    'captcha':"SDGdfg"
}
url = 'hydraclubbioknikokex7njhwuahc2l67lfiz7z36md2jvopda7nchid.onion'

res = session.get(url, headers=headers)
pprint(res.text)

data['captcha']= input('Ввести капчу:')
r= session.post(url + '/gate', headers=headers, data=data)
pprint(r.next)
