import random
import sys

# Evita erro de recursão no desafio com vetores ordenados/invertidos.
sys.setrecursionlimit(5000)


def bubble_sort(v):
    comparacoes = 0
    trocas = 0
    n = len(v)

    for i in range(n - 1):
        trocou = False

        for j in range(n - 1 - i):
            comparacoes += 1

            if v[j] > v[j + 1]:
                v[j], v[j + 1] = v[j + 1], v[j]
                trocas += 1
                trocou = True

        # Se nenhuma troca ocorreu, o vetor já está ordenado.
        if not trocou:
            break

    return comparacoes, trocas


def insertion_sort(v):
    comparacoes = 0
    movimentacoes = 0

    for i in range(1, len(v)):
        chave = v[i]
        j = i - 1

        while j >= 0:
            comparacoes += 1

            if v[j] > chave:
                v[j + 1] = v[j]
                movimentacoes += 1
                j -= 1
            else:
                break

        # Conta a recolocação da chave somente quando ela muda de posição.
        if j + 1 != i:
            v[j + 1] = chave
            movimentacoes += 1

    return comparacoes, movimentacoes


def selection_sort(v):
    comparacoes = 0
    trocas = 0
    n = len(v)

    for i in range(n - 1):
        menor = i

        for j in range(i + 1, n):
            comparacoes += 1

            if v[j] < v[menor]:
                menor = j

        if menor != i:
            v[i], v[menor] = v[menor], v[i]
            trocas += 1

    return comparacoes, trocas


def quick_sort(v):
    comparacoes = 0
    movimentacoes = 0

    def particionar(inicio, fim):
        nonlocal comparacoes, movimentacoes

        pivo = v[fim]
        i = inicio - 1

        for j in range(inicio, fim):
            comparacoes += 1

            if v[j] <= pivo:
                i += 1

                if i != j:
                    v[i], v[j] = v[j], v[i]
                    movimentacoes += 1

        if i + 1 != fim:
            v[i + 1], v[fim] = v[fim], v[i + 1]
            movimentacoes += 1

        return i + 1

    def ordenar(inicio, fim):
        if inicio < fim:
            posicao_pivo = particionar(inicio, fim)
            ordenar(inicio, posicao_pivo - 1)
            ordenar(posicao_pivo + 1, fim)

    ordenar(0, len(v) - 1)
    return comparacoes, movimentacoes


def executar_algoritmos(original):
    vetor_bubble = original.copy()
    vetor_insertion = original.copy()
    vetor_selection = original.copy()
    vetor_quick = original.copy()

    bubble = bubble_sort(vetor_bubble)
    insertion = insertion_sort(vetor_insertion)
    selection = selection_sort(vetor_selection)
    quick = quick_sort(vetor_quick)

    # Verificação para garantir que todos realmente ordenaram.
    esperado = sorted(original)
    assert vetor_bubble == esperado
    assert vetor_insertion == esperado
    assert vetor_selection == esperado
    assert vetor_quick == esperado

    return bubble, insertion, selection, quick


def experimento_principal():
    # A semente deixa o experimento reproduzível.
    random.seed(42)

    print("\nRESULTADOS DO EXPERIMENTO PRINCIPAL\n")
    print(
        f"{'Tamanho':<8} "
        f"{'Bubble Comp.':<14} {'Bubble Trocas':<15} "
        f"{'Insertion Comp.':<16} {'Insertion Mov.':<15} "
        f"{'Selection Comp.':<16} {'Selection Trocas':<17} "
        f"{'Quick Comp.':<12} {'Quick Mov.':<10}"
    )

    resultados = []

    for tamanho in [10, 20, 1000]:
        # Um único vetor aleatório por tamanho.
        original = random.sample(range(1, 100000), tamanho)

        bubble, insertion, selection, quick = executar_algoritmos(original)

        resultados.append(
            (tamanho, bubble, insertion, selection, quick)
        )

        print(
            f"{tamanho:<8} "
            f"{bubble[0]:<14} {bubble[1]:<15} "
            f"{insertion[0]:<16} {insertion[1]:<15} "
            f"{selection[0]:<16} {selection[1]:<17} "
            f"{quick[0]:<12} {quick[1]:<10}"
        )

    return resultados


def desafio_adicional():
    print("\nDESAFIO ADICIONAL - 1.000 ELEMENTOS\n")

    random.seed(42)
    aleatorio = random.sample(range(1, 100000), 1000)
    ordenado = sorted(aleatorio)
    inverso = sorted(aleatorio, reverse=True)

    casos = [
        ("Aleatório", aleatorio),
        ("Ordenado", ordenado),
        ("Inverso", inverso),
    ]

    print(
        f"{'Caso':<10} "
        f"{'Bubble C.':<11} {'Bubble T.':<11} "
        f"{'Insertion C.':<14} {'Insertion M.':<14} "
        f"{'Selection C.':<14} {'Selection T.':<14} "
        f"{'Quick C.':<11} {'Quick M.':<10}"
    )

    for nome, vetor in casos:
        bubble, insertion, selection, quick = executar_algoritmos(vetor)

        print(
            f"{nome:<10} "
            f"{bubble[0]:<11} {bubble[1]:<11} "
            f"{insertion[0]:<14} {insertion[1]:<14} "
            f"{selection[0]:<14} {selection[1]:<14} "
            f"{quick[0]:<11} {quick[1]:<10}"
        )


if __name__ == "__main__":
    experimento_principal()
    desafio_adicional()
