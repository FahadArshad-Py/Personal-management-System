import os 
from datetime import datetime
import getpass

# Classes
class User:
    def __init__(self,username,password,type='basic',created_at=None):
        self.username=username
        self.password=password
        self.type=type
        self.created_at=created_at or datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

    def display(self):
        print(f"{self.username},{self.password},{self.type},{self.created_at}")

    def to_file(self):
        return(f"{self.username},{self.password},{self.type},{self.created_at}\n")


class Task:
    def __init__(self,username,task,priority,status='Pending',created_at=None):
        self.username=username
        self.task=task
        self.priority=priority
        self.status=status
        self.created_at=created_at or datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

    def to_file(self):
        return(f"{self.username},{self.task},{self.priority},{self.status},{self.created_at}\n")
    
    def display(self):
        return(f"{self.username} | {self.task} | {self.priority} | {self.status} | {self.created_at}\n")


class Expense:
    def __init__(self,username,category,amount,created_at=None):
        self.username=username
        self.amount=amount
        self.category=category
        self.created_at=created_at or datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

    def to_file(self):
        return(f"{self.username},{self.category},{self.amount},{self.created_at}\n")
    def display(self):
        return(f"{self.username} | {self.category} | {self.amount} | {self.created_at}\n")
    

class Goal:
    def __init__(self,username,title,target,saved_amount,deadline,status='Active',created_at=None):
        self.username=username
        self.title=title
        self.target=target
        self.saved_amount=saved_amount
        self.deadline=deadline
        self.status=status
        self.created_at=created_at or datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        
    def to_file(self):
        return(f"{self.username},{self.title},{self.target},{self.saved_amount},{self.deadline},{self.status},{self.created_at}\n")
    
    def display(self):
        return(f"{self.username} | {self.title} | {self.target} | {self.saved_amount} | {self.deadline} | {self.status} | {self.created_at}")
    

class PremiumUser(User):
    def __init__(self, username, password, created_at=None):
        super().__init__(username, password, type='premium', created_at=created_at)

    def display(self):
        print(f"{self.username}: is a premium user")

    def premium_info(self):
        return(f"username: {self.username} is a Premium User\n")
    

#File names
tasks=[]
expenses=[]
goals=[]
tasks_file="tasks.txt"
expenses_file="expenses.txt"
goals_file="goals.txt"
user_file="users.txt"


#File Handling for Tasks data
def load_tasks_file():
    
    if not os.path.exists(tasks_file):
        return tasks
    with open(tasks_file,"r") as tf:
        for x in tf:
            data=x.strip().split(",")
            if len(data)<5:
                continue
            username,task,priority,status,created_at=data[0],data[1],data[2],data[3],data[4]

            tasks.append(Task(username,task,priority,status,created_at=created_at))
    return tasks


def save_task(task):
    with open(tasks_file,'a') as tf:
        tf.write(task.to_file())


def save_all_tasks(task):
    with open(tasks_file,'w') as tf:
        for x in task:
            tf.write(x.to_file())


#File Handling for Expenses Data

def load_expenses_file():
    if not os.path.exists(expenses_file):
        return expenses
    
    with open(expenses_file,'r') as ef:
        for x in ef:
            data=x.strip().split(",")
            if len(data)<4:
                continue
            username,category,amount,created_at=data[0],data[1],data[2],data[3]
            expenses.append(Expense(username,category,float(amount),created_at))
    return expenses
        

def save_expense(expense):
    with open(expenses_file,'a') as ef:
        ef.write(expense.to_file())
    

def save_all_expenses(expense):
    with open(expenses_file,'w') as ef:
        for x in expense:
            ef.write(x.to_file())


# File Handling for Goals Data

def load_goals_file():
    if not os.path.exists(goals_file):
        return goals
    

    with open(goals_file,'r') as gf:
        for goal in gf:
            data=goal.strip().split(",")
            if len(data)<6:
                continue
            username,title,target,saved_amount,deadline,status,created_at=data[0],data[1],float(data[2]),float(data[3]),int(data[4]),data[5],data[6]
            goals.append(Goal(username,title,target,saved_amount,deadline,status,created_at=created_at))
        return goals
    
def save_goal(goals):
    with open(goals_file,'a') as gf:
        gf.write(goals.to_file())

def save_all_goals(goals):
    with open(goals_file,'w') as gf:
        for goal in goals:
            gf.write(goal.to_file())

# File Handling for User data

def load_user_file():
    users=[]
    if not os.path.exists(user_file):
        return users
    with open(user_file,'r') as uf:
        for x in uf:
            data=x.strip().split(",")
            if len(data)<4:
                continue
            username,password,acc_type,created_at=data[0],data[1],data[2],data[3]
            if acc_type.lower()=="premium":
                users.append(PremiumUser(username,password,created_at=created_at))
            else:
                users.append(User(username,password,type=acc_type,created_at=created_at))
    return users


def save_user(user):
    with open(user_file,'a') as uf:
        uf.write(user.to_file())


def save_all_users(users):
    with open(user_file,'w') as uf:
        for x in users:
            uf.write(x.to_file())


def check_user_exists(users,username):
    username=username.lower()
    for user in users:
        if user.username.lower()==username.lower():
            return user
    return None



# User Authentications

def login_user(users):
    print("\n----- Login -----")
    username=input("\nEnter username").strip()
    try:
        password=getpass.getpass().strip()
    except Exception:
        password=input("\nEnter Password").strip()

    user=check_user_exists(users,username)
    if not user:
        print("No User found. Please Register")
        return None
    if user.password==password:
        print("\nLogged in Sucessfully")
        return user
    else:
        print("\nInvalid Password")
        return None


def register_user(users):
    print("\n----- Register -----")
    while True:
        username=input("\nEnter Username").strip()
        if not username:
            print("\nUsername cannot be empty")
            continue
        if check_user_exists(users,username):
            print("User already exists")
            continue
        break
    
    try:
        password=getpass.getpass("\nEnter Password").strip()
    except Exception:
        password=input("\nEnter Password").strip()

    if not password:
        print("\nPassword cannot be empty")
        return None
    
    while True:
        acc_type=input("\n Enter Account type 'Basic' or 'Premium' default=[Basic]").strip().lower()
        if acc_type in('basic','premium'):
            break
        print("\nInvalid Account Type")

    if acc_type=='premium':
        user=PremiumUser(username,password)
    else:
        user=User(username,password,type='basic')

    users.append(user)
    save_user(user)
    print(f"{username} registered ass {acc_type} successfully")
    return user

# Task Management functions

def add_task(current_user):
    task=input("\nEnter task")
    priority=input("\n What is the priority for this task")
    task_obj=Task(current_user,task,priority)
    tasks.append(task_obj)
    save_task(task_obj)
    print("\nTask added successfully!")
    return task_obj


def view_task(tasks,current_user):
    for task in tasks:
        if task.username.lower()==current_user.lower():
            print(task.display())


def mark_task(tasks,current_user):
    print(f"\n All tasks for {current_user}")
    x=1
    user_tasks=[]
    for task in tasks:
        if task.username.lower()==current_user.lower():
            print(x,". ", task.display())
            user_tasks.append(task)
            x+=1
    if not user_tasks:
        print("No task found for user")
        return
    

    choice=int(input("Enter task number to mark as completed"))
    if 1<= choice<=len(user_tasks):
        task_to_mark=user_tasks[choice-1]
        task_to_mark.status='Completed'
        print("\nTask marked completed")

        save_all_tasks(tasks)
    else:
        print("Invalid task number")
    

def delete_task(tasks,current_user):
    print(f"\n All tasks for {current_user}")
    x=1
    user_tasks=[]
    for task in tasks:
        if task.username.lower()==current_user.lower():
            print(x,". ", task.display())
            user_tasks.append(task)
            x+=1
    if not user_tasks:
        print("No task found for user")
        return
    choice=int(input("Enter task number to delete"))
    if 1<= choice<=len(user_tasks):
        task_to_delete=user_tasks[choice-1]
        tasks.remove(task_to_delete)
        print("task deleted ")

        save_all_tasks(tasks)
    else:
        print("Invalid task number")


def filter_task(tasks,current_user):
    user_tasks=[]
    for task in tasks:
        if task.username.lower()==current_user.lower():
            user_tasks.append(task)
    
    while True:
        print("\nPress '1' to filter by Status")
        print("Press '2' to filter by Priority")
        print("Press '3' to Exit\n")
        choice=int(input("\nEnter your choice"))

        match choice:
            case 1:
                status_choice=input("Enter 'c' for completed and 'p' for Pending")
                
                if status_choice.lower()=='c':
                    for task in user_tasks:
                        if task.status.lower()=='completed':
                            print(task.display()) 
                        
                    print("NO task completed!")
                            
                elif status_choice.lower()=='p':
                    for task in user_tasks:
                        if task.status.lower()=='pending':
                            print(task.display())
                    print("All tasks completed")      
            case 2:
                user_tasks=[]
                for task in tasks:
                    if task.username.lower()==current_user.lower():
                        user_tasks.append(task)
                
                priority_choice=input("Enter choice (High | Medium | Low)")
                match priority_choice:
                    case 'high':
                        for task in user_tasks:
                            if task.priority.lower()==priority_choice.lower():
                                print(task.display()) 
                    case 'medium':
                        for task in user_tasks:
                            if task.priority.lower()==priority_choice.lower():
                                print(task.display()) 
                    case 'low':
                        for task in user_tasks:
                            if task.priority.lower()==priority_choice.lower():
                                print(task.display()) 

            case 3:
                break
            case _:
                print("Invalid choice! Try again")


# Expense Management functions


def add_expense(current_user):
    category=input("\nEnter category of expense e.g. (Food,Shopping, etc.)")
    amount=float(input("Enter amount of expense"))
    exp_obj=Expense(current_user,category,amount)
    expenses.append(exp_obj)
    print("Expense Added successfully")
    save_expense(exp_obj)
    return exp_obj


def view_expenses(expenses,current_user):
    for x in expenses:
        if x.username.lower()==current_user.lower():
            print(x.display())


def delete_expense(expenses,current_user):
    print(f"\nAll tasks of {current_user}")
    x=1
    user_expense=[]
    for expense in expenses:
        if expense.username.lower()==current_user.lower():
            print(f"{x}. ",expense.display())
            user_expense.append(expense)
            x+=1
    if not user_expense:
        print("No Expense found! Please add")
        return
        
    choice=int(input("Enter number of expense to delete"))
    if 1<=choice<=len(user_expense):
        expense_to_delete=user_expense[choice-1]
        expenses.remove(expense_to_delete)
        print("\nExpense Deleted successfully")
        save_all_expenses(expenses)
    else:
        print("\nInvalid choice")


def total_expense(expenses,current_user):
    sum=0
    for exp in expenses:
        if exp.username.lower()==current_user.lower():
            sum=+exp.amount
    print(f"\nTotal Expenses :  Rs{sum}")


# Goal manager Functions

def add_goal(current_user):
    title=input("\nEnter title for the goal")
    target=float(input("\nEnter Target amount for the Goal"))
    saved_amount=0
    deadline=int(input("\nEnter deadline in days"))

    goal_obj=Goal(current_user,title,float(target),float(saved_amount),int(deadline))

    goals.append(goal_obj)
    save_goal(goal_obj)
    print("\nGoal Added sucessfully")

def view_goals(goals,current_user):
    for goal in goals:
        if goal.username.lower()==current_user.lower():
            print(goal.display())


def add_saving(goals,current_user):
    print(f"\nAll goals for {current_user}")
    x=1
    user_goals=[]
    for goal in goals:
        if goal.username.lower()==current_user.lower():
            print(f"{x}.", goal.display())
            user_goals.append(goal)
            x+=1
            

    if not user_goals:
        print("No Goals found")
        return
    
    choice=int(input("\nEnter goal number to add saving"))
    amount=float(input("\nEnter amount to add"))

    if 1<=choice<len(user_goals):
        goal_to_add=user_goals[choice-1]
        goal_to_add.saved_amount+=amount
        
        if goal_to_add.saved_amount>=goal_to_add.target:
            goal_to_add.saved_amount=goal_to_add.target
            goal_to_add.status='Completed'
        
        print("Saved amount updated successfully")
        save_all_goals(goals)
    else:
        print("Invalid choice")
        return


def delete_goal(goals,current_user):
    print(f"\nAll goals for {current_user}")
    x=1
    user_goals=[]
    for goal in goals:
        if goal.username.lower()==current_user.lower():
            print(f"{x}.", goal.display())
            user_goals.append(goal)
            x+=1
            

    if not user_goals:
        print("No Goals found")
        return
    
    choice=int(input("\nEnter goal number to delete"))

    if 1<=choice<=len(user_goals):
        goal_to_delete=user_goals[choice-1]
        goals.remove(goal_to_delete)
        print("Goal deleted successfully")
        save_all_goals(goals)
    else:
        print("Invalid choice")
        return


# Function for Report

def show_reports(tasks, expenses, goals, current_user):
    print("\n----- REPORTS -----")

    # TASK REPORT
    total_tasks = 0
    completed_tasks = 0
    pending_tasks = 0

    for task in tasks:
        if task.username.lower() == current_user.lower():
            total_tasks += 1
            if task.status.lower() == 'completed':
                completed_tasks += 1
            else:
                pending_tasks += 1

    print("\n--- Task Report ---")
    print("Total Tasks:", total_tasks)
    print("Completed Tasks:", completed_tasks)
    print("Pending Tasks:", pending_tasks)

    # EXPENSE REPORT
    total_expense_amount = 0

    for exp in expenses:
        if exp.username.lower() == current_user.lower():
            total_expense_amount += exp.amount

    print("\n--- Expense Report ---")
    print("Total Expense: Rs", total_expense_amount)

    # GOAL REPORT
    total_goals = 0
    completed_goals = 0
    active_goals = 0

    for goal in goals:
        if goal.username.lower() == current_user.lower():
            total_goals += 1
            if goal.status.lower() == 'completed':
                completed_goals += 1
            else:
                active_goals += 1

    print("\n--- Goal Report ---")
    print("Total Goals:", total_goals)
    print("Completed Goals:", completed_goals)
    print("Active Goals:", active_goals)


#main Menu
def main():
    expenses=load_expenses_file()
    tasks=load_tasks_file()
    users=load_user_file()
    goals=load_goals_file()
    current_user=None
    while True:
        if current_user is None:
            print("----- Personal Management System -----")
            print("\nPress '1' to login")
            print("Press '2' to Register")
            print("Press '3' to Exit\n")

            choice=int(input("\nEnter your choice\n"))
    
            match choice:
                case 1:
                    user=login_user(users)
                    if user:
                        current_user=user
                case 2:
                    register_user(users)
                case 3:
                    print("Good Bye!")
                    break
                case _:
                    print("\nInvalid Choice! Try again")
        else:
            print(f"\nWelcome {current_user.username}")
            print("\nPress '1' to view profile")
            print("Press '2' for Task Manager")
            print("Press '3' for Expense Manager")
            print("Press '4' for Goal Syatem")
            print("Press '5' for reports")
            print("Press '6' to log out")
            print("Press '7' to Exit\n")
            choice=int(input("\nEnter your choice"))

            if choice==1:
                current_user.display()
                if isinstance(current_user,PremiumUser):
                    current_user.premium_info()
            elif choice==2:
                while True:
                    print("\n----- Task Manager -----")
                    print("\nPress '1' to add task")
                    print("Press '2' to view task")
                    print("Press '3' to mark task as completed")
                    print("Press '4' to delete task")
                    print("Press '5' to view tasks by category")
                    print("Press '6' to Exit\n")
                    choice=int(input("\nEnter your choice\n"))

                    match choice:
                        case 1:
                            add_task(current_user.username)
                        case 2:
                            view_task(tasks,current_user.username)
                        case 3:
                            mark_task(tasks,current_user.username)
                        case 4:
                            delete_task(tasks,current_user.username)
                        case 5:
                            filter_task(tasks,current_user.username)
                        case 6:
                            break
                        case _:
                            print("\nInvalid choice! Try Again")
            elif choice==3:
                while True:
                    print("\n----- Expense Manager -----")
                    print("\nPress '1' to Add expense")
                    print("Press '2' to View all expense")
                    print("Press '3' to delete expense")
                    print("Press '4' to Calculate Total Expense")
                    print("Press '5' to Exit\n")

                    choice=int(input("Enter your choice"))

                    match choice:
                        case 1:
                            add_expense(current_user.username)
                        case 2:
                            view_expenses(expenses,current_user.username)
                        case 3:
                            delete_expense(expenses,current_user.username)
                        case 4:
                            total_expense(expenses,current_user.username)
                        case 5:
                            break
                        case _:
                            print("Invalid Choice! Try again")
            elif choice==4:
                while True:
                    print("\n----- Goal Manager -----")
                    print("\nPress '1' to add Goal")
                    print("Press '2' to view all goals")
                    print("Press '3' to add savings to goals")
                    print("Press '4' to delete goal")
                    print("Press '5' to Exit\n")

                    choice=int(input("\nEnter your choice"))

                    match choice:
                        case 1:
                            add_goal(current_user.username)
                        case 2:
                            view_goals(goals,current_user.username)
                        case 3:
                            add_saving(goals,current_user.username)
                        case 4:
                            delete_goal(goals,current_user.username)
                        case 5:
                            break
                        case _:
                            print("Invalid choice! Try again")
            elif choice==5:
                show_reports(tasks,expenses,goals,current_user.username)
            elif choice==6:
                print("Logged out")
                current_user=None
            elif choice==7:
                break
            else:
                print("Invalid choice")

if __name__=="__main__":
    main()