import sys
from smpl import SmplProcessor


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <file.smpl>")
        return

    file_path = sys.argv[1]
    compiler = SmplProcessor(mode="Compiler")

    compiler.run_file(file_path)


if __name__ == "__main__":
    main()
