# Asennusohje

1. Lataa sovellus Githubista "Clone or download" painikkeesta valitsemalla "Download ZIP".
2. Pura sovellus haluamaasi sijaintiin.
3. Avaa sovelluskansion juuri terminaalissa tai Windowsissa terminaaliemulaattorissa.
4. Luo sovellukselle virtuaaliympäristö syöttämällä terminaaliin `python3 -m venv venv`.
5. Aktivoi virtuaaliympäristö syöttämällä terminaaliin `source venv/bin/activate` tai Windowsissa `source venv/scripts/activate`.
6. Päivitä pip komennolla `pip install --upgrade pip`.
7. Asenna projektin vaativuudet syöttämällä `pip install -r requirements.txt`.
8. Nyt sovellus voidaan käynnistää komennolla `python3 run.py`.
9. Sovellus voidaan avata selaimessa osoitteessa `localhost:5000`.

## Käynnistäminen Herokussa

1. Luo projektille mahdollisuus git-versionhallintaan komennolla `git init`
2. Luo projektille repositorio Githubissa ja lisätään se versionhallinnan etäpisteeksi komennolla `git remote add origin <osoite>`
3. Siirrä tiedostot githubiin komennoilla `git add .` ja `git push -u origin master`
4. Luo projektille paikka Herokussa komennolla `heroku create <projektin nimi>`
5. Lisää tieto herokusta versionhallintaan komennolla `git remote add heroku https://git.heroku.com/<projektin-nimi>.git`
6. Lähetä projekti herokuun seuraavasti:
  `git add .`
  `git commit -m "Initial commit"`
  `git push heroku master'`
7. Nyt projekti on avattavissa kerrotussa osoitteessa.
