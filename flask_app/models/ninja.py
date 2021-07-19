from flask_app.config.mySQLconnect import MySQLConnection
class Ninja:
    def __init__(self, data):
        self.id=data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.age = data['age']
        self.dojo_id=data['dojo_id']
        self.updated_at=data['updated_at']
        self.created_at=data['created_at']
    @classmethod
    def get_all(cls):
        query='SELECT * FROM ninjas;'
        results=MySQLConnection.connectToMySQL('dojosnninjas').query_db(query)
        ninjas=[]
        for each in results:
            ninjas.append(cls(each))
        return ninjas
    @classmethod
    def insert(cls,data):
        idTag=len(cls.get_all())+1
        query='INSERT INTO ninjas (id, first_name, last_name, age, dojo_id) VALUES ('+str(idTag)+',%(first_name)s,%(last_name)s,%(age)s,%(dojoId)s);'
        MySQLConnection.connectToMySQL('dojosnninjas').query_db(query, data)
    @classmethod
    def getByDId(cls, data):
        query="SELECT * FROM ninjas WHERE dojo_id = %s"%(data)
        results=MySQLConnection.connectToMySQL('dojosnninjas').query_db(query)
        return results