import unittest
class Area:
    def __init__(self,height,width):
        self.height=height
        self.width=width

    def __str__(self):
        return f"this is the height {self.height} and the width is {self.width}"

    def get_Area(self):
        return self.width * self.height
    
    def set_Width(self,width):
        self.width=width

    def set_Height(self,height):
        self.height=height

class GetArea(unittest.TestCase):
    def test_area(self):
        area1=Area(3,3)
        self.assertEqual(area1.get_Area(),9,"Incorrect area")
unittest.main()



