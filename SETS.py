word1 = str(input("Enter first word (A): "))
word2 = str(input("Enter second word (B): "))
word3 = str(input("Enter third word (C): "))

print("=============================================")
print("1. Cardinality of each set")
print("2. A ∪ B")
print("3. (A ∪ B) ∩ C")
print("4. (B ∩ C) ∪ (B ∩ A)")
print("5. B' ∩ C'")
print("6. A - C")
print("7. A' ∩ B' ∩ C'")
print("8. (A ∪ B)'")
print("9. Number of subsets of each word")
print("10. Number of proper subsets of each word")
print("11. Exit the program")
print("=============================================")

def word_to_set(word): # Converts the words to individual letters
    word_set = set() # Creating an empty set to store letters
    for n in word:
        if n.isalpha(): # Checks if the character is a letter
            word_set.add(n.lower().strip()) # Adds the letter in the empty set
        else:
            print(f"'{n}' is not a letter. Must be all letters.")
    return word_set
    
A = word_to_set(word1)
B = word_to_set(word2)
C = word_to_set(word3)
U = set("abcdefghijklmnopqrstuvwxyz") # set() splits all the letters individually

# OPERATIONS THAT ARE NOT INCLUDED TO BE DISPLAYED
def union(set1, set2):
    return set1.union(set2) # alternatively, set1 | set2
def intersection(set1, set2):
    return set1.intersection(set2) # alternatively, set1 & set2
def complement(s, U): 
    return U - s


# OPERATIONS THAT NEED TO BE DISPLAYED
def Op1(s):
    return len(s) # len() returns the number of items in the sets
def Op2(set1, set2):
    return union(set1, set2) 
def Op3(set1, set2, set3):
    return intersection(union(set1, set2), set3) 
def Op4(set1, set2, set3):
    return union(intersection(set2, set3), intersection(set2, set1))
def Op5(B, C, U):
    B_complement = complement(B, U)
    C_complement = complement(C, U)
    return B_complement.intersection(C_complement)
def Op6(A, C):
    return A - C
def Op7(A, B, C, U):
    B_complement = complement(B, U)
    C_complement = complement(C, U)
    A_complement = complement(A, U)
    B_com_C = B_complement.intersection(C_complement)
    return A_complement.intersection(B_com_C)
def Op8(A, B, U):
    return complement(union(A, B), U)
def Op9(s):
    return 2 ** len(s)
def Op10(s):
    return 2 ** len(s) - 1

while True: # Infinitely runs the code for choosing a choice
    choice = input("Enter a choice (1-11): ")

    if choice == '1':
        print(f"Cardinality of word A: {Op1(A)}")
        print(f"Cardinality of word B: {Op1(B)}")
        print(f"Cardinality of word C: {Op1(C)}")
    elif choice == '2':
        print(f"A ∪ B: {sorted(Op2(A, B))}") # sorted() sorts the letters in alphabetical order
    elif choice == '3':
        print(f"(A ∪ B) ∩ C: {sorted(Op3(A, B, C))}")
    elif choice == '4':
        print(f"(B ∩ C) ∪ (B ∩ A): {sorted(Op4(A, B, C))}")
    elif choice == '5':
        print(f"B' ∩ C': {sorted(Op5(B, C, U))}")
    elif choice == '6':
        print(f"A - C: {sorted(Op6(A, C))}")
    elif choice == '7':
        print(f"A' ∩ B' ∩ C': {sorted(Op7(A, B, C, U))}")
    elif choice == '8':
        print(f"(A ∪ B)': {sorted(Op8(A, B, U))}")
    elif choice == '9':
        print(f"The number of subsets in set A is {Op9(A)}")
        print(f"The number of subsets in set B is {Op9(B)}")
        print(f"The number of subsets in set C is {Op9(C)}")
    elif choice == '10':
        print(f"The number of proper subsets in set A is {Op10(A)}")
        print(f"The number of proper subsets in set B is {Op10(B)}")
        print(f"The number of proper subsets in set C is {Op10(C)}")
    elif choice == '11':
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Select from 1-11.")