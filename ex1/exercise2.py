from automata.fa.dfa import DFA

alphabet = {'0', '1'}
states = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7'}
accept_states = {'q4'}
input_state = 'q0'

transitions = {
    'q0': { '0': 'q5', '1': 'q1' },
    'q1': { '0': 'q2', '1': 'q1' },
    'q2': { '0': 'q5', '1': 'q3' },
    'q3': { '0': 'q4', '1': 'q1' },
    'q4': { '0': 'q4', '1': 'q4' },
    'q5': { '0': 'q5', '1': 'q6' },
    'q6': { '0': 'q7', '1': 'q1' },
    'q7': { '0': 'q5', '1': 'q4' }
}

dfa = DFA(
    states=states,
    input_symbols=alphabet,
    transitions=transitions,
    initial_state=input_state,
    final_states=accept_states
)


acp_inputs = [
    '01100010010100110',
    '1010',
    '1011010',
    '0100101',
    '1011010',
    '10011101010'
]

decline_inputs = [
    '',
    ' ',
    '101',
    '010',
    '011100100',
    '100'
]

result_accept_inputs = []
result_decline_inputs = []

print('ACCEPT INPUTS')
for i in acp_inputs:
    print(f'{i} =', f'{len(i)},', dfa.accepts_input(i))

print('')

print('DECLINE INPUTS')
for i in decline_inputs:
    print(f'{i} =', f'{len(i)},', dfa.accepts_input(i))
