---
title: Team Files
weight: 25
---

Team files are SQL, diagram or other files stored in DbGate internal storage. Desktop DbGate stores files in users folder, Team edition allows storing files in the same manner (in docker volume), but more appropriate is to store files in storage database, which is not recreated when DbGate container is recreated.

- Disk files 
    - files stored on disk or docker volume
    - unless you don't define docker volume explicitly (eg. in docker-compose.yaml), files are recreated when container is recreated.
- Team files 
    - files stored in storage database
    - are not lost when container is recreated, without need to define docker volume
    - allow to define fine-grained access permissions for users and roles

## Save SQL file as team file
When saving SQL file, just check "Save to team folder" checkbox. The file will be saved as team file. 