# Shion House - Fonctionnalités Principales

## Vue d'ensemble
Shion House est une plateforme e-commerce développée avec Django, offrant une expérience d'achat moderne et intuitive. Le projet met l'accent sur une interface utilisateur élégante et un système de recommandation intelligent pour améliorer l'expérience d'achat.

## Fonctionnalités Clés

### 1. Gestion des Produits
- Système de catégorisation des produits
- Support pour les images multiples par produit
- Système de notation intégré (échelle de 1 à 5)
- Description détaillée des produits
- Prix avec validation (minimum 100)

### 2. Système de Recommandation
Le système de recommandation est basé sur plusieurs facteurs :

#### Popularité des Produits
- Suivi des votes de popularité par utilisateur
- Système unique de vote (un vote par utilisateur par produit)
- Calcul de popularité sur les 30 derniers jours
- Affichage des produits les plus populaires sur la page d'accueil

#### Nouveautés
- Tri des produits par date d'ajout
- Section "Nouvelles Arrivées" pour mettre en avant les derniers produits

### 3. Panier d'Achat
- Panier personnalisé par utilisateur
- Gestion des quantités de produits
- Association unique produit-utilisateur dans le panier
- Mise à jour en temps réel du panier

### 4. Interface Utilisateur
- Design moderne et responsive
- Navigation intuitive par catégories
- Affichage optimisé des images de produits
- Système de recherche intégré
- Composants réutilisables pour une expérience cohérente

### 5. Sécurité et Authentification
- Système d'authentification utilisateur
- Protection des routes sensibles
- Validation des données utilisateur
- Gestion sécurisée des sessions

## Aspects Techniques
- Framework : Django
- Base de données : Intégration Django ORM
- Frontend : HTML/CSS avec composants modulaires
- Gestion des médias : Système de fichiers optimisé pour les images
- SEO : Sitemap intégré avec mise à jour hebdomadaire
