import sys
import math
import time

file_path = sys.argv[1]

operation = sys.argv[2]
curval = 0
maxcount = 0
modecount = 0
mode = []
valGlobal = 0
countGlobal = 0
max_count = 0

i = 0
try:
    r = int(sys.argv[3])
    hay_r = True
except IndexError:
    hay_r = False


# Clase de Nodo
class newNode:

    # Constructor para crear un nodo nuevo
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# funcion para insertar en el nodo
def insert(node, key):
    # Si el abb esta vacio, retorna un nuevo nodo
    if (node is None):
        return newNode(key)
    # de otra forma, recorre el arbol
    if (int(key) < node.data):
        node.left = insert(node.left, key)
    elif (int(key) > node.data):
        node.right = insert(node.right, key)
    # devuelve el puntero al nodo
    return node


# funcion para contar nodos en el abb
# usando recorrido inorder
# por ser inorder tarda O(N)
def suma(root):
    if (root is None):
        return 0
    return (root.data + suma(root.left) + suma(root.right))


def counNodes(root):
    # Inicializa el contador en 0
    count = 0
    if (root is None):
        return count
    current = root
    while (current is not None):
        if (current.left is None):
            # Cuenta el nodo si el hijo izq es None
            count += 1
            # Se mueve a la derecha
            current = current.right
        else:
            # Encuentra el predecesor inorder de la actual.
            pre = current.left
            while (pre.right is not None and pre.right != current):
                pre = pre.right
            # Hace al actual como hijo derecho del
            # predecesor inorder
            if(pre.right is None):
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
    while (current.right is not None):
        current = current.right

    return current.data


# Implementación:
# 1- Contar el número de nodos en el BST dado usando Inorder
# 2- Luego recorro Inorder una vez más contando los nodos y verificando
#    si cuenta es igual al punto medio. Para considerar el número par de nodos,
#    se utiliza un puntero adicional que apunta al nodo anterior
# O(N) en tiempo y O(1) en espacio.
def mediana(root):
    if (root is None):
        return 0
    count = counNodes(root)
    currCount = 0
    current = root
    prev = root
    while (current is not None):
        if (current.left is None):
            # contador del nodo actual
            currCount += 1
            # se fija si el nodo actual es la mediana
            if (count % 2 != 0 and currCount == (count + 1) // 2):
                return prev.data
            elif (count % 2 == 0 and currCount == (count // 2) + 1):
                return (prev.data + current.data) // 2
            prev = current
            current = current.right
        else:
            pre = current.left
            while (pre.right is not None and pre.right != current):
                pre = pre.right
            if (pre.right is None):
                pre.right = current
                current = current.left
            else:
                pre.right = None
                prev = pre
                currCount += 1
                if (count % 2 != 0 and currCount == (count + 1) // 2):
                    return current.data
                elif (count % 2 == 0 and currCount == (count // 2) + 1):
                    return (prev.data + current.data) // 2
                prev = current
                current = current.right


# Temporal : O(n)
# Espacial : O(n)
def moda(root):
    ans = []
    inorder(root, ans)
    return ans


def visit(valor, ans):
    global valGlobal
    global countGlobal
    global max_count
    if (countGlobal > 0 and valor == valGlobal):
        countGlobal += 1
    else:
        valGlobal = valor
        countGlobal = 1

    if (countGlobal > max_count):
        max_count_ = countGlobal
        ans.clear()

    if (countGlobal == max_count):
        ans.append(valor)


def inorder(root, ans):
    if (root is None):
        return
    inorder(root.left, ans)
    visit(root.data, ans)
    inorder(root.right, ans)


def media(root):    # O(N) + O(log N)
    sumatoria = int(suma(root))
    cont = counNodes(root)
    promedio = sumatoria / cont
    return promedio


def desviacion_estandar(root):
    suma1 = suma(root)
    cont = counNodes(root)
    media = suma1 / cont
    suma_distancias = 0
    suma_distancias = aux_desviacion(root, media)
    media_de_suma = suma_distancias / cont
    # sqrt O(log n)
    return (math.sqrt(media_de_suma))

# Es la misma idea que suma


def aux_desviacion(root, media):
    if (root is None):
        return 0
    dist_media = root.data - media
    suma_dist = + (dist_media ** 2)
    return (suma_dist +
            aux_desviacion(root.left, media) +
            aux_desviacion(root.right, media))


def variaciones_r_elementos_sin_repeticion(root, r):
    n = counNodes(root)

    if r >= n:
        print("Numero invalido.")
        raise SystemExit

    variaciones = []

    # Mi lista de indices va a tener las posiciones de la proxima
    # variacion
    indices = list(range(r))    # genera una lista asi:
    # lista = [0,1,2,3,...,r]
    # Trivial, los primeros r elementos de la lista
    lista = listNodes(root)

    variaciones.append(list(lista[i] for i in indices))

    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return

        indices[i] += 1

        for j in range(i + 1, r):
            indices[j] = indices[j - 1] + 1
            variaciones.append(list(lista[i] for i in indices))

    return variaciones


def variaciones_r_elementos(root, r):
    n = counNodes(root)

    if r >= n:
        print("Numero invalido.")
        raise SystemExit

    variaciones = []
    indices = list(range(r))
    lista = listNodes(root)

    # Inicializo los r indices en 0, ya que es el primer caso trivial
    indices = [0] * r

    variaciones.append(list(lista[i] for i in indices))

    while True:
        for i in reversed(range(r)):
            if indices[i] != n - 1:
                break
        else:
            return

        indices[i:] = [indices[i] + 1] * (r - i)

        variaciones.append(list(lista[i] for i in indices))

    return variaciones

# devuelve una lista de los valores
# de los nodos usando recorrido inorder
# por ser inorder tarda O(N)
# No tengo pruebas de que esto anda,
# pero tampoco dudas (mentira)


def listNodes(root):
    lista = []
    if (root is None):
        return count
    current = root
    while (current is not None):
        lista.append(current.data)
        if (current.left is None):
            # se mueve a la derecha si el
            # hijo izq no existe
            current = current.right
        else:
            # Encuentra el predecesor inorder de la actual.
            pre = current.left
            while (pre.right is not None and pre.right != current):
                pre = pre.right
            # Hace al actual como hijo derecho del
            # predecesor inorder
            if(pre.right is None):
                pre.right = current
                current = current.left
            else:
                pre.right = None
                # Aumenta el contador si el nodo
                # actual tiene que ser visitado
                current = current.right
    return lista


# Entran todos los elementos del arbol
# Importa el orden
# No se repiten los elementos
# Temporal : O(n!)
# Espacial : O(n!)
def permutaciones(root):  # O(n!)
    permutaciones = []
    lista = listNodes(root)

    def swap(n1, n2):
        tmp = lista[n1]
        lista[n1] = lista[n2]
        lista[n2] = tmp

    def generar_permutaciones(k, lista):
        if k == 1:
            permutaciones.append(lista)
            return

        for i in range(0, k - 1):
            generar_permutaciones(k - 1, lista)

            if i % 2 == 0:
                swap(i, k - 1)
            else:
                swap(0, k - 1)

    # Llamo a la funcion
    generar_permutaciones(len(lista), lista)

    return permutaciones


# encuentra la suma de todos los elementos.
# tarda O(log N) en caso normal
# y en el peor caso es O(N)
def cargar_numeros(file_path):  # O(n)
    file = open(file_path, "r")
    root = None
    lines = file.readlines()

    for line in lines:  # ver esto root deberia estar fuera del ciclo
        number_tmp = line.rstrip()
        if (root is None):
            root = newNode(int(number_tmp))
            continue
        insert(root, int(number_tmp))

    file.close()
    return root


def archivo_resultados(resultados):  # O(1)
    file_path = "resultados.txt"

    file = open(file_path, 'w+')

    if isinstance(resultados, str):
        file.write(resultados)
    else:
        file.write(str(resultados))

    file.close()

    raise SystemExit


if __name__ == "__main__":
    root = cargar_numeros(file_path)

    operations_without_r = {
        "maximo": maximo,
        "media": media,
        "moda": moda,
        "mediana": mediana,
        "desviacion_estandar": desviacion_estandar,
        "permutaciones": permutaciones
    }

    operations_with_r = {
        "variaciones": variaciones_r_elementos_sin_repeticion,
        "variaciones_con_repeticion": variaciones_r_elementos
    }

    start = time.time()
    if hay_r and operation in operations_with_r:
        resultado = operations_with_r[operation](root, r)
    elif not hay_r and operation in operations_without_r:
        resultado = operations_without_r[operation](root)
    else:
        print("Argumentos invalidos")
    end = time.time()
    abb = counNodes(root)
    print("Tiempo de ejecucion de " + operation + " en abb con " +
          str(abb) + " elementos : " + str(end - start))
    archivo_resultados(resultado)



main()
