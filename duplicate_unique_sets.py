a={"one","two","three"}
b={"three","four","five"}

duplicates = set()
for elem in a:
    if elem in b:
        duplicates.add(elem)

if duplicates:
    print("duplicates value found",duplicates)
else:
    print("all unique")

uniques= set()
for elem in a:
    if elem not in b:
        uniques.add(elem)
        for elem in b:
            if elem not in a:
                uniques.add(elem)

if uniques:
    print("unique value exist",uniques)
else:
    print("no unique")
