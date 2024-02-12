import requests, string, random, base64, json, websocket

import solve
xtrack = 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExMy4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTEzLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjk5OTksImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9'
s = requests.Session()

def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))

def user_name():
    verbs = ['awkward','thin','thick','happy','sad','tall','short','malious','ravenous','smooth','loving','mean','weird','high','sober',"smart",'dumb','rich','poor','mega','music','lord']
    nouns = ['hacker','lumberjack','horse','unicorn','guy','girl','man','woman','male','female','men','women','duck','dog','sheep','zombie','tennis','doctor']
    starts = ['Touches_','Loves_','Hates_','Licks_','Feels_']

    global_user_name = random.choice(starts) + random.choice(verbs) + '_' + random.choice(nouns) + 's'
    username = random.choice(verbs) + '_' + random.choice(nouns) + 's'


    replace_char = random.randint(1,10)
    if replace_char == 1:
        global_user_name = global_user_name.replace('i', '1')
        global_user_name = global_user_name.replace('a', '4')
        global_user_name = global_user_name.replace('e', '3')
        global_user_name = global_user_name.replace('l','|')
    elif replace_char == 2:
        global_user_name = global_user_name.replace('_', '-')
    elif replace_char == 3:
        global_user_name = global_user_name.replace('_', '7')
    elif replace_char == 4:
        global_user_name = global_user_name.replace('m','nn')
    else:
        global_user_name = global_user_name

    return global_user_name, username

try:
    buildNumber = int(requests.get("https://raw.githubusercontent.com/EffeDiscord/discord-api/main/fetch").json()['client_build_number']) # Get Discord build number
except Exception:
    buildNumber = 218604 

def super_pro() -> str: return base64.b64encode(json.dumps({"os":"Windows","browser":"Chrome","device":"","system_locale":"en-US","browser_user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.192 Safari/537.36","browser_version":"110.0.5481.192","os_version":"10","referrer":"","referring_domain":"","referrer_current":"","referring_domain_current":"","release_channel":"stable","client_build_number":buildNumber,"client_event_source":None}).encode()).decode()

def get_proxies() -> str:
    response = requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=yes&anonymity=anonymous")
    proxy_list = response.text.split('\n')

    return random.choice(proxy_list)

def online(token, proxy):
    try:
        proxytest = f"http://{proxy}"
        proxyweb = str(proxytest.split("http://")[1]).split("@")
        username, password, host, port = proxyweb[0].split(":")[0], proxyweb[0].split(":")[1], proxyweb[1].split(":")[0], proxyweb[1].split(":")[1]
        ws = websocket.WebSocket()
        ws.connect('wss://gateway.discord.gg/?v=9&encoding=json',http_proxy_host=host,http_proxy_port=str(port),proxy_type="http",http_proxy_auth=(username,password))        
        hello = json.loads(ws.recv())
        versionb = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36".split("Chrome/")[1].split(" ")[0]
        auth = {
                "op": 2,
                "d": {
                    "token": token,
                    "capabilities": 125,
                    "properties":{
                        "os":"Windows",
                        "browser":"Chrome",
                        "device":"",
                        "system_locale":"en-US",
                        "browser_user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
                        "browser_version":versionb,
                        "os_version":"10",
                        "referrer":"",
                        "referring_domain":"",
                        "referrer_current":"",
                        "referring_domain_current":"",
                        "release_channel":"stable",
                        "client_build_number":buildNumber,
                        "client_event_source":None
                    },
                    "presence": {
                        "status": "dnd",
                        "since": 0,
                
                        "activities": [
                            {
                                "name": "Visual Studio Code",
                                "type": 0,
                                "url": None
                            }
                        ],
                        "assets": {
                            "large_image": 'visualstudiocode',
                            "large_text": 'Visual Studio Code',
                            "small_image": 'visualstudiocode',
                            "small_text": 'Visual Studio Code'
                        },
                        "timestamps": {
                            "start": 0
                        },


                        "afk": False


                    },
                    "compress": False,
                    "client_state": {
                        "guild_hashes": {},
                        "highest_last_message_id": "0",
                        "read_state_version": 0,
                        "user_guild_settings_version": -1,
                        "user_settings_version": -1
                    }
                }
            }
        ws.send(json.dumps(auth))

    except:
        pass

def register(serverinv, captchakey):
    proxy = get_proxies()
    proxies = {
        "https://": f"https://{proxy}"
    }

    # global_username, username = user_name()
    global_username, username = random_char(10), random_char(10)
    # email = random_char(10) + "@" + random_char(10) + ".com"
    password = random_char(18)
    header1 = {
        "Host": "discord.com",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "sec-ch-ua": '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
        "sec-ch-ua-mobile": "?0",
        "Upgrade-Insecure-Requests": "1",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-us,en;q=0.9",
    }

    getcookie = s.get("https://discord.com/register", headers=header1, proxies=proxies).headers['set-cookie']
    sep = getcookie.split(";")
    sx = sep[0]
    sx2 = sx.split("=")
    dfc = sx2[1]
    split = sep[6]
    split2 = split.split(",")
    split3 = split2[1]
    split4 = split3.split("=")
    sdc = split4[1]
    header2 = {
        "Host": "discord.com",
        "Connection": "keep-alive",
        "sec-ch-ua": '"Chromium";v="92", " Not A;Brand";v="99", "Microsoft Edge";v="92"',
        "X-Super-Properties": super_pro(),
        "X-Context-Properties": "eyJsb2NhdGlvbiI6IlJlZ2lzdGVyIn0=",
        "Accept-Language": "en-US",
        "sec-ch-ua-mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
        "Authorization": "undefined",
        "Accept": "*/*",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://discord.com/register",
        "Accept-Encoding": "gzip, deflate, br"
    }

    fingerprintres = s.get("https://discord.com/api/v9/experiments", headers=header2, timeout=10, proxies=proxies)

    while True:
        if fingerprintres.text != "":
            fingerprint = fingerprintres.json()['fingerprint']
            break


    header3 = {
        "Host": "discord.com",
        "sec-ch-ua": '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
        "X-Super-Properties": super_pro(),
        "X-Fingerprint": fingerprint,
        "Accept-Language": "en-US",
        "sec-ch-ua-mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
        "Content-Type": "application/json",
        "Authorization": "undefined",
        "Accept": "*/*",
        "Origin": "https://discord.com",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://discord.com/register",
        "X-Debug-Options": "bugReporterEnabled",
        "Accept-Encoding": "gzip, deflate, br",
        "Cookie": f"__dcfduid={dfc}; __sdcfduid={sdc}",
        "X-Captcha-Key": captchakey,
        'X-Track': xtrack
    }
    s.get('https://discord.com/api/v9/auth/location-metadata', headers= {"Host": "discord.com","sec-ch-ua": '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',"X-Super-Properties": super_pro(), "X-Fingerprint": fingerprint, "Accept-Language": "en-US", "sec-ch-ua-mobile": "?0","User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36","Content-Type": "application/json", "Authorization": "undefined", "Accept": "*/*", "Origin": "https://discord.com", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://discord.com/register","X-Debug-Options": "bugReporterEnabled","Accept-Encoding": "gzip, deflate, br","Cookie": f"__dcfduid={dfc}; __sdcfduid={sdc}",})
    payload = {
        "fingerprint": fingerprint,
        "email": email,
        "username": username,
        "password": password,
        "invite": serverinv,
        "consent": "true",
        "date_of_birth": f'{random.randint(1990, 2000)}-{random.randint(1, 12)}-{random.randint(1, 28)}',
        "gift_code_sku_id": "",
        "global_name": global_username
    }

    registerreq = s.post("https://discord.com/api/v9/auth/register", proxies=proxies, headers=header3, json=payload, timeout=10)
    print("Account Registered")

    token = registerreq.json()['token']
    print("TOKEN IS >>>", token)

    with open("tokens.txt", "r") as f:
        c = f.read()
    with open("tokens.txt", "w") as f:
        f.write(f"{c}\n{email}|{password}|{token}")

    try:
        online(token, proxy)
    except:
        pass
        
    newheaders = {'authority': 'discord.com', 'accept': '*/*', 'accept-language': 'en-US,en;q=0.9', "Cookie": f"__dcfduid={dfc}; __sdcfduid={sdc}", 'authorization': token, 'origin': 'https://discord.com', 'referer': 'https://discord.com/@me', 'Content-Type': 'application/json', 'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36", 'x-debug-options': 'bugReporterEnabled', 'x-discord-locale': 'en-US', 'x-fingerprint': fingerprint, 'x-super-properties': super_pro()}
    while True:
        try:
            r = s.get("https://discord.com/api/v9/users/@me/affinities/users", headers=newheaders, proxy=f"http://{proxy}")
            break
        except:
            continue

async def main():
    invitecode = "haihu"
    solved = await solve.manage()
    if not solved == False:
        register(invitecode, solved)

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
