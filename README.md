![image](https://github.com/marcosstgo/heictojpg/assets/50328367/10a8e0e3-8c9a-45c8-9c1a-1f1df3809df8)


### Dependencias

Este programa requiere las siguientes dependencias para funcionar correctamente:

- **Python**: Asegúrate de tener Python instalado en tu sistema. Este programa es compatible con Python 3.x. Puedes descargarlo desde [python.org](https://www.python.org/downloads/).
- **Tkinter**: Usado para la interfaz gráfica de usuario. Tkinter generalmente viene preinstalado con las distribuciones estándar de Python. Si no está instalado, puedes añadirlo utilizando el gestor de paquetes de tu sistema operativo o mediante pip:

  ```bash
  pip install tk
  ```

- **ImageMagick**: Necesario para la conversión de imágenes de HEIC a JPG. Debes instalar ImageMagick en tu sistema y asegurarte de que el ejecutable `magick` está accesible desde el PATH.

### Instalación de ImageMagick

Para que el programa funcione, debes instalar ImageMagick. Aquí te muestro cómo puedes instalarlo y configurarlo en Windows:

1. **Descargar ImageMagick**:
   - Ve a la [página de descargas de ImageMagick](https://imagemagick.org/script/download.php).
   - Descarga la versión apropiada para tu sistema operativo (asegúrate de elegir una versión que incluya soporte para archivos HEIC/HEIF si está disponible).

2. **Instalar ImageMagick**:
   - Ejecuta el instalador descargado.
   - Durante la instalación, asegúrate de seleccionar la opción para añadir ImageMagick al PATH de tu sistema. Esto es esencial para que el programa pueda invocar `magick` directamente desde la línea de comandos.

3. **Verificar la Instalación**:
   - Abre una ventana de comando y escribe `magick -version` para verificar que ImageMagick se ha instalado correctamente y que el comando `magick` está disponible en el PATH.

### Ejecución del Programa

Una vez instaladas las dependencias, puedes ejecutar el programa de la siguiente manera:

- **Clonar el Repositorio**:
  ```bash
  git clone https://github.com/marcosstgo/heictojpg.git
  ```
- **Navega al directorio del proyecto**:
  ```bash
  cd heictojpg
  ```
- **Iniciar el Programa**:
  ```bash
  python heictojpg.py
  ```

### Nota Adicional

Si encuentras errores relacionados con la ubicación de ImageMagick en tu sistema, verifica la ruta especificada en el script y ajusta la variable `magick_path` dentro de `convert_heic_to_jpg` para que coincida con la ruta de instalación de ImageMagick en tu máquina.
