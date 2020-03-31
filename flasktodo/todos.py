from flask import Blueprint, render_template, request

from . import db


bp = Blueprint("todos", __name__)

@bp.route("/", methods=("GET", "POST"))
def index():
    """View for home page which shows list of to-do items."""
    conn = db.get_db()
    cur = conn.cursor()

    if request.method == 'POST':
        #Put in additional tasks the user wants
        description = request.form['description']
        cur.execute(
        'INSERT INTO todos (description, completed, created_at) VALUES (%s, FALSE, CURRENT_TIMESTAMP)',
    (description,)
        )
        conn.commit()
    cur.execute('SELECT * FROM todos')
    todos = cur.fetchall()
    cur.close()


    return render_template("index.html", todos=todos)

[1, 2]
(1,)
