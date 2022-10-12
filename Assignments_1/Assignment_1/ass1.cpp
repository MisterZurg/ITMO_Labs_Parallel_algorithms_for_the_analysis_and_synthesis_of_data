#include <iostream>
#include <vector>
#include <random>
#include <algorithm>
#include <ctime>
#include <omp.h>
#include <chrono>


// 	g++ -o ./Assignments_1/Assignment_1/ass1 ./Assignments_1/Assignment_1/ass1.cpp -fopenmp
//  ./Assignments_1/Assignment_1/ass1

using namespace std::chrono;
using std::vector;

//prototypes cause we alse live not in 2k222
int getMaxFromVector(vector<int> vc, int threads_number);
vector<int> generateRandomVector(int size);
// void printVector(vector<int> vc);
void getTime(vector<int> vc);


int main(int argc, char* argv[]) {
    int size = atoi(argv[1]);
    vector<int> vc = generateRandomVector(size);

    getTime(vc);
}

int getMaxFromVector(vector<int> vc, int threads_number) {
    int max_value = vc[0];
    #pragma omp parallel for num_threads(threads_number) reduction(max : max_value)
    for (auto it = vc.begin(); it != vc.end(); it++) {
        max_value = max_value < *it ? *it : max_value;
    }
    // printf("max_value=%d", max_value);
    return max_value;
}

void getTime(vector<int> vc) {
    // printf("vc[0]=%d vc[1]=%d", vc[0], vc[1]);

    for (int thrs = 1; thrs <= 10; thrs++) {
        auto time_start = high_resolution_clock::now(); // time recording starting point

        int max_value = getMaxFromVector(vc, thrs);
        
        auto time_stop = high_resolution_clock::now(); // time recording starting point
        auto exectime = duration_cast<microseconds>(time_stop - time_start); // execution time calculation

        printf("Execution time via %d thread(s) in microseconds: %lld\n", thrs, exectime.count()); 
        printf("Maximum value: %d\n", max_value);
    }
}

vector<int> generateRandomVector(int size) {
    vector<int> rand_vc(size);

    //
    srand(unsigned(time(nullptr))); // I want2die
    generate(rand_vc.begin(), rand_vc.end(), rand);
    
    return rand_vc;
}

// printVector() — is a helper function to output the vector
// void printVector(vector<int> vc) {
//     for (auto it = vc.begin(); it != vc.end(); it++) {
//         cout << *it << "\n";
//     }
// }