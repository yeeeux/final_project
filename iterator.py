import os
class Fibonacci:
    """
    Итератор для чисел Фибоначи
    """

    def __init__(self, quantity):
        self.quantity = quantity
        self.counter = 0
        self.first_number = 0
        self.second_number = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter > self.quantity:
            raise StopIteration
        answer = self.first_number
        self.counter += 1
        self.first_number, self.second_number = self.second_number, self.first_number + self.second_number
        return answer


class Showfiles:
    """
    Show all files in chosen directory
    """

    def __init__(self, directory):
        self.__directory = directory
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        dirs = os.listdir(self.__directory)
        return next(iter(dirs))



if __name__ == "__main__":
    for item in Fibonacci(10):
        print(item)
    example = Fibonacci(5)
    print(next(example))
    print(next(example))
    print(next(example))
    print(next(example))
    file_exam = Showfiles("/home/yeeeux/git/Homework/iterators_and_generators")
    print(next(file_exam))
    print(next(file_exam))
    print(next(file_exam))

