---
title: Data archives
weight: 1
---

Archives are folders with data in JSONL (NDJSON) format. DbGate allows work with them very efficiently, you could import them into database, export them to other formats or directly edit data in archive. Archive behaves as a very fast and lighweight database stored in local files.

## JSONL format
DbGate uses JSONL format internally everywhere. JSONL is text file, where every line contains JSON stringified row. DbGate assumes, that first line could contain header (also as JSON), with table structure. When you use JSONL with dynamic structure (without first fixed line), this format is standardized and could be loaded into many other tools. 

## Archive folders
Archive is organized into folders, with JSONL files. It has similar structure as database. You could than export whole database into new archive - every table is exported into one JSON file, thanks to header line, table structure is also persisted.

## View and edit archive files
You could open JSONL files in different modes:
- context menu "Open" - opens data grid, which allows sorting, filtering and editing your JSONL data
- context menu "Open in text editor" - allows manualy editing JSONL file

## Archives and DB models
Archive folders are also used as storage for DB models. You could export DB model in database context menu, "Export DB model". You could than edit this model (YAML files for table structure, SQL files for views and stored procedures), compare it with real database and deploy it into database
