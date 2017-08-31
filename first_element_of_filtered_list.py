"""
This snippet shows how to filter a list and retrieve the first
element which passes the filter. If no element was found the
result will be None.

"""
items = list(range(5))
res = next(x for x in items if x > 3), None)
