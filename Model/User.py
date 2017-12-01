class User:
    name = None
    id = None
    money = None

    # Constructor for user instance
    def __init__(self):
        self.name = "a"
        self.id = "a"
        self.pw = "wwg1226"
        self.money = 0

    # Set user data
    def setUser(self, name, id, money):
        self.name = name
        self.id = id
        self.money = money

    # get user data
    def getUser(self):
        return self.name, self.money
