---
sourceHash: d544deb1088946415d8fae3a2b5da3de8bee338a8dfe25d4d99541b1252b56c5
language: es
title: Autenticación
weight: 10
---

## Pestaña Authentication
Existen varios métodos de autenticación. El usuario elegirá el método de autenticación en la página de inicio de sesión. Si solo tiene habilitado un método de autenticación y este no requiere página de inicio de sesión, dicha página se omite.

![Administración de la autenticación - DbGate](https://media.dbgate.io/img/authentication-administration-light.png)

- Método de autenticación local: el usuario se selecciona de la lista de usuarios de la base de datos de almacenamiento (configurada en la pestaña "Users")
- Anonymous: no se requieren credenciales, el usuario tiene los permisos del rol "anonymous-user"
- Use database login: las credenciales se redirigen al servidor de base de datos. El usuario elegirá la conexión en la pestaña "Connections"
- OAuth 2.0: proveedor OAuth genérico. Con un poco de esfuerzo y los conocimientos adecuados, puede configurarse con la mayoría de los proveedores de identidad actuales, como Google, Facebook o Keycloak
- Active Directory: acceso a AD mediante el protocolo LDAP
- Microsoft Entra: anteriormente Azure Active Directory, acceso de inicio de sesión único a bases de datos de Azure

### Opción "Allow only defined logins"
En el caso de los proveedores de identidad externos, el usuario no tiene que existir en la base de datos de almacenamiento de DbGate. Si esta casilla está marcada, un usuario que no se encuentre en la base de datos de almacenamiento no podrá iniciar sesión

### Keycloak

Keycloak se puede integrar con DbGate utilizando el proveedor genérico de OAuth 2.0. Para configurar la autenticación con Keycloak, debe:

1. Crear un nuevo cliente en su realm de Keycloak
2. Configurar los ajustes del cliente
3. Configurar el proveedor de OAuth 2.0 en DbGate con los siguientes parámetros:

**Configuración obligatoria:**
- **OAuth auth endpoint**: `https://keycloak.company.com/realms/your-realm/protocol/openid-connect/auth`
- **OAuth token endpoint**: `https://keycloak.company.com/realms/your-realm/protocol/openid-connect/token`
- **OAuth logout endpoint**: `https://keycloak.company.com/realms/your-realm/protocol/openid-connect/logout`
- **OAuth client**: el ID de cliente de Keycloak
- **OAuth login field**: el claim de Keycloak que contiene el identificador de inicio de sesión del usuario (habitualmente `preferred_username`; según la configuración de su Keycloak, también puede usar `given_name`, `email` u otro claim adecuado)

**Configuración del cliente de Keycloak:**
- Valid Redirect URIs: `https://dbgate.company.com/`

Asegúrese de que los atributos de usuario de Keycloak estén correctamente mapeados para proporcionar los claims necesarios (email, name, username) que DbGate espera del proveedor de OAuth.


