import re


def find_name(line):
    # # full name (last and first) with salutation
    # pattern = r"\b(M[srx]\.)"
    # result = re.findall(pattern,line)

    # last name with Mr., Mx. or Ms. salutation
    pattern = r"(M[srx]\. [A-Z][a-z]*)"
    result = re.findall(pattern,line)

    # last name with Mrs. salutation
    pattern = r"(Mrs\. [A-Z][a-z]*)"
    result = result + re.findall(pattern,line)

    # full name (last and first) without salutation
    # note: this is picking up proper nouns that aren't names
    pattern = r"([A-Z]{1}[a-z]* [A-Z]{1}[a-z]*)"
    result = result + re.findall(pattern,line)
    return result


#result = find_date("10/15/2023 is a October 13, 2025 date as is 1/23/19")
#print(result)

f = open("names.txt")
for line in f.readlines():
    print(line)
    result = find_name(line)
    if (len(result)>0):
        print(result)
