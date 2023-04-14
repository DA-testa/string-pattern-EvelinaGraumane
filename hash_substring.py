# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    lietotaja_ievade = input()
    burts = ""
    teksts = ""
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 

    if "F" in lietotaja_ievade:
        file = open("./tests/06", "r")
        lietotaja_ievade = file.read()
        lietotaja_ievade = lietotaja_ievade.split("\n")
        burts = lietotaja_ievade[0]
        teksts = lietotaja_ievade[1]

    elif "I" in lietotaja_ievade:
        burts = input()
        teksts = input()

    # return both lines in one return

    burts = burts.strip()
    teksts = teksts.strip()
    return (burts, teksts)

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(burts, teksts):
    # this function should find the occurances using Rabin Karp alghoritm 
    skaits = []

    for i in range(len(teksts)):
        if teksts[i] == burts[0] and len(burts) + i <= len(teksts):
            t = True
            for j in range(len(burts)):
                if teksts[i+j] != burts[j]:
                    t = False
            if t:
                skaits.append(i)
    # and return an iterable variable
    return skaits


# this part launches the functions
if __name__ == '__main__':
    burts, teksts = read_input()
    gadijums = get_occurrences(burts, teksts)
    print_occurrences(gadijums)

