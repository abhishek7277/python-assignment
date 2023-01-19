def count_substring(string, sub_string):
    return string.count(sub_string)

string = "The quick brown fox jumps over the lazy dog"
sub_string = "the"
count = count_substring(string, sub_string)
print("The count of substring '"+sub_string+"' in the string is:", count)
