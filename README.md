Piedra, Papel o Tijera (Python)

Autor: Matías Castro Guerra
Docente: Estefanía Vanessa Heredia Jiménez
Materia: Lógica de Programación – Proyecto Integrador
Fecha: 24 de agosto de 2025

Descripción

Juego de consola para Piedra, Papel o Tijera contra la computadora. Valida la entrada, repite automáticamente en caso de empate y muestra el resultado de cada ronda. El código usa dos bucles while anidados y una única condición compuesta para decidir la victoria.

Requisitos

Python 3.x

Ejecución
# 1) Clonar o descargar el repositorio
git clone <(https://github.com/MatixProx/Matias-Castro---Piedra-Papel-o-tijera-FINAL.git)>
cd Matias-Castro---Piedra-Papel-o-tijera

# 2) Ejecutar
En python piedra_papel_tijera.py

Uso

Ingresa: 1 = piedra, 2 = papel, 3 = tijera.

Si la entrada no es 1/2/3, se avisa y se vuelve a pedir.

Si hay empate, ambos vuelven a elegir automáticamente.

El juego continúa indefinidamente; para salir cierra la consola.

Ideas clave del código

Diccionario de opciones: opciones = {1: "piedra", 2: "papel", 3: "tijera"}.

Elección de la computadora con random.randint(1, 3).

Bucle interno: valida entrada y gestiona el empate (con continue).

Bucle externo: permite jugar rondas continuas.

Regla de victoria en una sola condición compuesta:

piedra > tijera,

tijera > papel,

papel > piedra.
