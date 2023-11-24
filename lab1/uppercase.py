def uppercase_count(string):
    """Return the number of uppercase letters inside the string.

    Arguments:
    string - input string which will be checked
    """

    count = 0;
    allowed_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for char in string:
        if char in allowed_chars:
            count += 1

    return count

def main():
    strings = [
            "pero", 
            "Pero",
            "PEROPERO",
            "WySiWyG"
    ]   

    for string in strings:
        print(f"String '{string}' has {uppercase_count(string)} uppercase letters")

if __name__ == "__main__":
    main()
