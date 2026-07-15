---
sourceHash: fd6032a57cb859a0d8cb5046fde87de9bf1a85de56c66586391e84ecbbdc24c1
language: es
title: Desplegar en AWS
subtitle: Despliegue con un solo clic en un clúster de Amazon EC2
icon: aws.svg
weight: 10
demo_url: https://aws.amazon.com/marketplace/pp/prodview-glw7okfnhf4cy
demo_title: View on AWS
edition: 'premium'
---

DbGate AWS edition es una plataforma web colaborativa y multiusuario diseñada específicamente para la gestión de bases de datos dentro de Amazon Web Services (AWS). Aprovechando la infraestructura de AWS, agiliza el trabajo en equipo para las organizaciones que operan en entornos de nube. Su interfaz compartida basada en navegador simplifica la colaboración, el acceso a los datos y la supervisión de bases de datos, a la vez que se integra sin problemas con AWS.

{{< button href="https://aws.amazon.com/marketplace/pp/prodview-glw7okfnhf4cy" style="blue" icon="fa-solid fa-arrow-up-right-from-square" >}}DbGate en AWS{{< /button >}}

## Características principales de DbGate AWS
DbGate AWS admite las mismas características que DbGate Team Premium, pero está optimizado para AWS

* Compatibilidad con AWS IAM
* Administración de usuarios, conexiones y roles
* Exploración, filtrado y edición de datos
* Importación y exportación de datos
* Constructor visual de consultas

## Proceso de instalación
La instalación en AWS es muy sencilla, es un proceso de casi un solo clic.

Recomendamos el tipo de instancia t2.medium para obtener la mejor experiencia de usuario, pero t2.micro, disponible en la capa gratuita, será suficiente para un número reducido de usuarios.

Después de la instalación, debe establecer la contraseña de administrador; a continuación, podrá administrar conexiones, usuarios y roles, y conceder permisos.

## Suscripción y licencias
Puede suscribirse a DbGate AWS a través de AWS Marketplace, con precios basados en el tamaño de la instancia elegida. Las instancias más grandes admiten más usuarios simultáneos.

Una prueba gratuita de 30 días le da acceso a todas las características de DbGate. Después de la prueba, la facturación sigue el plan de precios de AWS según el tamaño de instancia seleccionado. No se requiere ninguna licencia adicional, ya que todos los pagos se gestionan a través de la suscripción de [AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-glw7okfnhf4cy).

## Actualizaciones de DbGate AWS
DbGate AWS tiene su compilación especial y se ejecuta directamente en un servidor virtual en EC2 (no hay ninguna capa de virtualización adicional como docker). Existe una funcionalidad de actualización automática: después del inicio, el contenedor solicita la compilación más reciente y, si la encuentra, sustituye la versión antigua. No tiene que actualizar manualmente.

Si crea manualmente un nuevo contenedor EC2 con una versión nueva, este tendrá su propia base de datos nueva (la base de datos interna MySQL forma parte del contenedor), por lo que no hay una forma sencilla de trasladar las conexiones y los usuarios al nuevo contenedor EC2.

{{< button href="https://aws.amazon.com/marketplace/pp/prodview-glw7okfnhf4cy" style="blue" icon="fa-solid fa-arrow-up-right-from-square" >}}DbGate en AWS{{< /button >}}
