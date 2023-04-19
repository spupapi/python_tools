import re

list1 = ["item1", "item2"]
list2 = ["item1", "item2"]

for item in list1:
    for item2 in list2:
        if re.match(item, item2):
            print("duplicate: ", item)