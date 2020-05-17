from app import *
from flask import render_template, url_for, redirect, session, request
@app.route('/', methods=['GET'])
def index():
    if 'list' not in session:
        session['list'] = []

    return render_template('index.html', items=session['list'])

@app.route('/add-new-item', methods=['POST'])
def update_list():
    current_list = session['list']
    current_list.append(request.form.get('listitem'))
    session['list'] = current_list
    return redirect(url_for('index'))
    

@app.route('/delete/<listitem>', methods=['GET'])
def delete(listitem):
    current_list = session['list']
    current_list.remove(listitem)
    session['list'] = current_list

    
    return redirect(url_for('index'))