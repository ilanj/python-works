"""Little Shino and Common factors
Max. Marks: 100

Little Shino loves maths. Today her teacher gave her two integers. Shino is now wondering how many integers can divide both the numbers. She is busy with her assignments. Help her to solve the problem.

Input:
First line of the input file contains two integers, a and b.

Output:
Print the number of common factors of a and b.

Constraints:

SAMPLE INPUT

10 15

SAMPLE OUTPUT

2

Explanation

The common factors of
and

are 1 and 5.
Time Limit: 1.0 sec(s) for each input file.
Memory Limit: 256 MB
Source Limit: 1024 KB
Marking Scheme: Marks are awarded if any testcase passes.
Allowed Languages: C, C++, Clojure, C#, D, Erlang, F#, Go, Groovy, Haskell, Java, Java 8, JavaScript(Rhino), JavaScript(Node.js), Lisp, Lisp (SBCL), Lua, Objective-C, OCaml, Octave, Pascal, Perl, PHP, Python, Python 3, R(RScript), Racket, Ruby, Rust, Scala, Swift, Visual Basic
"""


class Factors:
    def input_nos(self):
        nos = input()
        a, b = nos.split()
        a = int(a)
        b = int(b)
        # b=int(input())
        maxi = a if a > b else b
        return a, b, maxi

    def commonfactors(self):
        flag = 0
        a, b, maxi = Factors.input_nos(self)
        for no in range(1, maxi):
            if a % no == 0 and b % no == 0:
                flag = flag + 1
        return flag


if __name__ == "__main__":
    obj = Factors()
    print(obj.commonfactors())
