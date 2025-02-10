import os

def main():
    cur_path = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(cur_path, 'gotexas'), 'w') as file:
        file.write(f"""
        #!/bin/bash

        python3 {cur_path}/go_texas.py "$@"
        """)



if __name__ == '__main__':
    main()