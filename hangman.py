#---------IMPORTS-----------------
import random
from tkinter import *
from tkinter import messagebox
import csv
from pygame import mixer

mixer.init()

score = 0
run = True

#----Importing data from external file-----
f_name = "data.csv"
items = list()
with open(f_name, 'r') as csvfile:  # opens, reads and closes csv file
    handle = csv.reader(csvfile)  # csv file handler
    header = next(handle)
    for rows in handle:  # going in each row in that file
        items.append(rows)

no_of_items = len(items)  # Counts the number of items



#Generates a list of index
choices=list(range(no_of_items))
#shuffles the index
random.shuffle(choices)
#Counter to check if all index are complete
index_run=0
# main loop
while run:
    root = Tk()
    root.geometry('905x700+300+100')
    root.title('Hangman')
    root.iconbitmap(r'img/hangman.ico')
    root.config(bg='#E7FFFF')

    # Playing sound
    mixer.music.load("main.mp3")
    mixer.music.set_volume(0.1)
    mixer.music.play()

    run=False  #Destroys the root on clicking the cross
    count = 0
    win_count = 0

    #Checking if all words are complete.
    if index_run==no_of_items:
        run = False
        messagebox.showinfo(title="Completed", message="All complete.\nThank you for playing.")
        root.destroy()
        exit()

    # choosing word
    index = choices.pop()
    index_run+=1
    selected_word = items[index][0]

    # Displaying Hints
    hint = 'Hint: ' + str(items[index][1])
    hint = Label(root, text=hint,bg="#E7FFFF", font=("courier", 15))
    hint.place(x=300, y=375)

    # Display's the name of the game
    title_game = 'HANGMAN'
    title_game_l = Label(root, text=title_game, bg="#E7FFFF" ,font=("courier", 18,'underline bold'))
    title_game_l.place(x=0, y=0)

    # creation of word dashes variables
    x = 250
    for i in range(0, len(selected_word)):
        x += 50
        exec('d{}=Label(root,text="_",bg="#E7FFFF",font=("verdana",30))'.format(i))
        exec('d{}.place(x={},y={})'.format(i, x, 425))

    # letters icon
    al = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z']
    for let in al:
        exec('{}=PhotoImage(file="img/{}.png")'.format(let, let))

    # hangman images
    h123 = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7']
    for hangman in h123:
        exec('{}=PhotoImage(file="img/{}.png")'.format(hangman, hangman))

    # letters placement
    button = [['b1', 'a', 105, 520], ['b2', 'b', 180, 520], ['b3', 'c', 250, 520], ['b4', 'd', 320, 520],
              ['b5', 'e', 390, 520], ['b6', 'f', 460, 520], ['b7', 'g', 525, 520], ['b8', 'h', 600, 520],
              ['b9', 'i', 670, 520], ['b10', 'j', 740, 520], ['b11', 'k', 105, 577], ['b12', 'l', 180, 577],
              ['b13', 'm', 250, 577], ['b14', 'n', 320, 577], ['b15', 'o', 390, 577], ['b16', 'p', 460, 577],
              ['b17', 'q', 525, 577], ['b18', 'r', 600, 577], ['b19', 's', 670, 577], ['b20', 't', 740, 577],
              ['b21', 'u', 250, 635], ['b22', 'v', 320, 635], ['b23', 'w', 390, 635], ['b24', 'x', 460, 635],
              ['b25', 'y', 525, 635], ['b26', 'z', 600, 635]]

    for q1 in button:
        exec(
            '{}=Button(root,bd=0,command=lambda:check("{}","{}"),bg="#E7FFFF",activebackground="gainsboro",font=10,image={})'.format(
                q1[0], q1[1], q1[0], q1[1]))
        exec('{}.place(x={},y={})'.format(q1[0], q1[2], q1[3]))

    # hangman placement
    han = [['c1', 'h1'], ['c2', 'h2'], ['c3', 'h3'], ['c4', 'h4'], ['c5', 'h5'], ['c6', 'h6'], ['c7', 'h7']]
    for p1 in han:
        exec('{}=Label(root,bg="#E7FFFF",image={})'.format(p1[0], p1[1]))

    # placement of first hangman image
    c1.place(x=300, y=40)


    # exit buton
    def close():
        global run
        answer = messagebox.askyesno('ALERT', 'YOU WANT TO EXIT THE GAME?')
        if answer == True:
            run = False
            messagebox.showinfo(title="Thanks", message="Thank you for playing.")
            root.destroy()

    def sound():
        mixer.music.pause()

    def play():
        mixer.music.unpause()



    # Displays the exit button
    e1 = PhotoImage(file='img/exit_1.png')
    ex = Button(root, bd=0, command=close,bg="#E7FFFF" ,activebackground="red", font=10, image=e1)
    ex.place(x=760, y=0)

    #The mute button
    mute = PhotoImage(file='img/mute.png')
    mute_b = Button(root, bd=0, command=sound, bg="#E7FFFF", activebackground="light gray", font=5, image=mute)
    mute_b.place(x=830, y=135)

    #The play button
    unpause = PhotoImage(file='img/play.png')
    unpause_p = Button(root, bd=0, command=play, bg="#E7FFFF", activebackground="light gray", font=10,
                       image=unpause)
    unpause_p.place(x=830, y=200)

    # Displays the score
    s2 = 'SCORE:' + str(score)
    s1 = Label(root, text=s2, bg="#E7FFFF", font=("ms serif", 18))
    s1.place(x=0, y=70)




    # button press check function
    def check(letter, button):
        global count, win_count, run, score
        exec('{}.destroy()'.format(button))
        if letter in selected_word:
            for i in range(0, len(selected_word)):
                if selected_word[i] == letter:
                    win_count += 1
                    exec('d{}.config(text="{}")'.format(i, letter.upper()))
            if win_count == len(selected_word):
                score += 1
                answer = messagebox.askyesno('Winner', 'YOU WON!\nWANT TO PLAY AGAIN?')
                if answer == True:
                    run = True
                    root.destroy()

                else:
                    run = False
                    messagebox.showinfo(title="Thanks", message="Thank you for playing.")
                    root.destroy()
        else:
            count += 1
            exec('c{}.destroy()'.format(count))
            exec('c{}.place(x={},y={})'.format(count + 1, 300, 40))
            if count == 6:
                answer = messagebox.askretrycancel('GAME OVER', 'YOU LOST!\nWANT TO PLAY AGAIN?')
                if answer == True:
                    run =True
                    score = 0
                    root.destroy()
                else:
                    run = False
                    messagebox.showinfo(title="Thanks", message="Thank you for playing.")
                    root.destroy()




    root.mainloop()
