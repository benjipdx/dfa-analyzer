#general info:
#statename,[0 for start state, 1 for non-accepting state, 2 for accepting state, 3 for starting and accepting state]

#connections
fromstatename,tostatename,substringoflanguage

example simple dfa:
--> (q1) -> 0 -> ((q2))
         <- 1 < -

STATES
q1,0
q2,2
CONNECTIONS
q1,q2,0
q2,q1,1


q1 loops on itself, 0,1
--> ((q1)) ---
             |
      ^-- 1,0-

STATES
q1,3
CONNECTIONS
q1,q1,1-0




q1 loops on itself, 0,1
--> ((q1)) ---
             |
      ^-- 1,0,3,4,5-

STATES
q1,3
CONNECTIONS
q1,q1,1-0-3-4-5
