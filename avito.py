import requests

def get_session(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0)   Gecko/20100101 Firefox/69.0',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language':'ru,en-US;q=0.5',
        'Accept-Encoding':'gzip, deflate, br',
        'DNT':'1',
        'Connection':'keep-alive',
        'Upgrade-Insecure-Requests':'1',
        'Pragma':'no-cache',
        'Cache-Control':'no-cache',
        'cookie': 'u=2ke27a18.cwvccb.larrql2rql00; v=1605384124; buyer_laas_location=637640; buyer_location_id=637640; luri=moskva; buyer_selected_search_radius4=0_general; sessid=843c308c7ecc2fc458a591ee394233a5.1605384125; __cfduid=d46312dccdada4db0792865983306342f1605384125; abp=2; showedStoryIds=48-47-46-45-43-41-42-39-32-30-25; lastViewingTime=1605384124030; no-ssr=1; _ym_uid=1605384124717309615; _ym_d=1605384124; _ym_visorc_34241905=b; _ym_isad=1; _ga=GA1.2.1050134589.1605384124; _gid=GA1.2.1663257147.1605384124; _ym_visorc_419506=w; __gads=ID=1f2e444728effe47:T=1605384126:S=ALNI_MZiTJ7Hj-6Yd83kZX9-wNz7QQEYGw; isCriteoSetNew=true; f=5.f229b7465e2ca598c1c3cf21d33666d747e1eada7172e06c47e1eada7172e06c47e1eada7172e06c47e1eada7172e06cb59320d6eb6303c1b59320d6eb6303c1b59320d6eb6303c147e1eada7172e06c8a38e2c5b3e08b898a38e2c5b3e08b890df103df0c26013a0df103df0c26013a2ebf3cb6fd35a0ac0df103df0c26013a8b1472fe2f9ba6b9e2bfa4611aac769efa4d7ea84258c63d59c9621b2c0fa58f915ac1de0d034112ad09145d3e31a56946b8ae4e81acb9fae2415097439d40473de19da9ed218fe287829363e2d856a2e992ad2cc54b8aa8d99271d186dc1cd03de19da9ed218fe2d50b96489ab264ed3de19da9ed218fe23de19da9ed218fe246b8ae4e81acb9fa51b1fde863bf5c12f8ee35c29834d631c9ba923b7b327da78fe44b90230da2aceb6fa41872a5ca4e2985db2d99140e2d9149e7c08f48f76ae1b31d40e35adfda38f0f5e6e0d2832eb907e62b194c67812ab6859d9dfa137b46b8ae4e81acb9fa46b8ae4e81acb9fa02c68186b443a7ac9317cdb1f8e40fc8bc7e7f380aa6ad772da10fb74cac1eab2da10fb74cac1eabf67834b86360393cfa48ea3860c445aa3778cee096b7b985bf37df0d1894b088; _ym_visorc_189903=w; sx=H4sIAAAAAAACAwXBMQ6AIAwAwL90diiIUvhOJU1sQodGOxD%2F7t2C%2FHCiHWe%2BtCCpoDtLWDj0BS90aHHbyHXKMFInVRFGliIRZOSwwYCeTjxKTbXR9%2F3eaG1aVAAAAA%3D%3D; dfp_group=4; _dc_gtm_UA-2546784-1=1',
        'set_cookie': 'v=1605384124; path=/; expires=Sat, 14-Nov-20 20:53:20 GMT; HttpOnly; Max-Age=1800; secure; domain=.avito.ru; SameSite=Lax',
        'cookies': "XgGnzBjNiR8ydwkODiKtF4CYSDXhLgvFSpFiOmuJlrOmMJ_IIweGC4bbCgbkL70__6Fyylf81Zbs5U5eLgkldez3bz1Fwz_w8NbpYnozjObsTtel2dhXv1n0u56xtTvdWf7GDs6PtqkRlpE2zngXqFhESTwMSECVpB94xV_yhr7h-UDOZfvcdw==",
        'cookies_sign': "cIayr9LbgCsvm5zIdgei-A=="
    }
    session = requests.get(url, headers=headers)
    return session

avito = get_session("https://www.avito.ru/moskva")
print(avito)
