import sys
def xSum():
    # Read number of test cases
    t = int(sys.stdin.readline().strip())

    for _ in range(t):
        # Read matrix dimensions

        m,n = map(int, sys.stdin.readline().split())
        matrix = [list(map(int,input().split())) for _ in range(m)]
        # Read the matrix
        #matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
    # print(matrix)         m,n = map(int, input().split())  # Read matrix dimensions
        # print(matrix)
        diagonal_1 = {}
        for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if i + j not in diagonal_1:
                        diagonal_1[i+j] = matrix[i][j]
                    else:
                        diagonal_1[i+j] += matrix[i][j]
        # Now let's repeat this process for the roated matrix
        rotated_matrix = [[matrix[j][i] for j in range(len(matrix) - 1, -1, -1)] for i in range(len(matrix[0]))]
        diagonal_2 = {}
        for i in range(len(rotated_matrix)):
                for j in range(len(rotated_matrix[i])):
                    if i + j not in diagonal_2:
                        diagonal_2[i+j] = rotated_matrix[i][j]
                    else:
                        diagonal_2[i+j] += rotated_matrix[i][j]

        # now let's create a sum array and return the maximum sum
        print(diagonal_1)     
        print(diagonal_2)      
        result = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                result.append(diagonal_1[i+ j] + diagonal_2[i+j] - matrix[i][j]) 
        return max(result)

print(xSum())


                
        


        
