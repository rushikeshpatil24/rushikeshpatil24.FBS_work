# Distance

class Distance:
    def __init__(self, km=0, m=0, cm=0):
        self.km = km
        self.m = m
        self.cm = cm

    def __add__(self, d):
        cm = self.cm + d.cm
        m = self.m + d.m + cm // 100
        cm = cm % 100
        km = self.km + d.km + m // 1000
        m = m % 1000

        return Distance(km, m, cm)

    def __str__(self):
        return str(self.km) + " km " + str(self.m) + " m " + str(self.cm) + " cm"

    def __del__(self):
        pass


d1 = Distance(2, 500, 50)
d2 = Distance(3, 700, 60)

d3 = d1 + d2

print("First distance:", d1)
print("Second distance:", d2)
print("Addition:", d3)
