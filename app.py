from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# This will store  data while the app is running
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
    
    full_schedule = fixed + flexible 
    return jsonify(full_schedule)

if __name__ == '__main__':
    app.run(debug=True)