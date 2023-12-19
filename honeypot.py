from pyHoneygain import HoneyGain
from discord_webhook import DiscordWebhook, DiscordEmbed
from datetime import date, datetime
import os

# Get email and pass from env var
EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')
URL = os.getenv('URL')
ID = os.getenv('ID')

if ID != "" :
    webhook = DiscordWebhook(url=URL, id=ID)
else :
    webhook = DiscordWebhook(url=URL)

#CACHED_TOKEN_PATH = '/root/.jwt-token'
CACHED_TOKEN_PATH = 'C:\Sauvegarde Syno\Projets\HoneyGain\honeygain-honeypot-main\honeygain-honeypot-main\.jwt-token'

#Function Login
def login():
    if os.path.exists(CACHED_TOKEN_PATH):
        with open(CACHED_TOKEN_PATH, 'r+') as file:
            user.set_jwt_token(file.read())
    else:
        user.login(EMAIL, PASSWORD)

        with open(CACHED_TOKEN_PATH, 'w') as file:
            file.write(user.jwt)

user = HoneyGain()

login()

#Si token est différent
if(os.path.exists(CACHED_TOKEN_PATH) and not user.me()):
    os.remove(CACHED_TOKEN_PATH)
    login()

#Variables
Balance = str(user.wallet_stats()["data"]["{}".format(date.today())]["hg_credits"])
Total = str(user.balances()["payout"]["usd_cents"]/100)+"$"
honeypot_status = user.get_honeypot_status()
message = "error"
# Obtenez la date et l'heure actuelles
Now = (datetime.now()).strftime("%Y-%m-%d %H:%M:%S")

#Si pas cliquer
if str(honeypot_status["winning_credits"]) != "None":
    message = "{} a déjà réclamé le pot de miel aujourd'hui.{}".format(user.me()['email'], Balance)
    Claimed = str(user.stats_today()["winning"]["credits"])
else:
    if honeypot_status["progress_bytes"] == honeypot_status["max_bytes"]:
        result = user.open_honeypot()
        if result["success"]:
            message = "Ouverture du pot."           
            Claimed = str(user.stats_today()["winning"]["credits"])
        else:
            message = "Impossible de réclamer le pot."
            Claimed="Echec"            
    else:
        message = "Impossible d'ouvrir le pot de miel pour {}, je n'ai pas rassemblé 15 Mo. {}\nProgression en octets : {}/15000000".format(
            user.me()['email'], Balance, user.get_honeypot_status()["progress_bytes"])

print(message)

#embed.set_author(name="Docker_Bot")
# set thumbnail
embed = DiscordEmbed(title="HoneyGain - {}".format(user.me()['email']), description="Mise a jour le "+Now , color="03b2f8")
embed.set_thumbnail(url="https://cdn.jsdelivr.net/gh/Kenny3231/Dashboard-Icons@master/png/honeygain.png")
embed.add_embed_field(name="Total", value=Total, inline=True)
embed.add_embed_field(name="Balance du jour", value=Balance, inline=True)
embed.add_embed_field(name="Bonus", value=Claimed, inline=True)
webhook.add_embed(embed)
webhook.edit()

if ID != "" :
    webhook.edit()
else :
    webhook.execute()