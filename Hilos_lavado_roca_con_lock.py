import threading
import time

# Recurso compartido y candado de exclusión mutua
prendas_lavadas = 0
candado = threading.Lock()

def lavar_ropa(tipo_ropa, cantidad_prendas):
    global prendas_lavadas
    print(f"Lavando {tipo_ropa} ({cantidad_prendas} prendas)...")
    time.sleep(4)  # El lavado ocurre en paralelo
    
    # Sección crítica protegida con Lock
    with candado:
        registro_temporal = prendas_lavadas
        time.sleep(0.1)  # Simula el retraso de lectura/escritura en memoria
        prendas_lavadas = registro_temporal + cantidad_prendas
        print(f"{tipo_ropa} lavada. Total registrado por este hilo: {prendas_lavadas}")

inicio = time.perf_counter()

tandadas = [
    "Ropa Blanca",
    "Ropa de Color",
    "Ropa Delicada"
]

hilos = []

for ropa in tandadas:
    hilo = threading.Thread(target=lavar_ropa, args=(ropa, 10))
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()

fin = time.perf_counter()

print("Prendas lavadas esperadas: 30")
print(f"Prendas lavadas registradas: {prendas_lavadas}")
print(f"Tiempo total de lavado: {fin - inicio:.2f} segundos")