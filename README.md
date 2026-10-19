# NOsteam

## Descripción del proyecto

NOsteam es una aplicación web de una tienda de videojuegos desarrollada en Python utilizando el framework Flet. Su interfaz está inspirada en las plataformas digitales de distribución de videojuegos y permite explorar un catálogo, consultar información de los juegos y administrar un carrito.

El proyecto tiene como objetivo aplicar conocimientos de programación y desarrollo de interfaces mediante una aplicación interactiva.

## Características principales

- **Catálogo de videojuegos:** muestra los juegos disponibles con sus imágenes, nombres, géneros, precios y descripciones.
- **Búsqueda:** permite localizar videojuegos por su nombre.
- **Filtros por género:** facilita la exploración del catálogo según el género de los juegos.
- **Detalles de los videojuegos:** permite consultar información individual de cada título.
- **Carrito:** permite agregar juegos, evitar duplicados, eliminar artículos y calcular el importe total.
- **Navegación:** incluye las secciones Home, Store, News, Community y Cart.
- **Interfaz visual:** utiliza imágenes y componentes interactivos para presentar el contenido.

## Tecnologías utilizadas

- **Python:** lenguaje de programación principal.
- **Flet:** framework para construir la interfaz de usuario.
- **uv:** herramienta de gestión del entorno y las dependencias del proyecto.
- **HTML y tecnologías web:** Flet utiliza tecnologías web para mostrar la aplicación en el navegador.

## Requisitos

- Python 3.14 o una versión compatible con la configuración del proyecto.
- uv instalado.
- Un navegador web actualizado.
- Los archivos del proyecto y la carpeta de recursos gráficos `assets`.

## Estructura del proyecto

```text
NOsteam/
├── assets/
│   ├── Melda.png
│   ├── boosborne.png
│   ├── falos.png
│   └── walcra III silla helada.png
├── src/
│   └── nosteam/
│       ├── __init__.py
│       ├── main.py
│       └── game.py
├── pyproject.toml
├── uv.lock
├── .gitignore
└── README.md
```

### Descripción de los archivos

- `main.py`: contiene la lógica principal de la aplicación, la interfaz, la navegación, el catálogo y las operaciones del carrito.
- `game.py`: define la clase `Game`, utilizada para representar cada videojuego y almacenar sus datos.
- `assets/`: contiene las imágenes utilizadas para las portadas de los juegos.
- `pyproject.toml`: especifica los datos del proyecto y sus dependencias.
- `uv.lock`: registra las versiones resueltas de las dependencias.
- `.gitignore`: indica qué archivos o carpetas deben excluirse del control de versiones.
- `README.md`: contiene la documentación principal del proyecto.

## Instalación y ejecución

1. Instalar Python y uv.
2. Abrir una terminal en la carpeta raíz del proyecto.
3. Instalar o sincronizar las dependencias ejecutando:

```powershell
uv sync
```

4. Iniciar la aplicación en el navegador con el siguiente comando:

```powershell
uv run flet run --web --assets ..\..\assets .\src\nosteam\main.py
```

La carpeta `assets` debe conservar su ubicación junto a `pyproject.toml` para que la ruta de recursos funcione correctamente con el comando indicado.

## Funcionamiento general

Al iniciar NOsteam, el usuario puede acceder al catálogo y explorar los videojuegos disponibles. Puede utilizar la búsqueda o los filtros para encontrar títulos, abrir sus páginas de detalles y agregarlos al carrito.

Dentro del carrito, puede revisar los artículos seleccionados, retirar juegos y consultar el importe total calculado a partir de sus precios. La navegación permite regresar al catálogo y consultar las secciones informativas de la aplicación.

## Limitaciones actuales

- El carrito se mantiene en memoria durante la ejecución y no se conserva permanentemente al cerrar la aplicación.
- No se encuentra implementado un proceso de compra o pago real.
- Las secciones informativas no constituyen un sistema completo de noticias o comunidad.
- El catálogo está definido dentro del código y no utiliza una base de datos.

## Estado del proyecto

NOsteam constituye una versión funcional de una tienda web de videojuegos con navegación, consulta de información y gestión básica de un carrito. Su estructura permite ampliar posteriormente las funcionalidades y mejorar la organización del sistema.

## Autor

Yenderson Uribe
