# BASE DE DATOS
## Importante
- Los modelos van en `src/models`
- cada modelo en su propio archivo
- Usa los modelos de reflex
- No use el SQL directo usa el ORM de reflex
## TABLAS
## Tabla: usuarios

| Campo           | Tipo     |
| --------------- | -------- |
| id_usuario PK   | INT      |
| nombres         | VARCHAR  |
| apellidos       | VARCHAR  |
| correo          | VARCHAR  |
| contraseña_hash | VARCHAR  |
| telefono        | VARCHAR  |
| rol             | ENUM     |
| fecha_registro  | DATETIME |
| estado          | BOOLEAN  |

---

## Tabla: parcelas

| Campo          | Tipo     |
| -------------- | -------- |
| id_parcela PK  | INT      |
| id_usuario FK  | INT      |
| nombre         | VARCHAR  |
| ubicacion      | VARCHAR  |
| area_hectareas | DECIMAL  |
| tipo_suelo     | VARCHAR  |
| fecha_registro | DATETIME |

Relación:

```text
Usuario 1 ------ N Parcela
```

---

## Tabla: cultivos

| Campo          | Tipo    |
| -------------- | ------- |
| id_cultivo PK  | INT     |
| id_parcela FK  | INT     |
| nombre_cultivo | VARCHAR |
| variedad       | VARCHAR |
| fecha_siembra  | DATE    |
| area_sembrada  | DECIMAL |
| estado         | VARCHAR |

Relación:

```text
Parcela 1 ------ N Cultivo
```

---

## Tabla: actividades_agricolas

| Campo           | Tipo     |
| --------------- | -------- |
| id_actividad PK | INT      |
| id_cultivo FK   | INT      |
| tipo_actividad  | ENUM     |
| fecha_actividad | DATETIME |
| descripcion     | TEXT     |
| responsable     | VARCHAR  |

Tipos:

* Riego
* Fertilización
* Pesticida
* Poda
* Cosecha

---

## Tabla: observaciones

| Campo             | Tipo     |
| ----------------- | -------- |
| id_observacion PK | INT      |
| id_cultivo FK     | INT      |
| id_usuario FK     | INT      |
| observacion       | TEXT     |
| fecha_observacion | DATETIME |

---

## Tabla: fotografias

| Campo            | Tipo     |
| ---------------- | -------- |
| id_fotografia PK | INT      |
| id_cultivo FK    | INT      |
| url_imagen       | VARCHAR  |
| fecha_subida     | DATETIME |

---

## Tabla: inspecciones

| Campo            | Tipo     |
| ---------------- | -------- |
| id_inspeccion PK | INT      |
| id_cultivo FK    | INT      |
| id_tecnico FK    | INT      |
| fecha_inspeccion | DATETIME |
| resultado        | TEXT     |

---

## Tabla: incidencias

| Campo            | Tipo     |
| ---------------- | -------- |
| id_incidencia PK | INT      |
| id_cultivo FK    | INT      |
| id_tecnico FK    | INT      |
| descripcion      | TEXT     |
| severidad        | ENUM     |
| fecha_registro   | DATETIME |
| estado           | VARCHAR  |

---

## Tabla: recomendaciones

| Campo               | Tipo     |
| ------------------- | -------- |
| id_recomendacion PK | INT      |
| id_incidencia FK    | INT      |
| id_tecnico FK       | INT      |
| recomendacion       | TEXT     |
| fecha_recomendacion | DATETIME |

---

## Tabla: productos_inventario

| Campo          | Tipo    |
| -------------- | ------- |
| id_producto PK | INT     |
| nombre         | VARCHAR |
| categoria      | VARCHAR |
| unidad_medida  | VARCHAR |
| stock_actual   | DECIMAL |
| stock_minimo   | DECIMAL |

---

## Tabla: movimientos_inventario

| Campo            | Tipo     |
| ---------------- | -------- |
| id_movimiento PK | INT      |
| id_producto FK   | INT      |
| tipo_movimiento  | ENUM     |
| cantidad         | DECIMAL  |
| fecha_movimiento | DATETIME |

---

## Tabla: gastos

| Campo         | Tipo    |
| ------------- | ------- |
| id_gasto PK   | INT     |
| id_parcela FK | INT     |
| concepto      | VARCHAR |
| monto         | DECIMAL |
| fecha_gasto   | DATE    |

---

## Tabla: ingresos

| Campo         | Tipo    |
| ------------- | ------- |
| id_ingreso PK | INT     |
| id_parcela FK | INT     |
| concepto      | VARCHAR |
| monto         | DECIMAL |
| fecha_ingreso | DATE    |

---

## Tabla: alertas

| Campo         | Tipo     |
| ------------- | -------- |
| id_alerta PK  | INT      |
| id_usuario FK | INT      |
| tipo_alerta   | VARCHAR  |
| mensaje       | TEXT     |
| prioridad     | ENUM     |
| atendida      | BOOLEAN  |
| fecha_alerta  | DATETIME |

---

## Tabla: diagnosticos_ia

| Campo                | Tipo     |
| -------------------- | -------- |
| id_diagnostico PK    | INT      |
| id_cultivo FK        | INT      |
| id_fotografia FK     | INT      |
| enfermedad_detectada | VARCHAR  |
| confianza            | DECIMAL  |
| recomendacion        | TEXT     |
| fecha_analisis       | DATETIME |

---

## Tabla: predicciones_cosecha

| Campo                | Tipo     |
| -------------------- | -------- |
| id_prediccion PK     | INT      |
| id_cultivo FK        | INT      |
| rendimiento_estimado | DECIMAL  |
| margen_error         | DECIMAL  |
| fecha_prediccion     | DATETIME |

---

## Tabla: sincronizaciones

| Campo              | Tipo     |
| ------------------ | -------- |
| id_sync PK         | INT      |
| id_usuario FK      | INT      |
| fecha_sync         | DATETIME |
| registros_enviados | INT      |
| estado             | VARCHAR  |