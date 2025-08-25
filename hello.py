class people:
    def __init__(self,name, birth):
        self.name = name
        self.birth = birth
    def __str__(self):
        return f'{self.name} {self.birth}'