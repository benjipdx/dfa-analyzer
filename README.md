dfa-analyzer
============

CS 311 project 1

###Writeup at writeup.pdf and writeup.tex

###script at dfa-analyzer.py

###How it works:

```
$ ./dfa-analyzer.py dfa-not-in-language.csv 
$ cat dfa-not-in-language.csv 
1,0
S
Q
S->1->S,S->0->Q,Q->0->Q,Q->1->S
S
1000010101010010100101001000101000000
$ ./dfa-analyzer.py dfa-not-in-language.csv 
Welcome to the DFA-Analyzer
String is not in the language.
$ cat dfa.csv
1,0
S
Q
S->1->S,S->0->Q,Q->0->Q,Q->1->S
S
100001
$ ./dfa-analyzer.py dfa.csv
Welcome to the DFA-Analyzer
String is in the language.
```
