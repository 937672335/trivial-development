def evaluate_expression(expression, environment):
    try:
        return eval(expression, {}, environment)
    except NameError as e:
        print(f"Error: {e}")

def repeat_until(block, condition, environment):
    while not eval(condition, {}, environment):
        exec(block, {}, environment)

def switch_case(expression, cases, else_block, environment):
    expression_value = eval(expression, {}, environment)
    for case, block in cases.items():
        if eval(case, {}, environment) == expression_value:
            exec(block, {}, environment)
            return
    if else_block:
        exec(else_block, {}, environment)