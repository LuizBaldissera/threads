import random
import string
import time


def gerar_nome(tamanho=5):
    return ''.join(random.choices(string.ascii_letters, k=tamanho))

# ordenacao por pente (Comb Sort)
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

# gerar e salvar na lista e nor arquivo
def gerar_e_salvar_nomes(qtd_nomes, tamanho_nome):
    nomes = [gerar_nome(tamanho_nome) for _ in range(qtd_nomes)]
    with open("nomes.txt", "w") as f:
        f.write("\n".join(nomes))
    return nomes


def sem_threads():
    qtd_nomes = 1000000
    tamanho_nome = 8


    start = time.time()
    nomes = gerar_e_salvar_nomes(qtd_nomes, tamanho_nome)
    print(f"Tempo para gerar e salvar nomes: {time.time() - start:.2f} segundos")

    #ordenar usando o metodo criado e o sort
    start = time.time()
    nomes_sorted = sorted(nomes)
    print(f"Tempo para ordenar com sort: {time.time() - start:.2f} segundos")

 
    start = time.time()
    comb_sort(nomes)
    print(f"Tempo para ordenar com Comb Sort: {time.time() - start:.2f} segundos")

if __name__ == "__main__":
    sem_threads()
