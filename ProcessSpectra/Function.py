import os
import pickle
from Tool import *


class CRaw2MS:

    def FunctionRaw2MS(self, inputListPathRaw):

        exe_MSFileReader = 'MSExport.exe'
        cfg_MSFileReader = 'MSExport.cfg'
        path_raw = '|'.join(inputListPathRaw)

        with open(cfg_MSFileReader, 'w') as f:

            f.write("[Data]\n")
            f.write("PATH_RAW=" + path_raw + '\n')

        cmd = exe_MSFileReader + ' {:s}'.format(cfg_MSFileReader)

        try:
            os.system(cmd)
        except:
            print('MSExport.exe run wrong!')

class CFileMS2:

	INDEX_SCAN = []
	INDEX_RT = []

	LIST_RET_TIME = []
	LIST_ION_INJECTION_TIME = []
	LIST_ACTIVATION_CENTER = []
	LIST_PRECURSOR_SCAN = []

	MATRIX_PEAK_MOZ = []
	MATRIX_PEAK_INT = []
	MATRIX_CHARGE = []
	MATRIX_MZ = []

class CFuntionParseMS2ForReportIon:

    def __init__(self):

        pass

    def loadPKL(self, pathPKL):

        dataMS2 = CFileMS2()
        pklFile = open(pathPKL, 'rb')
        dataMS2 = pickle.load(pklFile)
        pklFile.close()
        return dataMS2

    def ms2TOpkl(self, pathMS2):

        # check
        path_pkl = pathMS2 + ".pkl"
        if os.access(path_pkl, os.F_OK):
            pass
        else:

            # init
            dataMS2 = CFileMS2()
            op_INIT_CFILE_MS2(dataMS2)

            # open
            with open(pathMS2, 'r', encoding='utf8') as f:

                i_MS2 = -1

                for line in f.readlines():

                    len_line = len(line)
                    if len_line > 1:

                        if line.startswith("S	"):
                            i_MS2 = i_MS2 + 1
                            tmpScan = int(toolGetWord(line, 1, '	'))
                            dataMS2.INDEX_SCAN.append(tmpScan)
                            dataMS2.MATRIX_PEAK_MOZ[tmpScan] = []
                            dataMS2.MATRIX_PEAK_INT[tmpScan] = []

                        elif line.startswith("H	"):
                            pass
                        elif line.startswith("I	"):
                            if line.startswith("I	IonInjectionTime"):
                                t = toolGetWord(line, 2, '	')
                                dataMS2.LIST_ION_INJECTION_TIME[tmpScan] = float(t)
                            elif line.startswith("I	RetTime	"):
                                t = toolGetWord(line, 2, '	')
                                dataMS2.LIST_RET_TIME[tmpScan] = float(t)
                        elif line.startswith("Z	"):
                            pass
                        else:
                            dataMS2.MATRIX_PEAK_MOZ[tmpScan].append(float(toolGetWord(line, 0, ' ')))
                            dataMS2.MATRIX_PEAK_INT[tmpScan].append(float(toolGetWord(line, 1, ' ')))

            # write pkl
            fid_pkl = open(path_pkl, 'wb')
            pickle.dump(dataMS2, fid_pkl)
            fid_pkl.close()

class CFunctionParseMS2ForLabelA1Ion:

    def __init__(self):

        pass

    def loadPKL(self, pathPKL):

        dataMS2 = CFileMS2()
        pklFile = open(pathPKL, 'rb')
        dataMS2 = pickle.load(pklFile)
        pklFile.close()
        return dataMS2

    def ms2Topkl(self, pathMS2):

        path_pkl = pathMS2 + ".pkl"
        if os.access(path_pkl, os.F_OK):
            pass
        else:

            # init
            dataMS2 = CFileMS2()
            op_INIT_CFILE_MS2(dataMS2)

            # open
            with open(pathMS2, 'r', encoding='utf8') as f:

                i_MS2 = -1

                for line in f.readlines():

                    len_line = len(line)
                    if len_line > 1:

                        if line.startswith("S	"):
                            i_MS2 = i_MS2 + 1
                            tmpScan = int(toolGetWord(line, 1, '	'))
                            dataMS2.INDEX_SCAN.append(tmpScan)
                            dataMS2.MATRIX_PEAK_MOZ[tmpScan] = []
                            dataMS2.MATRIX_PEAK_INT[tmpScan] = []

                        elif line.startswith("H	"):
                            pass
                        elif line.startswith("I	"):
                            if line.startswith("I	IonInjectionTime"):
                                t = line.split('\t')[2]
                                dataMS2.LIST_ION_INJECTION_TIME[tmpScan] = float(t)
                            elif line.startswith("I	RetTime	"):
                                t = line.split('\t')[2]
                                dataMS2.LIST_RET_TIME[tmpScan] = float(t)
                            elif line.startswith('I	ActivationCenter'):
                                t = line.split('\t')[2]
                                dataMS2.LIST_ACTIVATION_CENTER[tmpScan] = float(t)
                            elif line.startswith('I	PrecursorScan'):
                                t = line.split('\t')[2]
                                dataMS2.LIST_PRECURSOR_SCAN[tmpScan] = float(t)
                        elif line.startswith("Z	"):
                            pass
                        else:
                            dataMS2.MATRIX_PEAK_MOZ[tmpScan].append(float(toolGetWord(line, 0, ' ')))
                            dataMS2.MATRIX_PEAK_INT[tmpScan].append(float(toolGetWord(line, 1, ' ')))

            fid_pkl = open(path_pkl, 'wb')
            pickle.dump(dataMS2, fid_pkl)
            fid_pkl.close()