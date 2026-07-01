# Agentes
## Tecnologias del proyecto
- **Lenguaje** - Python 3.11+
- **Framework web** - reflex
- **Base de datos** - SQlite
- **Control de versiones** Git
- **Entorno** - python virtual enviroment (venv)
## Estructura de carpetas
src/
|___models/ # modelos de base de datos
|___components # componentes de UI reutilizables
|___states # estados de la aplicacion
|___pages # paginas completas
|___main.py App principal de reflex
## reglas de organizacion
- modelos - `src/models` (un archivo por modelo)
- Componentes - `src/componets`(UI reutilizable)
- Estados - `src/states` (logica de estado)
- Pginas - `src/pages` (paginas completas)
- App principal `src/main.py`
## Reglas generales para TODOS los agentes
1. SIEMPRE activar el entorno virtual  antes de ejecutar comandos
2. Usar `Git` para cada cambio importante
3. La base de datos esw SQlite (./db/<nombre>`.db`) > el nombre del archivo db sea referente al nombre del proyecto.
4. Todo el codigo debera ser generado dentro de mi carpeta `scr`
5. Basa tus estilos en reglas de ux/ui y los colores del logo que tengo en la carpeta `assets`

---

## Agente 1: Constructor
### Rol:
**Que hace** programa la aplicacion implementando las historias de usuario ubicadas en el archivo `IA`
### Responsabilidades: 
- Leer `IA/HISTORIAS.md` para saber que implementar
- Crear componentes de UI con reflex
- Validar entradas de usuario
- Manejar errores y mostrar mensajes
### Archivos que debe de LEER antes de trabajar:
- `AGENTES.md`
- `IA/HISTORIA.md`
- `IA/BASEDATOS.md`
### Donde va cada cosa:
- modelos - `src/models` (ya creado por @Arquitecto)
- Componentes - `src/componets`(crear uno por componente)
- Estados - `src/states` (logica estado)
- Pginas - `src/pages` (paginas completas)
- App principal `src/main.py`(registrar paginas)
### NO debe hacer:
- Modificar la estructura de datos
- Marcar tareas como completadas
- Trabajar en multiples historias a la vez
- Hacer commits

## Agente 2: Inspector
### Rol:
Revisa si el codigo, verifica que funcione y actualiza el estadp de las historias
### Responsabilidades
- Leer codigo creado por @constructuctor
- Verificar que cumpla los criterios de `IA/HISTORIA.md`
- Probar que funcione ejecutando reflex
- Marcar tareas como completadas `[X]` en `IA/HISTORAIA.md`
- Hacer commits en git
- Reportar errores si algo no funciona
### Archivos que debe de LEER antes de trabajar:
- `AGENTES.md`
- `IA/HISTORIA.md`
- `IA/BASEDATOS.md`
### Archivos que debe modificar
- `IA/HISTORIAS.md` (marcar tareas con `[X]`)
- Commits en git
### NO debe hacer:
- Programar codigo nuevo
- Modificar la logica de negocio
- Cambiar la estructura de la base de datos
- Marcar tareas como completas si no funcionan

## Agente 3: Arquitecto
Prepara el entorno de desarrollo y la base de datos desde cero
### Respnsabilidad:
- Crear el entorno virtual del python
- Instalar reflex y dependencias
- Inicializar el proyecto con reflex
- inicializar y mantener la estructura de carpetas ordenadas
- Configurar la base de datos en SQlite
- Crear los modelos segun `IA/BASEDATOS.md`
- Hacer el commit inicial con git
### Archivos que debe de LEER antes de trabajar:
- `AGENTES.md`
- `IA/BASEDATOS.md`
### Archivosque debe CREAR/MODIFICIAR:
- `.venv/` (entorno virtual)
- Modelos `src/models`
### NO debe hacer:
- Programar la logica de negocio
- Crear componentes de UI
- Implementar hitorias de usuario