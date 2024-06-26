# Web

## Requêtes HTTP

### URL

http://enedis.fr

- http : HyperText Transfer Protocol, c'est le protocole de communication utilisé sur le réseau internet.
- enedis.fr : nom de domaine

### Type de requêtes HTTP

- GET => index.html
- POST
- PUT
- DELETE
- PATCH
...

### Code Statut HTTP

- 100 : Information
- 200 : Succès
- 300 : Redirection
- 400 : Erreur client
- 500 : Erreur serveur

## HTML

```html
<html>
<head>
    <title>Titre de la page</title>
    <link rel="stylesheet" href="style.css" />
</head>
<body>
    <h1>Titre</h1>
    <p>
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam nec
        purus nec nunc ultricies ultricies. Nullam nec purus nec nunc ultricies
        ultricies. Nullam nec purus nec nunc ultricies ultricies. Nullam nec
    </p>
    <div>
        <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam nec
            purus nec nunc ultricies ultricies. Nullam nec purus nec nunc ultricies
            ultricies. Nullam nec purus nec nunc ultricies ultricies. Nullam nec
        </p>
        <a href="https://enedis.fr">Clique ici !</a>
        <img src="https://via.placeholder.com/150" />
    </div>

    <script src="script.js"></script>
</body>
</html>
```

### Lien entre page
- index.html
```html
<html>
    <head></head>
    <body>
        <nav>
            <a href="/index.html">Accueil</a>
            <a href="/a-propos.html">À propos</a>
        </nav>
        <p>Paragraphe</p>
        <a href="/shoyo.html">Detail de Shoyo</a>
        <button>Mon Bouton</button>
    </body>
</html>
```
- shoyo.html
```html
<html>
    <head></head>
    <body>
        <nav>
            <a href="/index.html">Accueil</a>
            <a href="/a-propos.html">À propos</a>
        </nav>
        <p>Shoyo c'est un mec cool</p>
    </body>
</html>
```

## CSS

### Couleur

```css
p {
    color: red;
}
.competence {
    color: #F08D36;
    background-color: blue;
}
```

### Taille & Marges

```css
.competence {
    height: 20px; /* 70%, 80vh */
    width: 300px; /* 70%, 60vw */
}
#resume {
    margin: 10px;
    padding: 10px;

    margin-right: 10px;
    /*
        -left
        -top
        -bottom
    */
    padding-right: 10px;
    /*
        -left
        -top
        -bottom
    */
    border: solid 1px red;
    border-radius: 10px;
}
img {
    height: 100px;
    width: 300px;
    /* Permet de changer la façon dont l'image est resize */
    object-fit: cover
}
```

### Positionnement

- Méthode de positionnement des éléments dans une div
```css
#resume {
    display: flex;
    flex-direction: row; /* column */
    column-gap: 10px; /* row-gap: 10px */
    justify-items: center; /* start, end */
    align-content: center; /* start, end */
}
```
- Gestion du positionnement dans la page
```css
.element {
    /* Positionnement de base, c'est celui par défaut */
    position: relative;
    /* Absolue, pour placer des éléments devant/derrière d'autres dans la page */
    position: absolute;
    /* Fixe, pour par exemple placer un bouton toujours en bas de l'écran */
    position: fixed;
}
```

## JavaScript

### Variables

```javascript
let prenom = "Dave"
let age = 10
let argent = 25.8
```

### Interactions Navigateur

```javascript
// Interagir avec la console de développement
console.log(prenom)
console.log("Bonjour")

// Envoyer une alerte dans le navigateur
alert("Ceci est une alerte.")
```

### Conditions

```javascript
if prenom === "Dave" {
    console.log("Salut Dave !")
} else {
    console.log("Ce n'est pas Dave :(")
}
```

### Structure de données

- Listes
```javascript
let fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
// Récupérer la longueur d'une liste
fruits.length
// Récupérer la position d'un élément de la liste
fruits.indexOf('banana')
// Ajouter un élément à la liste
fruits.push('grape')
// Ranger une liste
fruits.sort()
// Récupérer le dernier élément de la liste et l'enlever
fruits.pop()
// Enlever un élément précis d'une liste (ici, on enlève 'apple')
fruits.splice(fruits.indexOf('apple'), 1)
```
- Objets (Similaire aux dictionnaires en Python)
```javascript
let numeros = {
    'Augustin': '0123456789',
    'Arthur': '0123456789'
}
console.log(numeros['Augustin'])
```

### Boucles

```javascript
fruits.forEach((fruit) => {
  console.log(fruit)
})
```

### Fonctions

- Fonction classiques

```javascript
function estPair(x) {
    return x % 2 === 0
}

console.log(estPair(2))
console.log(estPair(7))
```
```javascript
function factorielle(n) {
  if (n === 0) {
    return 1
  }

  let resultat = 1
  for (let i = 1; i <= n; i++) {
    resultat *= i
  }
  return resultat
}

console.log(factorielle(5)) // => 120
```

- Arrow Functions (fonctions fléchées)

Les fonctions fléchées peuvent être définis à la volée et garde le contexte de code précédent. Dans d'autres langages, elles peuvent être appelés fonctions anonymes.

```javascript
const estPair = (x) => {
    return x % 2 === 0
}

console.log(estPair(2))
console.log(estPair(7))
```

### Manipulation du DOM

Le DOM (Document Object Model) est le nom donné à l'ensemble des éléments HTML, présenté sous forme de noeuds s'imbriquant les uns dans les autres.
JavaScript peut donc modifier le contenu HTML d'une page en utilisant le DOM.

- Sélection d'élément et ajout d'event
```html
<button id="mon-bouton">Clique ici !</button>
```
```javascript
let monBouton = document.querySelector("#mon-bouton")

mouBonton.onClick = () => {
    alert("Bouh !")
    console.log(monBouton.children)
    monBouton.style.color = "red"
}
```

- Création et insertion d'éléments dans le DOM
```javascript
let monNouveauBouton = document.createElement("button")

document.body.appendChild(monNouveauBouton)
```

- Ajout d'event lors du changement d'un input
```javascript
let monInput = document.querySelector("#monInput")

monInput.addEventListener("change", (e) => {
    console.log(e)
})
```

### Exemples

- setTimeout
```javascript
let titre = document.querySelector("#titre")

setTimeout(() => {
    // Changer le texte à l'intérieur
    titre.innerText = "Nouveau titre"
    // Changer le style
    titre.style.color = "red"
    // Accéder aux éléments enfants d'un élément
    console.log(titre.children)
}, 2000)
```

# Python

## Variables

Différents types de variables :
- int: -2, -1, 0, 1, 2, ...
- float: -10.71, 0.7, 1.00, 45.9, ...
- string(str): "Dave"
- boolean: True / False

## Input

```python
myName = input("Entrez votre nom : ")
myAge = int(input("Entre votre âge : "))
print(myName)
print(myAge)
```

## Conditions

```python
if myName == "Dave":
    print("Bonjour Dave !")
elif nyName == "John":
    print("bonjour John !")
else:
    print("Ce n'est pas Dave :(")
```

## Calculs

```python
 adition = 4 + 3
 print(7)

 saoustraction = 8 - 9
 print(-1)

 multiplication = 4 * 32
 print(128)

 division = 50 / 5
 print(10)

 # un nombre mit à la puissance
 puissance = 5**2
 print(25)

 # indique le reste d'une division
 modulo_ou_reste = 15 % 4
 print(3)

 # une division arrondie
 division_arrondie = 15 // 2
 print(7)
```

## Structures de données

Différentes structures de données :
- Listes
```python
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')
fruits.index('banana')
fruits.append('grape')
fruits.sort()
fruits.pop()
```
- Dictionnaires
```python
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
tel['jack']
del tel['sape']
list(tel)
'guido' in tel
'jack' not in tel
```

## Boucles

### For

```python
# For classique avec un chiffre
for x in range (0, 5);
    print(x) # Affiche 0, 1, 2, 3, 4

# For classique à travers une lsite
for x in range(len(fruits)):
    fruit = fruits[x]
    print(fruit)

# Raccourci pour itérer à travers une liste
for fruit in fruits:
    print(fruit)
```

### While

```python
# While classique
x = 0
while x != 5:
    print(x) # Affiche 0, 1, 2, 3, 4
    x += 1

# While avec une liste
x = 0
while x != len(fruits):
    fruit = fruits[x]
    print(fruit)
    x += 1
```
