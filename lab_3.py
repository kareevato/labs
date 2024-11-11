def remove_spaces(input_str):
    result = ""
    
    for char in input_str:
        if char != " ":
            result += char
    
    return result

user_input = input("Введіть рядок: ")
result = remove_spaces(user_input)
print("Рядок без пробілів:", result) 