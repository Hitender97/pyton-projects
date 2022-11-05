eng_branch = {
    "cs": "Computer science",
    "it": "Information technology",
    "extc": "Electronics and telecommunication",
    "ee": "Electronics Engineering",
    "Ints": "Instrumentation science"
}

a=input("Enter your branch name in short form: ")
print(eng_branch.get(a))