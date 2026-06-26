## ÉPICA 1: GESTIÓN DE CUENTA
---
## HU-001: Iniciar Sesión
**Como** usuario registrado, **quiero** iniciar sesión, **para** acceder a la información y funcionalidades de Agronova según mi rol

### Tareas pendientes
- [ ] El sistema valida las credenciales
- [ ] El sistema crea una sesión activa
- [ ] El usuario es redirigido al panel principal
- [ ] El sistema muestra un mensaje de bienvenida
- [ ] El sistema registra la fecha y hora de acceso
- [ ] El acceso es rechazado
- [ ] Se muestra el mensaje:
- [ ] El usuario permanece en la pantalla de inicio de sesión
- [ ] El sistema resalta los campos incompletos
- [ ] El sistema informa qué dato falta completar
- [ ] No se permite el envío del formulario
- [ ] El sistema informa que se requiere conexión
- [ ] Se ofrece reintentar la autenticación
**Estado:** Pendiente
---
## HU-002: Cerrar Sesión
**Como** usuario autenticado, **quiero** cerrar sesión, **para** proteger mi información

### Tareas pendientes
- [ ] El sistema elimina la sesión
- [ ] El usuario es redirigido a la pantalla de acceso
- [ ] Los datos sensibles dejan de estar accesibles
- [ ] El sistema informa la existencia de datos pendientes
- [ ] El usuario puede cancelar o continuar
**Estado:** Pendiente
---
## HU-003: Actualizar Perfil
**Como** usuario, **quiero** actualizar mis datos personales, **para** mantener mi información actualizada

### Tareas pendientes
- [ ] Los cambios son guardados
- [ ] El sistema muestra confirmación
- [ ] La información actualizada aparece inmediatamente
- [ ] El sistema identifica el error
- [ ] Indica claramente qué campo debe corregirse
- [ ] No guarda cambios inconsistentes
**Estado:** Pendiente
---
## ÉPICA 2: GESTIÓN DE PARCELAS
---
## HU-004: Registrar Parcela
**Como** agricultor, **quiero** registrar una parcela, **para** gestionar mis cultivos de forma organizada

### Tareas pendientes
- [ ] Nombre de la parcela
- [ ] Ubicación
- [ ] Área
- [ ] Tipo de suelo
- [ ] El sistema guarda la información
- [ ] La parcela aparece en la lista
- [ ] El sistema informa los campos faltantes
- [ ] No permite guardar el registro
- [ ] El sistema guarda localmente la información
- [ ] Marca el registro como pendiente de sincronización
**Estado:** Pendiente
---
## HU-005: Consultar Parcelas
**Como** agricultor, **quiero** visualizar mis parcelas registradas, **para** consultar información rápidamente

### Tareas pendientes
- [ ] Se muestra una lista de parcelas
- [ ] Cada registro muestra:
- [ ] Nombre
- [ ] Área
- [ ] Estado
- [ ] Cultivos asociados
- [ ] Los resultados se filtran en tiempo real
**Estado:** Pendiente
---
## HU-006: Actualizar Parcela
**Como** agricultor, **quiero** modificar la información de una parcela, **para** mantener datos actualizados

### Tareas pendientes
- [ ] Permitir editar únicamente parcelas propias
- [ ] Mostrar información actual antes de editar
- [ ] Validar datos obligatorios
- [ ] Confirmar actualización exitosa
- [ ] Sincronizar cambios cuando exista conexión
**Estado:** Pendiente
---
## HU-007: Eliminar Parcela
**Como** agricultor, **quiero** eliminar una parcela, **para** mantener organizado mi registro agrícola

### Tareas pendientes
- [ ] Solicitar confirmación antes de eliminar
- [ ] Advertir si existen cultivos asociados
- [ ] Eliminar lógicamente el registro
- [ ] Mantener trazabilidad histórica
**Estado:** Pendiente
---
## ÉPICA 3: GESTIÓN DE CULTIVOS
---
## HU-008: Registrar Cultivo
**Como** agricultor, **quiero** registrar un cultivo, **para** realizar seguimiento de su desarrollo

### Tareas pendientes
- [ ] Nombre del cultivo
- [ ] Variedad
- [ ] Fecha de siembra
- [ ] Parcela asociada
- [ ] Área sembrada
- [ ] Estado inicial
- [ ] Validar que exista una parcela disponible
- [ ] Guardar el cultivo
- [ ] Relacionarlo con la parcela correspondiente
- [ ] Permitir funcionamiento offline
**Estado:** Pendiente
---
## HU-009: Consultar Cultivos
**Como** agricultor, **quiero** consultar cultivos, **para** consultar información de mis cultivos

### Tareas pendientes
- [ ] Mostrar listado de cultivos
- [ ] Permitir búsqueda
- [ ] Permitir filtros por:
- [ ] Parcela
- [ ] Estado
- [ ] Fecha de siembra
- [ ] Mostrar indicadores visuales de estado
**Estado:** Pendiente
---
## HU-010: Actualizar Cultivo
**Como** agricultor, **quiero** actualizar cultivo, **para** mantener datos actualizados

### Tareas pendientes
- [ ] Permitir modificar información agronómica
- [ ] Registrar fecha de actualización
- [ ] Mantener historial de cambios
- [ ] Validar coherencia de datos
**Estado:** Pendiente
---
## HU-011: Eliminar Cultivo
**Como** agricultor, **quiero** eliminar cultivo, **para** mantener organizado mi registro

### Tareas pendientes
- [ ] Solicitar confirmación
- [ ] Mantener historial
- [ ] No eliminar actividades registradas
**Estado:** Pendiente
---
## ÉPICA 4: ACTIVIDADES AGRÍCOLAS
---
## HU-012: Registrar Riego
**Como** agricultor, **quiero** registrar riegos, **para** llevar control hídrico de mis cultivos

### Tareas pendientes
- [ ] Seleccionar cultivo
- [ ] Registrar fecha
- [ ] Registrar cantidad de agua
- [ ] Registrar método de riego
- [ ] Guardar observaciones
- [ ] Registrar usuario responsable
- [ ] Permitir uso offline
**Estado:** Pendiente
---
## HU-013: Registrar Fertilización
**Como** agricultor, **quiero** registrar fertilización, **para** llevar control de mis actividades

### Tareas pendientes
- [ ] Seleccionar cultivo
- [ ] Registrar fertilizante utilizado
- [ ] Registrar dosis
- [ ] Registrar fecha
- [ ] Registrar responsable
- [ ] Guardar historial permanente
**Estado:** Pendiente
---
## HU-014: Registrar Aplicación de Pesticidas
**Como** agricultor, **quiero** registrar aplicación de pesticidas, **para** llevar control de mis actividades

### Tareas pendientes
- [ ] Registrar producto
- [ ] Registrar dosis
- [ ] Registrar fecha
- [ ] Registrar motivo de aplicación
- [ ] Registrar observaciones
- [ ] Asociar evidencia fotográfica
**Estado:** Pendiente
---
## HU-015: Registrar Poda
**Como** agricultor, **quiero** registrar poda, **para** llevar control de mis actividades

### Tareas pendientes
- [ ] Registrar fecha
- [ ] Registrar tipo de poda
- [ ] Registrar observaciones
- [ ] Registrar responsable
**Estado:** Pendiente
---
## HU-016: Registrar Cosecha
**Como** agricultor, **quiero** registrar cosecha, **para** llevar control de mis actividades

### Tareas pendientes
- [ ] Registrar fecha
- [ ] Registrar cantidad cosechada
- [ ] Registrar unidad de medida
- [ ] Registrar calidad obtenida
- [ ] Registrar observaciones
- [ ] Actualizar indicadores productivos
**Estado:** Pendiente
---
## HU-017: Consultar Historial de Actividades
**Como** agricultor, **quiero** consultar historial de actividades, **para** consultar información de mis cultivos

### Tareas pendientes
- [ ] Mostrar línea temporal de actividades
- [ ] Permitir filtros
- [ ] Mostrar usuario responsable
- [ ] Mostrar evidencias asociadas
**Estado:** Pendiente
---
## ÉPICA 5: MONITOREO
---
## HU-018: Registrar Observaciones
**Como** agricultor, **quiero** registrar observaciones, **para** llevar control de mis actividades

### Tareas pendientes
- [ ] Definir tareas para esta historia de usuario
**Estado:** Pendiente
---
## HU-020: Consultar Estado del Cultivo
**Como** agricultor, **quiero** consultar estado del cultivo, **para** consultar información de mis cultivos

### Tareas pendientes
- [ ] Definir tareas para esta historia de usuario
**Estado:** Pendiente
---
## HU-022: Registrar Inspección Agrícola
**Como** agricultor, **quiero** registrar inspección agrícola, **para** llevar control de mis actividades

### Tareas pendientes
- [ ] Definir tareas para esta historia de usuario
**Estado:** Pendiente
---
## HU-024: Registrar Recomendación Técnica
**Como** agricultor, **quiero** registrar recomendación técnica, **para** llevar control de mis actividades

### Tareas pendientes
- [ ] Definir tareas para esta historia de usuario
**Estado:** Pendiente
---
## HU-025: Registrar Producto
**Como** agricultor, **quiero** registrar producto, **para** llevar control de mis actividades

### Tareas pendientes
- [ ] Definir tareas para esta historia de usuario
**Estado:** Pendiente
---
## HU-027: Consultar Inventario
**Como** agricultor, **quiero** consultar inventario, **para** consultar información de mis cultivos

### Tareas pendientes
- [ ] Definir tareas para esta historia de usuario
**Estado:** Pendiente
---
## ÉPICA 7: GESTIÓN ECONÓMICA
---
## HU-029: Registrar Gasto
**Como** agricultor, **quiero** registrar gasto, **para** llevar control de mis actividades

### Tareas pendientes
- [ ] Definir tareas para esta historia de usuario
**Estado:** Pendiente
---
## HU-031: Consultar Gastos
**Como** agricultor, **quiero** consultar gastos, **para** consultar información de mis cultivos

### Tareas pendientes
- [ ] Definir tareas para esta historia de usuario
**Estado:** Pendiente
---
## HU-033: Consultar Rentabilidad
**Como** agricultor, **quiero** consultar rentabilidad, **para** consultar información de mis cultivos

### Tareas pendientes
- [ ] Definir tareas para esta historia de usuario
**Estado:** Pendiente
---
## HU-034: Consultar Reporte de Producción
**Como** agricultor, **quiero** consultar reporte de producción, **para** consultar información de mis cultivos

### Tareas pendientes
- [ ] Definir tareas para esta historia de usuario
**Estado:** Pendiente
---
## HU-036: Consultar Rendimiento por Parcela
**Como** agricultor, **quiero** consultar rendimiento por parcela, **para** consultar información de mis cultivos

### Tareas pendientes
- [ ] Definir tareas para esta historia de usuario
**Estado:** Pendiente
---
## ÉPICA 9: ALERTAS
---
## HU-038: Consultar Alertas
**Como** agricultor, **quiero** consultar alertas, **para** consultar información de mis cultivos

### Tareas pendientes
- [ ] Definir tareas para esta historia de usuario
**Estado:** Pendiente
---
## ÉPICA 10: INTELIGENCIA ARTIFICIAL
---
## HU-040: Analizar Enfermedad mediante Fotografía
**Como** agricultor, **quiero** analizar enfermedad mediante fotografía, **para** obtener diagnósticos de mis cultivos

### Tareas pendientes
- [ ] Permitir captura desde cámara
- [ ] Permitir carga desde galería
- [ ] Analizar imagen
- [ ] Mostrar enfermedad detectada
- [ ] Mostrar nivel de confianza
- [ ] Mostrar recomendaciones
- [ ] Guardar resultado en historial
**Estado:** Pendiente
---
## HU-041: Recomendar Riego
**Como** agricultor, **quiero** recomendar riego, **para** optimizar el riego de mis cultivos

### Tareas pendientes
- [ ] Analizar clima
- [ ] Analizar humedad
- [ ] Analizar historial de riego
- [ ] Generar recomendación
- [ ] Explicar motivo de la recomendación
**Estado:** Pendiente
---
## HU-042: Predecir Rendimiento de Cosecha
**Como** agricultor, **quiero** predecir rendimiento de cosecha, **para** planificar mis cosechas

### Tareas pendientes
- [ ] Analizar datos históricos
- [ ] Analizar actividades agrícolas
- [ ] Analizar clima
- [ ] Mostrar predicción estimada
- [ ] Mostrar margen de error
- [ ] Mostrar factores considerados
**Estado:** Pendiente
---
## ÉPICA 11: SINCRONIZACIÓN
---
## HU-043: Sincronizar Datos Offline-Online
**Como** agricultor, **quiero** sincronizar datos offline-online, **para** mantener mis datos actualizados en todos los dispositivos

### Tareas pendientes
- [ ] Se inicia sincronización automática
- [ ] Se muestran registros sincronizados
- [ ] Se actualiza el estado de cada registro
- [ ] El sistema identifica el conflicto
- [ ] Solicita resolución al usuario
- [ ] Conserva ambas versiones hasta resolver
- [ ] El sistema informa el problema
- [ ] Mantiene los datos locales
- [ ] Permite reintentar posteriormente
**Estado:** Pendiente
---