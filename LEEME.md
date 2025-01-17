# busqueda-del-tesoro #

Esto es un juego de Búsqueda del Tesoro en comandos Linux. Nuestra meta es encontrar todas
las pistas y aprender cómo usar los comandos básicos de Linux en el proceso.

## Preparación ##

Si estás usando un Linux recién instalado o un Live CD, deberías empezar instalando
Git primero (`sudo apt-get install git` en Ubuntu). Abre una terminal e introduce:

    git clone https://github.com/Hodr25/busqueda-del-tesoro.git
    cd busqueda-tesoro

Primero, elige un número secreto para compartir con tu equipo,
o quédatelo para tí si trabajas solo. No introduzcas ningún espacio extra o carácteres no-numéricos. Escribe
debajo tu número sectreo. El número secreto crea tus pistas únicas, por lo que otros equipos no podrán mirar sobre tus hombros.
Después escribe:

    python generar_pistas.py [número_secreto]

NOTA: En algunos sistemas 'python' deberá escribirse como 'python3'.

Cada vez que encerramos algo en corchetes, necesitas reemplazarlo por
un valor real (llamado argumento). Por ejemplo, para empezar yo
podría poner:

    python generar_pistas.py 42

Esto creará un subdirectorio llamado `pistas`. Asegurate de mantener este archivo
(también llamado README) abierto en un visualizador a parte.

### Localización del Diccionario ###

Este código se ha probado en un Ubuntu 22.04. Si tu tienes un error acerca de no ser capaz
de encontrar tu diccionario, prueba el siguiente comando:

    cd /
    find . -name words

Cambia el valor dentro del archivo 'conf' para localizar tu diccionario.

## Referencia ##

Si quieres aprender más acerca de Linux cuando hayas terminado, o necesitas una referencia
durante la búsqueda, visita este enlace: http://www.tldp.org/LDP/intro-linux/html/index.html.

### Pista 1: Que comienze la caza ###

#### `man` ####

El primer comando que vamos a aprender es `man`, que es la abreviación de manual.
Ecribiendo `man [comando]` mostrará un manual o instrucciones para la mayoría de comandos

#### `ls` ####

El siguiente comando que necesitaremos aprender es `ls` (listar). Escribe `man ls` y lee la
descripción. Pulsa `q` para salir. luego escribe `ls` y deberías ver algo similar a esto:

    APPENDIX.md pistas generate_pistas.py LICENSE.md next_pista.py README.md

Aquello que está en azul son directorios y todo lo demás son archivos. Cada vez
que necesites saber qué archivos y directorios tienes disponible, pon `ls`.

#### `cd` ####

Necesitaremos aprender un par de herramientas más antes de que podamos empezar la caza y 
busqueda de las pistas. Para cambiar a otro directorio, usaremos `cd` (cambiar de directorio).
Habrás notado que `man cd` no funciona. Algunas veces no existe una guía para un comando. En esos
casos google es nuestro mejor amigo. Cambiar de directorios es bastante simple:

    cd pistas

Esto nos meterá en el directorio de pistas. Para ir un directorio por encima, o el directorio anterior,
podemos escribir el siguiente comando:

    cd ..

Si alguna vez te pierdes, siempre puedes poner lo siguiente:

    cd ~/busqueda-tesoro

Para volver tu directorio. Si haces un `cd` hacia el directorio `pistas` y haces un `ls`, te
darás cuenta que hay nn porrón de directorios. La mayoría de ellos tienen
pistas falsas. Sin envargo para nuestra caza buscaremos aquellas pistas reales. Usando
`cd`, navegaremos a `pistas/12345` y escribiendo `ls`. Deberías ver un único
archivo llamado `pista`.

#### `cat` ####

Finalmente necesitaremos ser capaces de ver a través de pistas. Primero lee la guía
`cat`, posteriormente haz:

    cat pista

Esto debería listar la pista en tu terminal. Por el momento, Todo lo que necesitamos
estará en el contenido del archivo pista. Es una buena idea registrar el rastro a través de los archivos de
pistas (como `123456`) en un trozo de papel. También podrías probar
cosas como copiar todos los archivos pista a tu directorio personal, o cortar y pegar
el texto de la pista a otro archivo de texto.
