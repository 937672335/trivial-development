from tokenizer import tokenize
from parser import parse
from evaluator import evaluate_expression, repeat_until, switch_case

def main():
    environment = {'x': 2, 'y': 0}

    # Test modulus operator
    print("Testing modulus operator:")
    expression = "8 % 3"
    tokens = tokenize(expression)
    parsed_expression = parse(tokens)
    result = evaluate_expression(' '.join(parsed_expression), environment)
    print(result)  # Output should be 2

    # Test repeat until
    print("\nTesting repeat until loop:")
    repeat_until("y += 1", "y == 3", environment)
    print(environment['y'])  # Output should be 3

    # Test switch case
    print("\nTesting switch case:")
    cases = {
        "1": "print('Case 1')",
        "2": "print('Case 2')"
    }
    switch_case("x", cases, "print('Else block executed')", environment)

if __name__ == "__main__":
    main()