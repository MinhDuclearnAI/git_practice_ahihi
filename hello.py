class people:
    def __init__(self,name, birth, job):
        self.__job = job
        self.__name = name
        self.__birth = birth
    def getName(self):
        return self.__name
    def __str__(self):
        return f'{self.__name} {self.__birth} {self.__job}'

class student(people):
    def __init__(self, name, birth, job, year):
        people.__init__(self, name, birth, job)
        self.year = year
    def __str__(self):
        return people.__str__(self) + f'{self.year}'

if __name__ == '__main__':
    n = int(input())
    DS = []
    for i in range(n):
        x = people(input(), input(), input())
        DS.append(x)
    for x in DS:
        print(x)
        print(x.getName().title())
    