from random import randint
class EvenNumbers:
    start = 0
    end = 1

    def __init__(self, start, end):
        self.start = start
        self.end = end
        print(f'start: {self.start}, end: {self.end}')
        if self.start > self.end:
            p = self.start
            self.start = self.end
            self.end = p
            print(f'start больше, чем end, меняем местами: start {self.start}, end {self.end}')

        if self.start == self.end:
            self.end += 5
            print('start равен end, прибавляем 5 к end')


    def __iter__(self):
        self.i = en.start - 1
        return self

    def __next__(self):
        self.i += 1

        if self.i % 2 == 0:
            return f'{self.i}'

        if self.i == en.end:
            raise StopIteration()



en = EvenNumbers(randint(0, 30), randint(0,30))

for i in range(en.start, en.end+1):
    if i % 2 == 0:
        print(i)
