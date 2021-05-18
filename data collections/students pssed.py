total_students=("anu","jiya","amal","adhul","nandu","aiswarya")
print("total students", total_students)
failed={"jiya","amal","nandu"}
print("failed students set",failed)
passed=set()
for i in total_students:
    if i not in failed:
        passed.add(i)
print("passed students are",passed)