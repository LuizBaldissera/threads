import threading
import random
import string
import time

# Função para gerar um nome aleatório
def gerar_nome(tamanho=8):
    return ''.join(random.choices(string.ascii_letters, k=tamanho))

# Função de ordenação por pente (Comb Sort)
def comb_sort(arr):
    gap = len(arr)
    shrink = 1.3
    sorted = False

    while not sorted:
        gap = int(gap / shrink)
        if gap <= 1:
            gap = 1
            sorted = True

        for i in range(len(arr) - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                sorted = False

# Gerar e salvar nomes em uma lista e em um arquivo
def gerar_e_salvar_nomes(qtd_nomes, tamanho_nome):
    nomes = [gerar_nome(tamanho_nome) for _ in range(qtd_nomes)]
    with open("nomes.txt", "w") as f:
        f.write("\n".join(nomes))
    return nomes

# Função principal com threads
def com_threads():
    qtd_nomes = 1000000
    tamanho_nome = 8

    # Gerar e salvar nomes
    start = time.time()
    nomes = gerar_e_salvar_nomes(qtd_nomes, tamanho_nome)
    print(f"Tempo para gerar e salvar nomes: {time.time() - start:.2f} segundos")

    # Função para ordenar usando sort
    def ordenar_sort():
        start = time.time()
        sorted(nomes)
        print(f"Tempo para ordenar com sort: {time.time() - start:.2f} segundos")

    # Função para ordenar usando Comb Sort
    def ordenar_comb_sort():
        start = time.time()
        comb_sort(nomes)
        print(f"Tempo para ordenar com Comb Sort: {time.time() - start:.2f} segundos")

    # Criar threads
    t1 = threading.Thread(target=ordenar_sort)
    t2 = threading.Thread(target=ordenar_comb_sort)

    # Iniciar threads
    start = time.time()
    t1.start()
    t2.start()

    # Aguardar threads terminarem
    t1.join()
    t2.join()
    print(f"Tempo total para ordenar com threads: {time.time() - start:.2f} segundos")

if __name__ == "__main__":
    com_threads()
