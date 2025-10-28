from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# Data notes (in-memory storage)
notes = []

# Template HTML untuk Notes App
TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Notes</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #f5f5f5; }
        .header { background-color: #ffd966; padding: 15px; border-bottom: 1px solid #ddd; }
        .header h2 { margin: 0; }
        .note-item { background-color: white; margin: 10px; padding: 15px; border-radius: 5px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); position: relative; }
        .note-title { font-weight: bold; margin-bottom: 5px; }
        .add-btn { position: fixed; bottom: 20px; right: 20px; width: 50px; height: 50px; background-color: #ffd966; border-radius: 50%; border: none; font-size: 30px; cursor: pointer; }
        .form-container { margin: 20px; }
        input[type="text"] { width: 100%; padding: 10px; margin: 5px 0; border: 1px solid #ddd; border-radius: 5px; }
        button[type="submit"] { background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer; }
    </style>
</head>
<body>
    <div class="header">
        <h2>Notes</h2>
    </div>
    
    {% if show_form %}
    <div class="form-container">
        <form method="POST" action="/add">
            <input type="text" name="title" placeholder="Note Title" required>
            <button type="submit">Add Note</button>
        </form>
    </div>
    {% endif %}
    
    {% for note in notes %}
    <div class="note-item">
        <div class="note-title">{{ note }}</div>
    </div>
    {% endfor %}
    
    {% if not show_form %}
    <form method="GET" action="/new">
        <button class="add-btn">+</button>
    </form>
    {% endif %}
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(TEMPLATE, notes=notes, show_form=False)

@app.route('/new')
def new_note():
    return render_template_string(TEMPLATE, notes=notes, show_form=True)

@app.route('/add', methods=['POST'])
def add_note():
    title = request.form.get('title')
    if title:
        notes.append(title)
    return redirect(url_for('index'))

@app.route('/health')
def health():
    return {"status": "healthy", "notes_count": len(notes)}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
