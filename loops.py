



#prints hello world 3 times 
def forLoopExample1():
    for i in range(3):
        print ('hello world')

#goes through all objects in a list and prints them
#'f' formats string and allows {} to be used
#allowing dynamic variable to be used instead of static name
def forLoopExample2():
    names: list[str] = ['agatha', 'john', 'dave', 'ben'] #list

    for name in names:
        print (f'hello {name}')



#will go on until 'i' is not longer less than 3 (until its 3)
def whileLoopExample1():
    i = 0
    while i < 3:
        print(i)
        i += 1



#while true goes on forever

#while True:
#   print('hello')

