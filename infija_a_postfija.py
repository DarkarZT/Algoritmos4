class node:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Pila:
    def __init__(self):
        self.tope = None

    def esta_vacia(self):
        return self.tope is None

    def push(self, dato):
        nuevo_nodo = node(dato)
        nuevo_nodo.siguiente = self.tope
        self.tope = nuevo_nodo

    def pop(self):
        if self.esta_vacia():
            return None
        else:
            dato = self.tope.dato
            self.tope = self.tope.siguiente
            return dato

    def peek(self):
        if self.esta_vacia():
            return None
        else:
            return self.tope.dato

def infija_a_postfija(expresion):
    precedencia = {
        '+':1,
        '-':1,
        '*':2,
        "/":2
    }
    
    salida = []
    pila = Pila()
    tokens = expresion.split()
    
    for token in tokens:
        if token.lstrip('-').replace('.','').isdigit():
            salida.append(token)
            print(f"Token '{token}' es un número, se agrega a la salida: {salida}")
        elif token == '(':
            pila.push(token)
            print(f" '{token} -> pila")
        elif token == ')':
            while not pila.esta_vacia() and pila.peek() != '(':
                salida.append(pila.pop())
            pila.pop()
            print(f" '{token}' -> pop hasta '(' ")
        elif token in precedencia:
            while (not pila.esta_vacia() and pila.peek() != '(' and pila.peek() in precedencia and precedencia[pila.peek()]>= precedencia[token]):
                salida.append(pila.pop())
            pila.push(token)
            print(f" '{token}' (operador) -> pila")
    while not pila.esta_vacia():
        salida.append(pila.pop())
    resultado = ' '.join(salida)
    print(resultado)
            
infija_a_postfija("3 + (5 * 2)")
    