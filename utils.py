## utils.py

def display_message(message: str):
    """Displays a message to the user.

    Args:
        message (str): The message to display.
    """
    print(message)

def get_user_input(prompt: str) -> str:
    """Gets input from the user.

    Args:
        prompt (str): The prompt to display to the user.

    Returns:
        str: The user's input.
    """
    return input(prompt)
