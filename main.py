import functions

try:
    fim = False
    while not fim:
        functions.menu()
        res = int(input(": "))
        while res>3 or res<0:
            print("Entry does not match an option. Try again")
            res = int(input(": "))

        if res == 1:
            functions.title("PERIODIC TABLE")
            i = int(input("\nEnter the atomic number of the element (0 to stop): "))
            if i>118 or i<0:
                print("\nThere are only 118 elements, so enter a positive number between 1 and 118.")
                i = int(input("Enter the atomic number of the element (0 to stop): "))
            while i != 0:
                i -= 1

                functions.show_table(i)
            
                i = int(input("\nEnter the atomic number of the element sought (0 to stop): "))
                if i>118 or i<0:
                    print("\nThere are only 118 elements, so enter a positive number between 1 and 118.")
                    i = int(input("Enter the atomic number of the element sought (0 to stop): "))

        if res == 2:
            functions.title("REACTIVITY SERIES")
            sym = input("\nEnter the symbol(0 to stop): ").capitalize()
            while sym != "0":
                aux = 0
                functions.reactivity_series(sym, aux)
                sym = input("\nEnter the symbol(0 to stop): ").capitalize()

        if res == 3:
            element = input("\nEnter the element or a oxidant's part(0 to stop): ")
            while element != "0":
                functions.electromotive_potentials(element)
                element = input("\nEnter the element or a oxidant's part(0 to stop): ")
            

        cont = input("\nCONTINUE(Y/N): ")
        while cont != "Y" and cont != "N":
            cont = input("\nCONTINUE(Y/N): ")
        if cont == "N":
            fim = True

except:
    print()