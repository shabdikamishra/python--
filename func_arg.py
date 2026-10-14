# *args, **kwargs, and keyword-only arguments
def foo(a, b, *args, keyword_only, **kwargs):
    print(a, b, args, keyword_only, kwargs)

foo(1, 2, 3, 4, 5, keyword_only=100, extra="value")

# Call by Object Reference
def modify_list(a_list):
    a_list.append(4)     #modifies caller list in-place
    # a_list = [10, 20]  #rebinding reference does NOT affect caller

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  