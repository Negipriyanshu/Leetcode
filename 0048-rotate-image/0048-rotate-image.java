class Solution {
    public void rotate(int[][] matrix)
     {  
        
        int rows = matrix.length;
        int coloums = matrix[0].length;
        int[][] matrix1;
        matrix1 = new int[rows][coloums];
        int m=rows-1;
        for(int i = 0;i<rows;i++)
        {
            for(int j=0;j<coloums;j++)
            {
                
                matrix1[j][m]=matrix[i][j];
            }
            m=m-1;
        }
        for(int i = 0;i<rows;i++)
        {
            for(int j=0;j<coloums;j++)
            {
                
                matrix[i][j]=matrix1[i][j];
                System.out.print(matrix[i][j]);
            }
            System.out.println("");
        }
}
}