class Product:
    def __init__(self, id, name, author, date):
        self.id = id
        self.name = name
        self.author = author
        self.date = date
        
        

    def toDBCollection(self):
        return{
            'id' : self.id,
            'name': self.name,
            'author': self.author,
            'date' : self.date
            
        }