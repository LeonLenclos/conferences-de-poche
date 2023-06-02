# Comment faire un livre


## Creer

```
python creer.py
```

Le livre est créé dans `index.html`

## Comment ça marche

1. `creer.py` récupère les données dans `data.yml`
2. Il va chercher les textes de chaque conférences citée dans les données dans `contenu/`. Et les converti de markdown vers html.
3. Il parcours le sommaire décrit dans les données et pour chaque élément il utilise le bon template trouvé dans `template/` en fonction du type et ajoute le html créé au livre.
4. tout est intégré dans le template `index.mustache`