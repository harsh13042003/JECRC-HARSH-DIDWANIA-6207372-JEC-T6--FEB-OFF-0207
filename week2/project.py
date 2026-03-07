import time

class TODO:
    todos = []

    def add_todo(self, desc):
        if(len(desc)==0):
            print('Task cannot be empty.')
        else:
            self.todos.append({'id':int(time.time()),'desc':desc,'isCompleted':False})

    def remove_todo(self, id):
        flag=False
        for i in self.todos:
            if(i['id']==id):
                print('deleted todo:',i)
                self.todos.remove(i)
                flag=True
        if(flag==False): 
            print('enter a valid id')

    def display_todos(self):
        for i in self.todos:
            print(i)

    def update_todo(self, id, new_desc):
        flag=False
        for i in self.todos:
            if(i['id']==id):
                i['desc']=new_desc
                flag=True
                break
        if(flag==False):
            print('Enter a correct id')

    def toggle_mark_as_completed(self, id):
        flag=False
        for i in self.todos:
            if(i['id']==id):
                i['isCompleted']=True
                flag=True
                break
        if(flag==False):
            print('Enter a valid id')

    def completed_todos(self):
        flag=False
        for i in self.todos:
            if(i['isCompleted']==True):
                flag=True
                print(i)
        if(flag==False):
            print('no completed todos')

    def incompleted_todos(self):
        for i in self.todos:
            if(i['isCompleted']==False):
                print(i)




t = TODO()

t.add_todo("Eat lunch")
t.add_todo("Study Python")

t.display_todos()

# kisi task ko completed mark karne ke liye
first_id = t.todos[0]['id']
t.toggle_mark_as_completed(first_id)

t.display_todos()

t.completed_todos()
t.incompleted_todos()