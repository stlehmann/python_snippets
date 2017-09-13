# Remove a part of a string by specifying index and length
# of the characters you want to remove.
def remove_by_index(s, start_index, length):
    return s[:start_index] + s[start_index + length:]

remove_by_index('0123456789', 4, 2)
# result: '01236789'
