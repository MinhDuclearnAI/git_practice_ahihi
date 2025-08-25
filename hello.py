class people:
    def __init__(self,name, birth):
        self.name = name
        self.birth = birth
    def __str__(self):
        return f'{self.name} {self.birth}'

if __name__ == '__main__':
    n = int(input())
    DS = []
    for i in n:
        x = people(input(), input())
        DS.append(x)
    for x in DS:
        print(x)
    