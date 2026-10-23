# Check if a List is Contained Within Another
main_list = [1, 2, 3, 4, 5, 6]
sub_list = [3, 4, 5]
is_sub = any(
    main_list[i : i + len(sub_list)] == sub_list
    for i in range(len(main_list) - len(sub_list) + 1)
)
print(f"Is sublist present? {is_sub}")

# Basic Stack Operations Using a List
stack = []
stack.append(10)  # Push
stack.append(20)
stack.append(30)
print(f"Top element (Peek): {stack[-1]}")
print(f"Popped element: {stack.pop()}")
print(f"Remaining stack: {stack}")