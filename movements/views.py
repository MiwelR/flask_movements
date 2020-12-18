from movements import app
from flask import render_template, request, url_for, redirect
from movements import forms
from movements.dataaccess import *


@app.route('/')
def listaIngresos():
    form = forms.MiForm()

    ingresos = consulta('SELECT fecha, concepto, cantidad, id FROM movimientos;')

    total = 0
    for ingreso in ingresos:
        total += float(ingreso['cantidad'])

    return render_template('movementsList.html', datos=ingresos, total=total, form=form)

@app.route('/creaalta', methods=['GET', 'POST'])
def nuevoIngreso():
    form = forms.MiForm()
    fecha = form.fecha.data
    concepto = form.concepto.data
    cantidad = form.cantidad.data

    if request.method == 'POST':
        if form.validate():
            consulta('INSERT INTO movimientos (cantidad, concepto, fecha) VALUES (?, ? ,? );', 
                    (float(cantidad), concepto, fecha))
            return redirect(url_for('listaIngresos'))

    return render_template("alta.html", form=form)

@app.route('/creagasto', methods=['GET', 'POST'])
def nuevoGasto():
    form = forms.MiForm()
    fecha = form.fecha.data
    concepto = form.concepto.data
    cantidad = form.cantidad.data

    if request.method == 'POST':
        if form.validate():
            consulta('INSERT INTO movimientos (cantidad, concepto, fecha) VALUES (?, ? ,? );', 
                    (float(-cantidad), concepto, fecha))
            return redirect(url_for('listaIngresos'))

    return render_template("gasto.html", form=form)

@app.route('/modifica/<id>', methods=['GET', 'POST'])
def modificaIngreso(id):
    form = forms.MiForm()
    fecha = form.fecha.data
    concepto = form.concepto.data
    cantidad = form.cantidad.data

    if request.method == 'GET':
        registro = consulta('SELECT fecha, concepto, cantidad, id FROM movimientos WHERE id=?;', (id,))[0]
        return render_template('modifica.html', form=form, registro=registro)

    elif request.method == 'POST':
        consulta('UPDATE movimientos SET fecha=?, concepto=?, cantidad=? WHERE id=?;', 
                (fecha, concepto, float(cantidad), id))
        return redirect(url_for('listaIngresos'))

@app.route('/elimina/<id>', methods=['GET', 'POST'])
def eliminaIngreso(id):
    form = forms.MiForm()

    if request.method == 'GET':
        registro = consulta('SELECT fecha, concepto, cantidad, id FROM movimientos WHERE id=?;', (id,))[0]
        return render_template('elimina.html', form=form, registro=registro)

    elif request.method == 'POST':
        consulta('DELETE FROM movimientos WHERE id=?;', (id,))
        return redirect(url_for('listaIngresos'))