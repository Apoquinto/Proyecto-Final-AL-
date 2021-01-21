# Proyecto Final AL
<center>

![calculator](/images/calculator.svg)

</center>

<div>Icons made by <a href="https://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>

El proyecto final consiste de una serie de programas para correr en SageMath para resolver diferentes problemas de Álgebra Lineal.

## Requerimientos
1. La calculadora debe de hallar el conjunto solución de un sistena de ecuaciones.
2. La calculadora debe de determinar el conjunto generador para un subespacio.
3. La calculadora debe de determinar la matriz de relaciones para un subespacio <v,v',...vn>.
4. La calculadora debe calcular las proyecciones ortogonales y aplicar el proceso de Gram - Schmid (Para una matriz simétrica y positiva).

Este proyecto se conforma por 5 módulos para realizar los requerimientos necesarios:
- Main. El módulo principal de python que une todas las partes del sistema y de recibir e interpretar el input del sistema.
- SystemSolution. Módulo destinado a resolver matrices y dar los resultados de las mismas.
- GeneratorSet. Módulo encargado de encontrar e imprimir el set generador.
- RelationshipMatrix. Módulo encargado de determinar la matriz de relaciones dado un subconjunto 'v'.
- OctogonalProjections. Módulo encargado de calcular las proyecciones octogonales usando el proceso de Gram - Schmid dada una simétrica y positiva.

Al finalizar el desarrollo, se reunirá cada parte para crear la entrega final del proyecto, pero para fines educativos/explicativos, se desarrollaran y trabajaran separados.