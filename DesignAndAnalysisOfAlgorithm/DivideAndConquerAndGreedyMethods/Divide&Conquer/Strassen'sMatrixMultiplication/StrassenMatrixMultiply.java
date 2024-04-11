import java.util.Arrays;

public class StrassenMatrixMultiply {

    public static int[][] strassenMatrixMultiply(int[][] A, int[][] B) {
        int n = A.length;
        int[][] C = new int[n][n];

        if (n == 1) {
            C[0][0] = A[0][0] * B[0][0];
        } else {
            int[][] A11 = subMatrix(A, 0, 0, n / 2);
            int[][] A12 = subMatrix(A, 0, n / 2, n / 2);
            int[][] A21 = subMatrix(A, n / 2, 0, n / 2);
            int[][] A22 = subMatrix(A, n / 2, n / 2, n / 2);

            int[][] B11 = subMatrix(B, 0, 0, n / 2);
            int[][] B12 = subMatrix(B, 0, n / 2, n / 2);
            int[][] B21 = subMatrix(B, n / 2, 0, n / 2);
            int[][] B22 = subMatrix(B, n / 2, n / 2, n / 2);

            int[][] P1 = strassenMatrixMultiply(addMatrix(A11, A22), addMatrix(B11, B22));
            int[][] P2 = strassenMatrixMultiply(addMatrix(A21, A22), B11);
            int[][] P3 = strassenMatrixMultiply(A11, subtractMatrix(B12, B22));
            int[][] P4 = strassenMatrixMultiply(A22, subtractMatrix(B21, B11));
            int[][] P5 = strassenMatrixMultiply(addMatrix(A11, A12), B22);
            int[][] P6 = strassenMatrixMultiply(subtractMatrix(A21, A11), addMatrix(B11, B12));
            int[][] P7 = strassenMatrixMultiply(subtractMatrix(A12, A22), addMatrix(B21, B22));

            int[][] C11 = addMatrix(subtractMatrix(addMatrix(P1, P4), P5), P7);
            int[][] C12 = addMatrix(P3, P5);
            int[][] C21 = addMatrix(P2, P4);
            int[][] C22 = addMatrix(subtractMatrix(addMatrix(P1, P3), P2), addMatrix(P6, P7));

            joinSubMatrix(C11, C, 0, 0);
            joinSubMatrix(C12, C, 0, n / 2);
            joinSubMatrix(C21, C, n / 2, 0);
            joinSubMatrix(C22, C, n / 2, n / 2);
        }

        return C;
    }

    public static int[][] subMatrix(int[][] matrix, int startRow, int startCol, int size) {
        int[][] result = new int[size][size];
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                result[i][j] = matrix[startRow + i][startCol + j];
            }
        }
        return result;
    }

    public static int[][] addMatrix(int[][] A, int[][] B) {
        int n = A.length;
        int[][] result = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                result[i][j] = A[i][j] + B[i][j];
            }
        }
        return result;
    }

    public static int[][] subtractMatrix(int[][] A, int[][] B) {
        int n = A.length;
        int[][] result = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                result[i][j] = A[i][j] - B[i][j];
            }
        }
        return result;
    }

    public static void joinSubMatrix(int[][] subMatrix, int[][] matrix, int startRow, int startCol) {
        int n = subMatrix.length;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                matrix[startRow + i][startCol + j] = subMatrix[i][j];
            }
        }
    }

    public static void main(String[] args) {
        int[][] A = {{1, 2, 3, 4},
                     {1, 2, 3, 4},
                     {1, 2, 3, 4},
                     {1, 2, 3, 4}};

        int[][] B = {{1, 2, 3, 4},
                     {1, 2, 3, 4},
                     {1, 2, 3, 4},
                     {1, 2, 3, 4}};

        int[][] C = strassenMatrixMultiply(A, B);

        for (int[] row : C) {
            System.out.println(Arrays.toString(row));
        }
    }
}
