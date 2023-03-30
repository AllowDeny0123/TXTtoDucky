import sys
from DuckyConverter import DuckyConverter

def main():
    if len(sys.argv) > 2:
        print('Prepairing for work...')
        a = DuckyConverter(
            sys.argv[1],
            int(sys.argv[2]) if len(sys.argv) >= 3 else DuckyConverter.DEFAULTDELAY,
            sys.argv[3] if len(sys.argv) >=4 else DuckyConverter.DEFAULT_OUT_NAME
            )
        a.ComposeFile()
        print('Done!')
if __name__ == "__main__":
    main()