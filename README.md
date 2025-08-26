# Labo 01 – Client/Serveur, Persistence (DAO/RDBS/NoSQL)
<img src="https://upload.wikimedia.org/wikipedia/commons/2/2a/Ets_quebec_logo.png" width="250">    
ÉTS - LOG430 - Architecture logicielle - Chargé de laboratoire: Gabriel C. Ullmann, Automne 2025.    

## 🎯 Objectifs d’apprentissage

- Apprendre à créer une application **client-serveur** simple.
- Comprendre et mettre en œuvre la structure **MVC avec DAO** pour bien séparer les responsabilités.
- Comprendre les avantages et les inconvénients des bases de données relationnelles (ex. MySQL) par rapport aux bases « NoSQL » ou orientées à documents (ex. MongoDB).

--- 

## ⚙️ Setup
Dans ce laboratoire, vous développerez une application de gestion des personnes et des articles pour un petit magasin. Il ne s’agit pas d’une application commerciale complète, mais elle offre une structure de base qui nous permettra d’expérimenter une architecture Client–Serveur sous une forme simplifiée :

- Le client (`store_manager.py`) se connecte à un serveur (base de données), qui peut se trouver sur le même ordinateur ou sur un autre. Dans notre cas, nous utiliserons un seul conteneur dans la machine virtuelle pour l’ensemble de l’application.

- Cette architecture permet d’avoir plusieurs clients. Par exemple un poste à chaque caisse du magasin, afin que les vendeurs puissent consulter le catalogue d’articles et ajouter de nouveaux articles.

- Cette architecture permet également d’avoir plusieurs serveurs. Pour explorer les avantages et les inconvénients de différentes bases de données, nous utiliserons dans ce laboratoire deux serveurs : MySQL et MongoDB. Les avantages spécifiques d'utiliser les bases de données multiples seront étudiés plus en détail dans les prochains laboratoires.

- En travaillant sur les opérations de base de données, nous expérimenterons aussi les concepts de Data Access Object (DAO) et de MVC (Model–View–Controller).

### 1. Faites un fork et clonez le dépôt GitLab

```bash
git clone https://github.com/guteacher/log430-a25-labo1
cd log430-a25-labo1
```

### 2. Préparer l’environnement de développement
Suivez les mêmes étapes que dans le laboratoire 00.

### 3. Lancez l’application

```bash
cd src
python store_manager.py
```

---

## 🧪 Activités pratiques

### 1. DAO MySQL

Le fichier `UserDAO` (dans `dao/user_dao.py`) contient déjà les méthodes `select_all()` et `insert(user)`.

Complétez cette DAO en y ajoutant :
   - `update(user)` – pour modifier un utilisateur existant.
   - `delete(user_id)` – pour supprimer un utilisateur.

> 💡 Question 1 : Quelles commandes avez-vous utilisées pour effectuer les opérations UPDATE et DELETE dans MySQL ? Avez-vous uniquement utilisé Python ou également du SQL ? Veuillez inclure le code pour illustrer votre réponse.

#### Remarque : types de DAO
Il existe plusieurs manières d’implémenter une DAO. Par exemple, nous pourrions placer les opérations de base de données directement dans la classe Model. Dans notre cas, nous conservons la DAO et le Model séparés, comme décrit dans les ouvrages suivants : 
- 📘 Documenting Software Architectures: Views and Beyond, Clements et al., 2010, p. 97.
- 📕 Core J2EE Patterns: Best Practices and Design Strategies, Alur et al., 2001, p. 252.

### 2. DAO MongoDB

Créez une nouvelle DAO `UserDAOMongo` dans un fichier `dao/user_dao_mongo.py`.

Implémentez les mêmes méthodes :
   - `select_all()`
   - `insert(user)`
   - `update(user)`
   - `delete(user_id)`

Modifiez `test_user.py` pour utiliser `UserDAOMongo` en lieu de `UserDAO`, puis relancez les tests. Une implémentation correcte doit produire les mêmes résultats, en considérant que quelques ajustements mineurs dans les tests peuvent être nécessaires pour assurer l’interchangeabilité des DAO.

> 💡 Question 2 : Quelles commandes avez-vous utilisées pour effectuer les opérations dans MongoDB ? Avez-vous uniquement utilisé Python ou également du SQL ? Veuillez inclure le code pour illustrer votre réponse.

### 3. Nouveau tableau : Products
Insérez le code SQL pour créer le tableau `products` dans `db-init/init.sql`. Ce fichier sera executé a chaque fois qu'on démarre la conteneur.
```sql
CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(80) NOT NULL,
    brand VARCHAR(20) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);
```

Créez un nouvel Model, View, Controller et DAO pour `Product`. Utilisez une structure MVC similaire à `User`. Ajoutez les options `Montrer la liste d'items` et `Ajouter un item` dans `store_manager.py`. Vous pouvez également ajouter une option de `Supprimer un item` au menu (facultatif). Veuillez utiliser les diagrammes disponibles dans le dossier docs/uml comme référence pour l’implémentation.

> 💡 Question 3 : Comment avez-vous implémenté votre `product_view.py` ? Est-ce qu’il importe directement la `ProductDAO` ? Veuillez inclure le code pour illustrer votre réponse.

> 💡 Question 4 : Si nous devions créer une application permettant d’associer des achats d'articles aux utilisateurs (`Users` → `Products`), comment structurerions-nous les données dans MySQL par rapport à MongoDB ?


### ✅ Correction des activités

Des tests unitaires sont inclus dans le dépôt. Pour les exécuter :

```bash
python3 -m pytest
```

Si tous les tests passent ✅, vos implémentations sont correctes.

---

## 📦 Livrables

- Code compressé en `.zip` contenant **l'ensemble du code source** du projet Labo 01.
- Rapport `.pdf` répondant aux 4 questions presentées dans ce fichier. Il est **obligatoire** d'ajouter du code ou des sorties de terminal pour illustrer chacune de vos réponses.

