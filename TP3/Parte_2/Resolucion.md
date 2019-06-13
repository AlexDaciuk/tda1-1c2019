# Enunciado

Una empresa que produce partes de aviones solicita nuestros servicios para planificar su producción de las próximas n semanas. Produce 3 tipos de piezas complejas. Cada pieza lleva una semana de elaboración. Por restricciones espaciales solo puede generar un tipo de pieza simultáneamente. Asimismo cada vez que produce un tipo de pieza, no puede volver a realizarla en la siguiente semana para evitar el sobrecalentamiento de cierta maquinaria.

Tenemos una planilla de pedidos donde por semana nos indican el ofrecimiento monetario que nos hacen por construir cada tipo de pieza. Por ejemplo:
| arsa    | Semana 1 |	Semana 2 |	Semana 3 |
|---------|----------|-----------|-----------|
| Pieza 1 |	50       |	40       |	60       |
| Pieza 2 |	30       |	40       |	40       |
| Pieza 3 |	80       |	30       |	10       |

Debemos determinar qué tipo de pieza producir cada semana, intentando maximizar las ganancias respetando las restricciones.

Se pide:

* Proponer una solución greedy para el problema. Mostrar el pseudocódigo.
* Analizar y justificar la complejidad del algoritmo
* Determinar si la solución es óptima. En caso negativo, en qué condiciones lo puede ser?
* Proponer una solución con programación dinámica. Mostrar el pseudocódigo.
* Explicitar la relación de recurrencia y analizar la complejidad del algoritmo.
