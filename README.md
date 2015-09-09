# Ocr-PBI
Ocr-PBI est une fonte libre dévellopée par **Lise Brosseau** et **Antoine Gelgon**. Cette monospace est réalisé grâce au langage de programmation **Metafont**. Ce projet est un fork du projet de l'[**Ocr-B metafont**](https://www.ctan.org/tex-archive/fonts/ocr-b) fait dans les débuts 90 par **Norbert Schwarz**.

![Specimen](https://github.com/Antoine-Gelgon/Ocr-PBI/blob/master/screenshot/re.png?raw=true)

Ce caractère est pensé pour un projet particulier, le site de la **Petite Bibliothèque Infernale** de l'[Agence du Doute](http://agencedudoute.org/). Cependant nous encourrageons la réapropriation de son code et de ses formes, par d'autres pour d'autres contextes que celui d'orrigine. Fork this.

![Specimen](https://github.com/Antoine-Gelgon/Ocr-PBI/blob/master/screenshot/re.png?raw=true)

Le code source des fichiers metafont (.mf) est sous la license libre GNU/GPL.
Les fichiers fontes type : TrueType (.ttf), OpenType(.otf) .. sont sous la license [Syl Open Font License](http://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&id=OFL)

###Les programmes prérequis

Il exécuter la font il vous faut plusieurs programmes.

* **Texlive** -> [documentation](https://github.com/EtienneOz/MetaBlum)

* [**Fontforge**](http://fontforge.github.io/en-US/).

* [**Mftrace**](http://lilypond.org/mftrace/)

###Description des fichiers

Pour pouvoir exécuter cette fonte il faut la totalité des fichiers .mf de ce dossier à la même racine.

- **ocr-pbi-canonique.mf** // est le fichier réunissant l'entirèeté des fichiers sources. C'est le fichier à exécuter, pour générer la fonte. Il permet également de changer des paramètres globales de la fonte. (exemple mettre les glyphs sous fond noir)

- **ocr-pbi-canonique-set.mf** // l'ensemble des fonctions ce trouve dans ce fichiers.

- **variable.mf** // sont les variables simple à modifier. Par exemple changer le type et la taille du trait, la largeur de la chasse et la hauteur des lettres.

- **Letters** // dans ce dossier on trouve les fichiers séparés des glyphs.

- **ocr-pbi-canonique-def.mf** // un fichier avec le reste des glyphs.

- **exe.sh** // le script d'exécution.

- **print.py** // petit script en python pour changer le fichier le .pfa en .ttf.

- **speci.html** // permet de visualiser l'ensemble des lettres directement après l'exécution.

###Générer la fonte

Si tout les programmes prérequis sont correctement installés, exécution de la fonte se fait simplement dans le terminal. Il faut aller au dossier source avec la commande `cd`. Puis entrer cette ligne : `bash exe.sh ocr-pbi-canonique a`

###Création d'un nouveau glyph

Pour créer un nouveau glyph il faut faire de préférence un fichier séparé, enregistré dans le dossier `letters`.
Exemple pour la lettre bas de casse `a`  il faut créer un fichier `a.mf` dans `letters/bdc/`.
Puis dans ce fichier décrire la lettre de cette manière.
```
%--- a --- 

o.s[97][1]:= (3.5*x,8.5*y)--(3.5*x,0.65*y);

o.s[97][2]:= (0*x,8.65*y){left}..(-2*x,8.05*y)..(-3*x,6.9*y)..(-3.5*x,4.6*y){down}..
             (-3*x,2.35*y)..(-2*x,1.2*y)..(-1*x,0.73*y)..(0*x,0.6*y){right}..
             (1*x,0.73*y)..(2*x,1.2*y)..(3*x,2.35*y)..(3.5*x,4.6*y){up}..(3*x,6.9*y)..(2*x,8.05*y)..cycle;
o.i[97]:=2  ;
```
[lettre a]()





![Specimen](https://github.com/Antoine-Gelgon/Ocr-PBI/raw/master/screenshot/anime/2/recadre/anime-2.gif)
