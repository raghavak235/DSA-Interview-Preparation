
class HashTable:
    def __init__(self):
        self.max= 10
        self.arr=[None for i in range(self.max)]

    def hash_function(self, key):
        summation = 0
        m=10
        for char in key:
            summation += ord(char)

        return summation%m

    def addItem(self, key, value):
        h = self.hash_function(key)
        self.arr[h]=value


    def getItem(self, key):
        h = self.hash_function(key)
        return self.arr[h]


has_obj=HashTable()
has_obj.addItem('March 2024',123)
has_obj.getItem('March 2024')