def insertion_sort(collection):
    for i in range(1, len(collection), 1):
        for j in range(i, 0, -1):
            if collection[j-1] > collection[j]:
                collection[j-1], collection[j] = collection[j], collection[j-1]


if __name__ == "__main__":

    arr = [1381,20144,2937,8401,31904,22750,27539,6615,1492,8110,12833,11891,25449,14327,19563,21346,16756,16012,16590,7966,8155,10696,2560,18444,10171,22890,14236,21239,28678,22691,30682,1469,30065,1646,28317,29256,18829,6176,32180,11712,15667,10816,25177,2047,2598,21400,19454,22342,16372,28300]
    insertion_sort(arr)

    for elem in arr:
        # end 옵션을 이용해 linefeed를 다른 문자로 변경
        print(str(elem), end=' ')
