# Arquitectura y Flujo del Proyecto SpaceTraders CLI

Este documento detalla la arquitectura, el flujo de datos y el proceso de despliegue/uso del proyecto `spacetraders-cli`.

## 1. Arquitectura del Sistema

El proyecto sigue los principios de **Arquitectura Limpia (Clean Architecture)** y **Arquitectura Hexagonal**, organizando el código en capas desacopladas para facilitar el mantenimiento y las pruebas.

### Capas del Proyecto (`src/`)

#### A. Dominio (`src/traders/domain/`)
Es el corazón del negocio. No depende de ninguna otra capa.
- **Entidades (`entities/`)**: Clases que representan los objetos de negocio (Ship, Contract, Account, etc.). Incluyen métodos de factoría como `from_dict` y `from_list` para transformar datos JSON de la API en objetos de dominio.
- **Interfaces (`interfaces.py`)**: Define los contratos (clases abstractas) que deben cumplir los servicios y casos de uso. Asegura que la lógica de negocio no dependa de implementaciones concretas.
- **Constantes (`constants.py`)**: Configuración global, URLs de la API y gestión de cabeceras de autenticación usando variables de entorno.

#### B. Aplicación (`src/traders/application/`)
Contiene la lógica de negocio específica de la aplicación.
- **Casos de Uso (`use_cases/`)**: Implementaciones de acciones específicas (ej. `ContractAccepter`) que orquestan el flujo de datos entre el dominio y la infraestructura.

#### C. Infraestructura (`src/traders/infraestructure/`)
Implementa los detalles técnicos y herramientas externas.
- **Servicios (`services/`)**: Implementación de las interfaces de dominio. `SpaceTradersService` utiliza la librería `requests` para comunicarse con la API de SpaceTraders.

#### D. Presentación (`src/cli_textual/` y `main.py`)
La interfaz de usuario y cómo se muestran los datos.
- **Presenters (`presentation/presenters/`)**: Transforman los objetos de dominio en cadenas de texto formateadas o estructuras listas para ser mostradas en la UI.
- **Widgets (`domain/widgets/`)**: Componentes personalizados de la interfaz (ej. `CustomFormWidget` para Textual).
- **Entry Point (`main.py`)**: Configura e inicia la aplicación **Textual**. Define las pantallas (`Screens`) y maneja los eventos de usuario (clics de botones, entradas de teclado).

---

## 2. Flujo de Ejecución

El flujo típico de una acción (ej. "Aceptar Contrato") es:

1. **Usuario**: Presiona un botón en la interfaz Textual (`main.py`).
2. **Presentación**: El método `on_button_pressed` detecta el evento.
3. **Servicio/Caso de Uso**: Se llama a un método de `TradersService` (inyectado como `SpaceTradersService`) o se ejecuta un `UseCase`.
4. **Infraestructura**: `SpaceTradersService` realiza una petición HTTP a `api.spacetraders.io`.
5. **Dominio**: La respuesta JSON se convierte en una **Entidad** de dominio.
6. **Presentación**: Un **Presenter** toma la entidad, la formatea y la envía al widget de `Log` para mostrarla al usuario.

---

## 3. Despliegue y Uso Correcto

### Requisitos Previos
- Python 3.10 o superior.
- [uv](https://github.com/astral-sh/uv) (recomendado para gestión de paquetes y entornos virtuales).
- Una cuenta y un token de [SpaceTraders.io](https://spacetraders.io/).

### Configuración de Variables de Entorno
Crea un archivo `.env` en la raíz del proyecto con tu token de API:
```env
SPACETRADERS_TOKEN=tu_token_aqui
```

### Instalación
Si usas `uv`:
```bash
uv sync
```
Esto instalará todas las dependencias listadas en `pyproject.toml` (textual, requests, python-dotenv, etc.).

### Ejecución
Para iniciar la interfaz CLI:

dentro de la carpeta principal spacetraders-cli
```bash
uv run python main.py
```
O si prefieres usar el entorno virtual estándar:
```bash
source .venv/bin/activate
python main.py
```

### Uso de la Interfaz
- **Show Contract**: Lista los contratos actuales del jugador.
- **Accept Contract**: Acepta el primer contrato disponible.
- **View Available Ships**: Muestra los barcos que se pueden comprar en el astillero local.
- **Orbit/Navigate/Extract**: Funciones para manejar la navegación y minería de las naves (algunas requieren completar campos en el formulario superior).

---

## 4. Estándares y Convenciones
- **Tipado**: Se utiliza `typing` de Python (ej. `list[Contract]`) para asegurar la consistencia.
- **Manejo de Errores**: El servicio lanza `ValueError` ante fallos de la API, los cuales deberían ser capturados en la capa de presentación (pendiente de robustez en algunas secciones).
- **Estilos**: Los estilos visuales de la interfaz se definen en `styles.tcss`.

# FRONTEND
- cd ..spacetraders-cli/frontend
- uv run reflex run

