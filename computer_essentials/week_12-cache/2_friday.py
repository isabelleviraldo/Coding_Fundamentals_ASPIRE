
#2 wide
EYE_OPTIONS = [
    "/\\",    # triangle eye
    "()",     # round eye
    "[]",     # square eye
    "--"      # closed eye
]

#7 wide
MOUTH_OPTIONS = [
    "\\_____/", #happy
    "V^V^V^V",  #scary
    "-------",  #flat
    "v\\___/v"  #fangs
]

def pick_eye():
    print("Choose eye shape: ")
    print("1) triangle")
    print("2) circle")
    print("3) square")
    print("4) closed")
    
    eye_choice = int(input("> "))
    return eye_choice - 1

def pick_mouth():
    print("Choose mouth shape: ")
    print("1) happy")
    print("2) scary")
    print("3) flat")
    print("4) fangs")
    
    mouth_choice = int(input("> "))
    return mouth_choice - 1

def pick_leaf():
    print("Do you want a leaf on top? (y/n)")
    choice = input("> ")
    if choice == "y":
        return True
    else:
        return False

def print_pumpkin(eye, mouth, leaf):
    print("Here's your Jack-o-Lantern!")
    #total width 19
    
    #leaf and stem part
    if leaf:
        print("        ~^~        ")
    else:
        print("                   ")
    print("         #         ")
    
    #top of the head
    print("     .-''''''-.     ")
    print("   .'          '.   ")
    print("  /              \\  ")
    

    # eyes line
    print(f" |   {EYE_OPTIONS[eye]}     {EYE_OPTIONS[eye]}    | ")

    # middle line
    print(" |                | ")

    # mouth line
    print(f" |    {MOUTH_OPTIONS[mouth]}     | ")
    
    # bottom of the pumpkin
    print("  \\              /  ")
    print("   '.          .'   ")
    print("     '-.____.-'     ")
    
    print("Happy Halloween!!!")

def main():
    print("---Jack-o-Lantern Generator---")
    print("What should we carve our pumpkin to look like?")

    eye   = pick_eye()
    mouth = pick_mouth()
    leaf  = pick_leaf()

    print_pumpkin(eye, mouth, leaf)

    again = input("Make another? (y/n): ")
    if again == "y":
        print()
        main()

if __name__ == "__main__":
    main()
    print("Have a spooky halloween! bye!")
