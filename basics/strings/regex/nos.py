import os
import re


text = " hi this is a sample mobile no 478-785-7895 and this is a fake ni 859875s5 and another 879-754-9658"
# phone_no_regex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
phone_no_regex = re.compile(r"\d{3}-\d{3}-\d{4}")
match = phone_no_regex.findall(text)
print(match)
# if something is optional ? can be used.. if first 3 digits are optional
text1 = " hi this is a sample patient_name mobile no abc.txt and this patient_dob is a fake ni 859875s5 and another ddf.txt"
phone_no_regex1 = re.compile(r"patient_(name|dob)")
phone_no_regex2 = re.compile(r"\.txt$")
match1 = phone_no_regex2.findall(text1)
print(match1)
print(os.path.sep)
pass
