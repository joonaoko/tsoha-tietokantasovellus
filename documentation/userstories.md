# Käyttäjätarinat

* Käyttäjänä voin nähdä tietokannasta löytyvät sarjat listasta.

`SELECT * FROM series;`


* Käyttäjänä voin katsella sarjan tietoja sarjan omalta sivulta.

`SELECT * FROM series WHERE id = <series.id>;`

* Kirjautuneena käyttäjänä voin nähdä oman seurattavien sarjojen listan.

`SELECT * FROM user_series WHERE account_id = <current_user.id>;`

* Kirjautuneena käyttäjänä voin katsella seuratun sarjan tietoja omalta sivulta.

`SELECT * FROM user_series WHERE id = <userseries.id>;`

* Kirjautuneena käyttäjänä voin lisätä sarjoja seurattavien sarjojen listalle.

`INSERT INTO user_series (episodes_watched, status, account_id, series_id) VALUES (<form.episodes_watched>, <form.status>, <current_user.id>, <series.id>);`

* Kirjautuneena käyttäjänä voin poistaa sarjoja seurattavien sarjojen listalta.

`DELETE FROM user_series WHERE id = <userseries.id>;`

* Kirjautuneena käyttäjänä voin listasta kasvattaa yksittäisen sarjan katsottujen jaksojen määrää yhdellä.

`SELECT episodes_watched FROM user_series WHERE id = <userseries.id>` => episodesWatched<br>
`episodesWatched++`<br>
`UPDATE user_series SET episodes_watched = <episodesWatched> WHERE id = <userseries.id>;`

* Kirjautuneena käyttäjänä voin muokkausnäkymässä muokata katsottujen jaksojen määrää syöttämällä uuden määrän, ja siirtää sarjan "aktiivisesti katsottujen" listalta "mahdollisesti katsottavien" listalle, ja toisin päin.

`UPDATE user_series SET episodes_watched = <form.episodes_watched>, status = <form.status> WHERE id = <userseries.id>;`

* Järjestelmänvalvojana voin lisätä uusia sarjoja tietokantaan.

`INSERT INTO series (name, episodes_total) VALUES (<form.name>, <form.episodes_total>);`

* Järjestelmänvalvojana voin muokkausnäkymässä muokata kunkin sarjan nimeä sekä jaksomäärää.

`UPDATE series SET name = <form.name>, episodes_total = <form.episodes_total> WHERE id = <series.id>`

* Järjestelmänvalvojana voin poistaa sarjoja tietokannasta, jolloin sarja poistetaan myös kaikilta seurattavien sarjojen listoilta.

`DELETE FROM user_series WHERE series.id = <series.id>;`<br>
`DELETE FROM series WHERE id = <series.id>;`


### Yhteenvetokyselyt:
* Käyttäjänä voin nähdä listan suosituimmista sarjoista, ja sarjoja seuraavien käyttäjien määrät.
```sqlite
SELECT series.name AS name, COUNT(user_series.series_id) AS amount
  FROM user_series INNER JOIN series ON user_series.series_id = series.id
  GROUP BY series.name
  ORDER BY amount DESC
  LIMIT 5;
```

* Käyttäjänä voin nähdä listan viimeisimmän 24 tunnin aikana käyttäjien Watchlisteillä päivitetyistä sarjoista.
```sqlite
SELECT DISTINCT series.id, series.name AS name
  FROM user_series INNER JOIN series ON user_series.series_id = series.id
  WHERE user_series.date_modified >= datetime('now','-1 day')
  ORDER BY user_series.date_modified DESC
  LIMIT 10;
```

* Käyttäjänä voin nähdä listan käyttäjistä, jotka tällä hetkellä katsovat useimpia sarjoja, ja kuinka monta jaksoa niitä he ovat katsoneet.
```sqlite	
SELECT account.username AS username, COUNT(user_series.series_id) AS watching, SUM(user_series.episodes_watched) AS eps_watched_total "
  FROM account INNER JOIN user_series ON user_series.account_id = account.id "
  WHERE user_series.status = 'Watching' "
  GROUP BY username "
  ORDER BY watching DESC, eps_watched_total DESC
  LIMIT 5;
```
