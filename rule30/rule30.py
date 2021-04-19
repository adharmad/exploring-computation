# Rule30
# https://en.wikipedia.org/wiki/Rule_30

ITERATIONS = 100
RULE_30 = {
    '000': '0',    
    '001': '1',    
    '010': '1',    
    '011': '1',    
    '100': '1',    
    '101': '0',    
    '110': '0',    
    '111': '0',    
}

def applyRule30(row):
    global RULE_30

    newrow = row[0]
    for i in range(1, len(row)-1):
        newrow += RULE_30[row[i-1:i+2]]
    
    newrow += row[len(row)-1]
    return newrow

def main():
    i = 0
    row = '00000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000'
    global ITERATIONS

    while i < ITERATIONS:
        print(row)
        row = applyRule30(row)
        i += 1

if __name__ == '__main__':
    main()
