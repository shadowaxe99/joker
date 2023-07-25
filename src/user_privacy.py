```python
def checkConsent(userPreferences):
    """
    Function to check if the user has confirmed the recipient's consent to be pranked.
    """
    if 'consent' in userPreferences and userPreferences['consent']:
        return True
    else:
        return False
```