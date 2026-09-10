import random


def bubble_sort(vetor):
    comparacoes = 0
    trocas = 0

    n = len(vetor)

    for i in range(n - 1):
        houve_troca = False

        for j in range(n - 1 - i):
            comparacoes += 1

            if vetor[j] > vetor[j + 1]:
                vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]
                trocas += 1
                houve_troca = True

        if not houve_troca:
            break

    return comparacoes, trocas


def insertion_sort(vetor):
    comparacoes = 0
    movimentacoes = 0

    for i in range(1, len(vetor)):
        chave = vetor[i]
        movimentacoes += 1

        j = i - 1

        while j >= 0:
            comparacoes += 1

            if vetor[j] > chave:
                vetor[j + 1] = vetor[j]
                movimentacoes += 1
                j -= 1
            else:
                break

        vetor[j + 1] = chave
        movimentacoes += 1

    return comparacoes, movimentacoes


def selection_sort(vetor):
    comparacoes = 0
    trocas = 0

    n = len(vetor)

    for i in range(n - 1):
        menor = i

        for j in range(i + 1, n):
            comparacoes += 1

            if vetor[j] < vetor[menor]:
                menor = j

        if menor != i:
            vetor[i], vetor[menor] = vetor[menor], vetor[i]
            trocas += 1

    return comparacoes, trocas


def quick_sort(vetor, inicio, fim, contadores):
    if inicio < fim:
        pivo = particionar(vetor, inicio, fim, contadores)

        quick_sort(vetor, inicio, pivo - 1, contadores)
        quick_sort(vetor, pivo + 1, fim, contadores)


def particionar(vetor, inicio, fim, contadores):
    pivo = vetor[fim]
    i = inicio - 1

    for j in range(inicio, fim):
        contadores["comparacoes"] += 1

        if vetor[j] <= pivo:
            i += 1

            if i != j:
                vetor[i], vetor[j] = vetor[j], vetor[i]
                contadores["movimentacoes"] += 2

    if i + 1 != fim:
        vetor[i + 1], vetor[fim] = vetor[fim], vetor[i + 1]
        contadores["movimentacoes"] += 2

    return i + 1


def executar_teste(tamanho):
    original = [random.randint(1, 10000) for _ in range(tamanho)]

    vetor_bubble = original.copy()
    vetor_insertion = original.copy()
    vetor_selection = original.copy()
    vetor_quick = original.copy()

    comp_bubble, trocas_bubble = bubble_sort(vetor_bubble)

    comp_insertion, mov_insertion = insertion_sort(vetor_insertion)

    comp_selection, trocas_selection = selection_sort(vetor_selection)

    contadores_quick = {
        "comparacoes": 0,
        "movimentacoes": 0
    }

    quick_sort(
        vetor_quick,
        0,
        len(vetor_quick) - 1,
        contadores_quick
    )

    print("\n" + "=" * 50)
    print(f"TESTE COM {tamanho} ELEMENTOS")
    print("=" * 50)

    print("\nBubble Sort")
    print("Comparacoes:", comp_bubble)
    print("Trocas:", trocas_bubble)

    print("\nInsertion Sort")
    print("Comparacoes:", comp_insertion)
    print("Movimentacoes:", mov_insertion)

    print("\nSelection Sort")
    print("Comparacoes:", comp_selection)
    print("Trocas:", trocas_selection)

    print("\nQuick Sort")
    print("Comparacoes:", contadores_quick["comparacoes"])
    print("Movimentacoes:", contadores_quick["movimentacoes"])


random.seed(42)

executar_teste(10)
executar_teste(20)
executar_teste(1000)
