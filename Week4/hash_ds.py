# Time Complexity:O(n)
# Space Complexity:O(n)
def count_char(string):
    char_count={}
    for i in string:
        if i in char_count:
            char_count[i] += 1
        else:
            char_count[i]=1

    print(char_count)


count_char('abcdd')

