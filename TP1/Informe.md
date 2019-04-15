# Informe TP 1
## Grupo : 3 + 1
## Integrantes
  * Matias Onorato (93179)
  * Juan Cruz Opizzi (99807)
  * Francisco Strambini (92135)
  * Alexis Daciuk (97630)


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
### 1.1 Variante de Gale-Shapley para empates

Encontramos que podemos ejecutar practicamente el mismo algoritmo de Gale -Shapley si tomamos un correcto criterio de desempate en caso de ser necesario.

Si a diferencia del algoritmo tradicional, en nuestra variante permitimos más de un jugador en las lista de preferencias con un mismo numero de preferencia, ordenada de forma decreciente, es decir dado *a* ∈ ***A***, *x,y,z* ∈ ***B*** jugadores de los Grupos ***A*** y ***B***, un diccionario `{p:preferencia, j:jugador}` formando la lista `a → {p:1, j:x} →{p:2, j:y} →{p:2, j:z}` como lista de referencia de ***A***, el algoritmo de gale shapley sigue ofreciendo un correcto funcionamiento, entregando una pareja para cada jugador. Simplemente permitimos que la primer preferencia encontrada con un valor de referencia repetido de dicha lista, pueda formar pareja a la hora de encontrar un empate.

### 1.2 - Estabilidad de la Variante
Por lo visto en la introducción, el algoritmo de Gale-Shelley es por naturaleza estable, por lo cual analizamos nuestra variación para ver si su nueva implementación produce algún cambio que afecte su estabilidad a la hora de encontrar un posible bloqueo luego de formadas las parejas. 

Si definimos como criterio de desempate en el pareo (y por ende al consultar la preferencia) que la preferencia del proponente tiene que ser estrictamente mayor a la referencia de la pareja del propuesto, por más que esta sea la misma en más de un caso, el algoritmo de Gale-Shapley no encuentra alteraciones en su estabilidad. Esto se debe a que con el criterio mencionado, ante cada intento de formar una pareja entre los jugadores de ambos grupos, al tener que ser esta preferencia estrictamente mayor,  ningún jugador podrá cambiar su pareja para ninguno de los casos en los que se repita ese mismo valor de preferencia, conservándose la estabilidad al no generarse ningún bloqueo.

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

Al igual que el caso considerado al final del punto 1.2, no podemos permitir que ante un empate se generen casos donde el criterio de selección de pareja no sea arbitrario. Si permitimos que el azar resuelva un empate en una lista de preferencias, en lugar de que la diferencia de prioridades sea estrictamente mayor para romper una pareja ya armada, se podrían generar casos de bloqueo que romperían la estabilidad del pareo.

### 1.5 - Desarrolle un algoritmo que dado una pareo y las preferencias determina si el mismo es matching estable. ¿Qué complejidad algorítmica tiene?

instrucciones ejecución
explicar complejidad 

### 1.6 - Programación de los algoritmos

instrucciones ejecución
explicar complejidad 

### 1.7 - ¿Tiene su programa la misma complejidad algorítmica que la teórica?

## Parte 2 - Funciones matemáticas / estadísticas