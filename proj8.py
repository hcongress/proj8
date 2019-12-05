import argparse

#Hunter Congress
#hcongress/proj8

#python: 3.6.8
def simulate(PDA,w):
    currentState = PDA[3]
    stack = ['e']

    while stack:
        symbol = stack[0]
        if currentState not in PDA[0] or symbol not in PDA[1]:
            return 'symbol or state not found'
        else:
            for nextState in PDA[2]:
                print(nextState[0] + '--' + nextState[1] +'++' + currentState + '--' + symbol)
                if nextState[0] == currentState and nextState[1] == symbol:
                    print('in')
                    if nextState[3] != 'e':
                        print('pushed: '+ nextState[3])
                        stack.append(nextState[2])
                    if nextState[2] != 'e':
                        print('poped: '+ stack.pop())
                    currentState = nextState[4]
                    break
                    
    if currentState in PDA[4]:
        return 'ACCEPT'
    else:
        return 'REJECT'



ap = argparse.ArgumentParser()

ap.add_argument(
    'file',
    type=str,
    help='Please specify the file'
)

args = ap.parse_args()

with open(args.file) as fp:
    line=fp.readline()
    line = line.strip('\n')
    states = line.split(",")
    
    line = fp.readline()
    line = line.strip('\n')
    symbols = line.split(',')

    line=fp.readline()
    line = line.strip('\n')
    l = line.split(",")
    transitions = []
    for state in l:
        transitions.append(state.split('-'))


    
    line=fp.readline()
    startState = line.strip('\n')

    line= fp.readline()
    line.strip('\n')
    acceptState = line.split(',')

    PDA = [states,symbols,transitions,startState,acceptState]


while(True):
    w= input("Enter string: ")
    results = simulate(PDA,w)
    print(results)


