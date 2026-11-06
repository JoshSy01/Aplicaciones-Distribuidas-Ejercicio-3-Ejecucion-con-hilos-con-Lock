# Ejecución con Hilos y Condiciones de Carrera en Python: Lavado de Ropa

Este proyecto demuestra el funcionamiento de la programación multihilo en Python utilizando la librería estándar `threading`, comparando un escenario con **condición de carrera (Race Condition)** frente a su solución mediante **exclusión mutua (Lock)**.

Se simula el lavado simultáneo de 3 tandadas de ropa (Ropa Blanca, Ropa de Color y Ropa Delicada) de 10 prendas cada una:

1. **Sin Lock (Hilos_sin_lock.py):** Los 3 hilos terminan de lavar al mismo tiempo y leen la variable compartida `prendas_lavadas` cuando aún vale 0. Al sobrescribir el valor sin sincronización, el total final reporta erróneamente 10 prendas en lugar de 30.
2. **Con Lock (Hilos_con_lock.py):** El lavado de 4 segundos se mantiene en paralelo, pero se implementa `threading.Lock()` únicamente sobre la sección crítica donde se actualiza el contador. Cada hilo espera su turno para registrar sus prendas, obteniendo el total correcto de 30 prendas sin sacrificar la concurrencia del lavado.

## Estructura del Proyecto

```text
.
├── Hilos_lavado_ropa_sin_lock.py    # Demostración de condición de carrera (sin Lock)
├── Hilos_lavado_ropa_con_lock.py    # Demostración de sincronización (con Lock)
├── docker-compose.yml   # Configuración de servicios para ambos scripts
└── README.md            # Documentación e instrucciones de ejecución
```

## Requisitos Previos

* Tener instalado [Docker](https://docs.docker.com/get-docker/) y Docker Compose.

## Cómo ejecutar los scripts con Docker

Abre una terminal en la carpeta raíz del proyecto y utiliza cualquiera de las siguientes modalidades:

### Opción 1: Usando Docker Compose

Para ejecutar únicamente la demostración **con condición de carrera (sin Lock)**:
```bash
docker compose up sin-lock
```

Para ejecutar únicamente la demostración **corregida (con Lock)**:
```bash
docker compose up con-lock
```

Para limpiar los contenedores residuales al terminar:
```bash
docker compose down
```

## Salida Esperada

### 1. Ejecución sin Lock (Condición de carrera)
```text
Lavando Ropa Blanca (10 prendas)...
Lavando Ropa de Color (10 prendas)...
Lavando Ropa Delicada (10 prendas)...
Ropa Blanca lavada. Total registrado por este hilo: 10
Ropa de Color lavada. Total registrado por este hilo: 10
Ropa Delicada lavada. Total registrado por este hilo: 10

Prendas lavadas esperadas: 30
Prendas lavadas registradas: 10
Tiempo total de lavado: 4.10 segundos
```

### 2. Ejecución con Lock (Sincronizada)
```text
Lavando Ropa Blanca (10 prendas)...
Lavando Ropa de Color (10 prendas)...
Lavando Ropa Delicada (10 prendas)...
Ropa Blanca lavada. Total registrado por este hilo: 10
Ropa de Color lavada. Total registrado por este hilo: 20
Ropa Delicada lavada. Total registrado por este hilo: 30

Prendas lavadas esperadas: 30
Prendas lavadas registradas: 30
Tiempo total de lavado: 4.30 segundos
```