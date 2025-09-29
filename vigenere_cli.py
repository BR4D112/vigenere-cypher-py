import argparse
import sys
from vigenere_cypher import vigenere_cipher

class VigenereCLI:
    def run(self):
        parser = argparse.ArgumentParser(description='Cifrado Vigenère, para encriptar y desencriptar texto.')
        parser.add_argument('--mode', choices=['enc', 'dec'], required=True, help='Mode: enc para encriptar, dec para desencriptar')
        parser.add_argument('--key', required=True, help='Llave para el cifrado Vigenère')
        parser.add_argument('--in', dest='input_file', type=argparse.FileType('r'), default=sys.stdin, help='Archivo input (default: stdin)')
        parser.add_argument('--out', dest='output_file', type=argparse.FileType('w'), default=sys.stdout, help='Archivo output(default: stdout)')
        parser.add_argument('--normalize', choices=['strict', 'lax'], default='strict', help='Modo de normalización, sí estricta con los caracteres o laxa(default: strict)')
        parser.add_argument('--alpha', default='ABCDEFGHIJKLMNOPQRSTUVWXYZ', help='El alfabeto que se quiere usar (default: A-Z)')

        args = parser.parse_args()

        input_text = args.input_file.read()

        if args.normalize == 'strict':
            input_text = ''.join(filter(str.isalpha, input_text))

        mode = 'encrypt' if args.mode == 'enc' else 'decrypt'

        try:
            result = vigenere_cipher(input_text, args.key, mode, args.alpha)
            args.output_file.write(result)
            args.output_file.write('\n')
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)

if __name__ == '__main__':
    import time
    start_time = time.time()
    cli = VigenereCLI()
    cli.run()
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Script executed in: {execution_time:.3f} seconds")
