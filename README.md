# Proyecto: Cifrado Vigenère CLI

## Descripción
Este proyecto implementa un programa de línea de comandos (CLI) para realizar cifrado y descifrado de texto utilizando el cifrado Vigenère. El cifrado Vigenère es un método de cifrado por sustitución polialfabética que utiliza una clave para transformar el texto de entrada.

El programa permite:
- Cifrar texto en modo `enc`.
- Descifrar texto en modo `dec`.
- Leer texto desde un archivo o desde la entrada estándar (`stdin`).
- Escribir el resultado en un archivo o en la salida estándar (`stdout`).
- Configurar el alfabeto y el modo de normalización.

## Estructura del Proyecto
- `vigenere_cli.py`: Archivo principal que implementa la interfaz de línea de comandos.
- `vigenere_cypher.py`: Contiene la lógica del cifrado Vigenère.
- `vigenere_cypher_test.py`: Pruebas unitarias para verificar la funcionalidad del cifrado y descifrado.
- `input.txt`: Archivo de ejemplo para pruebas de entrada.
- `output.txt`: Archivo de ejemplo para pruebas de salida.

## Requisitos
- Python 3.6 o superior.

## Instalación
1. Clona este repositorio o descarga los archivos.
2. Asegúrate de tener Python instalado en tu sistema.
3. (Opcional) Crea un entorno virtual para aislar las dependencias:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

## Ejecución
El programa se ejecuta desde la línea de comandos. A continuación, se describen las opciones disponibles:

### Modos
- `--mode enc`: Cifra el texto de entrada.
- `--mode dec`: Descifra el texto de entrada.

### Opciones
- `--key`: Clave para el cifrado o descifrado (obligatoria).
- `--in`: Archivo de entrada (opcional, por defecto `stdin`).
- `--out`: Archivo de salida (opcional, por defecto `stdout`).
- `--normalize`: Modo de normalización (`strict` o `lax`, por defecto `strict`).
- `--alpha`: Alfabeto a utilizar (por defecto `A-Z`).

### Ejemplos de Uso
#### Cifrar texto desde un archivo:
```bash
python3 vigenere_cli.py --mode enc --key CLAVE --in input.txt --out output.txt
```

#### Descifrar texto desde la entrada estándar:
```bash
echo "JPLGS" | python3 vigenere_cli.py --mode dec --key CLAVE
```

#### Cifrar texto con normalización laxa:
```bash
python3 vigenere_cli.py --mode enc --key CLAVE --in input.txt --normalize lax
```

#### Usar un alfabeto personalizado:
```bash
python3 vigenere_cli.py --mode enc --key CLAVE --alpha "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
```

## Pruebas
El proyecto incluye pruebas unitarias para verificar la funcionalidad del cifrado y descifrado. Para ejecutar las pruebas:
```bash
python3 -m unittest vigenere_cypher_test.py
```

## Límites Conocidos
1. **Clave vacía o no alfabética**: El programa lanza un error si la clave está vacía o contiene caracteres no alfabéticos.
2. **Texto de entrada no normalizado**: En modo `strict`, solo se procesan caracteres alfabéticos.
3. **Alfabeto personalizado**: Si el alfabeto no incluye todos los caracteres necesarios, el resultado puede ser incorrecto.

## Créditos
- Implementación: Equipo de Ingeniería de Sistemas, 2025-II.
- Inspirado en el cifrado clásico de Vigenère.

## Licencia
Este proyecto es de uso educativo y no tiene licencia específica.