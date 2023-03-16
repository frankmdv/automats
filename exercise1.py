from automata.fa.dfa import DFA

alphabet = {'0', '1'}
states = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6'}
accept_states = {'q0', 'q2', 'q5'}
input_state = 'q0'

transitions = {
    'q0': { '0': 'q4', '1': 'q1' },
    'q1': { '0': 'q0', '1': 'q2' },
    'q2': { '0': 'q3', '1': 'q6' },
    'q3': { '0': 'q3', '1': 'q3' },
    'q4': { '0': 'q0', '1': 'q5' },
    'q5': { '0': 'q4', '1': 'q6' },
    'q6': { '0': 'q3', '1': 'q2' }
}

dfa = DFA(
    states=states,
    input_symbols=alphabet,
    transitions=transitions,
    initial_state=input_state,
    final_states=accept_states
)

acp_inputs = [
    '0010101010', '01010101', '000000', '111111',
    '100101', '0111', '0010101010', '01010101',
    '000000', '111111', '100101', '0111'
]

decline_inputs = [
    '111000', '111001', '011010', 
    '0110','110', '011', '01011','0010101'
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
