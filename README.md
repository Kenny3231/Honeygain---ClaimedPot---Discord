# honeygain---ClaimPot-Discord
Réclame automatiquement le pot
Lancement du script à 13H tous les jours

## Environment Variables

|Nom     |Valeur       |Optional|
|--------|-------------|--------|
|EMAIL   |Your email   |Non     |
|PASSWORD|Your password|Non     |
|URL     |URL WEBHOOK  |Non     |
|ID      |ID MESSAGE   |Oui     |

## Example
docker run --name honeygain-claim-honeypot -d  -e EMAIL=<-!your email!-> -e PASSWORD=<-!your password!-> arnesteinbach/honeygain-claim-honeypot

J'ai reprise et améliorer le github:
[https://hub.docker.com/r/arnesteinbach/honeygain-claim-honeypot](https://hub.docker.com/r/arnesteinbach/honeygain-claim-honeypot)
