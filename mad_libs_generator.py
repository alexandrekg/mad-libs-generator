people_playing_count = int(input('How much people are playing this game? '))

loop = 0

while loop < people_playing_count:
    name = input('A name... ')
    age = input('Integer number min 1 - max 100. ')
    hobby = input('Something fun to do. ')
    famous = input('Name someone famous. ')

    print('---------------------------------------------------------------')
    print('Hi, there! My name is ' + name + '.')
    print('I have ' + age + ' years old.')
    print('I like to ' + hobby + '.')
    print("Mom says that I look like " + famous + ". But I don't think so.")
    print('---------------------------------------------------------------')

    loop += 1