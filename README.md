# Le dépot des conférences de poche

Les Conférences de poche c'est un spectacle de Léon Lenclos de la Cie NOKILL.

L'ambition de ce dépôt est de rassembler :
- Les textes et les informations de chaque conférences.
- Les textes et les informations générales sur le spectacle.
- Les outils permettant de créer tous les documents (pour le web ou pour le papier) liés aux conférences.


## Les documents

- Le livre
- Le dossier
- La fiche technique
- L'affiche
- La page des conférences sur le site de la compagnie

## Comment ça marche

Ce qui suit est un pense-bête qui m'est déstiné à moi-même.

## Environnement

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

## Make

```
python make.py
```

Le livre est créé dans `index.html`

### Comment ça marche

1. `make.py` récupère les données dans `data.yml`
2. Il va chercher les textes de chaque conférences citée dans les données dans `contenu/`. Et les converti de markdown vers html.
3. Il parcours le sommaire décrit dans les données et pour chaque élément il utilise le bon template trouvé dans `template/` en fonction du type et ajoute le html créé au livre.




