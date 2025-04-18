with open("output.txt", "w+") as file:
    text = input("Enter text to write to the file: ") + "\n"

    file.write(text)
    print("Data successfully written to output.txt")

    print()
    print() # To maintain the gap similar to given screenshot

    # I am not reopening the file with 'a' mode because the pointer is already at the end of the file. Its same as appending to the file.
    add_text = input("Enter additional text to append: ") + "\n"
    file.write(add_text)
    print("Data successfully appened.")

    print()
    print()

    print("Final Content of output.txt:\n")


    # to read the file entire (instead of reopening with 'r' mode I am just moving the pointer to start of the file)
    file.seek(0)
    print(file.read())