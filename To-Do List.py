class ToDoList:
    def __init__(self):
        self.task=[]

    def addTask(self):
        number_of_task=int(input('Enter number of task you want to add:'.center(80)))
        for i in range(number_of_task):
            taskname=input('Enter Task:'.center(80))
            self.task.append(taskname)
            print('Task added'.center(80))

    def removeTask(self):
        taskname=input('Enter taskname you want to remove:'.center(80))
        if taskname in self.task:
            self.task.remove(taskname)
            print('Task remove successfully'.center(80))
        else:
            print('Task not found in the list'.center(80))
    
    def viewtask(self):
        if self.task:
            print('Your To-Do list:'.center(80))
            for i,task in enumerate(self.task,start=1):
                print(f'{i}.{task}'.center(80))
        else:
            print('Your To-Do List is Empty'.center(80))
    def mark_Done(self):
        taskindex=int(input('Enter taskindex you want to mark done:'.center(80)))
        if len(self.task)>taskindex>=0:
            self.task[taskindex]=self.task[taskindex]+'  Done'
            print('Task Mark as Done'.center(80))
        else:
            print('Invallid Task Number'.center(80))


tdl=ToDoList()
while True:
    print('**********To Do List Menu *******'.center(80))
    print('1.Add Task'.center(80))
    print('2.Remove Task'.center(80))
    print('3.View Task'.center(80))
    print('4.Mark Task as Done'.center(80))
    print('5.Exit'.center(80))

    choice=input('Enter choice:'.center(80))   
    if choice=='1':
        tdl.addTask()     
    elif choice=='2':
        tdl.removeTask()
    elif choice=='3':
        tdl.viewtask()
    elif choice=='4':
        tdl.mark_Done()
    elif choice=='5':
        print('Exit'.center(80))
        print('Thank you'.center(80))
        break
    else:
        print('Wrong Choice'.center(80))
        





