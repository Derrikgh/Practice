m=int(input('what was the midterm exam score?: '))
f=int(input('what was project score?: '))
p=int(input('what was the final exam  score?: '))

ws=(m*.30)+(f*.40)+(p*.30)
print(f'{ws}% is the final weighted sum of the 3 scores')
if ws >90:
    print('Letter grade of...A: excellent')
elif ws >80 and ws<+89:
    print('Letter grade of...B: good')
elif ws >70 and ws<=79:
    print('Letter grade of... C: satisfactory')
elif ws >60 and ws<=69:
    print(' Letter grade of... D: needs improvement')
elif ws<60:
    print('letter grade F: failed')

input('thank you!, press enter to exit')
