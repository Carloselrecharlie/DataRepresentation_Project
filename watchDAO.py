import mysql.connector
class WatchDAO:
    db=""
    def __init__(self): 
        self.db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1Recontrams",
        database="datarepresentation"
        )
    
            
    def create(self, values):
        cursor = self.db.cursor()
        sql="INSERT INTO watch (gender, display, price) values (%s,%s,%s)"
        cursor.execute(sql, values)
		
        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql="SELECT * FROM watch"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            print(result)
            returnArray.append(self.convertToDictionary(result))

        return returnArray

    def findByID(self, id):
        cursor = self.db.cursor()
        sql="SELECT * FROM watch WHERE id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDictionary(result)

    def update(self, values):
        cursor = self.db.cursor()
        sql="UPDATE watch SET gender= %s,display=%s,price=%s  where id = %s"
        cursor.execute(sql, values)
        self.db.commit()
		
    def delete(self, id):
        cursor = self.db.cursor()
        sql="DELETE FROM watch WHERE id = %s"
        values = (id,)

        cursor.execute(sql, values)

        self.db.commit()
        print("Deleted")

    def convertToDictionary(self, result):
        colnames=['id','Gender','Display',"Price"]
        item = {}
        
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        
        return item
        
watchDAO = WatchDAO()