class Animal:
    def activity(self, name, type):
        self.name = name
        self.type = type
        return self.name, self.type

class Child_Animal(Animal):
    pass

abc = Child_Animal()
print(abc.activity("Tiger", "Hunting"))
