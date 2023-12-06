# Python script to append ".txt" to each command line argument

# This script assumes that it's saved as a Python file (e.g., script.py) and executed from the command line.
# The command line arguments will be provided to the script when it's run from the command line.

# The sys module is used to access command line arguments
import sys

def append_txt_to_args():
    # sys.argv is a list in Python, which contains the command-line arguments passed to the script.
    # With the len(sys.argv) function you can count the number of arguments.
    if len(sys.argv) > 1:
        # Iterate over each argument in the command line after the script name
        for arg in sys.argv[1:]:
            # Append ".txt" to each argument and print
            print(f"@app.route('/{arg}')\ndef {arg.split('.')[0]}():\n   return render_template('{arg}')\n")
    else:
        print("No arguments provided.")

# The script can be run from the command line like this: python script.py arg1 arg2 arg3
# This will output: arg1.txt arg2.txt arg3.txt

# Call the function
append_txt_to_args()

# EXECUTE ARGUMENTS:
# create.html home.html inprogress.html invite-friends.html login.html onboarding.html signup.html user.html