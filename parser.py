
import re

def load_facts(file_path):
    facts = set()

    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()

            if line == "":
                continue

            facts.add(line.upper())

    return facts


def parse_single_condition(cond):
    cond = cond.strip()

    # case 1: comparison (>, <, =)
    match = re.match(r"(\w+)\s*(>|<|=)\s*(\d+)", cond)
    if match:
        var, op, value = match.groups()
        return (var.upper(), op, int(value))

    # case 2: "is"
    if " is " in cond:
        var, value = cond.split(" is ")
        return (var.strip().upper(), "is", value.strip().upper())

    # case 3: single fact
    return (cond.upper(), "EXISTS", True)


def parse_conditions(left):
    if " AND " in left:
        parts = left.split(" AND ")
        operator = "AND"
    elif " OR " in left:
        parts = left.split(" OR ")
        operator = "OR"
    else:
        parts = [left]
        operator = "SINGLE"

    conditions = [parse_single_condition(p) for p in parts]

    return conditions, operator


def load_rules(file_path):
    rules = []

    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()

            if not line:
                continue

            line = line.upper()

            if "IF" not in line or "THEN" not in line:
                print(f"Invalid rule: {line}")
                continue

            line = line.replace("IF", "").strip()

            left, right = line.split("THEN")

            conditions, operator = parse_conditions(left.strip())

            rules.append({
                "conditions": conditions,
                "operator": operator,
                "result": right.strip()
            })

    return rules
