import getpass # Utilizado na função 'getpass_with_mask(prompt)'
import sys # Utilizado na função 'getpass_with_mask(prompt)'

def getpass_with_mask(prompt):
    # Exibe " * " quando o usuário digita sua senha
    password = ""
    print(prompt, end='', flush=True)
    while True:
        char = None
        if sys.platform == 'win32':
            import msvcrt
            char = msvcrt.getwch()
        else:
            import termios
            import tty
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(fd)
                char = sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        if char == '\r' or char == '\n':
            print('')
            break
        elif char == '\b' or ord(char) == 127:  # Handle backspace
            if password:
                password = password[:-1]
                print('\b \b', end='', flush=True)
        else:
            password += char
            print('*', end='', flush=True)
    return password