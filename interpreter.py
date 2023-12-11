# Terrible Programming Language+ Interpreter (now uses Lark!)
# jdev082 & UniqueName12345/DifferentDance8, MIT License 2023
# It's in the name, don't bother.

from lark import Lark

grammar = '''
start: expression

?expression: term
           | expression "+" term   -> add
           | expression "-" term   -> sub

?term: factor
     | term "*" factor           -> mul
     | term "/" factor           -> div

?factor: NUMBER
       | "(" expression ")"

%import common.NUMBER
%import common.WS
%ignore WS
'''

parser = Lark(grammar, start='start')

ERRS = ["MISSING_ARGS", "UNSUPPORTED_FILE_TYPE", "MISSING_ARGTYPE_IDENTIFIER", "VAR_UNDEFINED"]
RT_VARS = [""]

def err(code):
    print(f"ERR: {ERRS[code]}")
    exit()

def intrp(lcont):
    try:
        tree = parser.parse(lcont)
        result = evaluate(tree)
        print(result)
    except Exception as e:
        print(f"Error: {e}")
        err(3)

def evaluate(tree):
    if tree.data == 'add':
        return evaluate(tree.children[0]) + evaluate(tree.children[1])
    elif tree.data == 'sub':
        return evaluate(tree.children[0]) - evaluate(tree.children[1])
    elif tree.data == 'mul':
        return evaluate(tree.children[0]) * evaluate(tree.children[1])
    elif tree.data == 'div':
        return evaluate(tree.children[0]) / evaluate(tree.children[1])
    elif tree.data == 'expression' or tree.data == 'term' or tree.data == 'factor':
        return evaluate(tree.children[0])
    else:
        return int(tree.children[0].value)