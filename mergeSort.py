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


def merge(arr, temp, left, mid, right):
    left_end = mid - 1
    temp_pos = left
    size = right - left + 1

    while left <= left_end and mid <= right:
        if arr[left] <= arr[mid]:
            temp[temp_pos] = arr[left]
            temp_pos += 1
            left += 1

        else:
            temp[temp_pos] = arr[mid]
            temp_pos += 1
            mid += 1
        displayarray(arr)

    while left <= left_end:
        temp[temp_pos] = arr[left]
        left += 1
        temp_pos += 1
        displayarray(arr)

    while mid <= right:
        temp[temp_pos] = arr[mid]
        mid += 1
        temp_pos += 1
        displayarray(arr)




def mergesort(array, temparr, left, right):
    if left < right:
        mid = int((left + right) / 2)
        mergesort(array, temparr, left, mid)
        mergesort(array, temparr, mid + 1, right)
        merge(array, temparr, left, mid + 1, right)

    else:
        pass



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
    #displayFPS.tick(144)


def main():
    arr = makeArray(240)
    temparr = [0] * len(arr)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                pass
            if event.type == pygame.KEYUP:
                pass

        if sorted(arr) != arr:
            mergesort(arr, temparr, 0, len(arr) - 1)
            print(arr)
        else:
            displayarray(arr)


main()
