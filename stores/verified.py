from itertools import chain
first_names_list_queryset = list()
last_names_list_queryset = list()
fist_name_startswith_queryset = list()
response = list(chain(first_names_list_queryset, last_names_list_queryset, fist_name_startswith_queryset))
if response:
    print("Response exist")
else:
    print("Not exist")
