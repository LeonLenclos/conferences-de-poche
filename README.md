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


### Étapes de la retranscription

VOIR [todo.ods](todo.ods)

1. Taper le texte : Écrire tout le contenu de la conférence du début à la fin.
2. Adapter le texte : Modifier le style litteraire du texte (voir details ci-dessous)
3. Formater le texte : Modifier le style typographique et la mise en page du texte (voir details ci-dessous)
4. Precorriger le texte : Faire une première verification de l'orthographe, de la grammaire et des règles typographiques en utilisant Gramalecte.
5. Corriger le texte : Demander à une personne exterieure de revoir l'orthographe grammaire et règles typographiques avec un oeuil neuf.

En parallèlle :

1. Lister les images : Sous la forme `![description de l'image](img/illu-livre/titre-de-la-conf/##.png)
2. integrer les images : Dessiner les images et les intéger au livre.


### Règles

Règle principale : Je préfère que le texte soit intéressant et agréable à lire plutôt qu'il soit fidèle au spectacle.

#### Adaptation du texte

Changer le sens dans les cas où :

* Le texte doit s'adresser à des lecteur·ices, pas à des spectateur·ices.


Sachant que :

* Taille d'une ligne : 55 caractères
* Taille d'une page : 28 lignes

Essayer de réspecter :

* Taille idéale pour une phrase : 1-3 lignes
* Taille d'un paragraphe : 2-15 lignes

Conserver ces particularité de style :

* Phrases ou paragraphes qui commencent par une conjonction : OK
* Usage abusif des parenthèses et parenthèses imbriquées : OK
* Répétition d'un même mot plein de fois dans une phrase/un paragraphe : OK
* Usage de la négation sans le ne : DÉPEND DES CAS

Sur la négation : 

- Omettre le *n'* quand il change la pronontiation des mots autours *C'est pas* plutot que *ce n'est pas*
- Mettre le *n'* quand il est muet : *on n'écoute pas* plutôt que *on écoute pas*
- Mettre le *ne* quand il ne change pas la pronontiation des mots autours  *Ça ne fait pas* plutot que *ça fait pas*.

Inclusivité :

- Les textes des conférences doivent être inclusifs autant que possible.
- Mais éviter les formes d'écritures inclusives qui peuvent être considérées comme difficiles à oraliser.

Modification par rapport à l'oralité.
- Ne pas conserver les "Bon" "Ben"
- Enlever quelques "Et" "E

#### Formatage du texte

Notes en bas de page :

- https://ateliers.esad-pyrenees.fr/web/pages/ressources/ctrl-alt-print/pagedjs/exemples/footnotes.html
- `<span class="footnote"></span>`

emphase `*texte*`:

- les noms d'oeuvres.
- Les noms de marques
- les mots/groupes de mots intégrés dans des phrases par exemple : on appelle ça un *truc*.

Citations `> texte` ou `<q>texte</q>`:

- Toute citation d'oeuvre
- Une personne qui parle



Equilibre texte image :

En général, le texte introduit l'image plutot que l'inverse.
