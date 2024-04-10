#!/usr/bin/python3
def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The text to be printed.

    Raises:
        TypeError: If text is not a string.

    Returns:
        None
    """
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Iterate through each character in the text
    for char in text:
        # Print the character without leading or trailing spaces
        if char == '.' or char == '?' or char == ':':
            print(char)
            print()
        else:
            print(char, end='')

    # Print a new line at the end if the text doesn't end with ., ? or :
    if text[-1] not in ['.', '?', ':']:
        print()

