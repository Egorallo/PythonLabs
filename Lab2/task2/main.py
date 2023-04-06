import sys

sys.path.append("..")

from package.terminal import Terminal


def main():
    terminal = Terminal()
    terminal.start_terminal()


if __name__ == '__main__':
    main()
