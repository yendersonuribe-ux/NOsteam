# NOsteam

## Descripción del proyecto

NOsteam es una aplicación web de una tienda de videojuegos desarrollada en Python utilizando el framework Flet. Su interfaz está inspirada en las plataformas digitales de distribución de videojuegos y permite explorar un catálogo, consultar información de los juegos y administrar un carrito de compras.

El proyecto tiene como objetivo aplicar conocimientos de programación y desarrollo de interfaces mediante una aplicación interactiva.

## Características principales

- **Catálogo de videojuegos:** muestra los juegos disponibles con sus imágenes, nombres, géneros, precios y descripciones.
- **Búsqueda:** permite localizar videojuegos por su nombre.
- **Filtros por género:** facilita la exploración del catálogo según el género de los juegos.
- **Detalles de los videojuegos:** permite consultar información individual de cada título.
- **Carrito de compras:** permite agregar juegos, evitar duplicados, eliminar artículos y calcular el importe total.
- **Navegación:** incluye las secciones Home, Store, News, Community y Cart.
- **Interfaz visual:** utiliza imágenes y componentes interactivos para presentar el contenido.

## Tecnologías utilizadas

- **Python:** lenguaje de programación principal.
- **Flet:** framework utilizado para desarrollar la interfaz de usuario.
- **uv:** herramienta para gestionar el entorno y las dependencias del proyecto.
- **Tecnologías web:** permiten ejecutar la interfaz de Flet en un navegador.

## Requisitos

- Python compatible con las dependencias definidas en el proyecto.
- uv instalado.
- Un navegador web actualizado.
- Los archivos del proyecto, incluida la carpeta `assets` con los recursos gráficos.

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
│       ├── game.py
│       └── cart.py
├── pyproject.toml
├── uv.lock
├── .gitignore
└── README.md
```

## Descripción de los archivos

- **`main.py`:** contiene la lógica principal de la aplicación, la interfaz, la navegación, el catálogo y la integración del carrito.
- **`game.py`:** define la clase `Game`, utilizada para representar cada videojuego y almacenar sus datos.
- **`cart.py`:** define la clase `Cart`, encargada de administrar los juegos seleccionados y calcular el total del carrito.
- **`assets/`:** contiene las imágenes utilizadas para las portadas de los videojuegos.
- **`pyproject.toml`:** contiene la configuración del proyecto y sus dependencias.
- **`uv.lock`:** registra las versiones resueltas de las dependencias.
- **`.gitignore`:** especifica los archivos y carpetas que deben excluirse del control de versiones.
- **`README.md`:** contiene la documentación principal del proyecto.

## Instalación y ejecución

1. Instalar Python y uv.
2. Abrir una terminal en la carpeta raíz del proyecto.
3. Sincronizar las dependencias:

```powershell
uv sync
```

4. Iniciar la aplicación en el navegador:

```powershell
uv run flet run --web --assets ..\..\assets .\src\nosteam\main.py
```

La carpeta `assets` debe conservar su ubicación en la raíz del proyecto para que el comando de ejecución encuentre correctamente los recursos gráficos.

## Funcionamiento general

Al iniciar NOsteam, el usuario puede explorar el catálogo de videojuegos y utilizar la búsqueda o los filtros por género para encontrar títulos. También puede abrir la página de detalles de cada juego y agregarlo al carrito.

Dentro del carrito, puede consultar los juegos seleccionados, retirar artículos y revisar el importe total. La navegación permite regresar a la tienda y acceder a las secciones informativas de noticias y comunidad.

## Limitaciones actuales

- El carrito se mantiene en memoria durante la ejecución y no se conserva permanentemente al cerrar la aplicación.
- No se encuentra implementado un proceso de compra o pago real.
- Las secciones de noticias y comunidad son informativas y no cuentan con todas las funcionalidades de una plataforma real.
- El catálogo está definido en el código y no utiliza una base de datos.

## Estado del proyecto

NOsteam es una aplicación funcional de una tienda web de videojuegos que incorpora navegación, consulta de información, búsqueda, filtros y gestión básica de un carrito de compras.

Su estructura permite ampliar las funcionalidades y mejorar la organización del sistema en futuras versiones.

## Autor

Yenderson Uribe