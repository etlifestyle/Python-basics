
print('Answer to question must be in upper case ONLY')
blood_group=input('Blood group: ')
if blood_group == 'A':
    print('Can not take sugar')
elif blood_group == 'B' :
    print('Can take half spoon of sugar a day ')
elif blood_group == 'AB':
    print('Can take little sugar')
elif blood_group == 'O':
    print('Can take much sugar as you wish')
else:
    print('Something went wrong pls read instructions')