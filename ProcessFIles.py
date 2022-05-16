


class ProcessFile:

    def __init__(self):
        self.INI_PATH_ELEMENT = ""
        self.INI_PATH_AA = ""
        self.INI_PATH_MOD = ""
        self.INI_PATH_GLYCO = ""
        self.INI_PATH_LINKER = ""

    def toolGetWord1(inputString, d1, d2):
        start = 0
        end = len(inputString)
        for i in range(len(inputString)):
            if inputString[i] == d1:
                start = i + 1
            if inputString[i] == d2:
                end = i
        return inputString[start:end]

    def toolGetWord(inputString, index, d):
        if inputString[0] != d:
            inputString = d + inputString
        if inputString[-1] != d:
            inputString = inputString + d
        p_d = []
        i = 0
        for c in inputString:
            if c == d:
                p_d.append(i)
            i = i + 1
        result = inputString[p_d[index] + 1:p_d[index + 1]]
        return result

    def toolStr2List(inputStr, inputSeparator):
        outputList = []
        word = ''
        if inputStr[-1] != inputSeparator:
            inputStr = inputStr + inputSeparator
        for c in inputStr:
            if c == inputSeparator:
                number = float(word)
                outputList.append(number)
                word = ''
            else:
                word = word + c
        return outputList

    def toolCountCharInString(inputStr, inputChar):
        result = 0
        for c in inputStr:
            if c == inputChar:
                result = result + 1
        return result

    def process(self):
        self.__captainFile2Element(self.INI_PATH_ELEMENT)
        self.__captainFile2AA(self.INI_PATH_AA)
        self.__captainFile2Mod(self.INI_PATH_MOD)
        self.__captainFile2Gly(self.INI_PATH_GLYCO)
        self.__captainFile2Link(self.INI_PATH_LINKER)

    def ini2file(self):

        self.__captainElement2File(self.myCFG.I0_INI_PATH_ELEMENT)

    def __captainFile2Link(self, path):

        isFirstLine = True

        with open(path, 'r', encoding='utf8') as f:

            for line in f.readlines():

                if len(line) > 1:

                    if line[-1] == '\n':

                        line = line[0:-1]  # 把最后一个\n干掉

                    if line.startswith("name"):

                        str_name = self.toolGetWord1(line, '=', ' ')
                        isFirstLine = False

                    else:

                        if isFirstLine:
                            pass
                        else:
                            str_comp = self.toolGetWord(line, 7, ' ')
                            self.myINI.DICT4_LINKER_COM[str_name] = str_comp

    def __captainFile2Gly(self, path):

        with open(path, 'r', encoding='utf8') as f:

            for line in f.readlines():

                if len(line) > 1:

                    if line[-1] == '\n':

                        line = line[0:-1]  # 把最后一个\n干掉

                    if line.startswith("G"):

                        str_name = self.toolGetWord1(line, 1, ' ')
                        str_comp = self.toolGetWord1(line, 4, ' ')

                        self.myINI.DICT3_GLYCO_COM[str_name] = str_comp

    def __captainFile2Mod(self, path):

        with open(path, 'r', encoding='utf8') as f:
            for line in f.readlines():

                if len(line) > 1:

                    if line[-1] == '\n':

                        line = line[0:-1]  # 把最后一个\n干掉

                    if line.startswith("@"):
                        continue

                    if line.startswith("name"):

                        str_name = self.toolGetWord1(line, '=', ' ')

                    else:

                        nBlank = self.toolCountCharInString(line, ' ')

                        if nBlank > 5:

                            str_comp = self.toolGetWord(line, 7, ' ')

                        else:

                            str_comp = self.toolGetWord(line, 5, ' ')

                        self.myINI.DICT2_MOD_COM[str_name] = str_comp

    def __captainElement2File(self, path):

        pass

    def __captainFile2AA(self, path):

        with open(path, 'r', encoding='utf8') as f:

            for line in f.readlines():

                if len(line) > 1:

                    str_name = self.toolGetWord(line, 0, '|')
                    str_comp = self.toolGetWord(line, 1, '|')

                    self.myINI.DICT1_AA_COM[str_name] = str_comp

    def __captainFile2Element(self, path):

        with open(path, 'r', encoding='utf8') as f:

            for line in f.readlines():

                if len(line) > 1:

                    str_name = self.toolGetWord(line, 0, '|')
                    str_mass = self.toolGetWord(line, 1, '|')
                    str_abdc = self.toolGetWord(line, 2, '|')

                    list_mass = self.toolStr2List(str_mass, ',')
                    list_abdc = self.toolStr2List(str_abdc, ',')

                    self.myINI.DICT0_ELEMENT_MASS[str_name] = list_mass
                    self.myINI.DICT0_ELEMENT_ABDC[str_name] = list_abdc

if __name__ == "__main__":
	process = ProcessFile()
	process.process()