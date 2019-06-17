# Enunciado

## A) Responda a las siguientes preguntas teóricas. Sea conciso y justifique claramente

#### 1. Defina y explique (si es necesario con ejemplos) qué significa que un problema sea P, NP, NP-Completo y NP-Hard

Que un problema sea **P** significa que puede resolverse en tiempo polinomico, osea, que su solucion optima tiene un costo temporal de O(n^k), con un k fijo y n siendo el tamaño del input.

La categoria **NP** corresponde a los problemas que dada una posible solucion, se puede comprobar que es valida o no en tiempo polinomico (aunque todavia no exista un algoritmo para encontrar soluciones en tiempo polinomico).

La categoria **NP Completo** agrupa a los problemas que no se le puede encontrar una solucion en tiempo polinomico, pero, muchos problemas de esta categoria, pueden ser reducidos en tiempo polinomico a otros de la misma categoria, entonces, de encontrarse una solucion polinomica a cualquier problema de esta categoria, signifca que todos pueden resolverse en tiempo polinomial.

La categoria **NP-Hard** son problemas, que son, al menos, tan complejos como los **NP** y que cualquier problema **NP** puede ser reducido a esta categoria en tiempo polinomial


#### 2. Tenemos un problema A, un problema B y una caja negra NA y NB que resuelven el problema A y B respectivamente. Sabiendo que B es NP

- Qué podemos decir de A si utilizamos NA para resolver el problema B (asumimos que la reducción realizada para adaptar el problema B al problema A el polinomial)



- Qué podemos decir de A si utilizamos NB para resolver el problema A (asumimos que la reducción realizada para adaptar el problema A al problema B el polinomial)


- Qué pasa con los puntos anteriores si no conocemos la complejidad de B, pero sabemos que A es P?.

## B) Demostrar que los siguientes problemas son NPC. Justificar claramente, escribiendo en pseudocódigo los algoritmos si cree conveniente

1. Dados 4 sets de elementos (W, X, Y, Z) (cada uno de tamaño n) y una colección C de 4-tuplas de la forma (w, x, y, z), tal que wW, xX, yY, zZ. El problema de 4-Dimensional Matching consiste en identificar si existen N 4-tuplas de C tal que ninguna de ellas tienen ningún elemento en común con las demás (es decir, si una tupla es (w1, x1, y1, z1) ∈ C y otra es (w2, x2, y2, z2) ∈ C, son distintas si w1 ≠ w2, x1 ≠ x2, y1 ≠ y2, and z1 ≠ z2). Sabiendo que el problema de 3-Dimensional Matching (el mismo que el anteriormente explicado pero con 3 sets y considerando 3-tuplas) es NP-Completo, demostrar que el problema de 4-Dimensional Matching es NP-Completo también.

*  Se tiene un conjunto de n tareas, con tiempo de ejecución ti​, una fecha límite de finalización di y una ganancia vi otorgada si se finaliza antes que su tiempo límite. Se pide devolver si existe alguna planificación que obtenga una ganancia total mayor o igual a K sin ejecutar dos tareas a la vez.
