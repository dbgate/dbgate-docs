---
sourceHash: fd6032a57cb859a0d8cb5046fde87de9bf1a85de56c66586391e84ecbbdc24c1
language: fr
title: Déployer sur AWS
subtitle: Déploiement en un clic sur un cluster Amazon EC2
icon: aws.svg
weight: 10
demo_url: https://aws.amazon.com/marketplace/pp/prodview-glw7okfnhf4cy
demo_title: View on AWS
edition: 'premium'
---

L'édition DbGate AWS est une plateforme web collaborative et multi-utilisateurs spécialement conçue pour la gestion de bases de données au sein d'Amazon Web Services (AWS). En tirant parti de l'infrastructure AWS, elle facilite le travail d'équipe pour les organisations opérant dans des environnements cloud. Son interface partagée, accessible depuis un navigateur, simplifie la collaboration, l'accès aux données et la supervision des bases de données, tout en s'intégrant parfaitement à AWS.

{{< button href="https://aws.amazon.com/marketplace/pp/prodview-glw7okfnhf4cy" style="blue" icon="fa-solid fa-arrow-up-right-from-square" >}}DbGate sur AWS{{< /button >}}

## Fonctionnalités clés de DbGate AWS
DbGate AWS prend en charge les mêmes fonctionnalités que DbGate Team Premium, mais est optimisé pour AWS

* Prise en charge d'AWS IAM
* Administration des utilisateurs, des connexions et des rôles
* Navigation, filtrage et édition des données
* Import et export de données
* Constructeur de requêtes visuel

## Processus d'installation
L'installation sur AWS est très simple, c'est presque un processus en un seul clic.

Nous recommandons le type d'instance t2.medium pour une expérience utilisateur optimale, mais l'instance t2.micro disponible dans l'offre gratuite sera suffisante pour un petit nombre d'utilisateurs.

Après l'installation, vous devez définir le mot de passe administrateur, puis vous pouvez administrer les connexions, les utilisateurs, les rôles et accorder des autorisations.

## Abonnement et licences
DbGate AWS peut être souscrit via AWS Marketplace, avec une tarification basée sur la taille de l'instance choisie. Les instances plus grandes prennent en charge davantage d'utilisateurs simultanés.

Un essai gratuit de 30 jours vous donne accès à toutes les fonctionnalités de DbGate. À l'issue de l'essai, la facturation suit le plan tarifaire d'AWS en fonction de la taille de l'instance sélectionnée. Aucune licence supplémentaire n'est requise, car tous les paiements sont gérés via l'abonnement [AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-glw7okfnhf4cy).

## Mises à jour de DbGate AWS
DbGate AWS dispose d'une build spéciale et s'exécute directement sur un serveur virtuel dans EC2 (il n'y a pas de couche de virtualisation supplémentaire comme docker). Une fonctionnalité de mise à niveau automatique est disponible : après le démarrage, le conteneur recherche la build la plus récente et, s'il en trouve une, il remplace l'ancienne version. Vous n'avez pas à effectuer la mise à niveau manuellement.

Si vous créez manuellement un nouveau conteneur EC2 avec une nouvelle version, celui-ci disposera de sa propre nouvelle base de données (la base de données MySQL interne fait partie du conteneur) ; il n'existe donc pas de moyen simple de transférer les connexions et les utilisateurs vers le nouveau conteneur EC2.

{{< button href="https://aws.amazon.com/marketplace/pp/prodview-glw7okfnhf4cy" style="blue" icon="fa-solid fa-arrow-up-right-from-square" >}}DbGate sur AWS{{< /button >}}
