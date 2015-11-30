# Tarea 08: Aprendizaje Supervisado

**Fecha limite de entrega de la tarea: 10 de diciembre de 2015**

## Introducción

En esta tarea se va a desarrollar dos de los métodos básicos de aprendizaje supervisado,
los *K* vecinos próximos y los árboles de desición, para la solución de un probleme conocido
desde la tarea anterior: La clasificación de la base de datos DNA.

## Instrucciones:

1. Abre el archivo `id3.py` y revisa el código del árbol de desición tipo ID3 que
   se encuentra programado. Ejecuta el archivo para observar como funciona.

2. Abre el archivo `tarea8.py` y revisa las funciones desarrolladas. Ejecuta el modulo donde en la funcion 
   principal se ejecuta la función `pruebaID3` y observa los resultados de salida.

3. Desarrolla en un módulo llamado `cart.py` una clase para realizar clasificación utilizando un árbol tipo CART para
   atributos cualitativos, que utilice al menos 3 criterios de prepoda (los mismos vistos para el árbol ID3).
   Contesta las siguientes preguntas (utilizando la función `pruebaCART` del modulo `tarea8.py`:
      + ¿Cual es la diferencia entre el árbol tipo CART y el ID3?
      + ¿Cual es más eficiente?
      + ¿Cuanto nodos genera cada uno?
      + ¿Cuantos nodos hoja genera cada uno?
      + ¿Cual tiene el menor error en los datos de prueba?
      + ¿A que crees que se debe que hay errores de aprendizaje con los datos de entrenamiento?

4. Desarrolla en un modulo llamado `knn.py` una clase para realizar clasificación con k vecinos próximos. Recuerda que 
   los datos de entrenamiento se utilizan para encontrar los vecinos (osea que los datos de entrenamiento sin ruido
   con los datos de prueba sin ruido, y los datos de entrenamiento con ruido con los datos de prueba con ruido).

5. Aplica el método de los K vecinos más próximos, y resuelve la siguiente tabla

      ==========================================================
      | Vecinos | error datos prueba | error datos prueba ruido|
      | 1       |                    |                         |
      | 3       |                    |                         |
      | 5       |                    |                         |
      | 7       |                    |                         |
      | 9       |                    |                         |
      ==========================================================
      
6. Contesta las siguientes preguntas:

  + ¿Que método da menos error entre knn, CART, Id3 y naive bayes en los datos sin ruido?
  + ¿Que método da menos error entre knn, CART, Id3 y naive bayes en los datos con ruido?
  + ¿Mejora al aumentar el número de vecinos? ¿Hasta cuantos vecinos?
