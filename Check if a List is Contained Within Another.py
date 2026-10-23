# Check if a List is Contained Within Another
main_list = [1, 2, 3, 4, 5, 6]
sub_list = [3, 4, 5]
is_sub = any(
    main_list[i : i + len(sub_list)] == sub_list
    for i in range(len(main_list) - len(sub_list) + 1)
)
print(f"Is sublist present? {is_sub}")