#Write a program that uses a Person class to keep track of a person's name, age, and address.

class Person():
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        
    def set_name(self, name):
        self.name = name
        return self
        
    def get_name(self):
        return self.name    
    
    def set_age(self, age):
        self.age = age
        return self
        
    def get_age(self):
        return self.age
    
    def set_address(self, address):
        self.address = address
        return self
        
    def get_address(self):
        return self.address
    
def main():
    matthieu = Person("Matthieu", 19, "somewhere")
    print(matthieu.get_age())
    matthieu.set_age(20)
    print(matthieu.get_age())

if __name__ == "__main__":
    main()