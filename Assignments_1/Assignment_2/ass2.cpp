#include <iostream>
#include <vector>
#include <random>
#include <algorithm>
#include <ctime>
#include <omp.h>
#include <chrono>

// 	g++ -o ./Assignments_1/Assignment_2/ass2 ./Assignments_1/Assignment_2/ass2.cpp -fopenmp
//  ./Assignments_1/Assignment_2/ass2

using namespace std::chrono;
using std::vector;

//prototypes cause we alse live not in 2k222
vector<vector<int>> generateRandomSquareMatrix(int size);
void getTime(vector<vector<int>> A, vector<vector<int>> B);
void productOfMatricies(vector<vector<int>> A, vector<vector<int>> B, int threads_number);


int main(int argc, char* argv[]) {
    int matrix_size = atoi(argv[1]);
    vector<vector<int>> A = generateRandomSquareMatrix(matrix_size);
    vector<vector<int>> B = generateRandomSquareMatrix(matrix_size);

    getTime(A, B);
}

vector<vector<int>> generateRandomSquareMatrix(int size){
    // intializing vector of vectors
    vector<vector<int>> matrix(size);

    for (int i =0; i < matrix.size();i++){
        vector<int> rand_vc(size);
        srand(unsigned(time(nullptr))); // I want2die
        generate(rand_vc.begin(), rand_vc.end(), rand);

        matrix[i] = rand_vc;
    }
    
    return matrix;
}

void getTime(vector<vector<int>> A, vector<vector<int>> B) {
    // printf("vc[0]=%d vc[1]=%d", vc[0], vc[1]);
    int one_thread_efficency;
    for (int thrs = 1; thrs <= 10; thrs++) {
        auto time_start = high_resolution_clock::now(); // time recording starting point

        productOfMatricies(A, B, thrs);
        
        auto time_stop = high_resolution_clock::now(); // time recording starting point
        auto exectime = duration_cast<microseconds>(time_stop - time_start); // execution time calculation

        printf("Execution time via %d thread(s) in microseconds: %lld\n", thrs, exectime.count()); 
        if (thrs == 1) {
            one_thread_efficency = exectime.count();
        } else {
            printf("Efficency: x%d\n", one_thread_efficency /  exectime.count());
        }
    }
}

void productOfMatricies(vector<vector<int>> A, vector<vector<int>> B, int threads_number){
    vector<vector<int>> C(A.size(), vector<int>(A.size()));
    int rows_size = A.size();
    int cols_size = A.size();

    #pragma omp parallel for num_threads(threads_number)
     for (int i = 0; i < rows_size; ++i) {
        for (int j = 0; j < cols_size; ++j) {
            for (int k = 0; k < cols_size; ++k) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }     
}