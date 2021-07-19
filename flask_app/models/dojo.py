from flask_app.config.mySQLconnect import MySQLConnection
class Dojo:
    def __init__(self, data):
        self.id=data['id']
        self.name=data['name']
        self.updated_at=data['updated_at']
        self.created_at=data['created_at']
    @classmethod
    def get_all(cls):
        query="SELECT * FROM dojos"
        results=MySQLConnection.connectToMySQL('dojosnninjas').query_db(query)
        dojos=[]
        for each in results:
            dojos.append(cls(each))
        return dojos
    @classmethod
    def insert(cls,data):
        query='INSERT INTO dojos (id,name) VALUES (%(id)s,%(name)s);'
        dictionary={'name':data, 'id':(len(cls.get_all())+1)}
        MySQLConnection.connectToMySQL('dojosnninjas').query_db(query, dictionary)
    @classmethod
    def getById(cls, id):
        query='SELECT * FROM dojos WHERE id = %s'%(id)
        results=MySQLConnection.connectToMySQL('dojosnninjas').query_db(query)
        return results