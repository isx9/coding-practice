def evaluate(problem: str):
    """Evaluate a simple addition or subtraction such as '2+3' or '7-4'."""
    if '+' in problem:
        first, second = problem.split('+')
        return int(first) + int(second)
    first, second = problem.split('-')
    return int(first) - int(second)


def filter_solutions():
    """Split solutions.csv into correct.csv and incorrect.csv."""
    with open('solutions.csv', 'r', encoding='utf-8') as source, \
         open('correct.csv', 'w', encoding='utf-8') as correct, \
         open('incorrect.csv', 'w', encoding='utf-8') as incorrect:

        for line in source:
            line = line.strip()
            _, problem, result = line.split(';')

            if evaluate(problem) == int(result):
                correct.write(line + '\n')
            else:
                incorrect.write(line + '\n')
