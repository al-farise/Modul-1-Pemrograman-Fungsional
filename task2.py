random_list = [105, 3.1, "Hello", 737, "Python", 2.7, "World", 412, 5.5, "AI"]

def float_data(random_data):
    data = [item for item in random_data if type(item) is float]
    return tuple(data)

def string_data(random_data):
    return [item for item in random_data if type(item) is str]

def integer_data(random_data):
    data = {
        'ratusan': [],
        'puluhan': [],
        'satuan': []
    }

    for item in random_data:
            if type(item) is int:
                data["ratusan"].append(int(item / 100))
                data["puluhan"].append(int((item % 100) / 10))
                data["satuan"].append(int(((item % 100) % 10) / 1))
                
    return data

print(f'Float data: {float_data(random_list)}')
print(f'String data: {string_data(random_list)}')
print(f'Integer data: {integer_data(random_list)}')
