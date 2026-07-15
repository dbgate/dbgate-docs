---
sourceHash: 4f9596eb7ab62bc22f186ebb87b019eb2986c18eb704368b8634ffc2cd471482
language: fr
title: Déployer sur Azure
weight: 20
---

L'édition DbGate Azure est une plateforme web collaborative et multi-utilisateurs spécialement conçue pour la gestion de bases de données au sein d'Azure. En tirant parti de l'infrastructure Azure, elle facilite le travail d'équipe pour les organisations opérant dans des environnements cloud. Son interface partagée, accessible depuis le navigateur, simplifie la collaboration, l'accès aux données et la supervision des bases de données, tout en s'intégrant parfaitement à Azure.

{{< button href="https://azuremarketplace.microsoft.com/en-us/marketplace/apps/sprinxsystemsas1582034211947.dbgate_azure_vm?tab=Overview" style="blue" icon="fa-solid fa-arrow-up-right-from-square" >}}DbGate sur Azure{{< /button >}}


## Fonctionnalités clés de DbGate Azure
DbGate Azure prend en charge les mêmes fonctionnalités que DbGate Team Premium, mais est optimisé pour Azure

* Prise en charge de l'identité managée Azure
* Administration des utilisateurs, des connexions et des rôles
* Navigation, filtrage et édition des données
* Import et export de données
* Constructeur de requêtes visuel

## Processus d'installation
L'installation sur Azure est très simple, c'est presque un processus en un seul clic.

Nous recommandons des machines virtuelles avec 2 Go de RAM.

Après l'installation, vous devez définir le mot de passe administrateur, puis vous pouvez administrer les connexions, les utilisateurs, les rôles et accorder des permissions.

## Abonnement et licences
DbGate Azure peut être souscrit via l'Azure Marketplace, avec une tarification basée sur le nombre de processeurs de la machine virtuelle choisie.

Un essai gratuit de 30 jours vous donne accès à toutes les fonctionnalités de DbGate. À l'issue de la période d'essai, la facturation suit le plan tarifaire Azure en fonction de la taille d'instance sélectionnée. Aucune licence supplémentaire n'est requise, car tous les paiements sont gérés via l'abonnement [Azure Marketplace](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/sprinxsystemsas1582034211947.dbgate_azure_vm?tab=Overview).

## Mises à jour de DbGate Azure
DbGate Azure dispose de sa propre build spéciale et s'exécute directement sur le serveur virtuel (il n'y a pas de couche de virtualisation supplémentaire comme docker). Une fonctionnalité de mise à jour automatique est disponible : après le démarrage, le conteneur demande la build la plus récente et, s'il en trouve une, il remplace l'ancienne version. Vous n'avez pas besoin d'effectuer la mise à jour manuellement.

Si vous créez manuellement une nouvelle machine virtuelle avec une nouvelle version, elle disposera de sa propre nouvelle base de données (la base de données MySQL interne fait partie de la machine virtuelle), il n'existe donc pas de moyen simple de transférer les connexions et les utilisateurs vers la nouvelle machine virtuelle.

{{< button href="https://azuremarketplace.microsoft.com/en-us/marketplace/apps/sprinxsystemsas1582034211947.dbgate_azure_vm?tab=Overview" style="blue" icon="fa-solid fa-arrow-up-right-from-square" >}}DbGate sur Azure{{< /button >}}
