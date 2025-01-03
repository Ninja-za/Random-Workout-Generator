from flask import Flask, render_template, jsonify
import random
import json

app = Flask(__name__)


legs = [
    "Goblet squat", "Racked squat", "Squat to press",
    "Single arm squat to press (thruster)", "Side lunge",
    "Lunge", "Deadlift", "Single arm dead lift"
]

arms = [
    "Push-ups", "Pike push-up", "Alternate side press-ups",
    "Press-up on kettlebell", "Press-up move kettlebell",
    "Press-up lift", "Clean", "Clean and press",
    "Single arm press", "Lying press", "Double press",
    "Swings", "Bent over row", "Single arm row",
    "Around the world", "Turkish get-up"
]

core = [
    "Side plank raises", "Plank", "Plank to press-up",
    "Sit-ups", "Russian twists", "Twist superman",
    "Hip raises", "Leg raises", "Lean on sofa and lift body",
    "Abdominal scissors"
]

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

