# Insert a string s2 in a string s1 at the specified index
def insert(s1, s2, index):
    return s1[:index] + s2 + s1[index:]

insert('0123456789', 'Hello', 4)
# result: '0123Hello456789'
