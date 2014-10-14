#! /usr/bin/env python
# ben reichert, cs311 dfa-analyzer
#be nice and follow the rules and you'll have a nice dfa, otherwise...well...a bad piece of software
import csv
import sys

class DFA:
  current_state = None
  def __init__(self, states, transition_functions, language, start_state, accept_states, test_string):
    self.states = states
    self.tf = transition_functions
    self.language = language
    self.start_state = start_state
    self.accept_states = accept_states
    self.test_string = test_string
    return
  
  def go_to_start(self):
    self.current_state = self.start_state
    return
  
  def in_accept_state(self):
    if(self.current_state in self.accept_states):
      return True
    else:
      return False

  def transition(self, input):
    self.current_state = self.tf[(self.current_state, input)]
    return

  def run(self):
    self.go_to_start()
    for i in self.test_string:
      self.transition(i)
    return self.in_accept_state()


def main():
  print("Welcome to the DFA-Analyzer")

  #./dfa-analyzer.py dfa.csv
  csv_file = open(sys.argv[1], 'rt')
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
    transition_functions[(temp[0],temp[1])]=temp[2]


  boom_the_dfa = DFA(states, transition_functions, language, start_state[0], accept_states, ''.join(test_string))
  return_value = boom_the_dfa.run()
  if(return_value == True):
    print("String is in the language.")
  else:
    print("String is not in the language.")

if __name__ == "__main__":
  main()
