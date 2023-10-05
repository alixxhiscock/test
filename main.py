#!/usr/bin/env python3

class Dog:
    def __init__(self,name, color):
        self.color = color
        self.name = name
    def speak(self):
        print(f"my name is {self.name}")

if __name__ == '__main__':
    peter = Dog("Peter", "Black")
    peter.speak()