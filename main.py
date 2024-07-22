import argparse
from DuckyConverter import DuckyConverter

def main():
    parser = argparse.ArgumentParser(description='Strings to DuckyScript converter. Makes simpler writing long scripts without thinking about Ducky syntax')
    
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
    parser.add_argument('-i', '--input', type=str, help="define input file")
    parser.add_argument('-o', '--output', type=str, help="define output file")
    parser.add_argument('-d', '--delay', type=int, help="define default delay")
    args = parser.parse_args()

    try:
        print('Prepairing for work...')
        a = DuckyConverter(
            args.input,
            args.delay if args.delay else DuckyConverter.DEFAULT_DELAY,
            args.output if args.output else DuckyConverter.DEFAULT_OUT_NAME
            )
        a.ComposeFile()
        print('Done!')

    except FileNotFoundError:
        print(f"File {args.input} not found")
    except Exception:
        print("Read error")

    

if __name__ == '__main__':
    main()
