# Assignment 2. OpenMP. Matrix multiplication

Write a program for multiplying two square matrices using OpenMP. Examine the performance of different modifications of the algorithm (different loop order), depending on the number of threads used for matrices of at least 800x800. Check the correctness of the multiplication on 5x5 matrices.

Calculate the efficiency by the formula t1 / t and display it, where t1 is the multiplication time on only one stream, t is the multiplication time on n streams (the number of streams is taken from 1 to 10).

The program should output number of threads,multiplication time and efficiency.

Transfer the size of matrices through the argv [] parameter.

**Hitns:**
Compile the program with the -fopenmp switch
## Compilation example:
```
gcc -o 3.o 3.c -fopenmp
```
or
```
g++ -o 3.o 3.cpp -fopenmp
```
Launch example:
```
./3.o matrix_size
```