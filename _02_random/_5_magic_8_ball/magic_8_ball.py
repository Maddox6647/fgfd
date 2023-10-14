import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # TODO Get the user to enter a question for the 8 ball to answer
    simpledialog.askstring(title='djhsdagjdfsgkfgfhsdghfkagkhfasghsdfk', prompt='PLS ask the magic 8 ball a question about yourself')
    # Make a variable and initialize it to a random number between 0 and 3
    bobby1545 = random.randint(0, 3)
    # If the random number is 0
    if bobby1545 == 0:
        messagebox.showinfo(title='Magic 8 Ball', message='YES!!!')

        # tell the user "Yes"

    # If the random number is 1
    elif bobby1545 == 1:
        messagebox.showinfo(title='Magic 8 Ball', promt='NO')
        # tell the user "No"

    # If the random number is 2
    elif bobby1545 == 2:
        messagebox.showinfo(title='Magic 8 Ball', message='Maybe you should ask Google?')
        # tell the user "Maybe you should ask Google?"

    # If the random number is 3
    elif bobby1545 == 3:
        messagebox.showinfo(title='Magic 8 Ball', message='I DON"T KNOW!!! ASK SOME OTHER BOZO!!!')
        # write your own answer
