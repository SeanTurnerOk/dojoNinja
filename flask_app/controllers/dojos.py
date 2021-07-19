from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


@app.route('/')
def mainPage():
    return redirect('/dojos')
@app.route('/dojos')
def dojoDisplay():
    dojos=Dojo.get_all()
    return render_template('dojoDisplay.html', dojos=dojos)
@app.route('/createDojo', methods=['POST'])
def createDojo():
    Dojo.insert(request.form['dojoName'])
    return redirect('dojos')
@app.route('/ninjas')
def ninjaCreation():
    dojos=Dojo.get_all()
    return render_template('ninjaCreate.html', dojos=dojos)
@app.route('/createNinja', methods=['POST'])
def createNinja():
    form=request.form
    Ninja.insert(form)
    return redirect('/dojos/'+form['dojoId'])
@app.route('/dojos/<int:x>')
def indivDojo(x):
    dojo=Dojo.getById(x)[0]
    ninjas=Ninja.getByDId(x)
    return render_template('indivDojo.html', dojo = dojo, ninjas=ninjas)
