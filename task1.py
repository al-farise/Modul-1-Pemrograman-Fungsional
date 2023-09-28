
# fungsi pengurangan
def add (left_operand, right_operand):
    return tree(left_operand) + tree(right_operand)

# fungsi pengurangan
def minus (left_operand, right_operand):
    return tree(left_operand) - tree(right_operand)

# fungsi perkalian
def multi (left_operand, right_operand):
    return tree(left_operand) * tree(right_operand)

# fungsi pembagian
def div (left_operand, right_operand):
    return tree(left_operand) / tree(right_operand)

# Definisikan pohon ekspresi sebagai fungsi
def tree(node):
    if type(node) in (int, float):
        return node
    elif type(node) is tuple and len(node) == 3:
        left_operand, operator, right_operand = node
        if operator == '+':
            return add(left_operand, right_operand)
        elif operator == '-':
            return minus(left_operand, right_operand)
        elif operator == '*':
            return multi(left_operand, right_operand)
        elif operator == '/':
            return div(left_operand, right_operand)
            

# Contoh pohon ekspresi: (2 + 3) * (5 - 1)
expression_tree = ((2, '+', 3), '*', (5, '-', 1))

# Evaluasi pohon ekspresi dengan fungsi pada paradigma fungsional
result = tree(expression_tree)

print("Hasil evaluasi pohon ekspresi:", result)
