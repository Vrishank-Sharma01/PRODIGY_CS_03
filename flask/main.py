from flask import Flask, render_template, request
import re

app = Flask(__name__)

def assess_password_strength(password):
    length_criteria = len(password) >= 8
    upper_criteria = re.search(r'[A-Z]', password) is not None
    lower_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'\d', password) is not None
    special_criteria = re.search(r'[\W_]', password) is not None

    strength = 0
    if length_criteria:
        strength += 1
    if upper_criteria:
        strength += 1
    if lower_criteria:
        strength += 1
    if digit_criteria:
        strength += 1
    if special_criteria:
        strength += 1

    return strength

def provide_feedback(strength):
    if strength == 5:
        return "Very strong password"
    elif strength == 4:
        return "Strong password"
    elif strength == 3:
        return "Moderate password"
    elif strength == 2:
        return "Weak password"
    else:
        return "Very weak password"

@app.route('/', methods=['GET', 'POST'])
def index():
    feedback = None
    if request.method == 'POST':
        password = request.form['password']
        strength = assess_password_strength(password)
        feedback = provide_feedback(strength)
    return render_template('index.html', feedback=feedback)

if __name__ == '__main__':
    app.run(debug=True)