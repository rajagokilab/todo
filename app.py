from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory task list (replace with DB in production)
tasks = []
task_id_counter = 1

@app.route('/')
def index():
    show_completed = request.args.get('completed')
    if show_completed == 'true':
        filtered_tasks = [task for task in tasks if task['completed']]
    else:
        filtered_tasks = tasks
    return render_template('index.html', tasks=filtered_tasks)

@app.route('/add', methods=['POST'])
def add_task():
    global task_id_counter
    task_text = request.form.get('task')
    if task_text:
        tasks.append({'id': task_id_counter, 'text': task_text, 'completed': False})
        task_id_counter += 1
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return redirect(url_for('index'))

# Optional: Toggle complete status (not required, but useful)
@app.route('/toggle/<int:task_id>')
def toggle_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = not task['completed']
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
