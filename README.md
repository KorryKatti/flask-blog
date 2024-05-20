# Simple Flask Blog

This is a simple blog application built using Flask, a lightweight web framework for Python.

## Features

- Add new blog posts with a title, tags, description, and content.
- View existing blog posts with a read more option.
- Edit existing blog posts with authentication.
- Basic password authentication (insecure, for demonstration purposes only).

## Prerequisites

Before running the application, make sure you have the following installed:

- Python 3.x
- Flask

## Getting Started

1. Clone this repository:

    ```bash
    git clone https://github.com/KorryKatti/flask-blog
    cd flask-blog
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:

    ```bash
    python app.py
    ```

4. Open your web browser and navigate to `http://127.0.0.1:5000/` to view the blog.

## Usage

- To add new content, click on the "Add New Content" link on the main page.
- To view existing content, click on the titles of blog posts.
- To edit existing content, click on the "Edit" link next to the blog post you want to edit. You will be prompted to enter a username and password (default credentials are provided in the code).


## Note

- This application uses basic password authentication for demonstration purposes only. It is not secure and should not be used in a production environment without proper security measures.
- Feel free to customize the application and improve its functionality according to your needs.

