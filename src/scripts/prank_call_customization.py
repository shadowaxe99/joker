```python
from src.backend.user_preferences import storeUserPreferences

def customizeScript(user_id, script):
    """
    Function to customize the prank call script based on user input.
    """
    # Store the customized script in user preferences
    storeUserPreferences(user_id, 'script', script)

def promptUserForInput(user_id, prompt_type):
    """
    Function to prompt the user for input to make the prank call more engaging.
    """
    # Define prompts for different types of input
    prompts = {
        'name': "Please enter the recipient's name: ",
        'location': "Please enter the recipient's location: "
    }

    # Get the prompt for the specified type
    prompt = prompts.get(prompt_type)

    if prompt:
        # Get user input
        user_input = input(prompt)

        # Store the user input in user preferences
        storeUserPreferences(user_id, prompt_type, user_input)
    else:
        print("Invalid prompt type.")
```