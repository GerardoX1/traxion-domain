# traxion-domain

**Traxion Domain Python** es una librería (conjunto de entidades y servicios) que encapsula funciopnes recuerrentes de dominio del proyecto Traxion. Su propósito principal es proporcionar modelos y funcionalidades core para gestionar autos,y demás conceptos de negocio relacionados con Traxion.

## Características

- **Modelos de Dominio**: Modelos Pydantic para representar y validar las entidades principales (por ejemplo, vehiculos, mantenimiento, etc.).
- **Servicios**: Funciones o clases que manipulan entidades.
- **Fácil Integración**: Diseñada para ser usada en proyectos que requieran la lógica de Traxion sin necesidad de duplicar código.

## Requisitos

- Python 3.11 o superior
- [Pydantic](https://docs.pydantic.dev/) (versión especificada en el `pyproject.toml`)

## Instalación

Si estás usando `pyproject.toml`, puedes instalarlo con:

```bash
pip install .
```

Para instalar con las dependencias de desarrollo (por ejemplo, pytest, pytest-mock):
```bash
pip install .[dev]
```

instalacion de libreria en un repositorio PyPI privado o en un índice público
```bash
pip install traxion-domain
```

## Uso (ejemplo básico)

```python
from traxion.models.v1.cars import CarModel, RoleTypes

# Create Car
car = CarModel(
    display_name="Gerardo F",
    disabled=False,
    phone_number="1234567890",
    roles=[RoleTypes.ADMIN]
)

# Acceder a los campos
print(car.display_name)  # Gerardo F
print(car.roles)         # [RoleTypes.ADMIN]
```
## Integración en otro proyecto

Instala la librería (ver sección de "Instalación").
Importa los modelos y/o servicios en tu proyecto.
Utiliza los modelos para validar datos de entrada/salida en tus endpoints o servicios.

## Estructura del Proyecto
```
traxion-domain/
├── traxion/
│   ├── models/
│   │   ├── base_models/
│   │   │   ├── base_model.py
│   │   │   ├── ...
│   │   └── v1/
│   │       └── users.py
│   └── services/
│       └── ...
├── pyproject.toml
├── README.md
├── tests/
│   └── ...
```

## Testing
Para ejecutar la suite de pruebas:
```bash
pytest
```

## Soporte
Si encuentras problemas o tienes preguntas, abre un issue en el repositorio o contactame en yeralway1@gmail.com