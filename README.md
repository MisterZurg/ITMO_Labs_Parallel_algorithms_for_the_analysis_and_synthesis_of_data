# Parallel algorithms for the analysis and synthesis of data

Lector: Sokhin Timur, PhD student

## Assignments
- [Assignment 1: MPI — C++](Assignments_1)
- [Assignment 2: MPI - Python](Assignments_2/README.md)
- Assignment 3: TBA
- Assignment 4: TBA


## Notes:
**С++ compiler for Windows:**

[I recommend using this version of gcc](http://www.equation.com/servlet/equation.cmd?fa=fortran)

**C++ for Ubuntu:**

probably you will need this: 
```sh
sudo apt install libomp-dev
sudo apt install build-essential
```


The compilation command in all cases should look like this: 
```
g++ -o output_name.o input_name.cpp -fopenmp. 
```
`-o` flag means destination file, 

`-fopenmp` allows you to use openmp directives in your code.

# C++ SUCK SO WHY I MADE A MAKE FILE
To run program simply type in a terminal
```
make PRG={RELATIVE PATH TO .cpp file}
```

```
Undefined symbols for architecture arm64:
  "___kmpc_end_reduce_nowait", referenced from:
      _.omp_outlined. in ass1-b940bc.o
```