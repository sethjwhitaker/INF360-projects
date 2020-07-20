# INF360 - Programming in Python
# Seth Whitaker
# Assignment 3
# Print Table Function
# 06/20/2020


tableData = [ # example given in the text
    ['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose'],
]

def printTable(table):
    # find longest nested list length and longest string lengths
    longestLen = 0
    stringLens = []
    for i in range(0,len(table)): # i is row
        # find longest string length
        longestStringLen = 0
        for j in range(0, len(table[i])): # j is column
            if len(table[i][j]) > longestStringLen:
                longestStringLen = len(table[i][j])
        stringLens.append(longestStringLen) # Add to list

        # check if longest list length
        if len(table[i]) > longestLen:
            longestLen = len(table[i])

    # output table
    for i in range(0,longestLen): # i is column
        for j in range(0, len(table)): # j is row
            if i < len(table[j]): # if current element exists
                #     |        add extra whitespace          |  concatenate table element
                print(" " * (stringLens[j] - len(table[j][i])) + table[j][i], end = ' ')
            else:
                print(" " * stringLens[j], end = ' ') # otherwise insert blank space
        print("")
# end def printTable 



printTable(tableData)

