---
title: API Connections
weight: 10
aliases:
  - /api-connections/
---

DbGate supports connections to REST APIs, GraphQL services, and OData endpoints. These API connections use the same interface patterns as database connections, allowing you to work with APIs and databases in a unified environment.

API connection support is available in DbGate Premium.

> Looking for API browsing without the desktop app? [DbGate Central](/dbgate-products/dbgate-central/connecting-to-api-endpoints/) is a separate, hosted implementation of GraphQL/oData/Shopify connections, reimplemented from the ground up for the browser.

## GraphQL

GraphQL connections allow you to interact with GraphQL APIs. DbGate provides schema introspection and query execution capabilities.

### Creating a GraphQL connection

To create a GraphQL connection, use the New Connection dialog and select GraphQL as the connection type. Enter the GraphQL endpoint URL and configure authentication if required.

### Schema introspection

DbGate automatically discovers the GraphQL schema, including available types, queries, mutations, and their arguments. The schema browser displays the type system and allows you to explore the API structure.

### Query editor

The GraphQL query editor allows you to write queries and mutations. You can use the GraphQL explorer to build queries by selecting fields and arguments from the schema.

![screenshot](https://media.dbgate.io/img/rest-graphql-query-light.png)

### Variables

GraphQL queries support variables. Define variables in the variables panel and reference them in your queries using the standard GraphQL variable syntax. Variables could be edited in a form or as raw JSON.

### Response viewer

Query results are displayed in a formatted JSON viewer with an expandable tree structure. If arrays are detected in the response, tabular view is displayed automatically. You can switch back to the raw JSON view if needed.

## OpenAPI (Swagger)

OpenAPI connections support REST APIs that provide OpenAPI specifications (versions 2.0 and 3.0).

### Creating an OpenAPI connection

Create a new connection and select OpenAPI as the connection type. Provide the URL to the OpenAPI specification file (typically swagger.json or openapi.json). DbGate will parse the specification and make available all documented endpoints.

### API documentation browser

The OpenAPI browser displays all available endpoints, organized by tags and paths. For each endpoint, you can view:
- HTTP method (GET, POST, PUT, DELETE, PATCH)
- Parameters (path, query, header, body)
- Request body schemas
- Documentation descriptions

### Request execution

Select an endpoint to open the request builder. Fill in required parameters, headers, and request body. Execute the request to send it to the API server.

![screenshot](https://media.dbgate.io/img/rest-openapi-query-light.png)

### Response inspection

View the response status code, headers, and body. JSON responses are formatted and can be displayed in both tree and table views. Non-JSON responses are displayed as text.

## OData

OData connections support querying OData services using standard OData query syntax.

### Creating an OData connection

Create a new connection with OData as the connection type. Enter the OData service root URL. DbGate will retrieve the service metadata document.

### Metadata exploration

The metadata browser shows available entity sets, entity types, properties, and relationships defined in the service metadata.

### Query execution

OData queries support standard OData query options:
- `$filter` - filter entities by property values
- `$select` - specify which properties to return
- `$expand` - include related entities
- `$orderby` - sort results
- `$top` and `$skip` - pagination
- `$count` - include result count

![screenshot](https://media.dbgate.io/img/rest-odata-query-light.png)

Results are displayed in tabular format, similar to database query results.

## Authentication

All API connection types support multiple authentication methods:

- **API Key** - specify key name and value, sent as header or query parameter
- **Bearer Token** - OAuth or JWT tokens sent in Authorization header
- **Basic Authentication** - username and password using HTTP Basic Auth
- **No Authentication** - for public APIs

Configure authentication in the connection properties.

## Data export

API response data can be exported to various formats using the standard DbGate export functionality:
- JSON
- CSV
- Excel
- SQL INSERT statements
- XML

Use the standard "Export" context menu option in tabular data browser.

## Working with multiple APIs

You can create connections to multiple APIs and databases. Open multiple request tabs to work with different endpoints simultaneously.

Tab state is preserved after closing and reopening app, you could reopen a request in closed tab history.