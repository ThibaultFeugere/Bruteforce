# Bruteforce

Les seules informations dont vous disposez à ce sujet, sont le nom du fichier : `shadow` ainsi qu'une wordlist nommée `dico_mini_fr`


## Rappels théoriques

### En vous aidant de la documentation disponible sur internet, expliquez en détail la structure du fichier qui vous a été fourni. 

On nous a fourni un fichier shadow qui possède 8 (doc : 9) “ : ”. 
Le premier élément est le nom d’utilisateur (login)
Le deuxième élément est le hash du mot de passe avec la structure $id$salt$hashed.
Information : parfois il y a un “ ! ” ou “ * “. Seulement signifie que le compte est verrouillé (ex mysql) mais un autre utilisateur peut quand même se connecter dessus. 
Le troisième élément est le jour où le mot de passe à été changé (depuis 1970) https://www.epochconverter.com/seconds-days-since-y0
Le quatrième élément et le nombre de jours minimum avant de changer son mot de passe.
Le cinquième élément et le nombre de jours maximum avant de changer son mot de passe.
Le sixième élément est le nombre de jours avant l’expiration de son mot de passe pendant lequel l’utilisateur est averti.


### Compte-tenu des résultats de cette analyse, déduisez le nom de l'algorithme utilisé pour générer les empreintes des mots de passe qui se trouvent dans ce fichier.

Nous pouvons voir trois hash :
Le compte de root : $1$934b4a210c17493f68bf6bfe74bff77a
Le compte de fred : $1$9ebf8e708dcb3f28cb43d5d52655ab14
Le compte de Giselle : $1$6e5fa4d9c48ca921c0a2ce1e64c9ae6f

Le $1$ nous informe que la fonction de hachage utilisée est le MD5.
On peut vérifier avec hash identifier.


## Rappelez moi en quoi consiste une attaque par force brute, ou recherche exhaustive

L’attaque par force brute consiste à générer des mots de passe en testant toutes les combinaisons possibles jusqu’à l’obtention du mot de passe.


## Rappelez moi en quoi consiste une attaque par dictionnaire 

L’attaque par dictionnaire consiste à lire un fichier plus ou moins long contenant des mots de passe qui ont pu être récupérés au cours de fuites de données ou les mots de passe qui, nous le savons, sont courants (azertyuiop, qwertyuiop, etc).


## Expliquez les avantages et inconvénients de chacune des deux méthodes.

L’avantage de l’attaque par force brute est, qu’avec une infinité de temps ou de puissance de calcul, nous sommes sûrs de connaître un succès. Le désavantage est que cela est très chronophage. L’avantage de l’attaque par dictionnaire est que cette méthode est très rapide, cependant, si le mot de passe en question n’est pas présent dedans, nous ne trouverons rien, de ce fait le succès est plus faible.


## Scripts

### Résultats de `dico_attack.py`

```
Utilisateur : root | Hash : $1$934b4a210c17493f68bf6bfe74bff77a
Utilisateur : fred | Hash : $1$9ebf8e708dcb3f28cb43d5d52655ab14
Utilisateur : giselle | Hash : $1$6e5fa4d9c48ca921c0a2ce1e64c9ae6f
-------------------------------
2 mots de passe trouvés
Résultats stockés dans : results_dico.txt
------------
Executés en : 0:00:00.007985
```

### results_dico.txt

```
User : giselle Password : brazil
User : root Password : t3_p@hEN_v12
```

### Résultats de bruteforce_multiprocessing.py

```
python3 bruteforce_multiprocessing.py                                                                   130 ⨯
Utilisateur : root | Hash : $1$934b4a210c17493f68bf6bfe74bff77a
Utilisateur : fred | Hash : $1$9ebf8e708dcb3f28cb43d5d52655ab14
Utilisateur : giselle | Hash : $1$6e5fa4d9c48ca921c0a2ce1e64c9ae6f
Longueur : 6
Longueur : 7
Longueur : 8
Mot de passe trouvé : brazil
Longueur 6 terminé.
```

(Nous n'avons pas le temps sur ce script car il continue de chercher les deux autres mots de passe)

### Résultats de bruteforce_multithreading.py

```
python3 bruteforce_multithreading.py                                                                    130 ⨯
Utilisateur : root | Hash : $1$934b4a210c17493f68bf6bfe74bff77a
Utilisateur : fred | Hash : $1$9ebf8e708dcb3f28cb43d5d52655ab14
Utilisateur : giselle | Hash : $1$6e5fa4d9c48ca921c0a2ce1e64c9ae6f
Thread numéro : 1 longueur : 1
Thread numéro : 1 longueur : 2
Thread numéro : 1 longueur : 3
Thread numéro : 1 longueur : 4
Thread numéro : 2 longueur : 6
Thread numéro : 3 longueur : 7
Thread numéro : 1 longueur : 5
Thread 1 terminé en 0:00:26.941222
Mot de passe trouvé : brazil
Thread 2 terminé en 0:00:36.745293
```

(On voit que je trouve le mot de passe brazil en 36 secondes, en général c'est plus souvent 40 secondes)

## Votre script a-t-il réussi à découvrir tous les mots de passe dissimulés dans le fichier shadow ?

Dans un temps raisonnable, mon script n'a trouvé qu'un seul mot de passe. Si ma puissance de calcul est infinie ou le temps disponible infini, alors j'aurais trouvé tous les mots de passe au bout d'un certains temps.

## Alphabet pour le bruteforce

`abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789;@_#`

### Conseil

Pour tester les deux scripts bruteforce et trouver le premier mot de passe, je recommande d'utiliser cet alphabet : `abcdefghijklmnopqrstuvwxyz`.


## Ressources

- [Fichier dico_mini_fr](./dico_mini_fr)
- [Fichier shadow](./shadow)
