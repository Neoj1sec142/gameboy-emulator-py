SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
MAX_KEY_SIZE = len(SYMBOLS)

def get_mode():
    while True:
        print('Do you wish to encrypt or decrypt or brute-force a message?')
        mode = input().lower()
        if mode in ['encrypt', 'e', 'decrypt', 'd', 'brute', 'b']:
            return mode
        else:
            print('Enter either "encrypt" / "e" or "decrypt" / "d" or "brute" / "b"')
            
def get_message():
    print('Enter your message: ')
    return input()

def get_key():
    key = 0
    while True:
        print(f'Enter the key number (1 - {MAX_KEY_SIZE})')
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key
        
def get_translated_msg(mode, msg, key):
    if mode[0] == 'd':
        key = -key
    trans = ''
    for symbol in msg:
        sym_index = SYMBOLS.find(symbol)
        if sym_index == -1:
            trans += symbol
        else:
            sym_index += key
            if sym_index >= len(SYMBOLS):
                sym_index -= len(SYMBOLS)
            elif sym_index < 0:
                sym_index += len(SYMBOLS)
            trans += SYMBOLS[sym_index]
    return trans

def main():
    mode = get_mode()
    msg = get_message()
    if mode[0] != 'b':
        key = get_key()
    print('Your translated text is: ')
    if mode[0] != 'b':
        print(get_translated_msg(mode, msg, key))
    else:
        for key in range(1, MAX_KEY_SIZE + 1):
            print(key, get_translated_msg('decrypt', msg, key))
            
if __name__ == '__main__':
    main()