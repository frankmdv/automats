from automata.fa.dfa import DFA

alphabet = {'0', '1'}
states = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', ''}
accept_states = {'E', 'F', 'G', 'H', 'I', 'J'}
initial_state = 'A'

transitions = {
        'A': {'0': 'B', '1': 'C'},
        'B': {'0': '', '1': 'D'},
        'C': {'0': 'E', '1': ''},
        'D': {'0': 'F', '1': ''},
        'E': {'0': '', '1': 'G'},
        'F': {'0': '', '1': 'H'},
        'G': {'0': 'I', '1': 'G'},
        'H': {'0': 'I', '1': 'J'},
        'I': {'0': '', '1': ''},
        'J': {'0': '', '1': 'J'},
    '': {'0': '', '1': ''}
}

dfa = DFA(
    states=states,
    input_symbols=alphabet,
    transitions=transitions,
    initial_state=initial_state,
    final_states=accept_states
)


entry = '01010'

print(f'Input = { entry },', f'Length = { len(entry) },', f'Result = { dfa.accepts_input(entry) }')

a
