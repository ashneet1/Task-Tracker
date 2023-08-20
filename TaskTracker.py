from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

habits = []


@app.route('/', methods=['GET', 'POST'])
def index():
    
    if request.method == 'POST':
        habit = request.form.get('habit')
        importance = request.form.get('importance')
        if habit:
            habits.append({'name': habit, 'completed': False, 'importance': importance})
    completion_percentage = calculateHabitPercentage(habits)   
    return render_template('index.html', habits=habits , completion_percentage = completion_percentage)

@app.route('/complete/<int:habit_index>')
def complete_habit(habit_index):
    if 0 <= habit_index < len(habits):
        habits[habit_index]['completed'] = not (habits[habit_index]['completed'])
        completion_percentage = calculateHabitPercentage(habits)
        render_template('index.html', habits=habits, completion_percentage=completion_percentage)
    return redirect(url_for('index'))

def calculateHabitPercentage(habits):
    total_habits = len(habits)
    completed_habits = sum(1 for habit in habits if habit['completed'])
    if total_habits > 0: 
        completion_percentage = int((completed_habits / total_habits) * 100)
    else: completion_percentage = 0
    return completion_percentage

if __name__ == '__main__':
    app.run()


