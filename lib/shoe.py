# lib/shoe.py

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.condition = "New"

    # brand getter and setter
    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if not isinstance(value, str):
            raise Exception("Brand must be a string")
        self._brand = value

    # size getter and setter
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, (int, float)):
            raise Exception("Size must be a number")
        self._size = value

    def cobble(self):
        """Repairs the shoe and sets condition to 'New'."""
        self.condition = "New"
        print("Your shoe is as good as new!")
