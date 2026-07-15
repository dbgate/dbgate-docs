---
sourceHash: 8396e36170a2f74ec485cc366db64869390b971ebf497d3127e7005ee1837c1d
language: fr
title: Fichiers d'équipe
weight: 25
---

Les fichiers d'équipe sont des fichiers SQL, des diagrammes ou d'autres fichiers stockés dans le stockage interne de DbGate. La version bureau de DbGate stocke les fichiers dans le dossier de l'utilisateur ; l'édition Team permet de stocker les fichiers de la même manière (dans un volume docker), mais il est plus approprié de les stocker dans la base de données de stockage, qui n'est pas recréée lorsque le conteneur DbGate est recréé.

- Fichiers sur disque
    - fichiers stockés sur disque ou dans un volume docker
    - si vous ne définissez pas explicitement un volume docker (par ex. dans docker-compose.yaml), les fichiers sont recréés lorsque le conteneur est recréé.
- Fichiers d'équipe
    - fichiers stockés dans la base de données de stockage
    - ne sont pas perdus lorsque le conteneur est recréé, sans qu'il soit nécessaire de définir un volume docker
    - permettent de définir des autorisations d'accès précises pour les utilisateurs et les rôles

## Enregistrer un fichier SQL en tant que fichier d'équipe
Lors de l'enregistrement d'un fichier SQL, il suffit de cocher la case « Save to team folder ». Le fichier sera enregistré en tant que fichier d'équipe.
