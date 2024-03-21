# Le dépot des conférences de poche

## Avis aux visiteur·euses

Les *Conférences de poche* c'est un spectacle de [Léon Lenclos](http://leonlenclos.net) de la [Cie NOKILL](http://cienokill.fr).

L'ambition de ce dépôt est de rassembler les textes, paratextes, outils informatifs, outils informatiques, données et métadonnées liés aux *Conférences de poche*.

L'ensemble de ce travail est placé sous la licence libre [CC0 1.0 universel](http://creativecommons.org/publicdomain/zero/1.0).

Ce dépôt est ouvert, néanmoins, sauf cas particulier, la visite de ce dépôt ne sera pas très intéressante pour vous.

Si vous vous intéressez aux *Conférences de poche*, je vous suggère de visiter plutôt [le site web des *Conférences de poche*](http://conferences.cienokill.fr).

Merci pour l'intérêt que vous portez à ce travail,

Bien à vous,

Léon.

## Avis à moi-même

Salut Léon, si ça fait longtemps que tu n'as pas mis les pieds ici, n'hésite pas à relire ce fichier avant de te remettre au travail. Ce fichier ne s'appelle pas *README* pour rien. Merci.

## Fonctionnement général du dépôt

### Les documents

Ce projet de documentation des *Conférences de poche* s'articule autour de la notion de *document*.

Un *document* peut être publié en HTML pour le web ou en PDF pour l'impression.

Les versions HTML des documents sont au premier niveau de ce dépôt.

Les versions PDF des documents sont rangés dans [pdf/](pdf/).

La publication des documents se fait semi-automatiquement grâce aux outils de publication.

La liste de tous les documents de ce projet est consultable dans le document [admin](http://conferences.cienokill.fr/admin.html)

### Les données

Le fichier [data.yml](data.yml) constitue la principale collection de données sur le projet.

C'est dans ce fichiers que sont définis chaque *documents* mais aussi chaque *conférences*.

### Les contenus

Les contenus textuels dont la longueur ou la nature ne sont pas adaptés à [data.yml](data.yml) sont rangés sous la forme de fichiers markdown (`.md`) dans le dossier [contenu/](contenu/)

### Définition des documents et modèles

la partie **documents** de [data.yml](data.yml) définie chaque document en donnant son *template* (modèle) et son *sommaire*.

On donne aussi le nom du document (*id*) et les noms des fichiers où il sera publié (*dist*) 

Le sommaire d'un **document** est la liste des parties du document. Chaque partie est défini par un identifiant (*id*) et un *template*.

Les *templates* sont écrits en mustache (`.mustache`) et sont rangés dans le dossier [template/](template/).

### Fabrication d'un document

Pour fabriquer un document :

- On prend le *template* principal du document.
- S'il y a une section `{{{html}}}` dans ce template, on y met les unes à la suite des autres toutes les parties du document.

Pour fabriquer une partie d'un document :

- On prend le *template* de la partie.
- S'il y a une section `{{{html}}}` dans ce template, on y met le contenu de la partie que l'on retrouve dans contenu/ grâce à l'*id* de la partie.

Les modèles peuvent aussi utiliser l'ensemble des données renseignées dans [data.yml](data.yml) et quelques données additionnelles :
- `date` : la date du jour de la publication.
- `sommaire` : le sommaire du livre.
- `id` : l'id du chapitre ou du document.
- `conf` : toutes les informations concernant la conférence si l'id est l'id d'une conférence.

### Publication en pratique

On peut publier un ou plusieurs documents :
- Soit en local en faisant tourner le serveur python ([server.py](server.py)) et en utilisant l'interface de [admin](http://conferences.cienokill.fr/admin.html) (fonctionne uniquement en local, uniquement avec le serveur python).
- Soit avec le script [make.py](make.py)

## Utilisation

### Environnement

Pour activer l'environnement sur ma machine (vegapunk) j'utilise :

```
workon conferences
```

Pour mettre à jour `requirements.txt`.

```
pip freeze > requirements.txt
```

### Server

```
python server.py
```

Et tout est dispo à [localhost:8080](http://localhost:8080/)

### Pdf

```
sh make-pdf.sh in.html out.pdf
```

Et le fichier `in.html` est converti en un PDF compressé portant le nom `out.pdf`. Un fichier `out-print.pdf`, non compressé, est aussi créé.

### Make

```
python make.py
```

Et tous les documents sont publiés !*

### Écriture des conférences

La facette principale de ce projet de documentation est la transcription de chaque conférences sous la forme d'un texte illustré.

Cette retranscription est motivée par :
- L'envie de publier les conférences de poche dans un livre de poche.
- La peur d'oublier les conférences, particulièrement celles que je ne joue plus.

La transcription du spectacle (textes parlés, dit devant un public, dessin en direct) à destination d'un livre (textes écrit, lu par une personne seule dans son coin, dessin immobile). Peut-être considéré comme un meurtre, la transformation d'une œuvre vivante en une œuvre morte.

### Règles

1. Je préfère que le texte soit intéressant et agréable à lire plutôt qu'il soit fidèle au spectacle.
2. 

Taille d'une ligne : 55 caractères
Taille d'une page : 28 lignes
Taille idéale pour une phrase : 1-3 lignes
Taille d'un paragraphe : 2-15 lignes

Particularité de style :
Phrases ou paragraphes qui commencent par une conjonction : OK
Usage abusif des parenthèses et parenthèses imbriquées : OK
Usage de la négation sans le ne : OK

C'est pas plutot que ce n'est pas
Ça ne fait pas plutot que ça fait pas
on n'écoute plutôt qu'on écoute
Typographie :
Mettre en emphase les noms d'oeuvres.
Les noms de marques
Mettre en emphase les mots/phrases intégrés dans des phrases par exemple : on appelle ça un *truc*.
Citations

Modification par rapport à l'oralité.
- Disparition des "Bon" "Ben"
- Enlever quelques "Et" "E


Equilibre texte image :

En général, le texte introduit l'image plutot que l'inverse.
