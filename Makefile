# When we run make without any arguments, it executes the first target.
# (target is the "name:" stuff)
# So why I named it like do all stuff
all: build run
 
# make PRG=./Assignment-0/HW2
 
# build - builds the C++ file with the given name
build:
   g++ -o ${PRG} ${PRG}.cpp
 
# run - runs the C++ program LIKE IN A NORMAL IDE'S FOR GODS...
run:
   ./${PRG}
 
# it’s a good idea to have a clean target to delete all the generated files,
# basically returning the project to a clean slate.
# clean:
#    rm ${PRG}
 
# 	AS = Assignment-NUMBER is a Main Assigment that cnsists from SA
#	SA = Sub-assignment-NUMBER is a Part of Main Assigment
#   Example:
#   ITMO_LABS....
#   |— Assignments_1    	// <- 1 is AS
#	|	|— Assignment_0		// <- 0 is SA
#	|	|— Assignment_1		// <- 1 is SA
#	...
wsbd:
	g++ -o ./Assignments_${AS}/Assignment_${SA}/ass${SA} ./Assignments_${AS}/Assignment_${SA}/ass${SA}.cpp

semirun:
   ./Assignments_${AS}/Assignment_${SA}/ass${SA}
 
# Also I was loking for the GUDE FOR AGES:
# Good paper about Makefile on "earthly" by Aniket Bhattacharyea
# https://earthly.dev/blog/g++-makefile/
