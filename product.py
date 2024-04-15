class Product:
    def __init__(self, name, author):
        self.name = name
        self.author = author
        

    def toDBCollection(self):
        return{
            'name': self.name,
            'author': self.author
            
        }