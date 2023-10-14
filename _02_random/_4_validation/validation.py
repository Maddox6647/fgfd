import random
from tkinter import messagebox, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
for i in range(10):
    random_number = random.randint(1, 10)

    if random_number == 1:
        messagebox.showinfo(title='shrek', message='u r awesome')
        print(random_number)
    elif random_number == 2:
        messagebox.showinfo(title='shrek', message='u r good')
        print(random_number)
    elif random_number == 3:
        messagebox.showinfo(title='shrek', message='u r bad')
        print(random_number)
    elif random_number == 4:
        messagebox.showinfo(title='shrek', message='u r dumb')
        print(random_number)
    elif random_number == 5:
        messagebox.showinfo(title='shrek', message='u r stupid')
        print(random_number)
    elif random_number == 6:
        messagebox.showinfo(title='shrek', message='u r OK')
        print(random_number)
    elif random_number == 7:
        messagebox.showinfo(title='shrek', message='u r an idiot')
        print(random_number)
    elif random_number == 8:
        messagebox.showinfo(title='shrek', message='u r amazing')
        print(random_number)
    elif random_number == 9:
        messagebox.showinfo(title='shrek', message='u r sus')
        print(random_number)
    elif random_number == 10:
        messagebox.showinfo(title='shrek', message='u r great')
        print(random_number)

    # TODO 1) Use each value of random_number to give the user a random compliment

    # TODO 2) Repeat all the code above 10 times

    # TODO 3) Find someone to test out your program. They will like it :)
