# Power Center Monitoring Firebase

Este programa permite recuperar datos de inversores de potencia y almacenarlos en una base de datos Firebase Realtime
Database. Está diseñado para ser ejecutado en un dispositivo como una Raspberry Pi, realizando peticiones periódicas a
los
inversores y actualizando la base de datos de Firebase con la información más reciente.

## Configuración Inicial

Para utilizar este programa, necesitarás realizar algunas configuraciones iniciales:

### Requisitos

- Python 3.x instalado en tu Raspberry Pi o en tu computadora.
- Acceso a internet para realizar peticiones a los inversores y para interactuar con Firebase.
- Una cuenta de Firebase y un proyecto configurado con Firebase Realtime Database.

### Instalación de Dependencias

Instala las dependencias necesarias ejecutando el siguiente comando en tu terminal:

```bash
pip install -r requirements.txt
```

Las dependencias requeridas están listadas en el archivo requirements.txt.

### Archivo de Configuración

Deberás crear un archivo `config.ini` en el directorio del programa con la siguiente estructura:

```ini
[DEFAULT]
SerialNos = [Lista de números de serie de los inversores, separados por comas]
FirebaseUserId = [Tu UID de usuario de Firebase]
FirebaseRealtimeDatabaseUrl = [URL de tu base de datos Firebase Realtime Database]
```

### Credenciales de Firebase

Deberás descargar el archivo de credenciales de Firebase (`credentials.json`) desde tu consola de Firebase y colocarlo
en el directorio del programa. Para obtener este archivo:

1. Ve a la [Consola de Firebase](https://console.firebase.google.com/) y selecciona tu proyecto.
2. Accede a la sección "Configuración del proyecto" (icono del engranaje).
3. Ve a la pestaña "Cuentas de servicio".
4. Haz clic en "Generar nueva clave privada" y descarga el archivo JSON resultante.

Este archivo contiene tus credenciales de administrador de Firebase y debe mantenerse seguro y privado.

## Uso del Programa

Una vez configurado, puedes ejecutar el programa con el siguiente comando:

```bash
python3 script.py
```

El programa realizará peticiones a los inversores especificados en config.ini y almacenará los datos en tu base de datos
Firebase bajo el FirebaseUserId proporcionado.

## Seguridad y Privacidad

Asegúrate de que tu archivo `config.ini` y `credentials.json` estén seguros y no sean accesibles públicamente, ya que
contienen información sensible. Nunca subas estos archivos a repositorios públicos o los compartas. Considera las
siguientes prácticas para mejorar la seguridad:

- Restringe los permisos de los archivos para que solo el usuario necesario tenga acceso de lectura.
- Utiliza variables de entorno o servicios de gestión de secretos para manejar las credenciales en entornos de
  producción.
- Revisa periódicamente tus políticas de seguridad en Firebase para asegurarte de que estén actualizadas y sean seguras.

## Mantenimiento y Actualizaciones

Es importante mantener el software actualizado y realizar mantenimientos periódicos para garantizar la seguridad y el
buen funcionamiento del sistema. Asegúrate de:

- Actualizar regularmente las dependencias del proyecto para incorporar correcciones de seguridad y mejoras.
- Probar cualquier cambio en un entorno de desarrollo antes de implementarlo en producción.
- Hacer copias de seguridad regulares de tu configuración y datos.

## Contribuciones

Si tienes sugerencias de mejoras o correcciones, eres bienvenido a contribuir al proyecto. Puedes hacerlo a través de '
issues' o 'pull requests' en el repositorio de GitHub. Agradecemos cualquier contribución que ayude a mejorar este
proyecto.

## Contacto y Soporte

Para soporte, preguntas o colaboraciones, no dudes en contactarme a través de [mariopastorlanchares@gmail.com] o a
través de los 'issues' en el repositorio de GitHub.

Agradecemos tu interés en este proyecto y esperamos que te sea de gran utilidad para la gestión y monitoreo de tus
inversores de potencia.

