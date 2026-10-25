import os

def check_contains(string1, string2):                               # Checks if string1 contains any character from string2
    for i in string1:
        if i in string2:
            return 1
    return 0

def check_strength(pswd):
    path = os.path.join(os.path.dirname(__file__), "rockyou.txt")   # Finds path of wordlist
    with open(path, "r", encoding="utf-8") as pass_file:
        passwords = pass_file.read().split("\n")                    # Converts txt file to a list
    if pswd in passwords:                                           # Checks if the password in a common wordlist
        print(f"{pswd} was found in a list of common passwords!")
        return 0

    # Adds points for each distinct type of characters, length of password
    strength = 2
    if len(pswd) >= 8:
        strength += 2
    strength += int(len(pswd) >= 18)
    strength += check_contains(pswd, "abcdefghijklmnopqrstuvwxyz") + check_contains(pswd, "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    strength += check_contains(pswd, " 1234567890") + check_contains(pswd, '!@#$%^&*()-=_+"') + check_contains(pswd, r"[]{}\\:;',./?")
    return strength

# MAIN
print("[=] Check your password strength!")
password = input("[+] Enter your password : ")
print()
print(f"[+] Your password's strength on a scale of 0 to 10 is {check_strength(password)}")