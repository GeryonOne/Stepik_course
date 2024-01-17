def main():
    generated_files_dict = generate_files_dict()
    operation_requests(generated_files_dict)


def generate_files_dict():
    files_operations_dict = {key: value.split() for key, value in
                             (input().split(maxsplit=1) for _ in range(int(input())))}
    return files_operations_dict


def operation_requests(local_files_dict):
    operation_commands = {'write': 'W', 'read': 'R', 'execute': 'X'}
    for operation in range(int(input())):
        current_operation = input().split()
        value, key = current_operation[0], current_operation[1]
        if operation_commands[value] in local_files_dict[key]:
            print('OK')
        else:
            print('Access denied')


main()

