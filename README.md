# Pur Beurre, that's a fat life
----------------
Pur Beurre is a web application using the open database provided by [Open Food Facts](https://world.openfoodfacts.org/).
By using Pur Beurre, you'll be able to find a substitute for a food product, with better nutritive grades and higher 
quality. The program also gives you the possibility of creating an user account to save all your search results.


# What does Pur Beurre really do ?
----------------
Once you arrive on the [Pur Beurre application page](https://gp-bot-app.herokuapp.com/) :\
	- you can make a simple request by using the query form, then visualize the results \
	- you can create an account and then log in to be able to save your future search results \

Pur Beurre is hosted by [Heroku](https://www.heroku.com/), and for now is only available in french language.	

# For developpers, how to install and work on the app :
--------------
Clone with https : https://github.com/Nastyflav/App_Pur_Beurre_OC.git \
or clone with SSH : git@github.com:Nastyflav/App_Pur_Beurre_OC.git \
into a repo on your local machine \
Documentation about pull --> https://help.github.com/en/articles/cloning-a-repository 

Set your virtual environment under python3.8.x `pip install virtualenv`\
Create an new virtual environment `virtualenv -p python env`\
Activate it `source env/Scripts/activate.bat`\
Install requirements `pip install -r requirements.txt`\

## Dependancies :

Python 3.8.2 \
download : https://www.python.org/downloads/ \
install : https://realpython.com/installing-python/ 

Depending of your python's install, you might need PIP\
install pip : https://packaging.python.org/tutorials/installing-packages/

## Modules :

app_purbeurre (main project)\
app_purbeurre/authentication/ user profiles, sign in, log in and out functionalities\
app_purbeurre/save/ products saving functionalities\
app_purbeurre/search/ products searching and printing functionalities\
app_purbeurre/static/ all the static files, with Boostrap, JQuery, Java Script, images and css/sass libraries\
app_purbeurre/templates/ all the basics and home html templates\

## Built with :

Visual Studio Code (IDE)\
Python 3.8.2\
UTF-8

## Author :

Flavien Murail : https://github.com/Nastyflav


# How does Pur Beurre works ?
----------------

This application is working only when it's being used by the user's terminal. You just need to use your keyboard to interact with the app. Pur Beurre is for now only available in french language.
All the products are ranked by their Nova Group grade, which goes from 1 (high quality) to 4. The products with the highest ranking are those less transformed by the industry, healthy and with good nutritional intakes
More informations about the NOVA classification [here](https://fr.openfoodfacts.org/nova).

## 1. Create an account

At first, the user has to choose between two type of research :
```
Que souhaitez-vous faire ?
Pour consulter les catégories d'aliments disponibles -> Tapez 1
Pour consulter vos aliments favoris -> Tapez 2
```

## 2. Log in your account

If the user entered 1, he can choose a category among all that the program provides :
```
=======CATEGORIES=========
Choisissez un type d'aliment en tapant son numéro :

Pâtes à tartiner -> Tapez 1
Thés -> Tapez 2
Fromages blancs -> Tapez 3
Jus de fruits -> Tapez 4
Confitures -> Tapez 5
(etc)
```

# 3. Make a research

# 4. Select a product

Once the category is selected, the application returns a bunch of products associated. The user just has to choose which one he wants to substitute :
```
=======ALIMENTS=======
Choisissez un produit à substituer en tapant son numéro :
```
A selection of low-quality products is then showed, with their names and their Nova Group grades

# 4. Select a substitute

Based on the same system than during the product selection. The program show to the user a higher quality product and prints its caracteristics :
```
=======PRODUIT À REMPLACER=======

Voici les substituts pour Nutella, Nova GROUPE : 4

=======BETTER, HEALTHIER, TASTIER=======
```
A random high-quality product is then showed, with its name and its Nova Group grade.
The user can select it to see its details :
```
=======SUBSTITUT SÉLECTIONNÉ=======
Nom : Coquillettes (Maxi Format)

Description : Pâtes alimentaires au blé dur de qualité supérieure

Groupe Nova : 1

Disponible chez : Carrefour market

En savoir plus : https://fr.openfoodfacts.org/produit/3038350023001/coquillettes-maxi-format-panzani
```

# 5. Save a substitute

The program then asks the user if he wants to save his result into his favorites :
```
Souhaitez vous placer ce produit dans vos favoris ?
Oui -> Tapez 1
Non -> Tapez 2
```
If the user answers `1`, the program will record the new favorite in the local database. In any case, the user then has to choose to go back to the homepage or to close the app.

# 6. Consult your favorites in your account

At the beginning of the application, if the user chose to consult his records, all of his favorites products are displayed. \
Every substitute is associated with the original product it replaces :
```
=======HALL OF FAME=======
1 -> Sauce arrabbiata, comme substitut à Sauce tomate basilic
2 -> Brocolis En fleurettes, comme substitut à Poêlée la potagère
3 -> Tassimo - Lor café long intense, comme substitut à Nescafé 3 en 1 goût Café au Lait sucré
4 -> Nocciolata, comme substitut à Choco nussa
(etc)
```
By selecting the favorite's number, the user can see more details of the substitute he previously saved.

# 7. Log out of your account
Once you're connected to your account, you can at every moment log out of your account by clicking on the disconnect icon