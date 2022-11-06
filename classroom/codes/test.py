from __future__ import print_function
import ast

class FunctionCounter(ast.NodeVisitor):
    def __init__(self, filename):
        self.function_count = 0
        with open(filename) as f:
            module = ast.parse(f.read())
            self.visit(module)

    def visit_FunctionDef(self, node):
        #print('function: {}'.format(node.name))
        self.function_count += 1

    # Uncomment this to disable counting methods, properties within a
    # class
    # def visit_ClassDef(self, node):
    #     pass

if __name__ == '__main__':
    counter = FunctionCounter('code2.py')
    print('Number of functions: {}'.format(counter.function_count))


