class Fila:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            print("A fila está vazia.")
            return None

    def front(self):
        if not self.isEmpty():
            return self.items[0]
        else:
            print("A fila está vazia.")
            return None

    def size(self):
        return len(self.items)

# manipulando
fila = Fila()

# Inserindo elementos na fila
fila.enqueue("LImpar a casa")
fila.enqueue("Lavar o carro")
fila.enqueue("Arrumar o quarto")

# Imprimindo o elemento da frente da fila
print("Frente da fila:", fila.front())

# Removendo elementos da fila
print("Removido:", fila.dequeue())
print("Removido:", fila.dequeue())

# Verificando se a fila está vazia
print("A fila está vazia?", fila.isEmpty())
