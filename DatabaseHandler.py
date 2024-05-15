import psycopg2
import Classes
from config import config

#example code from tutorial
def create(item):
    connection = None
    try:
        params = config()
        print('Connecting to the postgreSQL database ...')
        connection = psycopg2.connect(**params)

        # create a cursor
        crsr = connection.cursor()
        if isinstance(item, Classes.Book):
            crsr.execute('INSERT INTO library ( id, title, author, number_available, special, type) VALUES ( \'{0}\', \'{1}\', \'{2}\', \'{3}\', \'{4}\', \'book\');'.format(item.id, item.title, item.author, item.numberAvailable, item.price))
            
        elif isinstance(item, Classes.Newspaper):
            crsr.execute('INSERT INTO library ( id, title, author, number_available, special, type) VALUES ( \'{0}\', \'{1}\', \'{2}\', \'{3}\', \'{4}\', \'newspaper\');'.format(item.id, item.title, item.author, item.numberAvailable, item.published_day))
            
        elif isinstance(item, Classes.Magazine):
            crsr.execute('INSERT INTO library ( id, title, author, number_available, special, type) VALUES ( \'{0}\', \'{1}\', \'{2}\', \'{3}\', \'{4}\', \'magazine\');'.format(item.id, item.title, item.author, item.numberAvailable, item.item))
        
        else:
            print("Unknown item type")
        
        crsr.close()
        connection.commit()
        print("Item saved successfully")
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
            print('Database connection terminated.')


def read():
    connection = None
    resultlist = []
    try:
        params = config()
        print('Connecting to the postgreSQL database ...')
        connection = psycopg2.connect(**params)

        # create a cursor
        crsr = connection.cursor()
        crsr.execute("SELECT * FROM Library;")
        for row in crsr.fetchall():
            if row[5] == "book" :
                b = Classes.Book(row[0],row[1],row[2],row[3],row[4])
                resultlist.append(b)
            elif row[5] == "newspaper" :
                b = Classes.Newspaper(row[0],row[1],row[2],row[3],row[4])
                resultlist.append(b)
            elif row[5] == "magazine" :
                b = Classes.Magazine(row[0],row[1],row[2],row[3],row[4])
                resultlist.append(b)
            else:
                print("unnown object")

        crsr.close()
        print("list fetched successfully")
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
            print('Database connection terminated.')
            return resultlist
        
def GetMaxID() -> int :
    connection = None

    try:
        params = config()
        print('Connecting to the postgreSQL database ...')
        connection = psycopg2.connect(**params)

        # create a cursor
        crsr = connection.cursor()
        crsr.execute("SELECT MAX(id) FROM Library;")
        temp = crsr.fetchone()
        print(temp)
        if temp is None: 
            returnValue = 1 
        else :
              returnValue = int(temp[0]) +1  
        print(returnValue)
        crsr.close()
        print("list fetched successfully")
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
            print('Database connection terminated.')
            return returnValue
        
def UpdateValue(item):
    connection = None
    try:
        params = config()
        print('Connecting to the postgreSQL database ...')
        connection = psycopg2.connect(**params)

        # create a cursor
        crsr = connection.cursor()
        print(item.id)
        print(item.numberAvailable)
        crsr.execute("UPDATE Library SET number_available = {0} WHERE id = {1};" .format(item.numberAvailable, item.id))

        crsr.close()
        print("data updated successfully")
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.commit()
            connection.close()
            print('Database connection terminated.')        


def GetItemByID(id) :
    connection = None
    result = None
    try:
        params = config()
        print('Connecting to the postgreSQL database ...')
        connection = psycopg2.connect(**params)

        # create a cursor
        crsr = connection.cursor()
        crsr.execute("SELECT * FROM Library where id = {0};".format(id))
        temp = crsr.fetchone()
        if temp[5] == "book" :
                result = Classes.Book(temp[0],temp[1],temp[2],temp[3],temp[4])
        elif temp[5] == "newspaper" :
                result = Classes.Newspaper(temp[0],temp[1],temp[2],temp[3],temp[4])
        elif temp[5] == "magazine" :
                result = Classes.Magazine(temp[0],temp[1],temp[2],temp[3],temp[4])
        else:
                print("unnown object")

        crsr.close()
        print("list fetched successfully")
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
            print('Database connection terminated.')
            return result
        
