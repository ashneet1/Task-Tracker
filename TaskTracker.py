from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

habits = [[],[],[]]


@app.route('/', methods=['GET', 'POST'])
def index():
    
    if request.method == 'POST':
        habit = request.form.get('habit')
        importance = request.form.get('importance')
        if habit:
            if importance == "box-red":
                habits[0].append({'name': habit, 'completed': False, 'importance': importance})
            elif importance == "box-yellow":
                habits[1].append({'name': habit, 'completed': False, 'importance': importance})
            else:
                habits[2].append({'name': habit, 'completed': False, 'importance': importance})
    completion_percentage = calculateHabitPercentage(habits)   
    return render_template('index.html', habits=habits , completion_percentage = completion_percentage)

@app.route('/complete/<int:list_index>/<int:habit_index>')
def complete_habit(list_index,habit_index):
    if 0 <= habit_index < len(habits):
        habits[list_index][habit_index]['completed'] = not (habits[list_index][habit_index]['completed'])
        completion_percentage = calculateHabitPercentage(habits)
        render_template('index.html', habits=habits, completion_percentage=completion_percentage)
    return redirect(url_for('index'))

def calculateHabitPercentage(habits):
    total_habits = len(habits[0]) + len(habits[1]) + len(habits[2])
    completed_habits = completed_habits = sum(1 for habit_list in habits for habit in habit_list if habit['completed'])
    if total_habits > 0: 
        completion_percentage = int((completed_habits / total_habits) * 100)
    else: completion_percentage = 0
    return completion_percentage

@app.route('/delete/<int:list_index>/<int:habit_index>')
def delete_habit(list_index,habit_index):
    if 0 <= habit_index < len(habits):
        del habits[list_index][habit_index]
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()


