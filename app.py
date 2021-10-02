
emergency=input('What is the emergency')

if emergency =='Fire':
    input('Location: ')
    input('House number: ')
    dis=input('Distance:  ')
    print('Distance must be in km in lower case')
    if dis == '3km':
        print('I will be there in 2 minutes')
    elif dis == '2km':
        print('I will be there in 1 minutes')
    else:
        print('I am on my way')
elif emergency =='Car accident' :
    input('Location: ')
    input('Registration No.: ')
    distance= input('Distance: ')
    if distance == '3km':
        print('I will be there in 2 minutes')
    elif distance == '2km':
        print('I will be there in 1 minutes')
    else:
        print('I am on my way')