# Assignment 1. OpenMP. Finding the maximum value of a vector

Write a parallel OpenMP program that finds the maximum value of a vector (one-dimensional array). Each thread should only store its maximum value; concurrent access to a shared variable that stores the maximum value is not allowed.

Study the dependence of the runtime on the number of threads used (from 1 to 10) for a vector that contains at least 1,000,000 elements (the more, the better).

Check the correctness of the program on 10 elements.

The program should display on the screen: the number of threads, the execution time.

Transfer the size of the vector through the `argv [1]` parameter.

**Hint1:** You can use the atoi function to convert the argv value to an int. To use the function, you need to connect the `<cstdlib>` library.
Example:
```cpp
int N = atoi (argv [1]);
```
Compile the program with the `-fopenmp` switch. 
### Compilation example:
```
gcc -o 2.o 2.c -fopenmp
g++ -o 2.o 2.cpp -fopenmp
```
### Startup example:
```
./2.o array_size
```
**Hint2:** To find the maximum number, you may need the option
```cpp
reduction (max:max_element);



gcc -Xpreprocessor -fopenmp hello.cpp -I /usr/local/include -L /usr/local/lib -lomp -o hello.bin
```



brew install cmake
brew install libomp

g++ -Xclang -fopenmp foo.cc -lomp

g++ -Xclang -fopenmp -o ./Assignment-0/ass0 ./Assignment-0/ass0.cpp  


clang++ -Xpreprocessor -fopenmp main.cpp -o main -lomp

clang++ -Xpreprocessor -fopenmp ./Assignment-1/ass1.cpp -o ./Assignment-1/ass1 -lomp 

g++ -std=c++11 -Xpreprocessor -L/opt/homebrew/opt/libomp/lib/ -fopenmp ./Assignment-1/ass1.cpp -o ./Assignment-1/ass1 -lomp




OPENMP FOR MAC M1
brew install cmake
brew install libomp


clang++ -Xpreprocessor -fopenmp -I/usr/local/include -L/opt/homebrew/opt/libomp/lib -lomp  ./Assignment-1/ass1.cpp -o ./Assignment-1/ass1