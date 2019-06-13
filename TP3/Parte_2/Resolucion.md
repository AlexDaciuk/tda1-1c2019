# Enunciado

Una empresa que produce partes de aviones solicita nuestros servicios para planificar su producción de las próximas n semanas. Produce 3 tipos de piezas complejas. Cada pieza lleva una semana de elaboración. Por restricciones espaciales solo puede generar un tipo de pieza simultáneamente. Asimismo cada vez que produce un tipo de pieza, no puede volver a realizarla en la siguiente semana para evitar el sobrecalentamiento de cierta maquinaria.

Tenemos una planilla de pedidos donde por semana nos indican el ofrecimiento monetario que nos hacen por construir cada tipo de pieza. Por ejemplo:

|         | Semana 1 | Semana 2 | Semana 3 |
| ------- | :------: | :------: | :------: |
| Pieza 1 | 50       | 40       | 60       |
| Pieza 2 | 30       | 40       | 40       |
| Pieza 3 | 80       | 30       | 10       |

Debemos determinar qué tipo de pieza producir cada semana, intentando maximizar las ganancias respetando las restricciones.

Se pide:

1.  Proponer una solución greedy para el problema. Mostrar el pseudocódigo.
-   Analizar y justificar la complejidad del algoritmo
-   Determinar si la solución es óptima. En caso negativo, en qué condiciones lo puede ser?
-   Proponer una solución con programación dinámica. Mostrar el pseudocódigo.
-   Explicitar la relación de recurrencia y analizar la complejidad del algoritmo.

## Resolucion

### 1) Proponer una solución greedy para el problema. Mostrar el pseudocódigo.

Guardo los precios de cada semana en una lista de tal manera que la posicion se condiga con el numero de pieza
y cada lista de precios, la guardo en otra lista (**semanas**) de tal manera que la primera sublista sea de la semana 1, y asi hasta la semana n

Guardo en producido_ultima_semana la pieza que se produjo la ultima semana, para poder chequear el cumplimiento de la condicion impuesta en  el enunciado

Recorro cada lista en **semanas** y busco la pieza que tenga el mayor precio en **semana - producido_ultima_semana**

Guardo en otra lista, las piezas a producir, ordenadas por semana.

```
producido_ultima_semana = -1


Por cada semana en precios_semana:
  pieza = mayor(semana - producido_ultima_semana)

  a_producir.agregar(pieza)
  producido_ultima_semana = pieza
```

### 2) Analizar y justificar la complejidad del algoritmo

Recorrer la lista **precios_semana** es O(n)

Buscar el mayor en una lista desordenada **semana - producido_ultima_semana** es O(m - 1)

=> O(n + m - 1) , siendo **n** la cantidad de semanas que se quieren calcular y **m** la cantidad de piezas que se pueden producir

### 3) Determinar si la solución es óptima. En caso negativo, en qué condiciones lo puede ser?

Se puede ver ya con un ejemplo chico como el del enunciado, que esa solucion no es la optima.

En la primera iteracion, se elije la pieza 3, que para esa semana, es la pieza mejor paga
En la segunda iteracion, nuestras opciones se reducen a Pieza 1 y Pieza 2, al tener la misma paga, se elije por defecto Pieza 1
En la tercera iteracion, solamente podemos elegir entre la Pieza 2 y la Pieza 3, ninguna de estas 2 opciones es la mejor paga en la semana 3, por ende, esta solucion no es optima.

Para que esta solucion sea optima ... 
