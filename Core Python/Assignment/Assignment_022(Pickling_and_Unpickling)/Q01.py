# Employee class

class Emp:
    def __init__(self, eid, ename, basic):
        self.eid = eid
        self.ename = ename
        self.basic = basic

    def __str__(self):
        return str(self.eid) + " " + self.ename + " " + str(self.basic)
