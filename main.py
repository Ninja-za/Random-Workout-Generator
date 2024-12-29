from flask import Flask, render_template, jsonify
import random
import json

app = Flask(__name__)

# Load exercises from JSON file
def load_exercises():
    with open('exercises.json', 'r') as f:
        data = json.load(f)
    return data['legs'], data['arms'], data['core']

# Load exercises when the app starts
legs, arms, core = load_exercises()

def ran(num1, num2, num3):
    leg_exercise = random.choice(num1)
    arm_exercise = random.choice(num2)
    core_exercise = random.choice(num3)
    return core_exercise, arm_exercise, leg_exercise

@app.route("/", methods=["GET"])
def home():
    exercises = ran(legs, arms, core)
    return render_template("index.html", exercises=exercises)

@app.route("/create_workout", methods=["GET"])
def create_workout():
    core_exercise, arm_exercise, leg_exercise = ran(legs, arms, core)
    return jsonify({
        'core': core_exercise,
        'arm': arm_exercise,
        'leg': leg_exercise
    })

if __name__ == "__main__":
    app.run(debug=True)
