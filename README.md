# Comment faire un livre


## Env


Pour activer l'environnement sur ma machine (vegapunk) j'utilise :

```
workon conferences
```

Pour mettre à jour `requirements.txt`.

```
pip freeze > requirements.txt
```

## Server

```
python server.py
```

Et tout est dispo à [localhost:8080](http://localhost:8080/)

## Pdf

```
sh make-pdf.sh
```

Les pdfs sont créés dans `pdf/`
## Make

```
python make.py
```

Le livre est créé dans `index.html`

### Comment ça marche

1. `make.py` récupère les données dans `data.yml`
2. Il va chercher les textes de chaque conférences citée dans les données dans `contenu/`. Et les converti de markdown vers html.
3. Il parcours le sommaire décrit dans les données et pour chaque élément il utilise le bon template trouvé dans `template/` en fonction du type et ajoute le html créé au livre.




