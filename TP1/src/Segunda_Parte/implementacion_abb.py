import sys
import math

file_path = sys.argv[1]

operation = sys.argv[2]

modecount = 0

# Clase de Nodo                                     
class newNode:  
  
    # Constructor para crear un nodo nuevo
    def __init__(self, data):  
        self.data = data  
        self.left = None
        self.right = None
  
# funcion para insertar en el nodo 
def insert(node,key): 
  
    # Si el abb esta vacio, retorna un nuevo nodo 
    if (node == None): 
        return newNode(key) 
  
    # de otra forma, recorre el arbol
    if (key < node.data): 
        node.left = insert(node.left, key) 
    elif (key > node.data): 
        node.right = insert(node.right, key) 
  
    # devuelve el puntero al nodo
    return node 
  
# funcion para contar nodos en el abb
# usando recorrido inorder
# por ser inorder tarda O(N)
def counNodes(root): 
  
    # Inicializa el contador en 0 
    count = 0
  
    if (root == None): 
        return count 
  
    current = root 
    while (current != None): 
      
        if (current.left == None): 
          
            # Count node if its left is None 
            count+=1
  
            # Move to its right 
            current = current.right 
          
        else:      
            # Encuentra el predecesor inorder de la actual.
            pre = current.left 
  
            while (pre.right != None and pre.right != current): 
                pre = pre.right 
  
            # Hace al actual como hijo derecho del 
            # predecesor inorder
            if(pre.right == None): 
              
                pre.right = current 
                current = current.left 
            else: 
              
                pre.right = None
  
                # Aumenta el contador si el nodo                
                # actual tiene que ser visitado
                count += 1
                current = current.right 
  
    return count 
  
# Implementacion:
# 1- Bajo todo a la derecha, donde va a estar el maximo 
# Tarda O(log N) (caso normal)
# Tarda O(N) en el peor caso
# El mejor caso es O(1) (la raiz es el maximo)
def maximo(node):
    current = node
    while (current.right != None):  
        current = current.right; 
      
    return (current.data); 



# Implementación:
# 1- Contar el número de nodos en el BST dado usando Inorder
# 2- Luego recorro Inorder una vez más contando los nodos y verificando 
#    si cuenta es igual al punto medio. Para considerar el número par de nodos, 
#    se utiliza un puntero adicional que apunta al nodo anterior
# O(N) en tiempo y O(1) en espacio.    
def mediana(root): 
    if (root == None): 
        return 0
    count = counNodes(root) 
    currCount = 0
    current = root 
  
    while (current != None): 
      
        if (current.left == None): 
          
            # contador del nodo actual
            currCount += 1
  
            # se fija si el nodo actual es la mediana
            if (count % 2 != 0 and currCount == (count + 1)//2): 
                return prev.data 
  
            elif (count % 2 == 0 and currCount == (count//2)+1): 
                return (prev.data + current.data)//2
  

            prev = current 
            current = current.right 
          
        else: 

            pre = current.left 
            while (pre.right != None and 
                    pre.right != current): 
                pre = pre.right 
  
            if (pre.right == None): 
              
                pre.right = current 
                current = current.left 
            else: 
              
                pre.right = None
                prev = pre 
                currCount+= 1
  
                if (count % 2 != 0 and currCount == (count + 1) // 2 ): 
                    return current.data 
  
                elif (count%2 == 0 and currCount == (count // 2) + 1): 
                    return (prev.data+current.data)//2
  
                prev = current 
                current = current.right 


# complejidad temporal: O(N) (?)
# complejidad espacial: O(N) (?)
# ver peor y mejor caso
def Moda(root):
    first(root)
    mode = int(modecount)
    curcount = 0
    modecount = 0
    second(root)
    return mode


def first(root):
    if (root == None):
         return
    first(root.left)
    val = root.val
    if (curval != val):
        curval = val
        curcount = 0
    curcount += 1
    if (curcount > maxcount):
        maxcount = curcount
        modecount = 1
    elif (curcount == maxcount):
        modecount += 1
    first(root.right)


def second(root):

    if (root == None): 
        return
    second(root.left)
    val = root.val
    if (curval != val):
        curval = val
        curcount = 0
    curcount += 1
    if (curcount == maxcount):
        mode[modecount] = curval
        modecount += 1
    second(root.right)

def Media(root):    # O(N) + O(log N)
    suma = suma(root)
    cont = counNodes(root)
    promedio = suma / cont
    return promedio
 
# encuentra la suma de todos los elementos.
# ehh ponele que esto tarda O(log N) en caso normal
# y en el peor caso es O(N)
def suma(root):  
    if (root == None): 
        return 0
    return (root.key + suma(root.left) +  suma(root.right))  



def cargar_numeros(file_path):  # O(n)
    file = open(file_path, "r")

    lines = file.readlines()

    for line in lines: # ver esto root deberia estar fuera del ciclo 
        number_tmp = line.rstrip()
        root = newNode(number_tmp)
        insert(root, number_tmp) 

    file.close()


def main():
    cargar_numeros(file_path)

    switch = {
        "maximo": "maximo",
        "media": "media",
        "moda": "moda",
        "mediana": "mediana",
        "desviacion_estandar": "desviacion_estandar",
        "permutaciones": "permutaciones",
        "variaciones": "variaciones_r_elementos_sin_repeticion",
        "variaciones_con_repeticion": "variaciones_con_repeticion"

    }

    func = switch.get(operation, lambda: "Operacion invalida")

    func()


main()
