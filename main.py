from parser import load_facts, load_rules
from forward import forward_chaining

facts = load_facts("data/facts.txt")
rules = load_rules("data/rules.txt")

final_facts = forward_chaining(facts,rules)

print("Final Facts :\n",new_facts)
