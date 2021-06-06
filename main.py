import random
import string
letters=string.ascii_lowercase
n=("".join(random.choice(letters) for q in range(8)))
k=["_"]*len(n)
j=0
g=len(n)
def hangman(n,j,g,k):
    for i in range(len(n)):
        m = input("Guess a word ")
        if m in n:
            j = j + 1
            g -= 1
            p = n.index(m)
            k[p] = n[p]
            print(k)
            if j == 1:
                print("0")
            elif j == 2:
                print("    /")
                print("  0  ")
            elif j == 3:
                print(" \ / ")
                print("  0  ")
            elif j == 4:
                print(" \ /")
                print("  0 ")
                print("  | ")
            elif j == 5:
                print(" \ / ")
                print("  0  ")
                print("  |  ")
                print(" /   ")
            elif j == 6:
                print(" \ / ")
                print("  0  ")
                print("  |  ")
                print(" / \ ")
            elif j == 7:
                print(" \ / |")
                print("  0  ")
                print("  |  ")
                print(" / \ ")
            elif j == 8:
                print(" \ /_|")
                print("  0  ")
                print("  |  ")
                print(" / \ ")

            print("you have {0} turns".format(g))
        else:
            g -= 1
            print("Wrong Word")
            print(("you have {0} turns".format(g)))

    if j == len(n):
        print("You killed a kind man")
    else:
        print("You saved the kind man")
hangman(n,j,g,k)