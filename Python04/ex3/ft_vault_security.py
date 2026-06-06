def secure_archive(name_file: str, action: str = 'r',
                   content: str = '') -> tuple[bool, str]:
    try:
        if action == 'r':
            with open(name_file) as f:
                read_file = f.read()
                return (True, read_file)
        else:
            with open(name_file, 'w') as f:
                f.write(content)
                return (True, 'Content successfully written to file')
    except OSError as e:
        return (False, str(e))


if __name__ == '__main__':
    print('=== Cyber Archive Security ===\n')
    print("Using 'secure_archive' to read from anonexistent file:")
    print(secure_archive('/not/existing/file'))
    print()
    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive('/etc/master.passwd'))
    print()
    print("Using 'secure_archive' to read from a regular file:")
    print(secure_archive('ancient_fragment.txt'))
    print()
    print("Using 'secure_archive' to write previous content to a new file:")
    temp2 = secure_archive('new_file', 'w', 'Bonjour ca va?')
    print(temp2)
