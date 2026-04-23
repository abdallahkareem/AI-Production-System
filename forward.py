import re


def check_condition(cond, facts):
    var, op, value = cond

    if op == "EXISTS":
        return var in facts

    if op == "is":
        return f"{var} is {value}".upper() in facts

    for fact in facts:
        match = re.match(rf"{var}\s*(>|<|=)\s*(\d+)", fact)
        if match:
            f_var, f_op, f_val = match.groups()
            f_val = int(f_val)

            if op == ">" and f_val > value:
                return True
            if op == "<" and f_val < value:
                return True
            if op == "=" and f_val == value:
                return True

    return False


def evaluate_conditions(conditions, operator, facts):
    results = [check_condition(cond, facts) for cond in conditions]

    if operator == "AND":
        return all(results)
    elif operator == "OR":
        return any(results)
    else:
        return results[0]


def forward_chaining(facts, rules):
    inferred = set(facts)
    changed = True

    while changed:
        changed = False
        print("Current facts:", inferred)

        for rule in rules:
            conditions = rule["conditions"]
            operator = rule["operator"]
            result = rule["result"]

            if evaluate_conditions(conditions, operator, inferred) and result not in inferred:
                print(f"Applying rule -> {result}")
                inferred.add(result)
                changed = True

    return inferred
