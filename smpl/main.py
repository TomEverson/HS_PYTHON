import sys
from smpl import SmplInterpreter


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <file.smpl>")
        return

    file_path = sys.argv[1]
    interpreter = SmplInterpreter()
    interpreter.run_file(file_path)


if __name__ == "__main__":
    main()
