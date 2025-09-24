operation = "multiply"
a, b = 5, 3

ops = {
    "add": lambda x, y: x + y,
    "subtract": lambda x, y: x - y,
    "multiply": lambda x, y: x * y,
}

result = ops.get(operation, lambda x, y: None)(a, b)

print(result)
