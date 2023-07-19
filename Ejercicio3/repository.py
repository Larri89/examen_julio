class InMemoryRepository:
    def __init__(self):
        self.data = []

    def add(self, item):
        self.data.append(item)

    def get(self, id):
        for i in self.data:
            for key, value in i.items():
                if key == "id" and value == id:
                    datos = i
        return datos


"""if __name__ == '__main__':

    repository = InMemoryRepository()
    repository.add({"id": 1, "nombre": "Juan", "edad": 35})
    repository.add({"id": 2, "nombre": "Pedro", "edad": 42})
    print(repository.get(1))
    print(repository.get(2))"""

"La última parte esta comentada ya que me he centrado en la capa de red, pero no he conseguido que funcione," \
"sin la capa de red, va perfecto, es decir, ejecutando este fichero solamente con la parte comentada"



