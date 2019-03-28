# TP 1, 1C2019

## Primera parte

### Como ejecutar

Primero, generar los archivos de preferencias y ranking general

```
cd src/tools
python3 player_generator.py
```

Asegurarse que el directorio **assets/txt** no tenga ningun archivo, solamente el readme

Para correr el programa que genera las parejas

```
cd src/Primera_Parte
python3 matcher.py 20 ../../assets/txt/20_jugadores.rank
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
