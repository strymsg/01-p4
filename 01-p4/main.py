# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

currentNote = 0
notesAvailable = ('G','F','E','D','C','B','A','g','f','e','d','c','b','a')
notesWithLine=['F','D','B','g','e','a']

def get_notes(input):
    nNotes = input.strip().splitlines()[0]
    notesLine = input.strip().splitlines()[1]
    if int(nNotes) != len(notesLine.split()):
        print(nNotes, len(notesLine.split()))
        raise Exception('Incorrect number of notes and lines')
    notes = notesLine.split()
    return nNotes, notes

def get_letter(note):
    return note[0]

def get_repetition(note):
    try:
        return int(note[1])
    except:
        return 1

def prepare_notes(notes):
    dictNotes = {'G':'','F':'','E':'','D':'','C':'','B':'','A':'','g':'','f':'',
                     'e':'','d':'','c':'','b':'','a':''}
    for note in notes:
        letter = get_letter(note)
        repetition = get_repetition(note)
        for key in dictNotes.keys():
            spacer = ' '
            if key in notesWithLine:
                spacer = '-'
            toDraw = spacer*repetition
            if key == letter:
                toDraw = '*'*repetition
            dictNotes[key] = dictNotes[key] + toDraw + spacer
    return dictNotes

def draw_screen(notes):
    dictnotes = prepare_notes(notes[1])
    #print('>>>ddd', dictnotes)
    firstColumn = True
    for letter in notesAvailable:
        if firstColumn:
            print(letter+': ', end='')
        print(dictnotes[letter])

if __name__ == '__main__':
    inp = '''27
C C D E C E D2 C C D E C2 B2 C C D E F E D C B g A B C2 C2'''
    print(inp)
    draw_screen(get_notes(inp))
    print('#########################################')
    print('Enter the number of notes:')
    numberofnotes = input()
    print('Enter the notes')
    notes = input()
    draw_screen(get_notes(numberofnotes+'\n'+notes))