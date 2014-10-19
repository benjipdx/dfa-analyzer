#! /usr/bin/env python
# ben reichert, cs311 dfa-analyzer
#be nice and follow the rules and you'll have a nice dfa, otherwise...well...a bad piece of software
#looked at these links for notes:
#http://pythonfiddle.com/dfa-simple-implementation/
#http://www.lamantia.org/archives/457
#https://github.com/reverie/python-automata/blob/master/DFA.py

import csv
import sys

class DFA:
  """Class to represent the traversal of a dfa, given the dfa's language, transition functions, states, and a string to test against"""
  current_state = None #required to set the current state to nothing, since you have to wait after init to set it to point to the start state, this is "global" to the class functions
  def __init__(self, states, transition_functions, language, start_state, accept_states, test_string):
    """just takes in input, and sets it in variables in the object"""
    self.states = states
    self.tf = transition_functions
    self.language = language
    self.start_state = start_state
    self.accept_states = accept_states
    self.test_string = test_string
    return
  
  def go_to_start(self):
    """we should really start at well, the start state..."""
    self.current_state = self.start_state
    return
  
  def in_accept_state(self):
    """returns True if we current state is an accepting one, used to check if after testing we should accept the string for that DFA language representation"""
    if(self.current_state in self.accept_states):
      return True
    else:
      return False

  def transition(self, input):
    """this its like current-> next, it literally just does a dict lookup and check where we currently are, and where we should go next and transitions accordinly"""
    self.current_state = self.tf[(self.current_state, input)]
    return

  def run(self):
    """this function initializes the testing of a string against the DFA given, by transitioning on each character of the string and then returning if we are on an accept state or not when done simulating a DFA"""
    self.go_to_start()
    for i in self.test_string:
      self.transition(i)
    return self.in_accept_state()


def main():
  print("Welcome to the DFA-Analyzer")

  #./dfa-analyzer.py dfa.csv
  csv_file = open(sys.argv[1], 'rt') #read in argv as filename
  if("csv" not in sys.argv[1]):
    print("Usage: ./dfa-analyzer dfa.csv")
  try:
    #read in csv datas
    reader = csv.reader(csv_file)
    language = reader.next() #get language line
    start_state = reader.next() #get start state, only should be one
    states = reader.next() #get rest of states
    states += start_state
    transitions = reader.next() #get transitions
    accept_states = reader.next() #get accepting states
    test_string = reader.next() #get test_string

  
  finally:
    csv_file.close()

  #make transitions table
  transition_functions = dict()
  for t in transitions:
    #split on ->
    temp = t.split("->")
    transition_functions[(temp[0],temp[1])]=temp[2] #add to our dict


  a_wild_dfa_appears = DFA(states, transition_functions, language, start_state[0], accept_states, ''.join(test_string)) #create a dfa object
  return_value = a_wild_dfa_appears.run() #initlize the test simulation
  if(return_value == True):
    print("String is in the language.")
  else:
    print("String is not in the language.")

if __name__ == "__main__":
  main()
