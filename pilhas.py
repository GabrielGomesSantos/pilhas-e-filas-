#Lendo sobre pilhas vi que precisa se usar uma class para usar a pilhas (ou geralmente se usa)

class Pilha:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            print("A pilha está vazia.")
            return None

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            print("A pilha está vazia.")
            return None

    def size(self):
        return len(self.items)

# Manipulando 
pilhas = Pilha()

# Inserindo elementos na pilha
pilhas.push("LImpar a casa")
pilhas.push("Lavar o carro")
pilhas.push("Arrumar o quarto")

# Imprimindo o topo da pilha
print("Topo da pilha:", pilhas.peek())

# # Removendo elementos da pilha
print("Removido:", pilhas.pop())
print("Removido:", pilhas.pop())

# # Verificando se a pilha está vazia
print("A pilha está vazia?", pilhas.isEmpty())
