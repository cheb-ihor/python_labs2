#Завдання 1. Отримати суму бюджетів осіб
def get_budget(lst_budgets): 
    sum = 0
    for i in lst_budgets: 
        sum += i['budget'] 
    return sum
print(get_budget([{ "name": "John", "age": 21, "budget": 23000 },{ "name": "Steve",  "age": 32, "budget": 40000 },{ "name": "Martin",  "age": 16, "budget": 2700 }]))
print('------------------')
#Завдання 2. Отримати імена студентів
def get_student_names(dict_names):
    names = list(dict_names.values())
    names.sort()
    return names
print(get_student_names({"Student 1" : "Steve","Student 2" : "Becky","Student 3" : "John"}))
print('------------------')
#Завдання 3. Відфільтрувати повторювані символи рядків
def identical_filter(words):
    new_list = []
    for i in words:     
        if len(set(i)) == 1:
            new_list.append(i)
    return new_list
print(identical_filter(['aaaaaa', 'bc', 'd', 'eeee', 'xyz']))
print('------------------')
#Завдання 4. Перевірка підмножини
def validate_subsets(subsets, one_set):
    for subset in subsets:
        if not set(subset).issubset(one_set):
            return False
    return True
print(validate_subsets([[1, 2], [2, 3], [1, 3]], {1, 2, 3}))
print('------------------')
#Завдання 5. Пріоритетне сортування
def priority_sort(unsort_lst, pri_set):
    priority_items = sorted(set(unsort_lst) and pri_set)
    sorted_list = sorted(unsort_lst)
    sorted_list.sort(key=lambda x: priority_items.index(x) if x in priority_items else len(priority_items))
    return sorted_list
print(priority_sort([-5, -4, -3, -2, -1, 0], {-4, -3}))
print('------------------')
#Завдання 6. Знайти максимальну довжину послідовності, що складається з існуючих пар
def len_longest_chain(chain_pairs):
    chain_pairs.sort(key=lambda x: x[1])
    lngofpairs= len(chain_pairs)
    dp = [1] * lngofpairs
    for i in range(1, lngofpairs):
        for j in range(i):
            if chain_pairs[j][1] < chain_pairs[i][0]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
print(len_longest_chain([(-15, -11), (17, 22), (8, 12), (-11, -10), (-4, -1)]))
print('------------------')
#Завдання 7. Інверсія кольору
def colour_invert(rgb):
        b = tuple(255 - x for x in rgb)
        return (b)
print(colour_invert((0, 0, 0)))
print('------------------')
#Завдання 8. 
def check(dict1, dict2, key_ch):
    if key_ch not in dict1 and key_ch not in dict2:
        return "Not found"
    elif key_ch not in dict1 or key_ch not in dict2:
        return "One's empty"
    elif dict1[key_ch] == dict2[key_ch]:
        return True
    else:
        return 'Not the same'
dict_first = { "sky": "temple", "horde": "orcs", "people": 12, "story": "fine", "sun": "bright" }
dict_second = { "people": 12, "sun": "star", "book": "bad" }
print(check(dict_first, dict_second, "sun"))
    