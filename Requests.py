import requests

URL = "https://datsedenspace.datsteam.dev"

UNIVERSE = URL + "/player/universe"
TRAVEL = URL + "/player/travel"
COLLECT = URL + "/player/collect"
RESET = URL + "/player/reset"
ROUNDS = URL + "/player/rounds"

AUTH = "660bceb945edd660bceb945ee1"

def Logger(text:str):
    with open("logging.txt", "a", encoding="utf8") as f:
        f.write(text)


def Get(url:str):
    header = {"X-Auth-Token": AUTH }
    response = requests.get(url=url, headers=header)

    Logger(url + "\n")
    Logger(response.text)
    Logger("\n\n\n")

    return response.json()


def Travel(planets:list):
    header = {"X-Auth-Token": AUTH }

    response = requests.post(TRAVEL, headers=header, json={ "planets" : planets })

    Logger(TRAVEL + "\n")
    Logger(response.text)
    Logger("\n\n\n")

    return response.json()

# may not work, didn't test
def Collect(garbage:dict):
    header = {"X-Auth-Token": AUTH }

    response = requests.post(COLLECT, headers=header, json=garbage)

    Logger(COLLECT + "\n")
    Logger(response.text)
    Logger("\n\n\n")

    return response.json()

def Reset():
    header = {"X-Auth-Token": AUTH }

    response = requests.delete(RESET, headers=header)

    Logger(RESET + "\n")
    Logger(response.text)
    Logger("\n\n\n")

    return response.json()
