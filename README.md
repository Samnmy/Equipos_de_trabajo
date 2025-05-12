# Task Management System

Este proyecto tiene como objetivo gestionar un sistema de tareas, permitiendo registrar, buscar, actualizar, eliminar tareas y generar informes sobre el progreso de las mismas. Es ideal para equipos de trabajo que deseen llevar un control eficiente de las tareas y su progreso.

## Funcionalidades

El sistema ofrece las siguientes funcionalidades clave:

1. **Registrar una tarea**: Permite registrar nuevas tareas con información como título, descripción, persona asignada, prioridad y estado.

2. **Buscar tareas**: Permite buscar tareas por el nombre del asignado o por el estado. La búsqueda es insensible a mayúsculas/minúsculas.

3. **Actualizar una tarea**: Permite actualizar la prioridad o el estado de una tarea registrada.

4. **Eliminar una tarea completada**: Permite eliminar tareas que tienen el estado "Done" después de confirmar la acción.

5. **Generar informes**: Genera dos tipos de informes:
    - Porcentaje de tareas completadas por cada miembro del equipo.
    - Lista de tareas pendientes, mostrando título, asignado y prioridad.

6. **Menú interactivo**: Ofrece una interfaz de usuario interactiva en la consola para realizar diversas operaciones con las tareas.

## Cómo funciona

El sistema mantiene una lista de diccionarios (`tasks`), donde cada diccionario contiene los detalles de una tarea. Cada tarea tiene los siguientes atributos:

- **title**: Título de la tarea.
- **description**: Descripción detallada de la tarea.
- **assigned_to**: Persona asignada para completar la tarea.
- **priority**: Prioridad de la tarea (Baja, Media, Alta).
- **status**: Estado de la tarea (Pendiente, En progreso, Hecha).

Las funciones principales del sistema permiten:

- **preload_tasks**: Inicializa la lista de tareas con algunos datos predeterminados.

- **register_task**: Permite registrar una nueva tarea validando que el estado de la tarea sea uno de los siguientes: "Pendiente", "En progreso" o "Hecha".

- **search_task**: Permite buscar tareas por el nombre de la persona asignada o el estado de la tarea.

- **update_task**: Permite actualizar la prioridad o el estado de una tarea.

- **delete_task**: Permite eliminar tareas que tienen el estado "Hecha" después de confirmar la eliminación.

- **generate_reports**: Genera un informe con el porcentaje de tareas completadas por cada miembro del equipo y una lista de tareas pendientes.

- **menu**: Muestra un menú interactivo donde el usuario puede seleccionar qué operación realizar.

## Uso

### Requisitos

Este proyecto requiere Python 3.x para ejecutarse correctamente.

### Ejecución

1. Clona o descarga este repositorio.
2. Ejecuta el archivo `task_manager.py` en tu terminal o entorno de desarrollo Python.
3. El sistema mostrará un menú interactivo en la consola donde podrás elegir entre las diferentes opciones para gestionar las tareas.

### Ejemplo de flujo

1. **Registrar una tarea**:
   - El usuario ingresa los detalles de la tarea (título, descripción, asignado, prioridad y estado), y la tarea se registra en el sistema.

2. **Buscar una tarea**:
   - El usuario puede buscar tareas por el nombre de la persona asignada o el estado de la tarea, y se mostrarán los resultados coincidentes.

3. **Actualizar una tarea**:
   - El usuario puede actualizar la prioridad o el estado de una tarea específica en el sistema.

4. **Eliminar una tarea completada**:
   - El usuario puede eliminar tareas con el estado "Hecha" después de confirmar la eliminación.

5. **Generar informes**:
   - El sistema muestra el porcentaje de tareas completadas por cada miembro del equipo y una lista de tareas pendientes.

## Objetivo

El objetivo de este proyecto es proporcionar una solución sencilla y efectiva para gestionar el progreso de las tareas de un equipo. Permite a los miembros del equipo y a los responsables realizar un seguimiento de las tareas de manera organizada y eficiente.

## Contribuciones

Si deseas contribuir al proyecto, puedes hacer un fork y enviar un pull request. Las mejoras y sugerencias son siempre bienvenidas.
