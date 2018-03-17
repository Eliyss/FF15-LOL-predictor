import requests

def getChampId(champ, apiKey):
    payload = {
        "api_key":apiKey,
        "locale":"en_US",
        "dataById":"false"
    }
    r = requests.get("https://na1.api.riotgames.com/lol/static-data/v3/champions", params = payload)
    print(r)    
    page = r.json()

    if champ in page["data"]:
        return page["data"][champ]["id"]

def getChampName(id, apiKey):
    payload = {
        "api_key":apiKey,
        "locale":"en_US",
        "dataById":"true"
    }
    r = requests.get("https://na1.api.riotgames.com/lol/static-data/v3/champions", params = payload)
    page = r.json()
    if id in page["data"]:
        return page["data"][champ]["name"]

def convertChamptoId(champ):
    champListbyKey = {
        "wukong": {
            "title": "the monkey king",
            "id": 62,
            "key": "wukong",
            "name": "wukong"
        },
        "jax": {
            "title": "grandmaster at arms",
            "id": 24,
            "key": "jax",
            "name": "jax"
        },
        "fiddlesticks": {
            "title": "the harbinger of doom",
            "id": 9,
            "key": "fiddlesticks",
            "name": "fiddlesticks"
        },
        "shaco": {
            "title": "the demon jester",
            "id": 35,
            "key": "shaco",
            "name": "shaco"
        },
        "warwick": {
            "title": "the uncaged wrath of zaun",
            "id": 19,
            "key": "warwick",
            "name": "warwick"
        },
        "xayah": {
            "title": "the rebel",
            "id": 498,
            "key": "xayah",
            "name": "xayah"
        },
        "nidalee": {
            "title": "the bestial huntress",
            "id": 76,
            "key": "nidalee",
            "name": "nidalee"
        },
        "zyra": {
            "title": "rise of the thorns",
            "id": 143,
            "key": "zyra",
            "name": "zyra"
        },
        "kled": {
            "title": "the cantankerous cavalier",
            "id": 240,
            "key": "kled",
            "name": "kled"
        },
        "brand": {
            "title": "the burning vengeance",
            "id": 63,
            "key": "brand",
            "name": "brand"
        },
        "rammus": {
            "title": "the armordillo",
            "id": 33,
            "key": "rammus",
            "name": "rammus"
        },
        "illaoi": {
            "title": "the kraken priestess",
            "id": 420,
            "key": "illaoi",
            "name": "illaoi"
        },
        "corki": {
            "title": "the daring bombardier",
            "id": 42,
            "key": "corki",
            "name": "corki"
        },
        "braum": {
            "title": "the heart of the freljord",
            "id": 201,
            "key": "braum",
            "name": "braum"
        },
        "darius": {
            "title": "the hand of noxus",
            "id": 122,
            "key": "darius",
            "name": "darius"
        },
        "tryndamere": {
            "title": "the barbarian king",
            "id": 23,
            "key": "tryndamere",
            "name": "tryndamere"
        },
        "missfortune": {
            "title": "the bounty hunter",
            "id": 21,
            "key": "missfortune",
            "name": "miss fortune"
        },
        "yorick": {
            "title": "shepherd of souls",
            "id": 83,
            "key": "yorick",
            "name": "yorick"
        },
        "xerath": {
            "title": "the magus ascendant",
            "id": 101,
            "key": "xerath",
            "name": "xerath"
        },
        "sivir": {
            "title": "the battle mistress",
            "id": 15,
            "key": "sivir",
            "name": "sivir"
        },
        "riven": {
            "title": "the exile",
            "id": 92,
            "key": "riven",
            "name": "riven"
        },
        "orianna": {
            "title": "the lady of clockwork",
            "id": 61,
            "key": "orianna",
            "name": "orianna"
        },
        "gangplank": {
            "title": "the saltwater scourge",
            "id": 41,
            "key": "gangplank",
            "name": "gangplank"
        },
        "malphite": {
            "title": "shard of the monolith",
            "id": 54,
            "key": "malphite",
            "name": "malphite"
        },
        "poppy": {
            "title": "keeper of the hammer",
            "id": 78,
            "key": "poppy",
            "name": "poppy"
        },
        "lissandra": {
            "title": "the ice witch",
            "id": 127,
            "key": "lissandra",
            "name": "lissandra"
        },
        "jayce": {
            "title": "the defender of tomorrow",
            "id": 126,
            "key": "jayce",
            "name": "jayce"
        },
        "nunu": {
            "title": "the yeti rider",
            "id": 20,
            "key": "nunu",
            "name": "nunu"
        },
        "trundle": {
            "title": "the troll king",
            "id": 48,
            "key": "trundle",
            "name": "trundle"
        },
        "karthus": {
            "title": "the deathsinger",
            "id": 30,
            "key": "karthus",
            "name": "karthus"
        },
        "graves": {
            "title": "the outlaw",
            "id": 104,
            "key": "graves",
            "name": "graves"
        },
        "zoe": {
            "title": "the aspect of twilight",
            "id": 142,
            "key": "zoe",
            "name": "zoe"
        },
        "gnar": {
            "title": "the missing link",
            "id": 150,
            "key": "gnar",
            "name": "gnar"
        },
        "lux": {
            "title": "the lady of luminosity",
            "id": 99,
            "key": "lux",
            "name": "lux"
        },
        "shyvana": {
            "title": "the half-dragon",
            "id": 102,
            "key": "shyvana",
            "name": "shyvana"
        },
        "renekton": {
            "title": "the butcher of the sands",
            "id": 58,
            "key": "renekton",
            "name": "renekton"
        },
        "fiora": {
            "title": "the grand duelist",
            "id": 114,
            "key": "fiora",
            "name": "fiora"
        },
        "jinx": {
            "title": "the loose cannon",
            "id": 222,
            "key": "jinx",
            "name": "jinx"
        },
        "kalista": {
            "title": "the spear of vengeance",
            "id": 429,
            "key": "kalista",
            "name": "kalista"
        },
        "fizz": {
            "title": "the tidal trickster",
            "id": 105,
            "key": "fizz",
            "name": "fizz"
        },
        "kassadin": {
            "title": "the void walker",
            "id": 38,
            "key": "kassadin",
            "name": "kassadin"
        },
        "sona": {
            "title": "maven of the strings",
            "id": 37,
            "key": "sona",
            "name": "sona"
        },
        "irelia": {
            "title": "the will of the blades",
            "id": 39,
            "key": "irelia",
            "name": "irelia"
        },
        "viktor": {
            "title": "the machine herald",
            "id": 112,
            "key": "viktor",
            "name": "viktor"
        },
        "rakan": {
            "title": "the charmer",
            "id": 497,
            "key": "rakan",
            "name": "rakan"
        },
        "kindred": {
            "title": "the eternal hunters",
            "id": 203,
            "key": "kindred",
            "name": "kindred"
        },
        "cassiopeia": {
            "title": "the serpent's embrace",
            "id": 69,
            "key": "cassiopeia",
            "name": "cassiopeia"
        },
        "maokai": {
            "title": "the twisted treant",
            "id": 57,
            "key": "maokai",
            "name": "maokai"
        },
        "ornn": {
            "title": "the fire below the mountain",
            "id": 516,
            "key": "ornn",
            "name": "ornn"
        },
        "thresh": {
            "title": "the chain warden",
            "id": 412,
            "key": "thresh",
            "name": "thresh"
        },
        "kayle": {
            "title": "the judicator",
            "id": 10,
            "key": "kayle",
            "name": "kayle"
        },
        "hecarim": {
            "title": "the shadow of war",
            "id": 120,
            "key": "hecarim",
            "name": "hecarim"
        },
        "khazix": {
            "title": "the voidreaver",
            "id": 121,
            "key": "khazix",
            "name": "kha'zix"
        },
        "olaf": {
            "title": "the berserker",
            "id": 2,
            "key": "olaf",
            "name": "olaf"
        },
        "ziggs": {
            "title": "the hexplosives expert",
            "id": 115,
            "key": "ziggs",
            "name": "ziggs"
        },
        "syndra": {
            "title": "the dark sovereign",
            "id": 134,
            "key": "syndra",
            "name": "syndra"
        },
        "drmundo": {
            "title": "the madman of zaun",
            "id": 36,
            "key": "drmundo",
            "name": "dr. mundo"
        },
        "karma": {
            "title": "the enlightened one",
            "id": 43,
            "key": "karma",
            "name": "karma"
        },
        "annie": {
            "title": "the dark child",
            "id": 1,
            "key": "annie",
            "name": "annie"
        },
        "akali": {
            "title": "the fist of shadow",
            "id": 84,
            "key": "akali",
            "name": "akali"
        },
        "volibear": {
            "title": "the thunder's roar",
            "id": 106,
            "key": "volibear",
            "name": "volibear"
        },
        "yasuo": {
            "title": "the unforgiven",
            "id": 157,
            "key": "yasuo",
            "name": "yasuo"
        },
        "kennen": {
            "title": "the heart of the tempest",
            "id": 85,
            "key": "kennen",
            "name": "kennen"
        },
        "rengar": {
            "title": "the pridestalker",
            "id": 107,
            "key": "rengar",
            "name": "rengar"
        },
        "ryze": {
            "title": "the rune mage",
            "id": 13,
            "key": "ryze",
            "name": "ryze"
        },
        "shen": {
            "title": "the eye of twilight",
            "id": 98,
            "key": "shen",
            "name": "shen"
        },
        "zac": {
            "title": "the secret weapon",
            "id": 154,
            "key": "zac",
            "name": "zac"
        },
        "talon": {
            "title": "the blade's shadow",
            "id": 91,
            "key": "talon",
            "name": "talon"
        },
        "swain": {
            "title": "the noxian grand general",
            "id": 50,
            "key": "swain",
            "name": "swain"
        },
        "bard": {
            "title": "the wandering caretaker",
            "id": 432,
            "key": "bard",
            "name": "bard"
        },
        "sion": {
            "title": "the undead juggernaut",
            "id": 14,
            "key": "sion",
            "name": "sion"
        },
        "vayne": {
            "title": "the night hunter",
            "id": 67,
            "key": "vayne",
            "name": "vayne"
        },
        "nasus": {
            "title": "the curator of the sands",
            "id": 75,
            "key": "nasus",
            "name": "nasus"
        },
        "kayn": {
            "title": "the shadow reaper",
            "id": 141,
            "key": "kayn",
            "name": "kayn"
        },
        "twistedfate": {
            "title": "the card master",
            "id": 4,
            "key": "twistedfate",
            "name": "twisted fate"
        },
        "chogath": {
            "title": "the terror of the void",
            "id": 31,
            "key": "chogath",
            "name": "cho'gath"
        },
        "udyr": {
            "title": "the spirit walker",
            "id": 77,
            "key": "udyr",
            "name": "udyr"
        },
        "lucian": {
            "title": "the purifier",
            "id": 236,
            "key": "lucian",
            "name": "lucian"
        },
        "ivern": {
            "title": "the green father",
            "id": 427,
            "key": "ivern",
            "name": "ivern"
        },
        "leona": {
            "title": "the radiant dawn",
            "id": 89,
            "key": "leona",
            "name": "leona"
        },
        "caitlyn": {
            "title": "the sheriff of piltover",
            "id": 51,
            "key": "caitlyn",
            "name": "caitlyn"
        },
        "sejuani": {
            "title": "fury of the north",
            "id": 113,
            "key": "sejuani",
            "name": "sejuani"
        },
        "nocturne": {
            "title": "the eternal nightmare",
            "id": 56,
            "key": "nocturne",
            "name": "nocturne"
        },
        "zilean": {
            "title": "the chronokeeper",
            "id": 26,
            "key": "zilean",
            "name": "zilean"
        },
        "azir": {
            "title": "the emperor of the sands",
            "id": 268,
            "key": "azir",
            "name": "azir"
        },
        "rumble": {
            "title": "the mechanized menace",
            "id": 68,
            "key": "rumble",
            "name": "rumble"
        },
        "morgana": {
            "title": "fallen angel",
            "id": 25,
            "key": "morgana",
            "name": "morgana"
        },
        "taliyah": {
            "title": "the stoneweaver",
            "id": 163,
            "key": "taliyah",
            "name": "taliyah"
        },
        "teemo": {
            "title": "the swift scout",
            "id": 17,
            "key": "teemo",
            "name": "teemo"
        },
        "urgot": {
            "title": "the dreadnought",
            "id": 6,
            "key": "urgot",
            "name": "urgot"
        },
        "amumu": {
            "title": "the sad mummy",
            "id": 32,
            "key": "amumu",
            "name": "amumu"
        },
        "galio": {
            "title": "the colossus",
            "id": 3,
            "key": "galio",
            "name": "galio"
        },
        "heimerdinger": {
            "title": "the revered inventor",
            "id": 74,
            "key": "heimerdinger",
            "name": "heimerdinger"
        },
        "anivia": {
            "title": "the cryophoenix",
            "id": 34,
            "key": "anivia",
            "name": "anivia"
        },
        "ashe": {
            "title": "the frost archer",
            "id": 22,
            "key": "ashe",
            "name": "ashe"
        },
        "velkoz": {
            "title": "the eye of the void",
            "id": 161,
            "key": "velkoz",
            "name": "vel'koz"
        },
        "singed": {
            "title": "the mad chemist",
            "id": 27,
            "key": "singed",
            "name": "singed"
        },
        "skarner": {
            "title": "the crystal vanguard",
            "id": 72,
            "key": "skarner",
            "name": "skarner"
        },
        "varus": {
            "title": "the arrow of retribution",
            "id": 110,
            "key": "varus",
            "name": "varus"
        },
        "twitch": {
            "title": "the plague rat",
            "id": 29,
            "key": "twitch",
            "name": "twitch"
        },
        "garen": {
            "title": "the might of demacia",
            "id": 86,
            "key": "garen",
            "name": "garen"
        },
        "blitzcrank": {
            "title": "the great steam golem",
            "id": 53,
            "key": "blitzcrank",
            "name": "blitzcrank"
        },
        "masteryi": {
            "title": "the wuju bladesman",
            "id": 11,
            "key": "masteryi",
            "name": "master yi"
        },
        "elise": {
            "title": "the spider queen",
            "id": 60,
            "key": "elise",
            "name": "elise"
        },
        "alistar": {
            "title": "the minotaur",
            "id": 12,
            "key": "alistar",
            "name": "alistar"
        },
        "katarina": {
            "title": "the sinister blade",
            "id": 55,
            "key": "katarina",
            "name": "katarina"
        },
        "ekko": {
            "title": "the boy who shattered time",
            "id": 245,
            "key": "ekko",
            "name": "ekko"
        },
        "mordekaiser": {
            "title": "the iron revenant",
            "id": 82,
            "key": "mordekaiser",
            "name": "mordekaiser"
        },
        "lulu": {
            "title": "the fae sorceress",
            "id": 117,
            "key": "lulu",
            "name": "lulu"
        },
        "camille": {
            "title": "the steel shadow",
            "id": 164,
            "key": "camille",
            "name": "camille"
        },
        "aatrox": {
            "title": "the darkin blade",
            "id": 266,
            "key": "aatrox",
            "name": "aatrox"
        },
        "draven": {
            "title": "the glorious executioner",
            "id": 119,
            "key": "draven",
            "name": "draven"
        },
        "tahmkench": {
            "title": "the river king",
            "id": 223,
            "key": "tahmkench",
            "name": "tahm kench"
        },
        "pantheon": {
            "title": "the artisan of war",
            "id": 80,
            "key": "pantheon",
            "name": "pantheon"
        },
        "xinzhao": {
            "title": "the seneschal of demacia",
            "id": 5,
            "key": "xinzhao",
            "name": "xin zhao"
        },
        "aurelionsol": {
            "title": "the star forger",
            "id": 136,
            "key": "aurelionsol",
            "name": "aurelion sol"
        },
        "leesin": {
            "title": "the blind monk",
            "id": 64,
            "key": "leesin",
            "name": "lee sin"
        },
        "taric": {
            "title": "the shield of valoran",
            "id": 44,
            "key": "taric",
            "name": "taric"
        },
        "malzahar": {
            "title": "the prophet of the void",
            "id": 90,
            "key": "malzahar",
            "name": "malzahar"
        },
        "kaisa": {
            "title": "daughter of the void",
            "id": 145,
            "key": "kaisa",
            "name": "kai'sa"
        },
        "diana": {
            "title": "scorn of the moon",
            "id": 131,
            "key": "diana",
            "name": "diana"
        },
        "tristana": {
            "title": "the yordle gunner",
            "id": 18,
            "key": "tristana",
            "name": "tristana"
        },
        "reksai": {
            "title": "the void burrower",
            "id": 421,
            "key": "reksai",
            "name": "rek'sai"
        },
        "vladimir": {
            "title": "the crimson reaper",
            "id": 8,
            "key": "vladimir",
            "name": "vladimir"
        },
        "jarvaniv": {
            "title": "the exemplar of demacia",
            "id": 59,
            "key": "jarvaniv",
            "name": "jarvan iv"
        },
        "nami": {
            "title": "the tidecaller",
            "id": 267,
            "key": "nami",
            "name": "nami"
        },
        "jhin": {
            "title": "the virtuoso",
            "id": 202,
            "key": "jhin",
            "name": "jhin"
        },
        "soraka": {
            "title": "the starchild",
            "id": 16,
            "key": "soraka",
            "name": "soraka"
        },
        "veigar": {
            "title": "the tiny master of evil",
            "id": 45,
            "key": "veigar",
            "name": "veigar"
        },
        "janna": {
            "title": "the storm's fury",
            "id": 40,
            "key": "janna",
            "name": "janna"
        },
        "nautilus": {
            "title": "the titan of the depths",
            "id": 111,
            "key": "nautilus",
            "name": "nautilus"
        },
        "evelynn": {
            "title": "agony's embrace",
            "id": 28,
            "key": "evelynn",
            "name": "evelynn"
        },
        "gragas": {
            "title": "the rabble rouser",
            "id": 79,
            "key": "gragas",
            "name": "gragas"
        },
        "zed": {
            "title": "the master of shadows",
            "id": 238,
            "key": "zed",
            "name": "zed"
        },
        "vi": {
            "title": "the piltover enforcer",
            "id": 254,
            "key": "vi",
            "name": "vi"
        },
        "kogmaw": {
            "title": "the mouth of the abyss",
            "id": 96,
            "key": "kogmaw",
            "name": "kog'maw"
        },
        "ahri": {
            "title": "the nine-tailed fox",
            "id": 103,
            "key": "ahri",
            "name": "ahri"
        },
        "quinn": {
            "title": "demacia's wings",
            "id": 133,
            "key": "quinn",
            "name": "quinn"
        },
        "leblanc": {
            "title": "the deceiver",
            "id": 7,
            "key": "leblanc",
            "name": "leblanc"
        },
        "ezreal": {
            "title": "the prodigal explorer",
            "id": 81,
            "key": "ezreal",
            "name": "ezreal"
        }
    }

    if champ in champListbyKey:
        return champListbyKey[champ]["id"]

def convertIdtoChamp(id):
    champListbyId = {
        "1": {
            "title": "the dark child",
            "id": 1,
            "key": "annie",
            "name": "annie"
        },
        "2": {
            "title": "the berserker",
            "id": 2,
            "key": "olaf",
            "name": "olaf"
        },
        "3": {
            "title": "the colossus",
            "id": 3,
            "key": "galio",
            "name": "galio"
        },
        "4": {
            "title": "the card master",
            "id": 4,
            "key": "twistedfate",
            "name": "twisted fate"
        },
        "5": {
            "title": "the seneschal of demacia",
            "id": 5,
            "key": "xinzhao",
            "name": "xin zhao"
        },
        "6": {
            "title": "the dreadnought",
            "id": 6,
            "key": "urgot",
            "name": "urgot"
        },
        "7": {
            "title": "the deceiver",
            "id": 7,
            "key": "leblanc",
            "name": "leblanc"
        },
        "8": {
            "title": "the crimson reaper",
            "id": 8,
            "key": "vladimir",
            "name": "vladimir"
        },
        "9": {
            "title": "the harbinger of doom",
            "id": 9,
            "key": "fiddlesticks",
            "name": "fiddlesticks"
        },
        "10": {
            "title": "the judicator",
            "id": 10,
            "key": "kayle",
            "name": "kayle"
        },
        "11": {
            "title": "the wuju bladesman",
            "id": 11,
            "key": "masteryi",
            "name": "master yi"
        },
        "12": {
            "title": "the minotaur",
            "id": 12,
            "key": "alistar",
            "name": "alistar"
        },
        "13": {
            "title": "the rune mage",
            "id": 13,
            "key": "ryze",
            "name": "ryze"
        },
        "14": {
            "title": "the undead juggernaut",
            "id": 14,
            "key": "sion",
            "name": "sion"
        },
        "15": {
            "title": "the battle mistress",
            "id": 15,
            "key": "sivir",
            "name": "sivir"
        },
        "16": {
            "title": "the starchild",
            "id": 16,
            "key": "soraka",
            "name": "soraka"
        },
        "17": {
            "title": "the swift scout",
            "id": 17,
            "key": "teemo",
            "name": "teemo"
        },
        "18": {
            "title": "the yordle gunner",
            "id": 18,
            "key": "tristana",
            "name": "tristana"
        },
        "19": {
            "title": "the uncaged wrath of zaun",
            "id": 19,
            "key": "warwick",
            "name": "warwick"
        },
        "20": {
            "title": "the yeti rider",
            "id": 20,
            "key": "nunu",
            "name": "nunu"
        },
        "21": {
            "title": "the bounty hunter",
            "id": 21,
            "key": "missfortune",
            "name": "miss fortune"
        },
        "22": {
            "title": "the frost archer",
            "id": 22,
            "key": "ashe",
            "name": "ashe"
        },
        "23": {
            "title": "the barbarian king",
            "id": 23,
            "key": "tryndamere",
            "name": "tryndamere"
        },
        "24": {
            "title": "grandmaster at arms",
            "id": 24,
            "key": "jax",
            "name": "jax"
        },
        "25": {
            "title": "fallen angel",
            "id": 25,
            "key": "morgana",
            "name": "morgana"
        },
        "26": {
            "title": "the chronokeeper",
            "id": 26,
            "key": "zilean",
            "name": "zilean"
        },
        "27": {
            "title": "the mad chemist",
            "id": 27,
            "key": "singed",
            "name": "singed"
        },
        "28": {
            "title": "agony's embrace",
            "id": 28,
            "key": "evelynn",
            "name": "evelynn"
        },
        "29": {
            "title": "the plague rat",
            "id": 29,
            "key": "twitch",
            "name": "twitch"
        },
        "30": {
            "title": "the deathsinger",
            "id": 30,
            "key": "karthus",
            "name": "karthus"
        },
        "31": {
            "title": "the terror of the void",
            "id": 31,
            "key": "chogath",
            "name": "cho'gath"
        },
        "32": {
            "title": "the sad mummy",
            "id": 32,
            "key": "amumu",
            "name": "amumu"
        },
        "33": {
            "title": "the armordillo",
            "id": 33,
            "key": "rammus",
            "name": "rammus"
        },
        "34": {
            "title": "the cryophoenix",
            "id": 34,
            "key": "anivia",
            "name": "anivia"
        },
        "35": {
            "title": "the demon jester",
            "id": 35,
            "key": "shaco",
            "name": "shaco"
        },
        "36": {
            "title": "the madman of zaun",
            "id": 36,
            "key": "drmundo",
            "name": "dr. mundo"
        },
        "37": {
            "title": "maven of the strings",
            "id": 37,
            "key": "sona",
            "name": "sona"
        },
        "38": {
            "title": "the void walker",
            "id": 38,
            "key": "kassadin",
            "name": "kassadin"
        },
        "39": {
            "title": "the will of the blades",
            "id": 39,
            "key": "irelia",
            "name": "irelia"
        },
        "40": {
            "title": "the storm's fury",
            "id": 40,
            "key": "janna",
            "name": "janna"
        },
        "41": {
            "title": "the saltwater scourge",
            "id": 41,
            "key": "gangplank",
            "name": "gangplank"
        },
        "42": {
            "title": "the daring bombardier",
            "id": 42,
            "key": "corki",
            "name": "corki"
        },
        "43": {
            "title": "the enlightened one",
            "id": 43,
            "key": "karma",
            "name": "karma"
        },
        "44": {
            "title": "the shield of valoran",
            "id": 44,
            "key": "taric",
            "name": "taric"
        },
        "45": {
            "title": "the tiny master of evil",
            "id": 45,
            "key": "veigar",
            "name": "veigar"
        },
        "48": {
            "title": "the troll king",
            "id": 48,
            "key": "trundle",
            "name": "trundle"
        },
        "50": {
            "title": "the noxian grand general",
            "id": 50,
            "key": "swain",
            "name": "swain"
        },
        "51": {
            "title": "the sheriff of piltover",
            "id": 51,
            "key": "caitlyn",
            "name": "caitlyn"
        },
        "53": {
            "title": "the great steam golem",
            "id": 53,
            "key": "blitzcrank",
            "name": "blitzcrank"
        },
        "54": {
            "title": "shard of the monolith",
            "id": 54,
            "key": "malphite",
            "name": "malphite"
        },
        "55": {
            "title": "the sinister blade",
            "id": 55,
            "key": "katarina",
            "name": "katarina"
        },
        "56": {
            "title": "the eternal nightmare",
            "id": 56,
            "key": "nocturne",
            "name": "nocturne"
        },
        "57": {
            "title": "the twisted treant",
            "id": 57,
            "key": "maokai",
            "name": "maokai"
        },
        "58": {
            "title": "the butcher of the sands",
            "id": 58,
            "key": "renekton",
            "name": "renekton"
        },
        "59": {
            "title": "the exemplar of demacia",
            "id": 59,
            "key": "jarvaniv",
            "name": "jarvan iv"
        },
        "60": {
            "title": "the spider queen",
            "id": 60,
            "key": "elise",
            "name": "elise"
        },
        "61": {
            "title": "the lady of clockwork",
            "id": 61,
            "key": "orianna",
            "name": "orianna"
        },
        "62": {
            "title": "the monkey king",
            "id": 62,
            "key": "monkeyking",
            "name": "wukong"
        },
        "63": {
            "title": "the burning vengeance",
            "id": 63,
            "key": "brand",
            "name": "brand"
        },
        "64": {
            "title": "the blind monk",
            "id": 64,
            "key": "leesin",
            "name": "lee sin"
        },
        "67": {
            "title": "the night hunter",
            "id": 67,
            "key": "vayne",
            "name": "vayne"
        },
        "68": {
            "title": "the mechanized menace",
            "id": 68,
            "key": "rumble",
            "name": "rumble"
        },
        "69": {
            "title": "the serpent's embrace",
            "id": 69,
            "key": "cassiopeia",
            "name": "cassiopeia"
        },
        "72": {
            "title": "the crystal vanguard",
            "id": 72,
            "key": "skarner",
            "name": "skarner"
        },
        "74": {
            "title": "the revered inventor",
            "id": 74,
            "key": "heimerdinger",
            "name": "heimerdinger"
        },
        "75": {
            "title": "the curator of the sands",
            "id": 75,
            "key": "nasus",
            "name": "nasus"
        },
        "76": {
            "title": "the bestial huntress",
            "id": 76,
            "key": "nidalee",
            "name": "nidalee"
        },
        "77": {
            "title": "the spirit walker",
            "id": 77,
            "key": "udyr",
            "name": "udyr"
        },
        "78": {
            "title": "keeper of the hammer",
            "id": 78,
            "key": "poppy",
            "name": "poppy"
        },
        "79": {
            "title": "the rabble rouser",
            "id": 79,
            "key": "gragas",
            "name": "gragas"
        },
        "80": {
            "title": "the artisan of war",
            "id": 80,
            "key": "pantheon",
            "name": "pantheon"
        },
        "81": {
            "title": "the prodigal explorer",
            "id": 81,
            "key": "ezreal",
            "name": "ezreal"
        },
        "82": {
            "title": "the iron revenant",
            "id": 82,
            "key": "mordekaiser",
            "name": "mordekaiser"
        },
        "83": {
            "title": "shepherd of souls",
            "id": 83,
            "key": "yorick",
            "name": "yorick"
        },
        "84": {
            "title": "the fist of shadow",
            "id": 84,
            "key": "akali",
            "name": "akali"
        },
        "85": {
            "title": "the heart of the tempest",
            "id": 85,
            "key": "kennen",
            "name": "kennen"
        },
        "86": {
            "title": "the might of demacia",
            "id": 86,
            "key": "garen",
            "name": "garen"
        },
        "89": {
            "title": "the radiant dawn",
            "id": 89,
            "key": "leona",
            "name": "leona"
        },
        "90": {
            "title": "the prophet of the void",
            "id": 90,
            "key": "malzahar",
            "name": "malzahar"
        },
        "91": {
            "title": "the blade's shadow",
            "id": 91,
            "key": "talon",
            "name": "talon"
        },
        "92": {
            "title": "the exile",
            "id": 92,
            "key": "riven",
            "name": "riven"
        },
        "96": {
            "title": "the mouth of the abyss",
            "id": 96,
            "key": "kogmaw",
            "name": "kog'maw"
        },
        "98": {
            "title": "the eye of twilight",
            "id": 98,
            "key": "shen",
            "name": "shen"
        },
        "99": {
            "title": "the lady of luminosity",
            "id": 99,
            "key": "lux",
            "name": "lux"
        },
        "101": {
            "title": "the magus ascendant",
            "id": 101,
            "key": "xerath",
            "name": "xerath"
        },
        "102": {
            "title": "the half-dragon",
            "id": 102,
            "key": "shyvana",
            "name": "shyvana"
        },
        "103": {
            "title": "the nine-tailed fox",
            "id": 103,
            "key": "ahri",
            "name": "ahri"
        },
        "104": {
            "title": "the outlaw",
            "id": 104,
            "key": "graves",
            "name": "graves"
        },
        "105": {
            "title": "the tidal trickster",
            "id": 105,
            "key": "fizz",
            "name": "fizz"
        },
        "106": {
            "title": "the thunder's roar",
            "id": 106,
            "key": "volibear",
            "name": "volibear"
        },
        "107": {
            "title": "the pridestalker",
            "id": 107,
            "key": "rengar",
            "name": "rengar"
        },
        "110": {
            "title": "the arrow of retribution",
            "id": 110,
            "key": "varus",
            "name": "varus"
        },
        "111": {
            "title": "the titan of the depths",
            "id": 111,
            "key": "nautilus",
            "name": "nautilus"
        },
        "112": {
            "title": "the machine herald",
            "id": 112,
            "key": "viktor",
            "name": "viktor"
        },
        "113": {
            "title": "fury of the north",
            "id": 113,
            "key": "sejuani",
            "name": "sejuani"
        },
        "114": {
            "title": "the grand duelist",
            "id": 114,
            "key": "fiora",
            "name": "fiora"
        },
        "115": {
            "title": "the hexplosives expert",
            "id": 115,
            "key": "ziggs",
            "name": "ziggs"
        },
        "117": {
            "title": "the fae sorceress",
            "id": 117,
            "key": "lulu",
            "name": "lulu"
        },
        "119": {
            "title": "the glorious executioner",
            "id": 119,
            "key": "draven",
            "name": "draven"
        },
        "120": {
            "title": "the shadow of war",
            "id": 120,
            "key": "hecarim",
            "name": "hecarim"
        },
        "121": {
            "title": "the voidreaver",
            "id": 121,
            "key": "khazix",
            "name": "kha'zix"
        },
        "122": {
            "title": "the hand of noxus",
            "id": 122,
            "key": "darius",
            "name": "darius"
        },
        "126": {
            "title": "the defender of tomorrow",
            "id": 126,
            "key": "jayce",
            "name": "jayce"
        },
        "127": {
            "title": "the ice witch",
            "id": 127,
            "key": "lissandra",
            "name": "lissandra"
        },
        "131": {
            "title": "scorn of the moon",
            "id": 131,
            "key": "diana",
            "name": "diana"
        },
        "133": {
            "title": "demacia's wings",
            "id": 133,
            "key": "quinn",
            "name": "quinn"
        },
        "134": {
            "title": "the dark sovereign",
            "id": 134,
            "key": "syndra",
            "name": "syndra"
        },
        "136": {
            "title": "the star forger",
            "id": 136,
            "key": "aurelionsol",
            "name": "aurelion sol"
        },
        "141": {
            "title": "the shadow reaper",
            "id": 141,
            "key": "kayn",
            "name": "kayn"
        },
        "142": {
            "title": "the aspect of twilight",
            "id": 142,
            "key": "zoe",
            "name": "zoe"
        },
        "143": {
            "title": "rise of the thorns",
            "id": 143,
            "key": "zyra",
            "name": "zyra"
        },
        "145": {
            "title": "daughter of the void",
            "id": 145,
            "key": "kaisa",
            "name": "kai'sa"
        },
        "150": {
            "title": "the missing link",
            "id": 150,
            "key": "gnar",
            "name": "gnar"
        },
        "154": {
            "title": "the secret weapon",
            "id": 154,
            "key": "zac",
            "name": "zac"
        },
        "157": {
            "title": "the unforgiven",
            "id": 157,
            "key": "yasuo",
            "name": "yasuo"
        },
        "161": {
            "title": "the eye of the void",
            "id": 161,
            "key": "velkoz",
            "name": "vel'koz"
        },
        "163": {
            "title": "the stoneweaver",
            "id": 163,
            "key": "taliyah",
            "name": "taliyah"
        },
        "164": {
            "title": "the steel shadow",
            "id": 164,
            "key": "camille",
            "name": "camille"
        },
        "201": {
            "title": "the heart of the freljord",
            "id": 201,
            "key": "braum",
            "name": "braum"
        },
        "202": {
            "title": "the virtuoso",
            "id": 202,
            "key": "jhin",
            "name": "jhin"
        },
        "203": {
            "title": "the eternal hunters",
            "id": 203,
            "key": "kindred",
            "name": "kindred"
        },
        "222": {
            "title": "the loose cannon",
            "id": 222,
            "key": "jinx",
            "name": "jinx"
        },
        "223": {
            "title": "the river king",
            "id": 223,
            "key": "tahmkench",
            "name": "tahm kench"
        },
        "236": {
            "title": "the purifier",
            "id": 236,
            "key": "lucian",
            "name": "lucian"
        },
        "238": {
            "title": "the master of shadows",
            "id": 238,
            "key": "zed",
            "name": "zed"
        },
        "240": {
            "title": "the cantankerous cavalier",
            "id": 240,
            "key": "kled",
            "name": "kled"
        },
        "245": {
            "title": "the boy who shattered time",
            "id": 245,
            "key": "ekko",
            "name": "ekko"
        },
        "254": {
            "title": "the piltover enforcer",
            "id": 254,
            "key": "vi",
            "name": "vi"
        },
        "266": {
            "title": "the darkin blade",
            "id": 266,
            "key": "aatrox",
            "name": "aatrox"
        },
        "267": {
            "title": "the tidecaller",
            "id": 267,
            "key": "nami",
            "name": "nami"
        },
        "268": {
            "title": "the emperor of the sands",
            "id": 268,
            "key": "azir",
            "name": "azir"
        },
        "412": {
            "title": "the chain warden",
            "id": 412,
            "key": "thresh",
            "name": "thresh"
        },
        "420": {
            "title": "the kraken priestess",
            "id": 420,
            "key": "illaoi",
            "name": "illaoi"
        },
        "421": {
            "title": "the void burrower",
            "id": 421,
            "key": "reksai",
            "name": "rek'sai"
        },
        "427": {
            "title": "the green father",
            "id": 427,
            "key": "ivern",
            "name": "ivern"
        },
        "429": {
            "title": "the spear of vengeance",
            "id": 429,
            "key": "kalista",
            "name": "kalista"
        },
        "432": {
            "title": "the wandering caretaker",
            "id": 432,
            "key": "bard",
            "name": "bard"
        },
        "497": {
            "title": "the charmer",
            "id": 497,
            "key": "rakan",
            "name": "rakan"
        },
        "498": {
            "title": "the rebel",
            "id": 498,
            "key": "xayah",
            "name": "xayah"
        },
        "516": {
            "title": "the fire below the mountain",
            "id": 516,
            "key": "ornn",
            "name": "ornn"
        }
    }
    
    if id in champListbyId:
        return champListbyId[id]["key"]