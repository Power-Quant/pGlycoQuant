import os
from Tool import *
from Function import *

class ProcessSpectra:

    def __init__(self):

        self.CFG_TYPE_MS2 = {'MS2': 0, 'RAW': 1}
        self.CFG_TYPE_QUANT = {'ReportIon': 0, 'DDA LabelFree': 1, 'DDA Labeling': 2, 'Train': 3, 'LabelA1Ion': 4}
        self.LIST_PATH_MS2 = []

    def process(self, TYPE_QUANT, TYPE_MS2, PATH_MS2):

        if TYPE_MS2 == self.CFG_TYPE_MS2['MS2']:

            op_FILL_LIST_PATH_MS(PATH_MS2, self.LIST_PATH_MS2, [".ms2", ".MS2"])

        elif TYPE_MS2 == self.CFG_TYPE_MS2['RAW']:

            LIST_PATH_RAW = []
            op_FILL_LIST_PATH_MS(PATH_MS2, LIST_PATH_RAW, [".raw"])
            functionRaw2MS = CRaw2MS()
            functionRaw2MS.FunctionRaw2MS(LIST_PATH_RAW)
            self.LIST_PATH_MS2 = [i_raw.replace('.raw', '.ms2') for i_raw in LIST_PATH_RAW]

        if TYPE_QUANT == self.CFG_TYPE_QUANT['ReportIon']:

            for path in self.LIST_PATH_MS2:

                functionMS2 = CFuntionParseMS2ForReportIon()
                functionMS2.ms2TOpkl(path)

        elif TYPE_QUANT == self.CFG_TYPE_QUANT['LabelA1Ion']:

            for path in self.LIST_PATH_MS2:

                functionMS2 = CFunctionParseMS2ForLabelA1Ion()
                functionMS2.ms2Topkl(path)


if __name__ == "__main__":
    TYPE_QUANT = 1
    A4_TYPE_MS2 = 1
    PATH_MS2 = "...sample1_A.raw"
    process = ProcessSpectra()
    process.process(TYPE_QUANT, A4_TYPE_MS2, PATH_MS2)