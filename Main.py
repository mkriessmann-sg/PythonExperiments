import Classes
import DatabaseHandler


def IntegerInput(message:str) -> int :
    try: 
        temp = int(input(message))
        return temp
    except ValueError:
        print("Invalid Input!\n")
        temp = IntegerInput(message)
        return temp


def AddBook():
    title = input("Enter title of the book:")
    author = input("Enter author of the book:")
    number_available = IntegerInput("Enter the number of copies available:")
    price = IntegerInput("Enter the price of the book:")
    book = Classes.Book(DatabaseHandler.GetMaxID(), title, author, number_available, price)
    DatabaseHandler.create(book)


def AddNewspaper():
    title = input("Enter title of the Newspaper:")
    author = input("Enter author or publisher of the Newspaper:")
    number_available = IntegerInput("Enter the number of copies available:")
    publishingDate = IntegerInput("Enter the publishing date of the newspaper:")
    Newspaper = Classes.Newspaper(DatabaseHandler.GetMaxID(), title, author, number_available, publishingDate)
    DatabaseHandler.create()

def AddMagazine():
    title = input("Enter title of the magazine:")
    author = input("Enter author of the magazine:")
    number_available = IntegerInput("Enter the number of copies available:")
    item = IntegerInput("Enter the name of the enclosed item:")
    magazine = Classes.Book(DatabaseHandler.GetMaxID(), title, author, number_available, item)
    DatabaseHandler.create(magazine)


def AddItem():
    print("""Select desired acttion:
        b... add a book
        n... add a newspaper
        m... add a magazine
          
      """)
    readKey = input("Enter here please:")
    if readKey == "b":
        AddBook()
    elif readKey == "n" :
        AddNewspaper()
    elif readKey == "m" :
        AddMagazine()
    else: 
        print("Please enter one of the designated inputs.")
        AddItem()


def ShowItems():
        items = DatabaseHandler.read()
        for i in items : 
            if isinstance(i, Classes.Book):
                print("This Book is {0} by {1} and costs {2}. There are {3} copies available.  ID = {4}".format(i.title, i.author, i.price, i.numberAvailable, i.id))
        
            elif isinstance(i, Classes.Newspaper):
                print("This Newspaper is {0} by {1} and was published on {2}. There are {3} copies available. ID = {4}".format(i.title, i.author, i.published_day, i.numberAvailable, i.id))
            
            elif isinstance(i, Classes.Magazine):
                print("This Magazine is {0} by {1} and comes with a {2}. There are {3} copies available. ID = {4}.".format(i.title, i.author, i.item, i.numberAvailable, i.id))
            
            else:
                print("Unknown item type")

        temp = input("Press e to edit number available, any key to return")
        if temp == "e" :
            pass


def MainMenu():
    repeat = True
    while repeat :
        print("""Select desired acttion:
            a... add an item
            r... show list of items

        """)
        readKey = input("Enter here please:")
        if readKey == "a":
            AddItem()
        elif readKey == "r" :
            ShowItems()
        else: 
            print("Please enter one of the designated inputs.")
            MainMenu()

    temp = input("Press Y to continue:")
    if temp == "Y" :
        pass
    else :
        repeat = False


print("Welcome to the Library management.")
MainMenu()


