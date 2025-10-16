from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

# Sample courses database (expand or connect to a real DB)
courses = {
    "technology": ["Full Stack Web Development", "AI & Machine Learning", "Cybersecurity"],
    "design": ["UI/UX Design", "Graphic Design Basics", "Motion Graphics"],
    "business": ["Digital Marketing", "Business Analytics", "Entrepreneurship"],
    "science": ["Physics Research Internship", "Biotechnology", "Data Science"],
    "arts": ["Creative Writing", "Fine Arts", "Photography"]
}

# Sample logic to predict based on answers
def evaluate_test(answers):
    # Basic interest evaluation using the form answers
    # For demonstration purposes, we'll use a simple weighted logic
    interest_area = answers.get("interest", "technology")
    math_interest = answers.get("math_interest", "medium")
    science_interest = answers.get("science_interest", "medium")
    arts_interest = answers.get("arts_interest", "medium")
    design_interest = answers.get("design_interest", "medium")
    business_interest = answers.get("business_interest", "medium")

    # Decide subject based on highest interest (this is a simplified logic)
    interests = {
        "technology": 0,
        "design": 0,
        "business": 0,
        "science": 0,
        "arts": 0
    }

    # Increase weights based on responses
    # Here we assign numeric values (high=3, medium=2, low=1)
    def score(response):
        if response.lower() == "high":
            return 3
        elif response.lower() == "low":
            return 1
        else:
            return 2

    interests["science"] += score(science_interest)
    interests["arts"] += score(arts_interest)
    interests["design"] += score(design_interest)
    interests["business"] += score(business_interest)
    # Also consider the default interest selection from the dropdown
    interests[interest_area] += 2

    # Determine which area has the highest score
    recommended_area = max(interests, key=interests.get)
    
    # Choose a course from the recommended area randomly
    recommended_course = random.choice(courses.get(recommended_area, ["General Career Development"]))
    return recommended_course

@app.route('/')
def home():
    return render_template('test_form.html')

@app.route('/submit', methods=['POST'])
def submit():
    user_answers = request.form.to_dict()
    recommended_course = evaluate_test(user_answers)
    return render_template('result.html', course=recommended_course)

if __name__ == '__main__':
    app.run(debug=True)
