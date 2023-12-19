# honeygain---ClaimPot-Discord
Réclame automatiquement le pot et lancement du script toutes les heures

## Environment Variables

|Nom     |Valeur       |Optional|
|--------|-------------|--------|
|EMAIL   |Your email   |Non     |
|PASSWORD|Your password|Non     |
|URL     |URL WEBHOOK  |Non     |
|ID      |ID MESSAGE   |Oui     |

## Example
docker run --name honeygain-claim-honeypot -d  -e EMAIL=<-!your email!-> -e PASSWORD=<-!your password!-> -e URL=<-!url webhook!-> -e ID==<-!ID!-> kenny31/honeygain-claimpod-discord:latest

##Docker Compose

```yaml
version: "3.5"
services:
  honeygaindiscord:
    container_name: honeygaindiscord
    image: kenny31/honeygain-claimpod-discord:latest
    environment:
      - EMAIL=@mail
      - PASSWORD=Password
      - URL=https://discord.com/api/webhooks/XXXXXXXXXXXXXXX/XXXXXXXX
      - ID=118XXXXXXXXXXXX323
    volumes:    
      - /etc/localtime:/etc/localtime:ro
    restart: always
```

J'ai repris et amélioré le github:
[https://hub.docker.com/r/arnesteinbach/honeygain-claim-honeypot](https://hub.docker.com/r/arnesteinbach/honeygain-claim-honeypot)
