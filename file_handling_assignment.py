def write_to_file():
    try:
        # Creating and writing to the file
        with open("my_file.txt", 'w') as file:
            file.write("This is line 1\n")
            file.write("12345\n")
            file.write("A line with text and numbers: 456abc\n")
    except FileNotFoundError:
        print("File not found!")
    except PermissionError:
        print("Permission denied!")
    finally:
        print("Write operation completed!")


def read_and_display_file():
    try:
        # Reading and displaying the contents of the file
        with open("my_file.txt", 'r') as file:
            print("Contents of my_file.txt:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("File not found!")
    except PermissionError:
        print("Permission denied!")
    finally:
        print("Read operation completed!")


def append_to_file():
    try:
        # Appending to the file
        with open("my_file.txt", 'a') as file:
            file.write("This is another line (appended)\n")
            file.write("67890\n")
            file.write("Appending more text and numbers: xyz789\n")
    except FileNotFoundError:
        print("File not found!")
    except PermissionError:
        print("Permission denied!")
    finally:
        print("Append operation completed!")


def main():
    write_to_file()
    read_and_display_file()
    append_to_file()
    read_and_display_file()


if __name__ == "__main__":
    main()
