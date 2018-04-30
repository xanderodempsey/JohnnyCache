####################################################################################
# main.py                                                                          #
# Author:        Alexander O'Dempsey (xander-odempsey@hotmail.com)                 #
# Modified by:   Alexander O'Dempsey (xander-odempsey@hotmail.com)                 #
# Date Created:  29/04/2018                                                        #
# Last Modified: 30/04/2018                                                        #
# Brief:         Implementation of a simple online cache to store documents        #
####################################################################################

import os
from flask import Flask, render_template
from werkzeug.contrib.cache import SimpleCache
from document_store_form import DocumentStore

docs = SimpleCache()
app = Flask(__name__)
port = os.getenv('PORT', '5000')

app.config.update(dict(
    SECRET_KEY="New Secret Key",
    WTF_CSRF_SECRET_KEY="New CSRF Key"
))

@app.route('/')
@app.route('/index')
def index():
    storeDoc = DocumentStore()
    return render_template('store.html', storeDoc=storeDoc)

@app.route('/messages', methods=["POST"])
def store():
    '''
    Performs the storing of document, returns back to the storing page.
    '''
    sFlag = False
    storeDoc = DocumentStore()
    if storeDoc.validate_on_submit():
        data = docs.get(storeDoc.id.data)
        if data is None:
            sFlag = docs.set(str(storeDoc.id.data), storeDoc.message.data, timeout=int(storeDoc.ttl.data))
        return render_template('store.html', storeDoc=storeDoc, succsessfulStore=sFlag)

@app.route('/messages/<id>', methods=["GET"])
def view(id):
    '''
    Takes in the assigned message ID and returns the ID & message in the following format:
        id: <id>
        message: <message>
    '''
    data = docs.get(id)
    if data is not None:
        return render_template('view.html', id=id, text=data)
    return render_template('view.html')

@app.route('/clear')
def clear():
    cleared = docs.clear()
    return render_template('clear.html', succsess=cleared)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port)
