---
sourceHash: 4f9596eb7ab62bc22f186ebb87b019eb2986c18eb704368b8634ffc2cd471482
language: es
title: Desplegar en Azure
weight: 20
---

DbGate Azure edition es una plataforma web colaborativa y multiusuario diseñada específicamente para la gestión de bases de datos dentro de Azure. Al aprovechar la infraestructura de Azure, agiliza el trabajo en equipo para las organizaciones que operan en entornos de nube. Su interfaz compartida basada en navegador simplifica la colaboración, el acceso a los datos y la supervisión de bases de datos, a la vez que se integra a la perfección con Azure.

{{< button href="https://azuremarketplace.microsoft.com/en-us/marketplace/apps/sprinxsystemsas1582034211947.dbgate_azure_vm?tab=Overview" style="blue" icon="fa-solid fa-arrow-up-right-from-square" >}}DbGate en Azure{{< /button >}}


## Características principales de DbGate Azure
DbGate Azure admite las mismas características que DbGate Team Premium, pero está optimizado para Azure

* Admite la identidad administrada de Azure
* Administración de usuarios, conexiones y roles
* Exploración, filtrado y edición de datos
* Importación y exportación de datos
* Constructor visual de consultas

## Proceso de instalación
La instalación en Azure es muy sencilla, es prácticamente un proceso de un solo clic.

Recomendamos máquinas virtuales con 2 GB de RAM.

Después de la instalación, debe establecer la contraseña de administrador; a continuación, podrá administrar conexiones, usuarios, roles y conceder permisos.

## Suscripción y licencias
Puede suscribirse a DbGate Azure a través de Azure Marketplace, con precios basados en el número de procesadores de la máquina virtual elegida.

Una prueba gratuita de 30 días le da acceso a todas las características de DbGate. Después de la prueba, la facturación sigue el plan de precios de Azure según el tamaño de la instancia seleccionada. No se requiere ninguna licencia adicional, ya que todos los pagos se gestionan a través de la suscripción de [Azure Marketplace](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/sprinxsystemsas1582034211947.dbgate_azure_vm?tab=Overview).

## Actualizaciones de DbGate Azure
DbGate Azure tiene su compilación especial y se ejecuta directamente en el servidor virtual (no hay ninguna capa de virtualización adicional como docker). Existe una funcionalidad de actualización automática: después del inicio, el contenedor solicita la compilación más reciente y, si la encuentra, reemplaza la versión antigua. No tiene que actualizar manualmente.

Si crea manualmente una nueva máquina virtual con una nueva versión, tendrá su propia base de datos nueva (la base de datos MySQL interna forma parte de la máquina virtual), por lo que no hay una forma sencilla de trasladar las conexiones y los usuarios a la nueva máquina virtual.

{{< button href="https://azuremarketplace.microsoft.com/en-us/marketplace/apps/sprinxsystemsas1582034211947.dbgate_azure_vm?tab=Overview" style="blue" icon="fa-solid fa-arrow-up-right-from-square" >}}DbGate en Azure{{< /button >}}
