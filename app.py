from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# 1. Input Page (Your start page)
@app.route('/')
def input_page():
    return render_template('input.html')

# 2. Loading Page
@app.route('/loading')
def loading_page():
    return render_template('loading.html')

# 3. Overview Page
@app.route('/overview')
def overview_page():
    return render_template('overview.html')

# 4. Insights Page
@app.route('/insights')
def insights_page():
    return render_template('insights.html')

# 5. Actions Page
@app.route('/actions')
def actions_page():
    return render_template('actions.html')

# 6. Report Page
@app.route('/report')
def report_page():
    return render_template('report.html')

if __name__ == '__main__':
    app.run(debug=True)