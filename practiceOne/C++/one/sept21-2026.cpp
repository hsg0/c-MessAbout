/*
  C++ Beginner-to-Advanced Guide (inside a .cpp file)

  This file is written as a learning guide: explanatory comments followed by
  short, runnable examples. Read the comments, then compile and run this file
  to see the examples in action.

  Compile with (example):
    g++ -std=c++17 -O2 practiceOne/C++/one/sept21-2026.cpp -o sept21-2026
    ./sept21-2026

  Sections included:
  1) Hello world, includes, main
  2) Variables and basic types: int, double, bool, char
  3) std::cout and std::cin (I/O)
  4) Strings (std::string)
  5) Arithmetic and operators
  6) Control flow: if, switch, for, while
  7) Functions and overloading
  8) Arrays and std::vector
  9) Pointers and references
 10) Simple classes / OOP: constructors, methods
 11) Inheritance and polymorphism (virtual)
 12) The Standard Library (STL): vector, map, algorithm, lambda
 13) Smart pointers: unique_ptr, shared_ptr
 14) File I/O and exceptions
 15) Templates (basic example)
 16) Next steps & tips

  Read each section's comment and the small example that follows.
*/

#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <memory>
#include <fstream>
#include <algorithm>
#include <functional>

using std::cout;
using std::cin;
using std::endl;

// 1) Hello world, includes, main
// A C++ program starts in `main()`. Includes bring in declarations from
// the standard library. `#include <iostream>` gives us std::cout.

// 2) Variables and basic types
// - `int` : integers
// - `double` : floating-point numbers
// - `bool` : true/false
// - `char` : single characters
// Always initialize your variables when possible.

void basics_example() {
    cout << "--- Basics: variables & I/O ---\n";
    int a = 7;                // integer
    double pi = 3.14159;     // floating point
    bool flag = true;         // boolean
    char ch = 'A';           // character

    cout << "int a = " << a << ", double pi = " << pi << "\n";
    cout << "bool flag = " << flag << ", char ch = " << ch << "\n";

    // 3) std::cout and std::cin
    // `<<` streams values to cout; `>>` reads from cin.
    // Example (commented so running the program doesn't stop for input):
    // cout << "Enter a number: ";
    // int x; cin >> x; cout << "You entered: " << x << "\n";
}

// 4) Strings
// `std::string` is the standard string class. It behaves like a dynamic
// array of characters with useful member functions.

void strings_example() {
    cout << "--- Strings ---\n";
    std::string s = "Hello";
    s += ", C++"; // concatenation
    cout << s << " (length=" << s.size() << ")\n";
}

// 5) Arithmetic and operators
// +, -, *, /, %, ++, --, compound assignment (+=, -=), comparison (==, !=, <, >)

void arithmetic_example() {
    cout << "--- Arithmetic ---\n";
    int x = 10;
    int y = 3;
    cout << "x+y=" << (x+y) << ", x/y=" << (x/ y) << " (integer div)\n";
    cout << "x%y=" << (x % y) << "\n";
    double dx = 10.0, dy = 3.0;
    cout << "dx/dy=" << (dx / dy) << " (floating div)\n";
}

// 6) Control flow: if, switch, for, while

void control_flow_example() {
    cout << "--- Control flow ---\n";
    int n = 5;
    if (n > 0) {
        cout << "n is positive\n";
    } else {
        cout << "n is non-positive\n";
    }

    // switch
    // - `switch` selects a branch based on an integer-like expression.
    // - Each `case` is compared to `code`. If matched, that `case` runs.
    // - `break` prevents "fall-through" to the next case; without it,
    //   execution continues into the following case (sometimes useful,
    //   but often a source of bugs).
    // - `default` runs when no `case` matches (like an `else`).
    int code = 2; // change this to 1 or another value to see different branches
    switch (code) {
        case 1:
            cout << "one\n"; // runs only when code == 1
            break;
        case 2:
            cout << "two\n"; // runs when code == 2
            break;
        default:
            cout << "other\n"; // runs if no case above matched
            break;
    }

    // for loop
    // - classic loop with `init; condition; update`.
    // - order: init -> check condition -> body -> update -> repeat.
    cout << "for: ";
    for (int i = 0; i < 5; ++i) // i is 0..4
        cout << i << " ";
    cout << "\n";

    // range-based for (C++11+)
    // - iterates each element of a container (no index required).
    // - `int val` copies each element; use `auto& val` to modify in-place.
    std::vector<int> v = {10, 20, 30};
    cout << "range-for: ";
    for (int val : v) // prints 10 20 30
        cout << val << " ";
    cout << "\n";

    // while
    // - condition is evaluated before each iteration.
    // - here `t--` is post-decrement: it returns the old value, then
    //   decreases `t`. That makes the loop run while the old value is
    //   non-zero; the printed value is the decremented `t`.
    // Example walk-through with t=3:
    //   check: t-- yields 3 (true), t becomes 2 => print 2
    //   check: t-- yields 2 (true), t becomes 1 => print 1
    //   check: t-- yields 1 (true), t becomes 0 => print 0
    //   check: t-- yields 0 (false) => loop ends
    int t = 3;
    cout << "while: ";
    while (t--) // prints: 2 1 0
        cout << t << " ";
    cout << "\n";
}

// 7) Functions and overloading
// Functions are declared with a return type and parameter list.

int add(int a, int b) { return a + b; }
double add(double a, double b) { return a + b; } // overloaded

void functions_example() {
    cout << "--- Functions ---\n";
    cout << "add(2,3)=" << add(2,3) << "\n";
    cout << "add(2.5,3.1)=" << add(2.5,3.1) << "\n";
}

// 8) Arrays and std::vector
// Use `std::vector` for dynamic arrays. `std::array` for fixed-size arrays.

void arrays_vectors_example() {
    cout << "--- Arrays & Vectors ---\n";
    int arr[3] = {1,2,3}; // C-array
    cout << "arr[0]=" << arr[0] << "\n";

    std::vector<int> vec;
    vec.push_back(10);
    vec.push_back(20);
    cout << "vec size=" << vec.size() << ", elements: ";
    for (int x : vec) cout << x << " ";
    cout << "\n";
}

// 9) Pointers and references
// - Reference (`T&`) is an alias, cannot be null.
// - Pointer (`T*`) holds an address and can be null.

void pointer_reference_example() {
    cout << "--- Pointers & References ---\n";
    int a = 42;
    int &ref = a; // reference
    int *ptr = &a; // pointer
    cout << "a=" << a << ", ref=" << ref << ", *ptr=" << *ptr << "\n";
    *ptr = 100; // change via pointer
    cout << "a after *ptr=100: " << a << "\n";
}

// 10) Simple classes / OOP: constructors, methods
class Point {
public:
    double x, y;
    Point(double x_=0, double y_=0) : x(x_), y(y_) {}
    double dist2() const { return x*x + y*y; }
};

void oop_example() {
    cout << "--- OOP: classes ---\n";
    Point p(3.0, 4.0);
    cout << "Point(" << p.x << "," << p.y << ") dist2=" << p.dist2() << "\n";
}

// 11) Inheritance and polymorphism
class Animal {
public:
    virtual ~Animal() = default;
    virtual void speak() const { cout << "Animal sound\n"; }
};
class Dog : public Animal {
public:
    void speak() const override { cout << "Woof\n"; }
};

void inheritance_example() {
    cout << "--- Inheritance & Polymorphism ---\n";
    std::unique_ptr<Animal> a = std::make_unique<Dog>();
    a->speak(); // calls Dog::speak via virtual dispatch
}

// 12) STL: vector, map, algorithms, lambda
void stl_example() {
    cout << "--- STL: vector, map, algorithm, lambda ---\n";
    std::vector<int> nums = {5,2,8,1};
    std::sort(nums.begin(), nums.end());
    cout << "sorted: "; for (int n : nums) cout << n << " "; cout << "\n";

    std::map<std::string,int> ages;
    ages["Alice"] = 30;
    ages["Bob"] = 25;
    for (auto &kv : ages) cout << kv.first << ": " << kv.second << "\n";

    // lambda
    auto square = [](int x){ return x*x; };
    cout << "square(6)=" << square(6) << "\n";
}

// 13) Smart pointers
void smart_pointers_example() {
    cout << "--- Smart pointers ---\n";
    auto up = std::make_unique<Point>(1.0, 2.0);
    cout << "unique_ptr Point dist2=" << up->dist2() << "\n";

    auto sp = std::make_shared<Point>(2.0, 3.0);
    auto sp2 = sp; // shared ownership
    cout << "shared_ptr use_count=" << sp.use_count() << "\n";
}

// 14) File I/O and exceptions
void file_io_example() {
    cout << "--- File I/O & Exceptions ---\n";
    std::ofstream ofs("example.txt");
    if (!ofs) {
        cout << "Failed to open file for writing\n";
        return;
    }
    ofs << "C++ file I/O example\n";
    ofs.close();

    std::ifstream ifs("example.txt");
    if (!ifs) { cout << "Failed to open for reading\n"; return; }
    std::string line;
    std::getline(ifs, line);
    cout << "Read from file: " << line << "\n";
}

// 15) Templates (basic example)
template <typename T>
T max_val(T a, T b) {
    return (a < b) ? b : a;
}

void templates_example() {
    cout << "--- Templates ---\n";
    cout << "max_val(3,7)=" << max_val(3,7) << "\n";
    cout << "max_val(2.5,1.7)=" << max_val(2.5,1.7) << "\n";
}

// 16) Next steps & tips: (not code)
// - Practice small programs: calculator, todo list, file parser
// - Learn RAII: resources tied to object lifetime
// - Learn move semantics (std::move) and rvalue references next
// - Read more on C++ core guidelines and effective modern C++

int main() {
    cout << "C++ Guide Demo - running examples...\n\n";
    basics_example();
    strings_example();
    arithmetic_example();
    control_flow_example();
    functions_example();
    arrays_vectors_example();
    pointer_reference_example();
    oop_example();
    inheritance_example();
    stl_example();
    smart_pointers_example();
    file_io_example();
    templates_example();

    cout << "\nGuide file created. See comments at top for sections and compile command.\n";
    return 0;
}
