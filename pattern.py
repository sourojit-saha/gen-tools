import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from basic_units import cm, inch

def chessboard(rows, cols, start):
    if "0" in start:
        mat = np.ones((rows, cols))
        for i in range(rows):
            for j in range(cols):
                if (i+j)%2 == 0:
                    mat[i,j] = 0
        # mat = mat * 250
        print(mat)
        return mat
    elif "1" in start:
        mat = np.zeros((rows, cols))
        for i in range(rows):
            for j in range(cols):
                if (i+j)%2 == 0:
                    mat[i,j] = 1
        # mat = mat * 250
        print(mat)
        return mat
    else: 
        print("wrong start...should be 0 or 1.")
        return
    

if __name__ == "__main__":
    mat = chessboard(5,5,"0")
    plt.figure(figsize=(5,5)) # this is 5 inch x 5 inch 
    plt.imshow(mat, cmap = 'gray')
    plt.axis('off')
    plt.savefig('foo.pdf', bbox_inches='tight')
    # plt.show()



