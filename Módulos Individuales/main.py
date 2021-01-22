import SystemSolution

def main():
    print("Bienvenido a la Calculadora-Inador 3000")
    
    # Entrada
    a = matrix(QQ, 1, 6, [2, 4, 6, 8, 10, 12])
    b = vector([5])

    SystemSolution(a, b)
    

if __name__ == "__main__":
    main()