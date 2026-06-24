## Problema a resolver

Muchos agricultores llevan el control de sus cultivos de forma manual, lo que dificulta:

* Registrar actividades agrícolas.
* Controlar gastos y ganancias.
* Monitorear el estado de los cultivos.
* Planificar riegos y fertilizaciones.
* Detectar problemas a tiempo (plagas, enfermedades, falta de agua).

## Objetivo general

Desarrollar una plataforma web y/o móvil que permita gestionar, monitorear y optimizar la producción agrícola mediante el registro y análisis de información de los cultivos.

## Objetivos específicos

1. Registrar parcelas y cultivos.
2. Gestionar calendarios de siembra y cosecha.
3. Controlar riegos, fertilización y tratamientos.
4. Registrar costos e ingresos.
5. Generar reportes de productividad.
6. Emitir alertas sobre actividades pendientes.
7. Visualizar estadísticas para apoyar la toma de decisiones.

---

# Usuarios del sistema
### Agricultor

* Registra cultivos.
* Registra actividades agrícolas.
* Consulta reportes y alertas.

### Técnico Agrícola (opcional)

* Realiza inspecciones.
* Emite recomendaciones.
* Registra incidencias.

---

# Módulos del sistema
## 1. Gestión de Parcelas

* Registro de terrenos.
* Ubicación.
* Área cultivable.
* Tipo de suelo.

## 2. Gestión de Cultivos

* Tipo de cultivo.
* Fecha de siembra.
* Fecha estimada de cosecha.
* Estado actual.

## 3. Gestión de Actividades

Registro de:

* Riego.
* Fertilización.
* Aplicación de pesticidas.
* Poda.
* Cosecha.

## 4. Monitoreo de Cultivos

* Estado del cultivo.
* Fotografías.
* Observaciones.
* Historial de incidencias.

## 5. Gestión de Inventario

* Fertilizantes.
* Semillas.
* Herramientas.
* Productos fitosanitarios.

## 6. Gestión Económica

* Gastos.
* Ingresos.
* Costos por cultivo.
* Rentabilidad.

## 7. Reportes y Estadísticas

* Producción por cultivo.
* Costos por campaña.
* Rendimiento por parcela.
* Gráficos y dashboards.

## 8. Sistema de Alertas

* Próximo riego.
* Próxima fertilización.
* Fecha de cosecha.
* Stock bajo de insumos.


# Funcionalidades innovadoras (para destacar el proyecto)

### Nivel intermedio

* Pronóstico meteorológico integrado.
* Calendario agrícola.
* Recordatorios automáticos.

### Nivel avanzado

* Uso de IA para detectar enfermedades mediante fotografías.
* Recomendaciones automáticas de riego.
* Predicción de rendimiento de cosecha.
* Análisis de datos históricos.

# Modelo de Base de Datos

### Tabla Usuarios

* id_usuario
* nombre
* correo
* contraseña
* rol

### Tabla Parcelas

* id_parcela
* nombre
* ubicación
* área
* tipo_suelo

### Tabla Cultivos

* id_cultivo
* id_parcela
* nombre_cultivo
* fecha_siembra
* fecha_cosecha_estimada
* estado

### Tabla Actividades

* id_actividad
* id_cultivo
* tipo
* fecha
* descripción

### Tabla Inventario

* id_producto
* nombre
* stock
* unidad
* costo

### Tabla Gastos

* id_gasto
* id_cultivo
* concepto
* monto
* fecha

### Tabla Ingresos

* id_ingreso
* id_cultivo
* monto
* fecha

# Problema de la conectivadad en el campo
## Modo Offline

Cuando el agricultor está en el campo y no tiene Internet:

* Puede registrar cultivos.
* Registrar riegos.
* Registrar fertilizaciones.
* Tomar fotografías.
* Registrar gastos.
* Consultar información almacenada.

Todos los datos se guardan localmente en el dispositivo.

## Modo Online

Cuando el dispositivo recupera Internet:

* La aplicación detecta conexión.
* Envía automáticamente los cambios al servidor.
* Descarga actualizaciones realizadas desde otros dispositivos.
* Resuelve conflictos de datos si existen.

---

# Flujo de funcionamiento

```text
┌─────────────────┐
│ Aplicación Móvil│
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Base Local      │
│ SQLite          │
└────────┬────────┘
         │
         │ Sin internet
         ▼
 Usuario trabaja normalmente

         ▲
         │ Internet disponible
         │
┌────────┴────────┐
│ Sincronización  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ API Backend     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Base Central    │
│ PostgreSQL      │
└─────────────────┘
```

---

# Tecnologías recomendadas

## Aplicación móvil

Si haces una app móvil:

* Flutter
* React Native

## Base de datos local

* SQLite
* Hive

## Servidor

* Node.js
* Laravel
* Spring Boot

## Base de datos central

* PostgreSQL
* MySQL

---

# Diseño de sincronización

Cada registro debe tener campos adicionales:

```sql
id
fecha_creacion
fecha_actualizacion
estado_sync
```

Donde:

```text
PENDIENTE
SINCRONIZADO
ERROR
ELIMINADO
```

Ejemplo:

| id | cultivo | estado_sync  |
| -- | ------- | ------------ |
| 1  | Maíz    | PENDIENTE    |
| 2  | Papa    | SINCRONIZADO |

Cuando hay Internet:

```text
Buscar registros PENDIENTE
↓
Enviar al servidor
↓
Servidor confirma
↓
Actualizar a SINCRONIZADO
```

---

# Manejo de conflictos

Imagina:

* Usuario A modifica un cultivo desde el celular.
* Usuario B modifica el mismo cultivo desde la oficina.

Opciones:

### Opción 1: Última modificación gana

```text
updated_at más reciente
↓
sobrescribe
```

Fácil de implementar.

### Opción 2: Solicitar resolución

```text
Conflicto detectado
↓
Mostrar diferencias
↓
Usuario decide
```

Más profesional, pero más compleja.

---

# Funcionalidad avanzada para destacar el proyecto

Podrías agregar:

### Cola de sincronización

```text
sync_queue
```

Tabla:

| id | operación | tabla   |
| -- | --------- | ------- |
| 1  | INSERT    | cultivo |
| 2  | UPDATE    | riego   |
| 3  | DELETE    | gasto   |

Cuando vuelve Internet:

```text
Procesar cola
↓
Enviar cambios
↓
Vaciar cola
```

Este es el mismo enfoque usado por muchas aplicaciones que trabajan en zonas rurales o con conectividad limitada.


# Propuesta de arquitectura final para tu proyecto

### App móvil (Flutter)

* Gestión de cultivos.
* Registro de actividades.
* Fotografías.
* Inventario.
* Alertas.

### Base local

* SQLite.

### API REST

* Node.js + Express.

### Base central

* PostgreSQL.

### Sincronización

* Offline First.
* Cola de cambios.
* Sincronización automática al recuperar Internet.

### Dashboard web

* Administración.
* Reportes.
* Estadísticas.
* Gestión de usuarios.
