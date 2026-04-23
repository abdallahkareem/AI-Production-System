from parser import load_facts, load_rules
from forward import forward_chaining

facts = load_facts("data/facts.txt")
rules = load_rules("data/rules.txt")

final_facts = forward_chaining(facts, rules)

print("\n=== Final Facts ===")
for f in sorted(final_facts):
    print(f)
