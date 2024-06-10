import os
import json
from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Path to JSON file to store blog content
JSON_FILE = "blog_content.json"

# Get credentials from environment variables
USERNAME = os.getenv('USERNAME', 'admin')
PASSWORD = os.getenv('PASSWORD', 'password')

# Load existing blog content from JSON file
try:
    with open(JSON_FILE, 'r') as f:
        blog_content = json.load(f)
except FileNotFoundError:
    blog_content = []

@app.route('/')
def index():
    return render_template('index.html', blog_content=blog_content)

@app.route('/add', methods=['GET', 'POST'])
def add_content():
    if request.method == 'POST':
        if request.form['username'] == USERNAME and request.form['password'] == PASSWORD:
            title = request.form['title']
            tags = request.form['tags']
            description = request.form['description']
            content = request.form['content']
            
            new_blog = {
                'title': title,
                'tags': tags,
                'description': description,
                'content': content
            }
            
            blog_content.append(new_blog)
            
            # Save updated blog content to JSON file
            with open(JSON_FILE, 'w') as f:
                json.dump(blog_content, f, indent=4)
                
            return redirect(url_for('index'))
        else:
            return "Invalid credentials. Please try again."
    return render_template('add_content.html')

# Add other routes here...

if __name__ == '__main__':
    app.run(debug=True)
