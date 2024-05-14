class Item:
    def  __init__(self,title, author,numberAvailable):
        self.title = title
        self.author = author
        self.numberAvailable = numberAvailable

    def lend_out(self):
        return ++self.numberAvailable 
    def bring_back(self):
        return --self.numberAvailable
    def display_information():
        pass

class Book(Item):
            def __init__(self, title, author, numberAvailable, price):
                 super().__init__(title, author, numberAvailable)
                 self.price = price
            
            def display_information(self):
                 print("This book is {0} by {1} and costs {2}. There are currently {3} copies available." .format(self.title, self.author, self.price, self.numberAvailable))

class Newspaper(Item):
            def __init__(self, title, author, numberAvailable, published_day):
                  super().__init__(title, author, numberAvailable)
                  self.published_day = published_day

            def display_information(self):
                  print("This Newspaper is {0} by {1} and was published on {2}. There are currently {3} copies available." .format(self.title, self.author, self.published_day, self.numberAvailable))

class Magazine(Item):
            def __init__(self, title, author, numberAvailable, item):
                  super().__init__(title, author, numberAvailable)
                  self.item = item

            def display_information(self):
                  print("This Newspaper is {0} by {1} and includes the item {2}. There are currently {3} copies available." .format(self.title, self.author, self.item, self.numberAvailable))
        