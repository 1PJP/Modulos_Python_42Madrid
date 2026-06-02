import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f'Usage {sys.argv[0]} <file>')
    else:
        print('=== Cyber Archives Recovery & Preservation ===')
        print(f"Accessing file '{sys.argv[1]}'")
        try:
            txt_op = open(sys.argv[1])
            print('---\n')
            txt_rd = txt_op.read()
            print(f'{txt_rd}\n')
            print('---')
            txt_op.close()
            print(f"File '{sys.argv[1]}' closed.\n")
            lines = txt_rd.split('\n')
            add = [line + '#' for line in lines]
            reverse = '\n'.join(add)
            print('Tranform data:')
            print('---\n')
            print(f'{reverse}\n')
            print('---')
            sys.stdout.write('Enter new file name (or empty):')
            sys.stdout.flush()
            new_name = sys.stdin.readline().strip()
            if new_name == '':
                print('Not saving data')
            else:
                try:
                    print(f"Saving data to '{new_name}'")
                    name_file = open(new_name, 'w')
                    name_file.write(reverse)
                    name_file.close()
                    print(f"Data saved in file '{new_name}'.")
                except OSError as e:
                    sys.stderr.write(f"[STDERR] Error opening file"
                                     f" '{new_name}': {e}\n")
                    sys.stderr.flush()
                    print('Data not saved.')
        except OSError as e:
            sys.stderr.write(f"[STDERR] Error opening file"
                             f" '{sys.argv[1]}': {e}\n")
