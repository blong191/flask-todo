from flask import Blueprint, render_template, request

from . import db


bp = Blueprint("todos", __name__)

@bp.route("/", methods=("GET", "POST"))
def index():
    """View for home page which shows list of to-do items."""
    conn = db.get_db()
    cur = conn.cursor()

    cur.execute('SELECT * FROM todos')
    print(request.form)
    if request.method == 'POST':
        #Put in additional tasks the user wants
        description = request.form.get('description')
        completed = request.form.get('completed')
        uncompleted = request.form.get('uncompleted')
        all = request.form.get('all')
        if description != None:
            #Add a new task
            cur.execute(
            'INSERT INTO todos (description, completed, created_at) VALUES (%s, FALSE, CURRENT_TIMESTAMP)',
            (description,)
            )
        #Make sure the new task is reconized by cur
        cur.execute('SELECT * FROM todos')
        if uncompleted != None or completed != None:
            #Checks for which submit was pushed
            if uncompleted != None:
                cur.execute('SELECT * FROM todos WHERE completed = FALSE')

            else:
                cur.execute('SELECT * FROM todos WHERE completed = TRUE')


    conn.commit()
    #if a button(submit) is pressed, show only certain tasks, completed, uncompleted, or all

    todos = cur.fetchall()
    cur.close()


    return render_template("index.html", todos=todos)

[1, 2]
(1,)
