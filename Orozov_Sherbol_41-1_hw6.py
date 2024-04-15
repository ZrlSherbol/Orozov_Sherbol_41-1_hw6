my_List = [64, 34, 25, 12, 22, 11, 90]


def bubble_sort(List):
    n = len(List)
    for i in range(n):
        for j in range(0, n - i - 1):
            if List[j] > List[j + 1]:
                List[j], List[j + 1] = List[j + 1], List[j]
    return List


sorted_List = bubble_sort(my_List)
print("Отсортированный лист:", sorted_List)

N = 5000
ResultOk = False
Pos = -1
First = 0
Last = N - 1


def binary_search(A, Val):
    global ResultOk, Pos, First, Last
    while First <= Last:
        Middle = (First + Last) // 2

        if Val == A[Middle]:
            Pos = Middle
            ResultOk = True
            break
        elif Val > A[Middle]:
            First = Middle + 1
        else:
            Last = Middle - 1

    if ResultOk:
        print('элемент найден')
        print(Pos)
    else:
        print('элемент не найден')


A = list(range(N))
Val = 43
binary_search(A, Val)
