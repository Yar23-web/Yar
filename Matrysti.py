import numpy as np

def matrix_input():
    """Функція для введення матриці з клавіатури"""
    rows = int(input("Введіть кількість рядків матриці: "))
    cols = int(input("Введіть кількість стовпців матриці: "))
    
    print("Введіть елементи матриці рядок за рядком (через пробіл):")
    matrix = []
    for i in range(rows):
        row = list(map(float, input().split()))
        if len(row) != cols:
            print(f"Помилка! Ви повинні ввести рівно {cols} елементів.")
            return None
        matrix.append(row)
    
    return np.array(matrix)

def add_matrices(matrix1, matrix2):
    """Додавання двох матриць"""
    return matrix1 + matrix2

def subtract_matrices(matrix1, matrix2):
    """Віднімання двох матриць"""
    return matrix1 - matrix2

def multiply_matrices(matrix1, matrix2):
    """Множення двох матриць"""
    return np.dot(matrix1, matrix2)

def display_menu():
    """Відображення меню для користувача"""
    print("\n--- Калькулятор матриць ---")
    print("1. Додавання матриць")
    print("2. Віднімання матриць")
    print("3. Множення матриць")
    print("4. Вихід")

def main():
    """Основна функція"""
    while True:
        display_menu()
        choice = input("Виберіть операцію (1/2/3/4): ")
        
        if choice == '4':
            print("До побачення!")
            break
        
        print("\nВведіть першу матрицю:")
        matrix1 = matrix_input()
        
        print("\nВведіть другу матрицю:")
        matrix2 = matrix_input()
        
        if matrix1 is None or matrix2 is None:
            print("Помилка при введенні матриць. Спробуйте ще раз.")
            continue
        
        if choice == '1':
            # Додавання
            if matrix1.shape == matrix2.shape:
                result = add_matrices(matrix1, matrix2)
                print("\nРезультат додавання:")
                print(result)
            else:
                print("Матриці повинні мати однакові розміри для додавання!")
        
        elif choice == '2':
            # Віднімання
            if matrix1.shape == matrix2.shape:
                result = subtract_matrices(matrix1, matrix2)
                print("\nРезультат віднімання:")
                print(result)
            else:
                print("Матриці повинні мати однакові розміри для віднімання!")
        
        elif choice == '3':
            # Множення
            if matrix1.shape[1] == matrix2.shape[0]:
                result = multiply_matrices(matrix1, matrix2)
                print("\nРезультат множення:")
                print(result)
            else:
                print("Кількість стовпців першої матриці повинна дорівнювати кількості рядків другої матриці для множення!")
        
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
    input("\n")
