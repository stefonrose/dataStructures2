import random
import pygame

displaySize = (width, height) = (720, 480)
display = pygame.display.set_mode(displaySize)
displayFPS = pygame.time.Clock()
pygame.display.set_caption("Selection Sort")

colors = {"white": (255, 255, 255), "black": (0, 0, 0), "red": (255, 0, 0), "green": (0, 255, 0), "blue": (0, 0, 255)}

items = 240


def makeArray(size):
    array = [2 * x for x in range(0, size)]
    random.shuffle(array)
    return array


class selectionSort():
    def __init__(self, arrayToSort):
        self.array = arrayToSort
        self.arraySize = len(arrayToSort)
        self.index = 1

        self.image = pygame.Surface(displaySize)
        self.rect = self.image.get_rect()
        self.rect.top = 0
        self.barWidth = int(self.rect.width / self.arraySize - 2)  # self.rect.width // (self.arraySize - 2)

        self.complete = False

    def refresh(self):
        if self.index < self.arraySize:
            self.image.fill(colors["white"])

            smallestIndex = self.index
            for j in range(self.index + 1, self.arraySize):
                if self.array[j] < self.array[smallestIndex]:
                    smallestIndex = j

            temp = self.array[self.index]
            self.array[self.index] = self.array[smallestIndex]
            self.array[smallestIndex] = temp

            self.index += 1

            num = 0
            for k in range(0, self.rect.width, self.barWidth + 2):
                bar = pygame.Surface((self.barWidth, self.array[num]))
                barShape = bar.get_rect()
                bar.fill(colors["red"])
                if num >= self.index:
                    bar.fill(colors["blue"])
                barShape.bottom = self.rect.height
                barShape.left = k

                self.image.blit(bar, barShape)
                num += 1

        else:
            self.complete = True
            pass

    def draw(self):
        display.blit(self.image, self.rect)


def main():
    runtimeArray = makeArray(items)
    runtimeSort = selectionSort(runtimeArray)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                pass
            if event.type == pygame.KEYUP:
                pass
        runtimeSort.refresh()
        runtimeSort.draw()
        pygame.display.update()
        displayFPS.tick(144)
        if runtimeSort.complete:
            quit()


main()


