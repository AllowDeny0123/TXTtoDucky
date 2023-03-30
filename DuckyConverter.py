from DuckyTemplates import DuckyTemplates

class DuckyConverter:
    
    DEFAULT_DELAY = 100
    DEFAULT_OUT_NAME = "output.txt"

    def __init__(self, filePath, delay=DEFAULT_DELAY, outputfilemane=DEFAULT_OUT_NAME):
        self._filePath = filePath
        self._delay = delay
        self._outname = outputfilemane

    def StringFromFileGenerator(self):
        '''File reader generator'''
        print("Reading file...")
        for i in open(self._filePath, 'r'):
            yield i

    def ComposeFile(self):
        '''Composing output file from input entry and replacement templates'''
        _strings = []
        for i in self.StringFromFileGenerator():
            j=i.strip()
            if j in DuckyTemplates.TEMPLATES:
                _strings.append(f'{DuckyTemplates.TEMPLATES[j]}\n')
                _strings.append(f'DELAY {str(self._delay)}\n')
            else:
                _strings.append(f'STRINGLN {j}\n')
                _strings.append(f'DELAY {str(self._delay)}\n')
        print('Processing things, please wait...')

        '''Remove last delay'''
        _strings.pop()
        
        with open(self._outname, 'w') as file:
            print('Creating output file...')
            file.writelines(_strings)
            file.close()