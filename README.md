# Compresor de Texto

Este proyecto es una herramienta con interfaz gráfica para la compresión y descompresión de texto mediante un mapa de palabras almacenado en un archivo JSON. Es ideal para reducir el tamaño de archivos de texto y facilitar su manejo y almacenamiento.

## Características principales

1. **Compresión de texto**:
   - Transforma el texto original utilizando un mapa de palabras optimizado para reducir su tamaño.

2. **Descompresión de texto**:
   - Reconstruye el texto original a partir del archivo comprimido utilizando el mapa de palabras.

3. **Gestión de mapas de palabras**:
   - Generación de un archivo `JSON` con un mapa de palabras desde el script `bancoPalabras.py`.

4. **Interoperabilidad**:
   - El mapa de palabras en formato JSON puede ser utilizado por otros scripts o programas.

## Estructura del proyecto
```
compresorTxt/
├── bancoPalabras.py       # Script para generar el archivo mapa_palabras.json
├── compresor_texto.py     # Script principal para compresión y descompresión de texto
├── mapa_palabras.json     # Archivo JSON con el mapa de palabras
├── txt_original.txt       # Archivo de texto de prueba
└── pycache/               # Archivos compilados de Python
```

## Instalación

1. Clona este repositorio en tu máquina local:
   ```bash
   git clone https://github.com/alegria666/compresorTxt.git
   ```

2. Asegúrate de tener instalado Python en su última versión.

3. Instala las dependencias necesarias (si las hay, dependiendo del código).

## Uso

1. **Generar el mapa de palabras**

   Ejecuta el script `bancoPalabras.py` para generar el archivo `mapa_palabras.json` en caso de que no esté creado:
   ```bash
   python bancoPalabras.py
   ```

2. **Comprimir y descomprimir un archivo de texto**

   Usa `compresor_texto.py` para comprimir y descomprimir un archivo de texto a través de la interfaz gráfica:
   ```bash
   python compresor_texto.py
   ```

## Tecnologías utilizadas

- **Python 3.13**:
  - Manejo de archivos.
  - Manipulación de datos JSON.
  - Implementación de algoritmos de compresión y descompresión.

## Funcionalidades clave

### `bancoPalabras.py`
- Genera un archivo `mapa_palabras.json` con la correspondencia entre palabras y códigos comprimidos.
- Utiliza técnicas básicas de optimización para mapear palabras de uso frecuente.

### `compresor_texto.py`
- **Comprimir**: Reduce el tamaño de archivos de texto usando el mapa de palabras.
- **Descomprimir**: Restaura el texto original utilizando el mapa.

## Créditos
Desarrollado por Daniel Esteban Alegría Zamora como un proyecto de aprendizaje y optimización de manejo de texto.

