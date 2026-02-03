import pandas as pd
import numpy as np  

name = "World"
def greet(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet(name))

    # Example usage of pandas and numpy to avoid unused import warnings
    df = pd.DataFrame({'A': np.random.rand(5), 'B': np.random.rand(5)})
    print(df)


    arr = np.array([1, 2, 3, 4, 5])
    print(arr)


    # sort the array
    arr1 = np.array([5, 2, 9, 1, 5, 6])
    sorted_arr = np.sort(arr1)  
    print("Sorted array:", sorted_arr)

    # butterfly pattern
    n = 3
    for i in range(n):
        for j in range(n):
            if j <= i or j >= n - i - 1:
                print(" * ", end="")
            else:
                print("   ", end="")
        print()
    for i in range(n-1, -1, -1):
        for j in range(n):
            if j <= i or j >= n - i - 1:
                print(" * ", end="")
            else:
                print("   ", end="")
        print()
