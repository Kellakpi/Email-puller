import pyperclip
import re

emails = set() # Builds a collection/list of unique elements

mode = input("Type 'file' or 'clipboard' to choose input method: ").strip().lower() # Prompt the user for an input method, between file and clipboard.
if mode == "file":
    fname = input("Whats the file name? ")  
    with open(fname, "r") as fh: # Open the file as Read only
        for line in fh: 
            matches = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", line) # Specify what its looking for, using Regex
            emails.update(matches) # Updates the set, every iteration
elif mode == "clipboard":
    text = pyperclip.paste() # Allows the pasting function from clipboard
    lines = text.splitlines()
    for line in lines:
        matches = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", line)
        emails.update(matches)
else:
    print("Invalid option. Please enter 'file' or 'clipboard'.") # This is what triggers if no option is taken, could add a way to keep program running/looping.
    


print("\nFound emails: ")
for email in emails:
    print("-", email)

with open("output.txt", "w") as output: # Create a file with all the emails found.
    for email in sorted(emails):    #Sort the email found in ascending order
        output.write(email + "\n")
print(f"\nSaved {len(emails)} emails to output.txt. Job is done!") # Print amount of emaiils found, using F string to save time.