#!/usr/bin/env python3

class Plant():
    def __init__(self, name, hei, age):
        self.name = name
        self.hei = hei
        self.age = age

    def show(self):
       print(f"{self.name}: {self.hei}, {self.age} days old")

def main():
    print("=== Garden Plant Registry ===")
    plant1 = Plant("Rose", "25cm", "30")
    plant2 = Plant("Sunflower", "30cm", "120")
    plant3 = Plant("Cactus", "10cm", "12")
    plant1.show()
    plant2.show()
    plant3.show()

if __name__ == "__main__":
    main()
