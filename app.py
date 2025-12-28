from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# This will store our data while the app is running
all_tasks = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/save-task', methods=['POST'])
def save_task():
    task = request.json
    all_tasks.append(task)
    return jsonify({"status": "success", "message": "Task added!"})

@app.route('/get-schedule')
def get_schedule():
    # 1. Separate Fixed and Flexible
    fixed = sorted([t for t in all_tasks if t['type'] == 'fixed'], key=lambda x: x['time'])
    flexible = [t for t in all_tasks if t['type'] == 'flexible']
    
    # 2. For now, let's just return them sorted to see the result
    # In the next step, we will write the logic to "interweave" them
    full_schedule = fixed + flexible 
    return jsonify(full_schedule)

if __name__ == '__main__':
    app.run(debug=True)