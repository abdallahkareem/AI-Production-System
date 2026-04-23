from parser import load_facts, load_rules

facts = load_facts("data/facts.txt")
rules = load_rules("data/rules.txt")
print(rules[1])
