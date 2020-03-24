from app import *
from app.models import Todo

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_list_item = request.form.get('listitem')
        add_item_to_db = Todo(item=new_list_item)
        db.session.add(add_item_to_db)
        db.session.commit()

        return redirect(url_for('index'))

    if request.method == 'GET':
        fetch_all_items = Todo.query.all()
       
        return render_template('index.html', items=fetch_all_items)

        
    return render_template('index.html')

@app.route('/delete/<itemID>', methods=['GET'])
def delete(itemID):
    if itemID == 'all':
        db.session.query(Todo).delete()
        db.session.commit()
        
        return redirect(url_for('index'))


    check_itemID_is_valid = Todo.query.filter_by(id=itemID).first()
    db.session.delete(check_itemID_is_valid)
    db.session.commit()
    
    return redirect(url_for('index'))
