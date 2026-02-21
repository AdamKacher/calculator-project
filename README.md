# Calculator Project 

Ce projet est un package Python proposant une calculatrice permettant d'effectuer des opérations mathématiques. Il a été conçu dans le cadre d'un projet sur les bonnes pratiques de gestion de codes.

## Fonctionnalités

La classe `SimpleCalculator` permet d'effectuer des opérations arithmétiques basiques de manière sécurisée :

**Addition** : `fsum(a, b)`
**Soustraction** : `substract(a, b)`
**Multiplication** : `multiply(a, b)`
**Division** : `divide(a, b)` 

**Sécurité et Typage :**
* Les méthodes n'acceptent que des entiers (`int`) en entrée. Une erreur `TypeError` est levée si d'autres types sont fournis.
* La division par zéro est gérée de manière sécurisée et lève une erreur `ZeroDivisionError`.

## Installation

Il est fortement recommandé d'utiliser un environnement virtuel (`venv`) pour installer ce projet, qui a été développé avec Python 3.13.

**1. Cloner le dépôt :**
```bash
git clone [https://github.com/TonNomUtilisateur/calculator-project.git](https://github.com/TonNomUtilisateur/calculator-project.git)
cd calculator-project
```

**2. Créer et activer l'environnement virtuel :**
```bash
python3 -m venv venv
source venv/bin/activate  # Sur Windows : venv\Scripts\activate
```

**3. Installer le package en mode éditable :**
```bash
pip install -e .
```

## Utilisation

Voici un exemple simple de la façon d'importer et d'utiliser la calculatrice dans vos scripts Python :

```python
from calculator import SimpleCalculator

# Initialisation de la calculatrice
calc = SimpleCalculator()

# Opérations de base
addition = calc.fsum(10, 5)        # Résultat : 15
soustraction = calc.substract(10, 5) # Résultat : 5
multiplication = calc.multiply(10, 5) # Résultat : 50
division = calc.divide(10, 5)      # Résultat : 2.0

print(f"10 + 5 = {addition}")
```

## Tests et Bonnes Pratiques

Ce projet respecte des standards stricts de qualité de code. Si vous souhaitez modifier le code, assurez-vous de lancer les outils suivants :

* **Tests unitaires (Pytest)** : `pytest tests/`
* **Formatage (Black)** : `black src/ tests/`
* **Analyse statique (Pylint)** : `pylint src/`

## Licence

Ce projet est distribué sous la licence Unlicense (Domaine Public).