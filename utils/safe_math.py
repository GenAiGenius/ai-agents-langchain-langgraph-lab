import ast
import operator as op

# Supported operators
_ops = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Pow: op.pow,
    ast.Mod: op.mod,
    ast.USub: op.neg,
    ast.UAdd: op.pos,
    ast.FloorDiv: op.floordiv
}

def eval_expr(expr: str) -> float:
    """Safely evaluate a simple arithmetic expression."""
    node = ast.parse(expr, mode='eval').body
    return _eval(node)

def _eval(node):
    if isinstance(node, ast.Num):  # <number>
        return node.n
    if isinstance(node, ast.BinOp):  # <left> <op> <right>
        return _ops[type(node.op)](_eval(node.left), _eval(node.right))
    if isinstance(node, ast.UnaryOp):  # <op> <operand> e.g., -1
        return _ops[type(node.op)](_eval(node.operand))
    raise ValueError("Unsupported expression")
