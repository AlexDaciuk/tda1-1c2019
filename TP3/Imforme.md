### (75.29 / 95.06) - Teoría de Algoritmos - FIUBA

# Informe Trabajo Práctico 3

## Grupo : 3 + 1
## Integrantes
  * Matias Onorato (93179)
  * Juan Cruz Opizzi (99807)
  * Francisco Strambini (92135)
  * Alexis Daciuk (97630)

---

## Parte 1
### Las preferencias de eleccion y el mapa
Como el mapa esta implementado como un grafo (o dicho de otra forma una lista de listas) para recorrerlo
utilizamos BFS y asignamos primero por proximidad y luego por cantidad de especia producida.
Con este objetivo maximizamos la probabilidad de mantener lo mas lejos posible al enemigo y a la vez maximizar la
recolección de especia, ya que ambas condiciones son necesarias para ganar.

### BFS
#### Pseudocodigo de BFS:
-Dada la metropolis del jugador, BFS sistemáticamente explora las ciudades del mapa para “encontrar” todos las ciudades a las que la metropolis puede acceder.
-Calcula la distancia (menor número de ciudades) desde la metropolis a todos las ciudades que puede acceder.
-Después produce una lista de recorridos desde la metropolis y que contiene a todas las ciudades accesibles.
-El camino desde la metropolis a cada vértice contiene el mínimo número de ciudades. Es el camino más corto medido en número de vértices.
-Llega a las ciudades de distancia k, sólo tras haber llegado a todos los ciudades a distancia k-1

#### Complejidad temporal:
La complejidad temporal del algoritmo se puede expresar como O (|V| + |E|), donde |V| es el número de ciudades y |E| es el número de rutas. En el peor caso, cada ciudad y cada ruta será visitado por el algoritmo.

#### Complejidad espacial:
El algoritmo necesita tener todas las ciudades cargadas en memoria O(V) de ante mano, ademas que devuelve la lista de preferencias de las ciudades para la metropolis O(V). Siendo V la cantidad total de ciudades. Entonces el algoritmo es O(2V) = O(V) en memoria.

### Inteligencia Artificial 
#### De los jugadores
Para la toma de decisiones de ambos jugadores utilizamos una tecnica llamada MinMax.

Minimax es un método de decisión para minimizar la pérdida máxima esperada en juegos con adversario y con información perfecta, utilizando un arbol de decision de forma recursiva.
El algoritmo funciona teniendo que tomar la mejor decision para uno mismo suponiendo que tu oponente escogerá la peor decision para ti.

La idea de Minimax es:

1. Generación del árbol de decision. Se generarán todos los nodos hasta llegar a un estado terminal o determinando una profundidad concreta.

Vamos aplicando el algoritmo por un número fijo de iteraciones hasta alcanzar una determinada profundidad. En estas aplicaciones la profundidad suele ser el número de movimientos o los incluso el resultado de aplicar diversos pasos de planificación en un juego de estrategia.

2. Cálculo de los valores de la función de utilidad para cada nodo terminal.

Para cada resultado final, cómo de beneficioso me resulta si estamos en MAX o cuanto me perjudicará si estamos en MIN.

3. Calcular el valor de los nodos superiores a partir del valor de los inferiores. Alternativamente se elegirán los valores mínimos y máximos representando los movimientos del jugador y del oponente, de ahí el nombre de Minimax.

4. Elegir la jugada valorando los valores que han llegado al nivel superior.

El algoritmo explorará los nodos del árbol asignándoles un valor numérico mediante una función de utilidad, empezando por los nodos terminales y subiendo hacia la raíz. La función de utilidad como se ha comentado, definirá lo buena que es la posición para un jugador cuando la alcanza.

Versiones más avanzadas como el minimax con poda alfa beta hacen que se reduzca considerablemente el número de nodos a visitar por lo que el tiempo de cálculo se reduce ampliamente.

Y para terminar comentar un ejemplo cásico, el tres en raya (juego del gato, tatetí, triqui, tres en gallo, michi, la vieja o tic tac toe). Se trata de hacer una fila de tres para ganar y evitar que el oponente la haga antes que tu.

Al aplicar el algoritmo, se suceden una serie de estados que se resumen en la fotografía. Un estado -1 significa que MAX gana, 0 empate o -1 pierde.

#### De la recoleccion de especias
Utilizamos el algoritmo de Ford-Fulkerson para implementar el tema de la recoleccion de especias.
El algoritmo provee una forma practica de transportar la mayor cantidad de especias (o flujo en general) desde una fuente a un sumidero, que en nuestro caso la fuente seria las ciudades pertenecientes al imperio y el sumidero la metropolis.

La siguiente es una idea simple del algoritmo Ford-Fulkerson:
1) La recoleccion inicial se setea en 0.
2) Mientras haya un camino de aumento desde cada ciudad hasta la metropolis.
        Añade la recoleccion de la ruta de la ciudad para el flujo.
3) Devuelve el flujo.

##### Complejijdad temporal
La complejidad del tiempo del algoritmo es O (max_flujo * E), siendo E la cantidad de rutas existentes en el mapa del imperio. 
Iteramos un loop mientras hay un camino de aumento. En el peor de los casos, podemos agregar 1 unidad de flujo en cada iteración. Por lo tanto, la complejidad del tiempo se convierte en O(max_flujo * E).