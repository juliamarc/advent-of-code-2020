from collections import namedtuple


def main():
    Instr = namedtuple("Instruction", "op arg")
    State = namedtuple("State", "cntr acc")

    def get_next_state(state, op, arg):
        cntr = arg if op == "jmp" else 1
        acc = arg if op == "acc" else 0

        return State(state.cntr + cntr, state.acc + acc)

    def get_clean_history(history=None, until=None):
        if history is None or until is None:
            return [State(0, 0)]

        while history:
            popped = history.pop()
            if popped.cntr == until:
                break
        else:
            history = get_clean_history()

        return history

    with open('input') as f:
        lines = f.read().splitlines()

    code = list(map(lambda l: Instr(l.split()[0], int(l.split()[1])), lines))

    history = get_clean_history()
    while True:
        prev_state = history[-1]
        next_instr = prev_state.cntr
        op, arg = code[next_instr].op, code[next_instr].arg

        next_state = get_next_state(prev_state, op, arg)

        if next_state.cntr in map(lambda s: s.cntr, history):
            break

        history.append(next_state)

    part_one = history[-1].acc

    history = get_clean_history()
    swap_history = []
    currently_swapped = None
    while history[-1].cntr < len(code):
        prev_state = history[-1]
        next_instr = prev_state.cntr
        op, arg = code[next_instr].op, code[next_instr].arg

        if currently_swapped is None and op in ["jmp", "nop"] and next_instr not in swap_history:
            currently_swapped = next_instr
            op = "jmp" if op == "nop" else "nop"

        next_state = get_next_state(prev_state, op, arg)

        if next_state.cntr in map(lambda s: s.cntr, history):
            history = get_clean_history(history, currently_swapped)
            swap_history.append(currently_swapped)
            currently_swapped = None
        else:
            history.append(next_state)

    part_two = history[-1].acc

    print("--- Part One ---", part_one, sep='\n')
    print("--- Part Two ---", part_two, sep='\n')


if __name__ == "__main__":
    main()
