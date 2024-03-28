class Task:
    def __init__(self, description, priority, deadline):
        self.__description = description
        self.__priority = priority
        self.__deadline = deadline

    def set_description(self, description):
        self.__description = description

    def get_description(self):
        return self.description

    def set_priority(self, priority):
        self.__priority = priority

    def get_priority(self):
        return self.priority

    def set_deadline(self, deadline):
        self.__deadline = deadline

    def get_deadline(self):
        return self.__deadline

    def __str__(self):
        return (Description: {self.__description}, Priority: {self.__priority}, Deadline: {self.__deadline})


class PriorityQueue:
    def __init__(self):
        self.__tasks = []

    def peek_task(self):
        if self.tasks:
            return self.__tasks[0]
        else:
            return None

    def get_tasks(self):
        return self.__tasks


class Scheduler:
    def __init__(self):
        self.__queue = PriorityQueue()

    def reorder_task(self, task, new_priority, new_deadline):
        tasks = self.__queue.get_tasks()
        for t in tasks:
            if t == task:
                t.set_priority(new_priority)
                t.set_deadline(new_deadline)
                tasks.remove(t)
                self.__queue.add_task(t)
                break

    def execute_task(self):
        task = self.__queue.remove_task()
        if task:
            print("Executing task:", task)
        else:
            print("No tasks to execute")

    def display_tasks(self):
        tasks = self.__queue.get_tasks()
        if tasks:
            print("Current tasks:")
            for task in tasks:
                print(task)
        else:
            print("No tasks")


if __name__ == '__main__':
    scheduler = Scheduler()

    scheduler.add_task(task1)
scheduler.add_task(task2)
scheduler.add_task(task3)

scheduler.display_tasks()

scheduler.execute_task()

scheduler.display_tasks()

scheduler.reorder_task(task3, 4, "10th May 2023")

scheduler.display_tasks()

while True:
    task = scheduler.remove_task()
    if task:
        scheduler.execute_task()
    else: