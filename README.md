# AgroNova 🌱

**Plataforma Inteligente para la Gestión y Optimización de Cultivos Agrícolas**

AgroNova es una aplicación web full-stack construida con [Reflex](https://reflex.dev) (Python) que permite a pequeños y medianos agricultores gestionar sus parcelas, cultivos, actividades agrícolas, inventario, finanzas y más. Incluye módulos de inteligencia artificial para detección de enfermedades y predicción de cosechas, con soporte offline para zonas rurales.

---

## Requisitos

- Python 3.11+
- pip

## Instalación y Ejecución

```bash
# 1. Crear y activar entorno virtual
python -m venv .venv
source .venv/Scripts/activate    # Windows
# source .venv/bin/activate       # Linux/Mac

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Inicializar base de datos y usuario de prueba
python seed.py

# 4. Ejecutar la aplicación
reflex run
```

La app estará disponible en `http://localhost:3000`

## Usuario de Prueba

| Campo       | Valor                |
|-------------|----------------------|
| Correo      | admin@agronova.com   |
| Contraseña  | admin123             |
| Rol         | administrador        |

## Seed de Base de Datos

Para resetear la base de datos:
```bash
rm db/agronova.db    # Windows: del db\agronova.db
python seed.py
```

## Estructura del Proyecto

```
AgroNova/
├── assets/             # Archivos estáticos (logo, imágenes)
├── db/                 # Base de datos SQLite
├── docs/               # Documentación del proyecto
├── IA/                 # Especificaciones de agente (historias, BD)
├── src/
│   ├── components/     # Componentes UI reutilizables
│   ├── models/         # Modelos de base de datos (17 tablas)
│   ├── pages/          # Páginas/rutas de la aplicación
│   └── states/         # Estados reactivos (lógica de negocio)
├── seed.py             # Script de inicialización de datos
├── rxconfig.py         # Configuración de Reflex
└── requirements.txt    # Dependencias del proyecto
```

## Stack Tecnológico

- **Framework**: Reflex 0.9.6 (full-stack Python)
- **Base de Datos**: SQLite + SQLModel (ORM)
- **Frontend**: Reflex components (Radix, Recharts, Lucide)

## Pruebas

Actualmente no hay suite de pruebas automatizada. Para probar manualmente:

```bash
# Iniciar la app
reflex run

# Abrir http://localhost:3000 en el navegador
# Iniciar sesión con admin@agronova.com / admin123
```
