


from audioop import add


class store:

    def __init__(self):
        self.__list=[]

    def add(self,element):
        self.__list.append(element)

    def get_element(self,position):
        try:
            if len(self.__list) == 0:
                raise Exception('empty list') 
            else:                
                element=self.__list[position]
                del self.__list[position]
                return element
        except Exception as e:
            return e
        
class stack(store):

    def __init__(self):
        super().__init__()
    def push(self,element):
        return store.add(element)
        
    def pop(self):
       position = -1
       return store.get_element(position)

class queue(store):

    def __init__(self):
        super().__init__()

    def put(self, element):
        return store.add(element)

    def get(self):
        position = 0
        return store.get_element(position)

# getting in put 
list=[]
print('what data store would you like to use', end='\n')
data_store=input('queue or stack: ')
while True:
      element=input('enter item in list: ')
      if element == 'end':
        break
      list.append(element)

      print('To exit enter end: ')

if data_store == 'stack':
    store=stack()
    for item in list:
        store.push(item)
    print(store.pop())
    print(store.pop())
else:
    store=queue()
    for item in list:
      store.put(item)
    print(store.get())
    print(store.get())
