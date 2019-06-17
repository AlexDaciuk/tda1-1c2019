# Enunciado

## A) Responda a las siguientes preguntas teóricas. Sea conciso y justifique claramente

#### 1. Defina y explique (si es necesario con ejemplos) qué significa que un problema sea P, NP, NP-Completo y NP-Hard

Que un problema sea **P** significa que puede resolverse en tiempo polinomico, osea, que su solucion optima tiene un costo temporal de O(n^k), con un k fijo y n siendo el tamaño del input.

La categoria **NP** corresponde a los problemas que dada una posible solucion, se puede comprobar que es valida o no en tiempo polinomico (aunque todavia no exista un algoritmo para encontrar soluciones en tiempo polinomico).

La categoria **NP Completo** agrupa a los problemas **NP** que pueden ser reducidos en tiempo polinomico a otros de la misma categoria, entonces, de encontrarse una solucion polinomica a cualquier problema de esta categoria, signifca que todos pueden resolverse en tiempo polinomial.

La categoria **NP-Hard** son problemas, que son, al menos, tan complejos como los **NP** (sin necesariamente estar en esta cateporia) y que cualquier problema **NP Completo** puede ser reducido a esta categoria en tiempo polinomial


#### 2. Tenemos un problema A, un problema B y una caja negra NA y NB que resuelven el problema A y B respectivamente. Sabiendo que B es NP

- Qué podemos decir de A si utilizamos NA para resolver el problema B (asumimos que la reducción realizada para adaptar el problema B al problema A el polinomial)

Siendo que no sabemos la categoria de **A**, **NA** o **NB**

Si existe una reduccion polinomial de **B** a **A** y **B** es **NP** entonces A es **NP**


- Qué podemos decir de A si utilizamos NB para resolver el problema A (asumimos que la reducción realizada para adaptar el problema A al problema B el polinomial)

Si existe una reduccion polinomial de **A** a **B**, entonces, siendo que **B** es **NP**, entonces:

**A** puede ser **P** siendo que todos los problemas **P** son **NP**, o, **NP Completo** ya que **B** es **NP** y **A** puede ser reducido a **NP**

- Qué pasa con los puntos anteriores si no conocemos la complejidad de B, pero sabemos que A es P?.

En caso de que **A** sea **P**, la reduccion de **B** (**NP**) a **A** (**P**) del primer problema, todavia no tiene solucion y es un problema abierto

En el segundo caso, si **A** es **P** y se reduce a **B**, **B** podria ser **P** ya que un problema polinomial reducido de forma polinomial a otro problema, sigue siendo polinomial o **NP** ya que todo problema **P** es **NP**

## B) Demostrar que los siguientes problemas son NPC. Justificar claramente, escribiendo en pseudocódigo los algoritmos si cree conveniente

1. Dados 4 sets de elementos (W, X, Y, Z) (cada uno de tamaño n) y una colección C de 4-tuplas de la forma (w, x, y, z), tal que wW, xX, yY, zZ. El problema de 4-Dimensional Matching consiste en identificar si existen N 4-tuplas de C tal que ninguna de ellas tienen ningún elemento en común con las demás (es decir, si una tupla es (w1, x1, y1, z1) ∈ C y otra es (w2, x2, y2, z2) ∈ C, son distintas si w1 ≠ w2, x1 ≠ x2, y1 ≠ y2, and z1 ≠ z2). Sabiendo que el problema de 3-Dimensional Matching (el mismo que el anteriormente explicado pero con 3 sets y considerando 3-tuplas) es NP-Completo, demostrar que el problema de 4-Dimensional Matching es NP-Completo también.

Se puede ver que 4-DM es **NP** ya que se puede comprobar en tiempo polinomial O(n) que una tupla de 4 elementos es disjunta, recorriendo la tupla y comparando cada elemento con el anterior.

Ahora, para ver que es **NP Completo**, nos bastaria con encontrar una reduccion a 3-DM que sabemos por enunciado que es **NP Completo**

Si consideramos una instancia de 3-DM con {X,Y,Z} de dimension N y C el conjunto de 3-tuplas que cumplen con la condicion de ser disjuntas

Armamos nuestro caso de 4-DM con {W,X,Y,Z} de dimension N y C' el conjunto de 4-tuplas definidas de tal manera que (Wi, Xj, Yk, Zl) con (Xj, Yk, Zl) en C y con i en 1 .. n

Entonces, si tenemos un conjunto H de las 3-tuplas disjuntas en C, encontrar el conjunto de 4-tuplas disjuntas en C' se resuelve de forma polinomica, agregando los elementos Wi tal que las 4-tuplas sigan siendo disjuntas 


2.  Se tiene un conjunto de n tareas, con tiempo de ejecución ti​, una fecha límite de finalización di y una ganancia vi otorgada si se finaliza antes que su tiempo límite. Se pide devolver si existe alguna planificación que obtenga una ganancia total mayor o igual a K sin ejecutar dos tareas a la vez.
