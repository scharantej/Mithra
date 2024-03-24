
# main.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('landing_page.html')

@app.route('/donate')
def donate():
    # Handle donation logic here
    return redirect(url_for('success'))

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/contact', methods=['POST'])
def contact():
    # Handle contact form submission here
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

### HTML Files

**landing_page.html:**
html
<!DOCTYPE html>
<html>
<head>
  <title>Mental Health Donation Campaign</title>
</head>
<body>
  <h1>Support Mental Health Today</h1>
  <p>Your donation will help provide critical mental health services to those in need.</p>
  <form action="/donate" method="POST">
    <input type="text" name="amount" placeholder="Amount">
    <input type="submit" value="Donate">
  </form>
  <p>Contact us at <a href="/contact">contact@example.com</a></p>
</body>
</html>


**success.html:**
html
<!DOCTYPE html>
<html>
<head>
  <title>Thank You for Your Donation</title>
</head>
<body>
  <h1>Thank you for your generous donation!</h1>
  <p>Your donation will make a real difference in the lives of those struggling with mental health issues.</p>
</body>
</html>
