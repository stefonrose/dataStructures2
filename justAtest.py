import random
import pygame

displaySize = (width, height) = (720, 480)
display = pygame.display.set_mode(displaySize)
displayFPS = pygame.time.Clock()
pygame.display.set_caption("Merge Sort")

colors = {"white": (255, 255, 255), "black": (0, 0, 0), "red": (255, 0, 0), "green": (0, 255, 0), "blue": (0, 0, 255)}

items = 240


def makeArray(size):
    array = [2 * x for x in range(0, size)]
    random.shuffle(array)
    return array


def merge(leftArray, rightArray, array):
    leftSize = len(leftArray)
    rightSize = len(rightArray)

    i = 0
    j = 0
    k = 0

    while (i < leftSize) and (j < rightSize):
        if leftArray[i] < rightArray[j]:
            array[k] = leftArray[i]
            k += 1
            i += 1
        else:
            array[k] = rightArray[j]
            k += 1
            j += 1

    while i < leftSize:
        array[k] = leftArray[i]
        k += 1
        i += 1

    while j < rightSize:
        array[k] = rightArray[j]
        k += 1
        j += 1


# def mergeSort(array):
#     size = len(array)
#
#     if size < 2:
#         return
#
#     mid = size // 2
#     lArr = array[:mid]
#     rArr = array[mid:]
#
#     mergeSort(lArr)
#     mergeSort(rArr)
#     merge(lArr, rArr, array)

def mergeSort(array):
    size = len(array)

    if size < 2:
        return

    mid = size // 2
    lArr = array[:mid]
    rArr = array[mid:]

    mergeSort(lArr)
    mergeSort(rArr)
    merge(lArr, rArr, array)


def displayarray(arr):
    image = pygame.Surface(displaySize)
    rect = image.get_rect()
    barWidth = int(rect.width / len(arr) - 2)

    num = 0
    for k in range(0, rect.width, barWidth + 2):
        bar = pygame.Surface((barWidth, arr[num]))
        barShape = bar.get_rect()
        bar.fill(colors["red"])
        barShape.bottom = rect.height
        barShape.left = k

        image.blit(bar, barShape)
        num += 1

    display.fill(colors["white"])
    display.blit(image, rect)
    pygame.display.update()
    displayFPS.tick(144)


def main():
    arr = makeArray(240)
    #temparr = [0] * len(arr)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                pass
            if event.type == pygame.KEYUP:
                pass

        if sorted(arr) != arr:
            mergeSort(arr)
        else:
            displayarray(arr)


main()
