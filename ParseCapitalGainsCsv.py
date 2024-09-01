import csv

mutualFundSchemeNameColumn = 3
purchaseDateColumn = 5
sellDateColumn = 10
purchaseCostColumn  = 17
sellCostColumn = 13
unitsColumn = 11

transactionStartRow = 5

def printColumnNames(data: list):
    for index,element in enumerate(data):
        print("%d : %s" % (index, element))
    
def convertCapitalGainStatementToTable(fileName: str) -> list:
    data = []

    with open(fileName, mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
    
    return data
    
def generateDistinctSchemeNames(inputTable: list) -> set:
    schemeNames = set()
    endRow = len(inputTable)
    for i in range(transactionStartRow, endRow):
        schemeNames.add(inputTable[i][mutualFundSchemeNameColumn])
    return schemeNames

def writeSchemesToFile(fileName: str, schemes: set):
    with open(fileName , 'a') as file:
        for scheme in schemes:
            file.write(scheme + '\n')


def parseCapitalGainStatement():
    inputTable = convertCapitalGainStatementToTable('inputs/cgs.csv')
    printColumnNames(inputTable[4])
    schemes = generateDistinctSchemeNames(inputTable)
    writeSchemesToFile('inputs/allschemes.txt', schemes)

parseCapitalGainStatement()
