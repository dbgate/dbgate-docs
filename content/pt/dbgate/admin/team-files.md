---
sourceHash: 8396e36170a2f74ec485cc366db64869390b971ebf497d3127e7005ee1837c1d
language: pt
title: Arquivos de Equipe
weight: 25
---

Arquivos de equipe são arquivos SQL, de diagrama ou outros armazenados no armazenamento interno do DbGate. O DbGate Desktop armazena os arquivos na pasta do usuário, e a edição Team permite armazenar arquivos da mesma maneira (em um volume do docker), mas o mais apropriado é armazenar os arquivos no banco de dados de armazenamento, que não é recriado quando o contêiner do DbGate é recriado.

- Arquivos em disco
    - arquivos armazenados em disco ou em volume do docker
    - a menos que você defina explicitamente um volume do docker (por exemplo, no docker-compose.yaml), os arquivos são recriados quando o contêiner é recriado.
- Arquivos de equipe
    - arquivos armazenados no banco de dados de armazenamento
    - não são perdidos quando o contêiner é recriado, sem a necessidade de definir um volume do docker
    - permitem definir permissões de acesso detalhadas para usuários e funções

## Salvar arquivo SQL como arquivo de equipe
Ao salvar um arquivo SQL, basta marcar a caixa de seleção "Save to team folder". O arquivo será salvo como arquivo de equipe.
