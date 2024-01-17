from flask import Flask, request, render_template, redirect, url_for
import json
import subprocess

app = Flask(__name__)

from flask import Flask, request, render_template, redirect, url_for
import json
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")#,posts=posts)

@app.route('/forms', methods=['GET', 'POST'])
def forms():
    if request.method == 'POST':
        # Get form data
        name = request.form.get('name')
        email = request.form.get('email')

        # Create a dictionary with form data
        form_data = {
            'name': name,
            'email': email
        }

        # Save the form data as JSON
        with open('form_data.json', 'w') as json_file:
            json.dump(form_data, json_file)

        return redirect(url_for('forms'))

    return render_template('forms.html')

@app.route('/shell', methods=['GET', 'POST'])
def shell():
    if request.method == 'POST':
        # Get the shell command from the form
        shell_command = request.form.get('shell_command')

        try:
            # Execute the shell command and capture its output
            result = subprocess.run(shell_command, shell=True, capture_output=True, text=True)

            # Check if the command was successful
            if result.returncode == 0:
                output = result.stdout
            else:
                output = f"Error: {result.stderr}"

            return render_template('shell.html', output=output)

        except Exception as e:
            return f'Error executing shell command: {str(e)}'

    return render_template('shell.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
