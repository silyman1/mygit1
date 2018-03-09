import requests
cookie = 'fts=1513149122; sid=4ima6h0u; buvid3=A7A1FD72-255A-4E66-97D6-A55B779CAC418020infoc; UM_distinctid=1604ebbd00d10-0d3ee385d46124-5f6c3a73-c0000-1604ebbd00e45; pgv_pvi=3520077824; LIVE_BUVID=f38d125bca4739c7d9af5035578a97ad; LIVE_BUVID__ckMd5=b8f06c8e7bee409c; finger=470190d9'
referer = 'https://www.bilibili.com/'
url = 'https://api.bilibili.com/x/web-interface/ranking/region?callback=jQuery17203646444796228778_1520559979920&jsonp=jsonp&rid=24&day=7&original=0&_=1520560031413'
headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
		'referer': referer,
		'authority':'api.bilibili.com',
		'accept': '*/*',
		'cookie' :cookie
	}
response = requests.get(url,headers=headers)

print response.text