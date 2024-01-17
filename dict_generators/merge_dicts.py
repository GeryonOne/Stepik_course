from collections import defaultdict

# 1-й вариант, с помощью метода defaultdict
def merge(dicts_list):
    merge_dict = defaultdict(set)

    for dict in dicts_list:
        for key, value in dict.items():
            merge_dict[key].add(value)

    return merge_dict


result = merge([{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}])


# 2-й вариант, с помощью метода setdefault
def merge(values):
    res = {}
    for d in values:
        for k, v in d.items():
            res.setdefault(k, set()).add(v)
    return res