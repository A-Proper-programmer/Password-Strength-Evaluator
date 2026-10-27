import os, argparse

def check_contains(string1, string2):       # Checks if string1 contains any character from string2
    for i in string1:
        if i in string2:
            return 1
    return 0

def password_leaked(pswd, _f):
    for i in _f:
        path = os.path.join(os.path.dirname(__file__), i)               # Finds path of wordlist
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as pass_file:
                passwords = pass_file.read().split("\n")                    # Converts txt file to a list
            if pswd in passwords:                                           # Checks if the password in a common wordlist
                print("This password was found in a list of common passwords!")
                return 0
        else:
            print(f"The file {_f} was not found!")

def check_strength(pswd, _files):
    if password_leaked(pswd, _files):
        return 0

    # Adds points for each distinct type of characters, length of password
    strength = 1
    if len(pswd) >= 8:
        strength += 1
    strength += int(len(pswd) >= 18)
    strength += check_contains(pswd, "abcdefghijklmnopqrstuvwxyz") + 2*check_contains(pswd, "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    strength += check_contains(pswd, " 1234567890") + 2*check_contains(pswd, '!@#$%^&*()-=_+"') + check_contains(pswd, r"[]{}\\:;',./?")
    return strength

# ARGUMENT PARSER
parser = argparse.ArgumentParser(description="A program to check the strength of the password")
parser.add_argument('-f', '--files', nargs='*', default=["rockyou1.txt", "rockyou2.txt"], help='Specify wordlist')
args = parser.parse_args()

# MAIN
print("[=] Check your password strength!")
password = input("[+] Enter your password : ")
print()
print(f"[+] Your password's strength on a scale of 0 to 10 is {check_strength(password, args.files)}")