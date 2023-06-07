def sort_names():
    names_list = input().split(', ')
    sorted_names = sorted(names_list, key=lambda x: (-len(x), x))   # -len(x) sorts from the biggest to lowest length
    return sorted_names                                             #  +inf --> -inf
                                                                    # after that we sort by 'x' -> so we sort by alphabet


result = sort_names()
print(result)


