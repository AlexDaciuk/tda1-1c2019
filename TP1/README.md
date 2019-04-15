# TP 1, 1C2019

## Primera parte

### Como ejecutar

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

## Segunda Parte

Primero, generar el archivo con los numeros aleatorios, el script recibe un parametro
**n** que indica la cantidad de numeros a generar

```
cd src/tools
python3 number_generator.py n
```

Despues en la carpeta **src/Segunda_Parte**, tenemos las diferentes implementaciones

siempre correr con el archivo con el path completo como argumento

```
python3 implementacion.py ../../assets/txt/numbers.txt
```
