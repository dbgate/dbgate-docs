---
title: DbGate Cloud
weight: 35
---

DbGate cloud is online storage for your connections, SQL scripts and other objects. Also it offers public knowledge base for useful SQL scripts.

## Sign in
To use DbGate cloud, it is neccessary to sign in. Use {{< mdi "account-remove-outline" >}} icon in left panel.

Your cloud storage is always associated with your e-mail address.  
You could choose one of following authentization providers:
* GMail
* GitHub
* E-mail - one-time sign-in magic link will be sent to your email

DbGate servers don't store your password.

## Use connections stored on cloud
Your cloud content appears under {{< mdi "cloud-key" >}} widget after sign-in. By default, you see your Private folder (with write access).

Save connection to cloud:
* Connection context menu, choose "Copy to cloud folder"
* Click {{<mdi "plus-thick" >}}, the choose "Add connection on cloud"

## Which connection is stored on the cloud?
* Your cloud connections are always under {{< mdi "cloud-key" >}} widget
* Your locally stored connections under {{< mdi "database" >}} widget

## Working with folders
You could create next folders besides your Private folder (Premium edition needed).

Under {{<mdi "plus-thick" >}} button, there are commandsL
* New shared folder - creates new shared folder. By default, it is accessible only to you, you could invite next users
* Add existing shared folder - if you have invite link to some shared folder (created by different user), this is the right place to use it

If you want to share your folder with other people, right-click on folder and choose "Copy invite link"

## Shared folder permissions
* Admin - you have full access to folder, you could invite other people and write content
* Write - You could write/delete content, but you could not invite other people
* Read - only read content of folder. Please keep in mind, this permission doesn't apply databases available inside server defined connection

## Public knowledge base
Public knowledge base is a collection of useful SQL scripts and charts for tasks like SQL performance tuning, deadlock analysis, index usage etc... Knowledge base is available in all editions, but charts are available only in Premium editions.

You could see all items under {{< mdi "cloud-search" >}} icon in left widget panel.  
Grayed scripts denotes scripts, which are not compatible with currently selected database.

If you would like to enhance knowledge base with your SQL scripts, please create pull request into [dbgate-knowledge-base](https://github.com/dbgate/dbgate-knowledge-base) GIT repository.

Scripts in knowledge base are anotated with [SQL front matter](/sql-front-matter) syntax

![DbGate screenshot](https://media.dbgate.io/img/public-knowledge-base-tables-sizes-light.png)

