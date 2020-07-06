Proyecto fin Bootcamp Aprender a programar desde cero - Pygame 

Resumen de los objetivos cumplidos (y de los que no...):
    • Objetivo cumplido
    X Objetivo no cumplido
    \ Objetivo cumplido parcialmente
  
INICIO DE NIVEL 
    • Nuestra nave aparecerá en el margen izquierdo de la pantalla en el centro vertical. 
    • La nave se moverá hacia arriba y abajo con las teclas del cursor. 
    • La nave se parará en su ascenso y descenso si deja de pulsarse la tecla del cursor que corresponda 

Restricciones 
    • La nave no podrá avanzar ni retroceder de derecha a izquierda ni viceversa. 
    • Una vez alcanzado el nivel superior o inferior de la pantalla la nave se quedará parada. No desaparecerá de la 
    pantalla ni aparecerá por el otro lado. 

Opciones 
    X El movimiento hacia arriba y hacia abajo de la nave podrá ser acelerado si se mantiene pulsada la tecla de flecha. 

DESARROLLO DE NIVEL 
    \ Aparecerán obstáculos de diferente tipo y tamaño en alturas aleatorias en el margen derecho de la pantalla -> Aparecen 
    en alturas aleatorias, pero son todos del mismo tipo y tamaño.
    • Los obstáculos avanzarán en línea recta con diferentes velocidades de derecha a izquierda y desaparecerán al llegar al 
    margen derecho de la pantalla.
    \ Si cualquiera de los obstáculos choca con la nave, esta se destruirá con una explosión (sonido y animación) y acabará 
    la partida -> Aparece una imagen de explosión, pero no genera sonido ni finaliza juego.
    \ La dificultad del nivel viene determinada por la frecuencia de creación de obstáculos y su velocidad -> La función para 
    pasar de nivel está hecha, pero no funciona ni se anota el cambio en pantalla.
    \ Un nivel siempre debe ser más difícil que los anteriores -> No funciona el cambio de nivel, la intención era que creara 
    más asteroides y aumentara la velocidad.

Opciones 
    \ El nivel se terminará transcurrido un determinado tiempo o número de obstáculos esquivados (a decidir por el desarrollador) -> 
    Sin desarrollar.
    X Puede acelerarse la frecuencia de aparición de obstáculos dentro de un nivel o bien que sea constante. 
    X El mínimo de niveles serán 2, pudiendo crearse tantos como se quiera -> No funcionan los niveles.
    • La imagen de fondo de cada nivel puede ser la misma o distinta para cada nivel.
    • Se puede dejar la imagen de fondo y que el movimiento lo aporten los obtáculos, o animar la imagen de fondo para simular avance 
    incluso sin obstáculos. 

PUNTUACIONES 
    X La puntuación se incrementará a medida que la nave del jugador va esquivando obstáculos y progresa. Cuanto más tiempo aguante (más 
    obstáculos esquive) mayor será la puntuación -> Realmente cuenta con la creacion de asteroides, no con los obstáculos esquivados.
    • La puntuación empezará en cero al iniciar la partida 
    X Aterrizar en un planeta puede dar puntos extra (fin de nivel) -> Sin desarrollar.
    • La puntuación debe aparecer continuamente en pantalla. En la esquina superior izquierda. 

FIN DE NIVEL 
    X Una vez se produzca la condición de final de nivel (tiempo o número de obstáculos generados y esquivados) se alcanzará el final de 
    nivel -> Sin desarrollar.
    X Aparecerá un planeta por la parte izquierda de la pantalla -> Sin desarrollar.
    X Dejarán de aparecer obstáculos pero los que estén en pantalla deberán continuar su movimiento hasta el borde derecho o chocar con la 
    nave -> Sin desarrollar.
    X La nave girará 180 grados y aterrizará sobre el planeta de forma automática -> Sin desarrollar.
    X Aparecerá un cartel que indique "Pulse <tecla elegida por el programador> para continuar" -> Sin desarrollar.
    X Si fuera el último nivel el cartel sería de felicitación e indicaría acción para reiniciar el juego -> Sin desarrollar.
    x Si el jugador no iniciara la partida trasncurrido un tiempo, se volverá a la portada. -> Sin desarrollar.

Restricciones 
    X En ningún caso el aterrizaje automático puede implicar la colisión con un obstáculo (si aún estuvieran en pantalla). Una vez el juego 
    toma el control de la nave no se pueden producir colisiones -> Sin desarrollar.

PANTALLA INICIAL 
    X Mostrará el nombre y la historia del juego (la búsqueda de otro planeta) -> No funciona.
    X Indicará como iniciar la partida (con un botón o pulsando una tecla) -> No funciona.
    X Si el usuario pulsa esa tecla o botón se iniciará la partida -> No funciona.
    X Mostrará las instrucciones del juego -> No funciona.

Opciones 
    X Las instrucciones podrán aparecer directamente en la pantalla inicial, o indicar que pulsando una tecla se mostrarán las instrucciones 
    en otra pantalla o encima de la actual -> Sin desarrollar.
 
RECORDS DEL JUEGO 
    X Podrán almacenarse las 5 o 10 mejores puntuaciones con las iniciales del jugador -> Sin desarrollar.
    X Se almacenarán en una base de datos de SQLite -> Sin desarrollar.
    X Al finalizar la partida, si la puntuación fuera mayor que cualquiera de las 5 almacenadas, se habilitará una pantalla de entrada de datos 
    en la que se podrán incluir 3 iniciales (como en los videojuegos antiguos) -> Sin desarrollar.
    X El juego actualizará la tabla de records y los presentará en la pantalla de final de partida -> Sin desarrollar.

Opciones 
    • Los records pueden mostrarse nada más al final de partida o alternar entre pantalla inicial y pantalla de records. cambiando cada pocos 
    segundos entre una y otra -> Sin desarrollar.