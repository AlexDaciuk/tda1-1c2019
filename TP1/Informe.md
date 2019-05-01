### (75.29 / 95.06) - Teoría de Algoritmos - FIUBA

# Informe Trabajo Práctico 1

## Grupo : 3 + 1
## Integrantes
  * Matias Onorato (93179)
  * Juan Cruz Opizzi (99807)
  * Francisco Strambini (92135)
  * Alexis Daciuk (97630)

---

## Introducción: Algoritmo Gale-Shapley
### El problema
En 1962 Gale y  Shapley estudiaron el problema de emparejar dos grupos, entendiendo como emparejamiento la asignación de un individuo de un grupo con el otro, y viceversa.

En este problema tenemos dos grupos, ***A*** y ***B***, de *n* individuos cada uno, siendo *n* la dimensión del problema.  Además, cada individuo del grupo ***A*** y ***B*** tiene una lista de preferencia donde ordena de forma discriminada, estricta y de forma decreciente a cada individuo del del grupo al cual no pertenece, según su orden de preferencia para formar pareja.

El objetivo del problema consiste es crear un emparejamiento en el que cada pareja sea satisfactoria para los individuos que la crean en base a las preferencias de cada uno. es decir crear un emparejamiento estable.

Para el problema planteado, Gale y shapley lograron implementar un algoritmo que logra este emparejamiento mencionado.

```
Inicialmente todos los proponentes estan sin emparejar

MIENTRAS (exista un proponente sin pareja)
  -propone a los que no haya propuesto segun su
  orden de preferencia.  
  SI (el propuesto esta libre)
    se acepta propuesta
  SI NO
    SI (el propuesto prefiere a su actual pareja)
      no se arma la pareja
    SI NO
      se arma la pareja
    FIN SI
  FIN SI
FIN MIENTRAS
```

para este algoritmo, Gale y shapley demostraron que:

* El algoritmo termina en un número finito de pasos y termina, a la sumo, en *n^2* pasos.
* El algoritmo produce un emparejamiento estable, es decir que no existe ningun par bloqueante entre un individuo de ***A*** y otro de ***B*** que quiera romper un emparejamiento constituido.
* El algoritmo Gale-Shapley genera un emparejamiento optimo para los proponentes y pesimo para los propuestos.

## Parte 1 - Resolución del problema del Club “PICA-PICA”
### 1.1 Variante de Gale-Shapley con Indiferencias

Encontramos que podemos ejecutar una variante conocida del algoritmo de Gale -Shapley si tomamos un correcto criterio de desempate en caso de ser necesario.

Si a diferencia del algoritmo tradicional, en nuestra variante permitimos más de un jugador en las lista de preferencias con un mismo numero de preferencia, ordenada de forma decreciente, es decir dado *a* ∈ ***A***, *x,y,z* ∈ ***B*** jugadores de los Grupos ***A*** y ***B***, un diccionario `{p:preferencia, j:jugador}` formando la lista `a → {p:1, j:x} →{p:2, j:y} →{p:2, j:z}` como lista de referencia de ***A***, el algoritmo de pareo con indiferencias sigue ofreciendo un correcto funcionamiento, entregando una pareja para cada jugador en un pareo conocido como debilmente estable en los casos donde exista indiferencia. Este pareo sigue ofreciendo un pareo estable por definición, ya que no altera el funcionamiento del algoritmo de Gale-shapley al momento de su comprobación de estabilidad.

La variante es representada por el algoritmo:

```
Inicialmente todos los proponentes estan sin emparejar

MIENTRAS (exista un proponente sin pareja)
  -propone a los que no haya propuesto segun su
  orden de preferencia.  
  SI (el propuesto esta libre)
    se acepta propuesta
  SI NO
    SI (el propuesto prefiere debilmente a su actual pareja)
      no se arma la pareja
    SI NO
      se arma la pareja
    FIN SI
  FIN SI
FIN MIENTRAS
```


### 1.2 - Estabilidad de la Variante
Por lo visto en la introducción, el algoritmo de Gale-Shelley es por naturaleza estable, por lo cual analizamos nuestra variación para ver si su nueva implementación produce algún cambio que afecte su estabilidad a la hora de encontrar un posible bloqueo luego de formadas las parejas.

Si definimos como criterio de desempate en el pareo (y por ende al consultar la preferencia) que la preferencia del proponente tiene que ser estrictamente mayor a la referencia de la pareja del propuesto, por más que esta sea la misma en más de un caso, el algoritmo de Gale-Shapley no encuentra alteraciones en su estabilidad. Esto se debe a que con el criterio mencionado, ante cada intento de formar una pareja entre los jugadores de ambos grupos, al tener que ser esta preferencia estrictamente mayor,  ningún jugador podrá cambiar su pareja para ninguno de los casos en los que se repita ese mismo valor de preferencia nen un pareo debilmente estable, conservándose la estabilidad al no generarse ningún bloqueo.

Por el contrario, si se permite en un caso de empate que se pueda cambiar de pareja si la preferencia además de ser mayor pueda ser igual, algunas preferencias con el mismo número de preferencia podrían querer cambiar la pareja que forma la primera preferencia con número de preferencia repetida, rompiendo la estabilidad.

### 1.3 - Complejidad de la Variante
La ejecución del algoritmo de Gale- Shappley se puede pensar como el recorrido de una matriz formada por las listas de preferencias de los integrantes de un grupo, por ejemplo *a,b,c* ∈ ***A*** -  *x,y,z* ∈ ***B*** representaría la matriz *3x3*

| a | b | c |
|:-:|:-:|:-:|
| {p: 1, j: x} | {p:1, j:x} | {p:1, j:z} |
| {p: 2, j: y} | {p:1, j:z} | {p:1, j:y} |
| {p: 2, j: z} | {p:3, j:y} | {p:2, j:x} |

para la cual se empieza a recorrer cada una de las preferencias hasta que todos los elementos de ***A*** forman pareja. En cada caso se ejecuta una simple comparación de complejidad *O(1)* para formar pareja, y en el peor de los casos hay que recorrer toda la matriz para que todas las parejas queden formadas.

por lo tanto el algoritmo de Gale-Shapley presenta una complejidad *O(n^2)*, siendo *n* el número de integrantes de un grupo.

### 1.4 - ¿Es posible un desempate mediante un tiro de moneda?
Esta opción no es posible.

Al igual que el caso considerado al final del punto 1.2, no podemos permitir que ante un empate se generen casos donde el criterio de selección de pareja no sea arbitrario. Si permitimos que el azar resuelva un empate en una lista de preferencias, en lugar de constatar ante cada caso de cambio de pareja el pareo debilmente estable antes mencionado, se podrían generar casos de bloqueo que romperían la estabilidad del pareo.

### 1.5 - Desarrolle un algoritmo que dado una pareo y las preferencias determina si el mismo es matching estable. ¿Qué complejidad algorítmica tiene?

ver 1.6 para ejecutar el algoritmo

#### Análisis de Complejidad

analizamos por partes:

hilo la parte inicial en el main.py

```
    if punto == "1.5":
        print('Parejas por archivo de pareo:')
        nombre_archivo_pareo = sys.argv[3]        
        grupoA, grupoB = armarParejas(jugadores, nombre_archivo_pareo) # O(armarParejas(n,a))

    if grupoA != None:           
        for jugador in grupoA: # O(n)
            print(jugador.nombre + ", " + jugador.pareja.nombre)
        print ('Es estable?:', parejasEstables(grupoA,grupoB)) # O(parejasEstables(n,n))

```

*O(algoritmo 1.5) = O(armarParejas(n,a)) + O(n) + O(parejasEstables(n,n))*

carga de parejas por archivo
```
def armarParejas(jugadores, nombre_archivo_pareo):    
    grupoA = jugadores[slice(0,len(jugadores)//2)] # O(1)
    grupoB = jugadores[slice(len(jugadores)//2,len(jugadores))] # O(1)

    archivo_pareo = open(Path("../../assets/txt/" + nombre_archivo_pareo),"r") # O(1)
    lineas_pareo = archivo_pareo.read().splitlines() # O(n)

    for pareo in lineas_pareo: # O(n)
        jugador1 = next(filter(lambda x: x.nombre == pareo.split(',')[0].strip(),jugadores)) # O(n)
        jugador2 = next(filter(lambda x: x.nombre == pareo.split(',')[1].strip(),jugadores)) # O(n)
        jugador1.formarPareja(jugador2) # O(1)

    return grupoA, grupoB # O(1)
```

*O(armarParejas(n,a)) = O(n^2)*

```
def parejasEstables(grupoA, grupoB):
    for jugadorA in grupoA: # O(n)
        for jugadorB in grupoB: # O(n)
            if jugadorA.pareja != jugadorB and jugadorA.prefiere(jugadorB) and jugadorB.prefiere(jugadorA): # O(1)
                return False
    return True   
```

*O(parejasEstables(n,n)) =  O(n^2)*

por lo tanto

*O(algoritmo 1.5) = O(n^2) + O(n) + O(n^2)*
*O(algoritmo 1.5) = O(n^2)*


### 1.6 - Programación de los algoritmos

instrucciones ejecución del TP:

Primero, generar los archivos de preferencias y ranking general

```
cd TP1/src/tools
python player_generator.py
```

el mismo guarda un *archivo_jugadores.rank* en la carpeta *TP1/assets/txt* con el nombre segun indica el tp, por ejemplo *20_jugadores.rank* y un archivo de preferencia por jugador *jugador_ranking.pref*

#### punto 1.1
luego, para ejecutar el punto 1.1 realizar los siguientes pasos:

```
cd TP1/src/Primera_Parte
python main.py 1.1 archivo_jugadores.rank
```

se imprime en pantalla las parejas que forman un pareo estable y se comprueba algoritmicamente dicha estabilidad.

#### punto 1.5
para ejecutar el punto 1.5 realizar los siguientes pasos:
Colocar un archivo *parejas_alternativas.txt* en el directorio *TP1/assets/txt* con las parejas propuestas, junto a los archivos de jugadores y preferencias.

luego ejecutar los siguientes comandos:

```
cd TP1/src/Priemra_Parte
python main.py 1.5 archivo_jugadores.rank parejas_alternativas.txt
```

La salida del programa imprimira las parejas cargadas y si las mismas son estables o no segun sus archivos de preferencias.


### 1.7 - ¿Tiene su programa la misma complejidad algorítmica que la teórica?

Analizo complejidad del algoritmo de Gale-Shapley

```
def armarParejasEstables(jugadores):    
    grupoA = jugadores[slice(0,len(jugadores)//2)] # O(1)
    grupoB = jugadores[slice(len(jugadores)//2,len(jugadores))] # O(1)

    proponentesLibres = len(grupoA)

    while proponentesLibres>0 : # O(n)
        for proponente in grupoA: # O(n)
            if proponente.pareja is None: # O(1)
                propuesto = proponente.proximoCandidato() # O(1)
                if propuesto.pareja is None: # O(1)
                    proponente.formarPareja(propuesto) # O(1)
                    proponentesLibres -= 1  # O(1)
                elif propuesto.prefiere(proponente): # O(n) (prefiere(a) recorre la lista de jugadores)
                    proponente.formarPareja(propuesto) # O(1)                
    return grupoA, grupoB
```

*O(armarParejasEstables(n)) = O(n^3)*

Esta complejidad difiere de la complejidad teórica de gale shapley tradicional, que es O(n^2), porque a diferencia de esta, en este caso la complejidad de comparar las preferencias pasa de O(1) (comparar index en un vector) a O(n) (buscar los números de preferencia de cada jugador y su pareja y compararlo)

## Parte 2 - Funciones matemáticas / estadísticas

### 2.1 - Proponga algoritmos para cada una de las resoluciones

los algoritmos estan propuestos en  */TP1/src/Segunda_Parte*

en *implementación_lista.py* estan implementadas todas las funciones para la lista y el array. En python encontramos la particularidad que los array y las listas funcionan de la misma forma, ambas quedan determinadas por el comando []

en *implementación_lista_ordenada.py* estan implementadas todas las funciones para el vector ordenado

en *implementación_abb.py* estan implementadas todas las funciones para nuestra implementación elegida, un arbol de busqueda binario.


### 2.2 - Analisis de complejidad algorítmica

#### Lista y vector en python:
Antes que nada aclaramos que para el calculo de complejidad "n" siempre es la cantidad de elementos de la estructura a menos que se indique lo contrario
* Máximo
  * Pseudo codigo:
    * maximo(lista):
      * maximo = lista[0]
      * for elemento in lista:
        * if elemento > maximo:
          * maximo = elemento
    * return maximo
  * Basicamente recorremos linealmente quedandonos con el mayor elemento visitado, esto claramente es O(n) en tiempo y O(1) en espacio porque usamos una variable para guardar el maximo
  * Temporal: *O(n)*
  * Espacial: *O(1)*
* Media
  * Pseudo codigo:
    * media(lista):
      * suma = 0
        * for number in lista:
          * suma += number
      * media = suma / largo(lista)
    * return media
  * Como hace falta recorrer todos los elementos de la lista esto es O(n), esto se guarda en una variable por lo que es O(1) en espacio.
  * Temporal: *O(n)*
  * Espacial: *O(1)*
* Moda
  * pseudo codigo:
    * moda(lista):
      * mas_frecuentes = [lista[0]]
      * frecuencia = 0
      * actual = lista[0]
      * frecuencia_actual = 0
      * for numero in lista:
        * if numero != actual:
          * actual = numero
          * frecuencia_actual = 0
        * frecuencia_actual ++
        * if frecuencia_actual > frecuencia:
          * frecuencia = frecuencia_actual
          * mas_frecuentes = [actual]
        * elif frecuencia_actual == frecuencia:
          * mas_frecuentes.append(actual)
    * return mas_frecuentes
  * Como recorremos toda la lista, esto es O(n) y como usamos una lista para guardar los elementos mas frecuentes, en espacio es O(n) en el peor caso, que seria que todos los elementos tienen igual frecuencia, en ese caso devolvemos la lista entera.
  * Temporal: *O(n)*
  * Espacial: *O(n)*
* Mediana
  * pseudo codigo:
    * mediana(lista):
      * lista.ordenar()
      * pos = (largo(lista) - 1) // 2
      * mediana = lista[pos]
      * if largo(lista) es par:
        * mediana = (lista[pos] + lista[pos + 1]) / 2
    * return mediana
  * Lo que hacemos primero es ordenar la lista, lo cual es O(n log n) en tiempo. Luego, si la lista tiene una cantidad par de elementos, devolvemos el promedio de los 2 elementos medios de la lista, de lo contrario la mediana es el valor en el medio.
  * Temporal: *O(n log n)*
  * Espacial: *O(1)*
* Desviación estándar
  * pseudo codigo: 
    * desviacion_estandar(lista):
      * calcular la media
      * suma_de_distancias = 0
      * for elemento in lista:
        * distancia_media = (elemento - media) ^ 2
        * suma_distancias += distancia_media
      * media_de_suma = suma_distancias / largo(lista)
    * return raiz cuadrada de media_de_suma
  * Calcular la media es O(n) en tiempo y O(1) en espacio, despues se recorre toda la lista calculando la suma de las distancias medias siendo la distancia media de cada elemento, el elemento menos la media al cuadrado, lo cual es O(n) en tiempo y O(1) en espacio, almacenar le media de sumas es O(1) en espacio y O(n) en tiempo (porque calculamos el largo de la lista, esto se podria haber calculado en el ciclo anterior pero O(n) + O(n) = O(n)). Finalmente, calcular la raiz cuadrada es O(log n) en tiempo, y O(1) en espacio (es inplace). Finalmente, en complejidad temporal esta funcion es O(n) + O(n) + O(n) + O(log n) = O(n) + O(log n) = O(n) y en complejidad espacial es O(1).
  * Temporal: *O(n)*
  * Espacial: *O(1)*
* Permutaciones del conjunto
  * pseudo codigo:
    * permutaciones(lista):
      * permutaciones = []

      * generar_permutaciones(k, lista):
        * if k == 1:
          * permutaciones.append(lista)
          * return
        * for i in range(0, k-1):
          * generar_permutaciones(k-1, lista)
            * if i es par:
              * swap(i, k-1)
            * else:
              * swap(0, k-1)

      * generar_permutaciones(largo(lista), lista)
    * return permutaciones
  * Como este algoritmo tiene que generar todas las permutaciones posibles y a la vez tiene que devolver dichas combinaciones (guardadas en una lista de listas) este algoritmo es tanto O(n!) en espacio como en tiempo.
  * Temporal: *O(n!)*
  * Espacial: *O(n|)*
* Variaciones del conjunto tomados de r elementos (r«n)
  * pseudo codigo:
    * variaciones_r_elementos_sin_repeticion(lista, r):  # O(n*r)
      * n = largo(lista)
      * variaciones = []
      * indices = list(range(r))
      * variaciones.append(list(lista[i] for i in indices))
      * while True:
        * for i in reversed(range(r)):
          * if indices[i] != i + n - r:
            * break
        * else:
          * break
        * indices[i] ++
        * for j in range(i + 1, r):
          * indices[j] = indices[j - 1] + 1
          * variaciones.append(list(lista[i] for i in indices))
      * return variaciones
  * VER COMPLEJIDAD
  * Temporal: *O(n!)*
  * Espacial: *O(n!)*
* Variaciones con repetición del conjunto de r elementos (r«n)
  * pseudo codigo:
    * variaciones_r_elementos(lista, r):
      * n = largo(lista)
      * variaciones = []
      * indices = [0] * r
      * variaciones.append(list(lista[i] for i in indices))
      * while True:
        * for i in reversed(range(r)):
          * if indices[i] != n - 1:
            * break
          * else:
            * break
        * indices[i:] = [indices[i] + 1] * (r - i)
        * variaciones.append(list(lista[i] for i in indices))
    * return variaciones
  * VER COMPLEJIDAD
  * Temporal: *O(n!)*
  * Espacial: *O(n!)*



#### Vector ordenado:

* Máximo
  * Pseudo codigo:
    * maximo(lista):
      * return lista[0]
  * En un vector ordenado descendente el primer elemento siempre tiene el maximo valor. Por ello esto solo requiere visitar un solo elemento y guardarlo en una sola variable.
  * Temporal: *O(1)*
  * Espacial: *O(1)*
* Media
  * Pseudo codigo:
    * media(lista):
      * for elemento in lista:
        * sumatoria = sumar todos los elementos
    * return sumatoria / largo(lista)
  * Es el mismo algoritmo que el usado para la lista y el vector, ya que en ambas estructuras no cambia el como se obtiene la media.
  * Temporal: *O(n)*
  * Espacial: *O(1)*
* Moda
  * pseudo codigo: Es exactamente el mismo algoritmo usado en 'lista y vector'.
  * Temporal: *O(1)*
  * Espacial: *O(n)*
* Mediana
  * Pseudo codigo:
    * mediana(lista):
      * if lista es impar:
        * return el elemento del medio
      * sino:
        * return el promedio de los 2 elementos del medio
  * Como sabemos que posiciones del vector hay que visitar y solo son un par de posiciones, esto es O(1), tanto en tiempo como en espacio.
  * Temporal: *O(1)*
  * Espacial: *O(1)*
* Desviación estándar
  * pseudo codigo: Es exactamente el mismo algoritmo usado en 'lista y vector'.
  * Temporal: *O(n)*
  * Espacial: *O(1)*
* Permutaciones del conjunto
  * pseudo codigo: Es exactamente el mismo algoritmo usado en 'lista y vector'.
  * VER COMPLEJIDAD
  * Temporal: *O(n!)*
  * Espacial: *O(n|)*
* Variaciones del conjunto tomados de r elementos (r«n)
  * pseudo codigo: Es exactamente el mismo algoritmo usado en 'lista y vector'.
  * VER COMPLEJIDAD
  * Temporal: *O(n!)*
  * Espacial: *O(n|)*
* Variaciones con repetición del conjunto de r elementos (r«n)
  * pseudo codigo: Es exactamente el mismo algoritmo usado en 'lista y vector'.
  * VER COMPLEJIDAD
  * Temporal: *O(n!)*
  * Espacial: *O(n|)*


#### Arboy de Busquda Binaria:
* Máximo
  * Pseudo codigo:
    * maximo(nodo_raiz):
      * actual = nodo_raiz
      * while (actual.derecho is not NULL):
        * actual = actual.derecho
      * return actual.dato
  * Bajamos todo a la derecha, donde va a estar el maximo, tarda O(log N) (caso normal) Tarda O(N) en el peor caso que seria que el arbol sea una lista enlazada. El mejor caso es O(1) (la raiz es el maximo)
  * Temporal: *O(log n)*
  * Espacial: *O(1)*
* Media
  * Temporal: *O(n)*
  * Espacial: *O(n)*
* Moda
  * Temporal: *O(n)*
  * Espacial: *O(n)*
* Mediana
  * pseudo codigo:
    * mediana(nodo_raiz):
      * if (nodo_raiz is NULL):
        * return 0
      * contador = contarNodos(nodo_raiz)
      * contadorActual = 0
      * actual = nodo_raiz
      * while (actual is not NULL):
        * if (actual.izq is NULL):
          * contadorActual ++
          * if (contador es impar and contadorActual == (contador + 1) // 2):
            * return previo.data
          * elif (contador es par and contadorActual == (contador // 2) + 1):
            * return (previo.data + actual.data) // 2
          * previo = actual
          * actual = actual.derecho
        * else:
            * pre = actual.izq
            * while (pre.derecho is not NULL and pre.derecho != actual):
              * pre = pre.derecho
            * if (pre.derecho is NULL):
              * pre.derecho = actual
              * actual = actual.izq
            * else:
              * pre.derecho = NULL
              * previo = pre
              * contadorActual ++
              * if (contador es impar and contadorActual == (contador + 1) // 2):
                * return actual.data
              * elif (contador es par and contadorActual == (contador // 2) + 1):
                * return (previo.data + actual.data) // 2
              * previo = actual
              * actual = actual.derecho
  * Lo que hacemos es recorrer Inorder el arbol, teniendo un contador del nodo actual, chequeando si el nodo actual es la mediana. Obviament en caso de encontrarse la media se chequea si hay que devolver el valor medio o el promedio de los valores medios. La mediana se guarda en una variable y al ser un recorrido inorder (recorrido lineal de los nodos) es O(n) en tiempo.
  * Temporal: *O(n)*
  * Espacial: *O(1)*
* Desviación estándar
  * Temporal: *O(n)*
  * Espacial: *O(n)*
* Permutaciones del conjunto
  * Temporal: *O(n!)*
  * Espacial: *O(n!)*
* Variaciones del conjunto tomados de r elementos (r«n)
  * Temporal: *O(n!)*
  * Espacial: *O(n!)*
* Variaciones con repetición del conjunto de r elementos (r«n)
  * Temporal: *O(n!)*
  * Espacial: *O(n!)*

  ### 2.3 - Gráficos de Complejidad

  Para armar los graficos de complejidad, usamos diferentes largos de vector para medir el tiempo real de ejecucion usando el comando **time** de Linux y tomando el tiempo de ejecucion total.

  ![Gráfico lista y vector sin ordenar](graf_1.png)

  ![Gráfico vector ordenado](graf_2.png)

  ### 2.4 - Programación Algoritmos

  Como ejecutar las distintas implementaciones

  1) Generamos el archivo txt con la cantidad de numeros que queremos, siendo **n** la cantidad de numeros
  ```
  cd TP1/src/Tools
  python number_generator.py n
  ```
  2) Ejecutar la implementacion deseada y funcion deseada conjunto
  ```
  cd TP1/src/Segunda_Parte/
  implentacion_lista.py ruta_archivo funcion r
  ```
  Siendo **r** un argumento necesario solo para las variaciones

  Las funciones son las siguientes:
  * Maximo : **maximo**
  * Media : **media**
  * Moda : **moda**
  * Mediana : **mediana**
  * Desviacion Estandar : **desviacion_estandar**
  * Permutaciones : **permutaciones**
  * Variaciones de r en r : **variaciones**
  * Variaciones de r en r con repeticion : **variaciones_con_repeticion**

  La ruta del archivo, si fue generado con el script en **tools** esta en **../assets/txt/numbers.txt**
