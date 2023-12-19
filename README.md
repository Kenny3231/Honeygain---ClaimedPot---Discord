# honeygain-claim-honeypot
Automatically claim the daily honeypot  
There is a crontab that will run the included python script at 1pm.

## Environment Variables

|Name    |Value        |Optional|
|--------|-------------|--------|
|EMAIL   |Your token   |No      |
|PASSWORD|Your password|No      |

## Example
docker run --name honeygain-claim-honeypot -d  -e EMAIL=<-!your email!-> -e PASSWORD=<-!your password!-> arnesteinbach/honeygain-claim-honeypot

[https://hub.docker.com/r/arnesteinbach/honeygain-claim-honeypot](https://hub.docker.com/r/arnesteinbach/honeygain-claim-honeypot)
