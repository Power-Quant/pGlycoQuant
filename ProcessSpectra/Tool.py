import os

def toolCountCharInString(inputStr, inputChar):

    result = 0

    for c in inputStr:
        if c == inputChar:
            result = result + 1

    return result

def op_INIT_CFILE_MS2(inputMS2):

    inputMS2.VALUE_MAX_SCAN = 2000000
    inputMS2.INDEX_SCAN = []
    inputMS2.INDEX_RT = []

    inputMS2.LIST_RET_TIME = [inputMS2.VALUE_ILLEGAL] * inputMS2.VALUE_MAX_SCAN
    inputMS2.LIST_ION_INJECTION_TIME = [inputMS2.VALUE_ILLEGAL] * inputMS2.VALUE_MAX_SCAN
    inputMS2.LIST_ACTIVATION_CENTER = [inputMS2.VALUE_ILLEGAL] * inputMS2.VALUE_MAX_SCAN
    inputMS2.LIST_PRECURSOR_SCAN = [inputMS2.VALUE_ILLEGAL] * inputMS2.VALUE_MAX_SCAN

    inputMS2.MATRIX_PEAK_MOZ = [[]*1] * inputMS2.VALUE_MAX_SCAN # 每一行是个list
    inputMS2.MATRIX_PEAK_INT = [[]*1] * inputMS2.VALUE_MAX_SCAN
    inputMS2.MATRIX_CHARGE = [[]*1] * inputMS2.VALUE_MAX_SCAN
    inputMS2.MATRIX_MZ = [[]*1] * inputMS2.VALUE_MAX_SCAN

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

def op_FILL_LIST_PATH_MS(inputPath, inputList, inputExt):

    separator = '|'
    listStrPath = []

    if len(inputPath) < 1:
        print("MSOperator.py, op_FILL_LIST_PATH_MS, MK_1: Path for MS is empty!")

    if inputPath[-1] == separator:
        pass
    else:
        inputPath = inputPath + separator

    nFile = toolCountCharInString(inputPath, separator)

    for i in range(nFile):
        listStrPath.append(toolGetWord(inputPath, i, separator))

    for strPath in listStrPath:

        if os.path.isdir(strPath):

            for maindir, subdir, file_name_list in os.walk(strPath):

                for filename in file_name_list:

                    tmpPath = os.path.join(maindir, filename)

                    ext = os.path.splitext(tmpPath)[1]

                    if ext in inputExt:
                        inputList.append(tmpPath)

        elif os.path.isfile(strPath):

            inputList.append(strPath)

        else:

            print("MSOperator.py, op_FILL_LIST_PATH_MS, MK_2: Path for MS is illegal!")