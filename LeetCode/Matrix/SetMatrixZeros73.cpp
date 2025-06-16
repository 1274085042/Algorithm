#include <vector>
#include <iterator>
#include <iostream>

using namespace std;

/*
* 使用两个标记数组，来标记某一行和某一列是否需要设置为0
*/
void SetMatrixZeroes(vector<vector<int>>& matrix) {
  int rows = matrix.size();
  int cols = matrix[0].size();
  vector<bool> row_flag(rows, false);
  vector<bool> col_flag(cols, false);

  for(int i=0;i<rows; ++i) {
    for(int j=0; j<cols; ++j) {
      if(matrix[i][j] == 0)
      {
        row_flag[i] = true;
        col_flag[j] = true;
      }
    }
  }

  for(int i=0;i<rows; ++i) {
    for(int j=0; j<cols; ++j) {
      if(row_flag[i] || col_flag[j]) {
        matrix[i][j] = 0;
      }
    }
  }
}


int main() {
  vector<vector<int>> matrix(3);
  matrix[0] = {0,1,2,0};
  matrix[1] = {3,4,5,2};
  matrix[2] = {1,3,1,5};
  SetMatrixZeroes(matrix);
  for(const auto & vec : matrix)
  {
    copy(vec.begin(), vec.end(), ostream_iterator<int>(std::cout," "));
    cout<<endl;
  }
}
