#include <iostream>
// #include <format> sorry it's C++20 but we live in paleozoic era
#include <vector>

// 	g++ -o ./Assignments_1/Assignment_0/ass0 ./Assignments_1/Assignment_0/ass0.cpp
//  ./Assignments_1/Assignment_0/ass0

using namespace std;

//prototypes cause we alse live not in 2k222

bool isSeparator(string);
int countWordsInString(vector<string>);
void printAnswer(int, char*);

// countWordsInString() — with a given counts words in it
int countWordsInString(vector<string> line) {
    int count = 0;
    for (int i = 0; i < line.size(); i++)  {
        if (isSeparator(line[i])) {
            continue;
        }

        count++ ;
    }
    
    return count;
}

// printAnswer() — with a given vector prints number of words in it
void printAnswer(vector<string> vc) {
    cout << vc.size();
    if (0 == vc.size()) {
        cout << "String Is Empty!";
        return;
    }
    
    int wordsNum = countWordsInString(vc);

    if (wordsNum > 0) {
        cout << "String Contains " << wordsNum << " Words!";
    } else {
        cout << "String Is Empty!";
    }
}

// isSeparator() — cheks if a string is a separator
bool isSeparator(string symbol) {
    return symbol == " " || symbol == "\t" || symbol == "\n";
}

int main(int argc, char* argv[]) {
    vector<string> allArgs(argv + 1, argv + argc);

    printAnswer(allArgs);
}

// printVector() — is a helper function to output the vector
void printVector(vector<string> vc) {
    for (auto it = vc.begin(); it != vc.end(); it++) {
        cout << *it << "\n";
    }
}