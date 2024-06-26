calls = 0


def count_calls():
    global calls
    calls += 1
    return calls


def string_info(string):
    string_inf = len(string), string.upper(), string.lower()
    count_calls()
    return string_inf


def is_contains(string, list_to_search):
    list_to_search = [i.lower() for i in list_to_search]
    var = string.lower() in list_to_search
    count_calls()
    return var


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
