from flask import Flask, render_template, request, redirect, url_for
import os
import datetime

app = Flask(__name__)

def get_today_filename():
    today = datetime.date.today()
    filename = f"{today.strftime('%Y-%m-%d')}_todo.txt"
    return filename

def add_task(task):
    filename = get_today_filename()
    with open(filename, 'a') as file:
        file.write(f"{task}\n")

def get_tasks():
    filename = get_today_filename()
    tasks = []
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            tasks = file.readlines()
    return tasks

def mark_task_as_done(task_number):
    filename = get_today_filename()
    tasks = get_tasks()
    if tasks and 1 <= task_number <= len(tasks):
        if "Выполнено" not in tasks[task_number - 1]:
            tasks[task_number - 1] = f"{tasks[task_number - 1].strip()} - Выполнено\n"
            with open(filename, 'w') as file:
                file.writelines(tasks)
            print(f"Задача {task_number} отмечена как выполненная.")
        else:
            print(f"Задача {task_number} уже отмечена как выполненная.")
    else:
        print("Некорректный номер задачи.")

@app.route('/')
def index():
    tasks = get_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    add_task(task)
    return redirect(url_for('index'))

@app.route('/done/<int:task_number>')
def done(task_number):
    mark_task_as_done(task_number)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)