from common import move_list_commands, crate_stacks


for move_command in move_list_commands:
    crate_count, from_stack, to_stack = move_command
    from_stack_index, to_stack_index = from_stack - 1, to_stack - 1
    for _ in range(crate_count):
        crate_stacks[to_stack_index].append(crate_stacks[from_stack_index].pop())


answer = "".join([crate_stack[-1] for crate_stack in crate_stacks])
print(answer)
