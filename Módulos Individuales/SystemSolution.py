def SystemSolution(a, b):
    """
    DESCRIPCION DE LA FUNCION :
    La función crea la matriz aumentada de una matriz y un vector y la lleva a su 
    forma escalonada reducida e imprime dicha matriz, las variables basicas y 
    libres y las variables basicas definidas en forma de las variables libres.


    ENTRADA ( INPUT ):
    * Una matriz a
    * Un vector b

    SALIDA ( OUTPUT ):
    * La matriz resultante en forma escalonada reducida.
    * Si el sistema es indeterminado o no.
    * Las variables básicas.
    * Las variables libres.
    * Las variables básicas definidas en terminos de las varibles libres

    """
    
    # Sacar las dimensiones de la matriz
    m, n = a.dimensions()
    bN = len( b )
    # Variables 
    variables = [ 0 ] * n # Sistema para saber si una variable es libre o basica, 
    basicas = [] 

    if( m == bN ): 

        # Procedemos a calcular la matriz aumentada
        result = a.augment( b, subdivide = True )
        # Para saber si una matriz tiene solución debemos comprabar si el rango de la matriz 
        # y el rango de la matriz aumentada son iguales.
        # En el caso contrario, podemos afirmar que la matriz no tiene solución.
        if ( result.rank() ==  a.rank() ):

            noPivotes = len( result.pivots() )          # Saco el número de variables libres.            
            result = result.rref()                      # Se pasa a la forma escalonada reducida de la matriz.

            print( "Matriz reducida: ")
            print( result, end = '\n\n' )                                                  # Imprimo la matriz resultante.
            
            # Se verifica si el sistema es determinado ( cumpliendo con el número de pivotes ) o si es indeterminado (
            # existencia de variables libres )
            if ( noPivotes == bN ):

                print( "El sistema es determinado" )

            else:

                print( "El sistema es indeterminado" )
            print()
            # Variables libres.
            columnasBasicas = result.pivots()                                # Obtengo las columnas de los pivotes
            filasBasicas = result.pivot_rows()                               # Obtengo las filas de los pivotes
            
            cont = 0                                                         # Agrego un indice para acceder a los valores de los pivotes
            for elemento in columnasBasicas:
                
                variables[ cont ] = 1                                        # Actualizo mi lista de variables
                
                variable = [ filasBasicas[ cont ], 
                             columnasBasicas[ cont ] ]                       # Creo la posición de las variable libres.
                
                basicas.append( variable )                                   # Agrego la variable libre a mi lista
                
                cont += 1;                                                   # Paso al siguiente elemento de los pivotes


                
            print( "Variables basicas: ", end = ' ' )
            for elemento in basicas:                                         # Se seleccionan las variables básicas.
                
                print( "x_{}".format( elemento[ 1 ] + 1 ), end = ', ' )      # Se imprime la variable deseada.
            
            print()
            print( "\nVariables libres: ", end = ' ' )                    
            for elemento in range( n ):
            
                if variables[ elemento ] == 0:                               # Se selecciona las variables que no sean básicas.
            
                    print( "x_{}".format( elemento + 1 ), end = ', ' )       # Imprime variables básicas.
            
            print()
            print("\nVariables basicas escritas en terminos de variables independientes.")
            for elemento in basicas:                                         # Selecciona la variable básica.
                
                print( "x_{}".format( elemento[ 1 ] + 1 ), end = ' = ' )     # Imprime el valor
                
                row = result.row( elemento[ 0 ] )                            # Guardo el renglón donde esta la matriz basica
                
                for x in range( elemento[ 1 ] + 1, n ):                      # leo las variables que siguen a la variable básica.
                    
                    if( row[ x ] != 0 ):                                     # Detecto si la variable en cuestión existe.
                        
                        if( row[ x ] > 0 ):                                  # Detecto si es positivo o negativo, considerando que se va invertir su signo.
                            
                            if( row[ x ] == 1 ):                             # Formato para valores iguales a 1.

                                print( "- x_{}".format( x + 1 ), end = ' ' )

                            else:                                            # Formato para valores mayores a 1.

                                print( "- {}x_{}".format( row[ x ], x + 1 ), end = ' ' )
                                
                        else:                                                # Detecto si es negativo
                            
                            row[ x ] *= -1                                   # Vuelvo el valor a positivo
                            
                            if( row[ x ] == 1 ):                             # Formato para valores iguales a 1.

                                print( "+ x_{}".format( x + 1 ), end = ' ' )

                            else:                                            # Formato para valores mayores a 1.

                                print( "+ {}x_{}".format( row[ x ], x + 1 ), end = ' ' )

                if( row[ n ] == 0 ):                                     # Detecto si existe un valor en la última posición del renglón.
                    
                    print( '\n' )
                
                else:                                                        # Si existe, debemos de considerarlo con su mismo signo
                    
                    if( row[ n ] > 0 ):                                  # Detecto si el valor es positivo.
                        
                        print( "+ {}".format( row[ n ] ) )                   # Imprimo con formato de positivo.
                        
                    else:                                                    # Detecto si el valor es negativo.
                        
                        row[ n ] *= -1
                        print( "- {}".format( row[ n ] ) )                   # Imprimo con formato de negativo.
            
        else:

            print("El sistema es inconsistente")

    else:

        print( "Las dimensiones de la matriz y el vector independiente no coinciden, intentelo otra vez." )