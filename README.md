# Ocr-PBI
Ocr-PBI est une fonte libre dévellopée par **Lise Brosseau** et **Antoine Gelgon**. Cette monospace est réalisée grâce au langage de programmation **Metafont**. Ce projet est un fork du projet de l'[**Ocr-B metafont**](https://www.ctan.org/tex-archive/fonts/ocr-b) fait dans les débuts 90 par **Norbert Schwarz**.

![Specimen](https://github.com/Antoine-Gelgon/Ocr-PBI/blob/master/screenshot/re.png?raw=true)

Ce caractère est pensé pour un projet en particulier, le site de la **Petite Bibliothèque Infernale** de l'[Agence du Doute](http://agencedudoute.org/). Cependant nous encourrageons la réapropriation de son code et de ses formes, par d'autres pour d'autres contextes. **Fork this.**

![Specimen](https://github.com/Antoine-Gelgon/Ocr-PBI/raw/master/screenshot/all.png)

Le code source des fichiers metafont (.mf) est sous la license libre **GNU/GPL**.
Les fichiers fontes type : TrueType (.ttf), OpenType(.otf) .. sont sous la license [**Syl Open Font License**](http://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&id=OFL)

###Les programmes prérequis

Pour exécuter la fonte il vous faut plusieurs programmes.

* **Texlive** -> [documentation](https://github.com/EtienneOz/MetaBlum)

* [**Fontforge**](http://fontforge.github.io/en-US/).

* [**Mftrace**](http://lilypond.org/mftrace/)

###Description des fichiers

Pour pouvoir exécuter cette fonte il faut la totalité des fichiers .mf de ce dossier à la même racine.

- `ocr-pbi-canonique.mf` // est le fichier réunissant l'entirèeté des fichiers sources. C'est le fichier à exécuter, pour générer la fonte. Il permet également de changer des paramètres globales de la fonte. (exemple mettre les glyphs sous fond noir)

- `ocr-pbi-canonique-set.mf` // l'ensemble des fonctions ce trouve dans ce fichiers.

- `variable.mf` // sont les variables simple à modifier. Par exemple changer le type et la taille du trait, la largeur de la chasse et la hauteur des lettres.

- `letters/` // dans ce dossier on trouve les fichiers séparés des glyphs.

- `ocr-pbi-canonique-def.mf` // un fichier avec le reste des glyphs.

- `exe.sh` // le script d'exécution.

- `print.py` // petit script en python pour changer le fichier le .pfa en .ttf.

- `speci.html` // permet de visualiser l'ensemble des lettres directement après l'exécution.

###Générer la fonte

Si tout les programmes prérequis sont correctement installés, exécution de la fonte se fait simplement dans le terminal. Il faut aller au dossier source avec la commande `cd`. Puis entrer cette ligne : `bash exe.sh ocr-pbi-canonique a`

###Création d'un nouveau glyph

Pour créer un nouveau glyph il faut faire de préférence un fichier séparé, enregistré dans le dossier `letters/`.
Exemple pour la lettre bas de casse `a`  il faut créer un fichier `a.mf` dans `letters/bdc/`.

![lettre a](https://github.com/Antoine-Gelgon/Ocr-PBI/blob/master/screenshot/a.png?raw=true)

Puis dans ce fichier décrire la lettre de cette manière.
```
%--- a --- 

o.s[97][1]:= (3.5,8.5)--(3.5,0.65);

o.s[97][2]:= (0,8.65){left}..(-2,8.05)..(-3,6.9)..(-3.5,4.6){down}..
             (-3,2.35)..(-2,1.2)..(-1,0.73)..(0,0.6){right}..
             (1,0.73)..(2,1.2)..(3,2.35)..(3.5,4.6){up}..(3,6.9)..(2,8.05)..cycle;
o.i[97]:=2 ; 
```
Un tracé est déclaré par `o.s[code HTML du caractère][numéro du tracé]:=`. Ici le code HTML du caractère `a` est `&#97` mais nous ne marquons que le nombre de ce code donc `97`.

La dernière ligne `o.i[code HTML du caractère]:= nombre de tracés total` ici il y a 2 tracés.
Les points d'encrages du tracé sont écrits `(x,y)`. Pour faire une courbe entre deux points on utilise `..` et `--` pour tracer une droite.

Le tracé peut-être orienté grâce à `{up}`, `{down}`, `{right}`, `{left}` ou bien par `{(x,y)}`.

Pour fermer un tracé on utilise `cycle`.

###Injecter les variables x et y

Pour permettre à la fonte de pouvoir changer de chasse ou de hauteur on peut injecter les variables `x` et `y` dans les glyphs.
![Specimen](https://github.com/Antoine-Gelgon/Ocr-PBI/raw/master/screenshot/anime/recadre/anime-ocr-pbi.gif)

Pour ça il suffit d'écrire `*x` et `*y` dans les coordonnées des points(le `*` est le signe multiplié). La description du `a` deviendra donc:
```
%--- a ---

o.s[97][1]:= (3.5*x,8.5*y)--(3.5*x,0.65*y);

o.s[97][2]:= (0*x,8.65*y){left}..(-2*x,8.05*y)..(-3*x,6.9*y)..(-3.5*x,4.6*y){down}..
             (-3*x,2.35*y)..(-2*x,1.2*y)..(-1*x,0.73*y)..(0*x,0.6*y){right}..
             (1*x,0.73*y)..(2*x,1.2*y)..(3*x,2.35*y)..(3.5*x,4.6*y){up}..(3*x,6.9*y)..(2*x,8.05*y)..cycle;
             
o.i[97]:=2  ;   o.m[97]  := 0.65;
```
La valeur de ces variables peuvent être changé dans le fichier `variable.mf`.

###Varier le type et la taille du tracé

Toujours dans le fichier `variable.mf` on peut faire varier le type et la taille du tracé. 
![Specimen](https://github.com/Antoine-Gelgon/Ocr-PBI/raw/master/screenshot/anime/2/recadre/anime-2.gif)
Grâce aux variables `strokeX` et `strokeY` on change la largeur, avec `strokeRotate` on change son inclinaison (en degré)

La variable `penStyle` définit le style de forme du trait. La valeur `0` corespond à un trait de forme carré(pensquare), la valeur `1` à celui de forme circulaire(pencircle).

![Specimen](https://github.com/Antoine-Gelgon/Ocr-PBI/blob/master/screenshot/circle-square/square.png?raw=true)
```
strokeX:=70;
strokeY:=50;
strokeRotate:=45;
penStyle:=0;
```
![Specimen](https://github.com/Antoine-Gelgon/Ocr-PBI/blob/master/screenshot/circle-square/circle.png?raw=true)
```
strokeX:=70;
strokeY:=50;
strokeRotate:=0;
penStyle:=1;
```
