from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql

app = Flask(__name__)
app.secret_key = 'ventorrillo_secret_2024'

def get_db():
    return pymysql.connect(
        host='192.168.1.214',
        user='web_user',
        password='web123',
        database='Ventorrillo_Canario',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=True
    )

# ─── INICIO ────────────────────────────────────────────────────────────────────
@app.route('/')
def index():
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT COUNT(*) as total FROM `Categorías`")
    categorias = cur.fetchone()['total']
    cur.execute("SELECT COUNT(*) as total FROM Platos")
    platos = cur.fetchone()['total']
    cur.execute("SELECT COUNT(*) as total FROM Mesas")
    mesas = cur.fetchone()['total']
    cur.execute("SELECT COUNT(*) as total FROM Pedidos")
    pedidos = cur.fetchone()['total']
    db.close()
    return render_template('index.html', categorias=categorias, platos=platos, mesas=mesas, pedidos=pedidos)

# ═══════════════════════════════════════════════════════════════════════════════
# CATEGORÍAS
# ═══════════════════════════════════════════════════════════════════════════════
@app.route('/categorias')
def categorias():
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM `Categorías`")
    datos = cur.fetchall()
    db.close()
    return render_template('categorias.html', categorias=datos)

@app.route('/categorias/nueva', methods=['GET', 'POST'])
def nueva_categoria():
    if request.method == 'POST':
        nombre = request.form['nombre']
        db = get_db()
        cur = db.cursor()
        cur.execute("INSERT INTO `Categorías` (Nombre) VALUES (%s)", (nombre,))
        db.close()
        flash('Categoría creada correctamente', 'success')
        return redirect(url_for('categorias'))
    return render_template('categoria_form.html', accion='Nueva', categoria=None)

@app.route('/categorias/editar/<int:id>', methods=['GET', 'POST'])
def editar_categoria(id):
    db = get_db()
    cur = db.cursor()
    if request.method == 'POST':
        nombre = request.form['nombre']
        cur.execute("UPDATE `Categorías` SET Nombre=%s WHERE `Id_categoría`=%s", (nombre, id))
        db.close()
        flash('Categoría actualizada correctamente', 'success')
        return redirect(url_for('categorias'))
    cur.execute("SELECT * FROM `Categorías` WHERE `Id_categoría`=%s", (id,))
    categoria = cur.fetchone()
    db.close()
    return render_template('categoria_form.html', accion='Editar', categoria=categoria)

@app.route('/categorias/eliminar/<int:id>')
def eliminar_categoria(id):
    db = get_db()
    cur = db.cursor()
    cur.execute("DELETE FROM `Categorías` WHERE `Id_categoría`=%s", (id,))
    db.close()
    flash('Categoría eliminada', 'warning')
    return redirect(url_for('categorias'))

# ═══════════════════════════════════════════════════════════════════════════════
# PLATOS
# ═══════════════════════════════════════════════════════════════════════════════
@app.route('/platos')
def platos():
    db = get_db()
    cur = db.cursor()
    cur.execute("""
        SELECT p.*, c.Nombre as categoria_nombre
        FROM Platos p
        LEFT JOIN `Categorías` c ON p.`Id_categoría` = c.`Id_categoría`
    """)
    datos = cur.fetchall()
    db.close()
    return render_template('platos.html', platos=datos)

@app.route('/platos/nuevo', methods=['GET', 'POST'])
def nuevo_plato():
    db = get_db()
    cur = db.cursor()
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = request.form['precio']
        id_categoria = request.form['id_categoria']
        cur.execute("INSERT INTO Platos (Nombre, Precio, `Id_categoría`) VALUES (%s, %s, %s)",
                    (nombre, precio, id_categoria))
        db.close()
        flash('Plato creado correctamente', 'success')
        return redirect(url_for('platos'))
    cur.execute("SELECT * FROM `Categorías`")
    categorias = cur.fetchall()
    db.close()
    return render_template('plato_form.html', accion='Nuevo', plato=None, categorias=categorias)

@app.route('/platos/editar/<int:id>', methods=['GET', 'POST'])
def editar_plato(id):
    db = get_db()
    cur = db.cursor()
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = request.form['precio']
        id_categoria = request.form['id_categoria']
        cur.execute("UPDATE Platos SET Nombre=%s, Precio=%s, `Id_categoría`=%s WHERE Id_plato=%s",
                    (nombre, precio, id_categoria, id))
        db.close()
        flash('Plato actualizado correctamente', 'success')
        return redirect(url_for('platos'))
    cur.execute("SELECT * FROM Platos WHERE Id_plato=%s", (id,))
    plato = cur.fetchone()
    cur.execute("SELECT * FROM `Categorías`")
    categorias = cur.fetchall()
    db.close()
    return render_template('plato_form.html', accion='Editar', plato=plato, categorias=categorias)

@app.route('/platos/eliminar/<int:id>')
def eliminar_plato(id):
    db = get_db()
    cur = db.cursor()
    cur.execute("DELETE FROM Platos WHERE Id_plato=%s", (id,))
    db.close()
    flash('Plato eliminado', 'warning')
    return redirect(url_for('platos'))

# ═══════════════════════════════════════════════════════════════════════════════
# MESAS
# ═══════════════════════════════════════════════════════════════════════════════
@app.route('/mesas')
def mesas():
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM Mesas")
    datos = cur.fetchall()
    db.close()
    return render_template('mesas.html', mesas=datos)

@app.route('/mesas/nueva', methods=['GET', 'POST'])
def nueva_mesa():
    if request.method == 'POST':
        numero = request.form['numero']
        capacidad = request.form['capacidad']
        db = get_db()
        cur = db.cursor()
        cur.execute("INSERT INTO Mesas (`Número_mesa`, Capacidad) VALUES (%s, %s)", (numero, capacidad))
        db.close()
        flash('Mesa creada correctamente', 'success')
        return redirect(url_for('mesas'))
    return render_template('mesa_form.html', accion='Nueva', mesa=None)

@app.route('/mesas/editar/<int:id>', methods=['GET', 'POST'])
def editar_mesa(id):
    db = get_db()
    cur = db.cursor()
    if request.method == 'POST':
        numero = request.form['numero']
        capacidad = request.form['capacidad']
        cur.execute("UPDATE Mesas SET `Número_mesa`=%s, Capacidad=%s WHERE Id_mesa=%s",
                    (numero, capacidad, id))
        db.close()
        flash('Mesa actualizada correctamente', 'success')
        return redirect(url_for('mesas'))
    cur.execute("SELECT * FROM Mesas WHERE Id_mesa=%s", (id,))
    mesa = cur.fetchone()
    db.close()
    return render_template('mesa_form.html', accion='Editar', mesa=mesa)

@app.route('/mesas/eliminar/<int:id>')
def eliminar_mesa(id):
    db = get_db()
    cur = db.cursor()
    cur.execute("DELETE FROM Mesas WHERE Id_mesa=%s", (id,))
    db.close()
    flash('Mesa eliminada', 'warning')
    return redirect(url_for('mesas'))

# ═══════════════════════════════════════════════════════════════════════════════
# PEDIDOS
# ═══════════════════════════════════════════════════════════════════════════════
@app.route('/pedidos')
def pedidos():
    db = get_db()
    cur = db.cursor()
    cur.execute("""
        SELECT p.*, m.`Número_mesa`
        FROM Pedidos p
        LEFT JOIN Mesas m ON p.Id_mesa = m.Id_mesa
        ORDER BY p.Id_pedido DESC
    """)
    datos = cur.fetchall()
    db.close()
    return render_template('pedidos.html', pedidos=datos)

@app.route('/pedidos/nuevo', methods=['GET', 'POST'])
def nuevo_pedido():
    db = get_db()
    cur = db.cursor()
    if request.method == 'POST':
        id_mesa = request.form['id_mesa']
        estado = request.form['estado']
        cur.execute("INSERT INTO Pedidos (Id_mesa, Estado) VALUES (%s, %s)", (id_mesa, estado))
        db.close()
        flash('Pedido creado correctamente', 'success')
        return redirect(url_for('pedidos'))
    cur.execute("SELECT * FROM Mesas")
    mesas = cur.fetchall()
    db.close()
    return render_template('pedido_form.html', accion='Nuevo', pedido=None, mesas=mesas)

@app.route('/pedidos/editar/<int:id>', methods=['GET', 'POST'])
def editar_pedido(id):
    db = get_db()
    cur = db.cursor()
    if request.method == 'POST':
        id_mesa = request.form['id_mesa']
        estado = request.form['estado']
        cur.execute("UPDATE Pedidos SET Id_mesa=%s, Estado=%s WHERE Id_pedido=%s",
                    (id_mesa, estado, id))
        db.close()
        flash('Pedido actualizado correctamente', 'success')
        return redirect(url_for('pedidos'))
    cur.execute("SELECT * FROM Pedidos WHERE Id_pedido=%s", (id,))
    pedido = cur.fetchone()
    cur.execute("SELECT * FROM Mesas")
    mesas = cur.fetchall()
    db.close()
    return render_template('pedido_form.html', accion='Editar', pedido=pedido, mesas=mesas)

@app.route('/pedidos/eliminar/<int:id>')
def eliminar_pedido(id):
    db = get_db()
    cur = db.cursor()
    cur.execute("DELETE FROM Pedidos WHERE Id_pedido=%s", (id,))
    db.close()
    flash('Pedido eliminado', 'warning')
    return redirect(url_for('pedidos'))

# ═══════════════════════════════════════════════════════════════════════════════
# DETALLE_PEDIDOS
# ═══════════════════════════════════════════════════════════════════════════════
@app.route('/detalles')
def detalles():
    db = get_db()
    cur = db.cursor()
    cur.execute("""
        SELECT dp.*, pl.Nombre as plato_nombre, pl.Precio as plato_precio
        FROM Detalle_Pedidos dp
        LEFT JOIN Platos pl ON dp.Id_plato = pl.Id_plato
        ORDER BY dp.Id_detalle DESC
    """)
    datos = cur.fetchall()
    db.close()
    return render_template('detalles.html', detalles=datos)

@app.route('/detalles/nuevo', methods=['GET', 'POST'])
def nuevo_detalle():
    db = get_db()
    cur = db.cursor()
    if request.method == 'POST':
        id_pedido = request.form['id_pedido']
        id_plato = request.form['id_plato']
        cantidad = request.form['cantidad']
        cur.execute("INSERT INTO Detalle_Pedidos (Id_pedido, Id_plato, Cantidad) VALUES (%s, %s, %s)",
                    (id_pedido, id_plato, cantidad))
        db.close()
        flash('Detalle añadido correctamente', 'success')
        return redirect(url_for('detalles'))
    cur.execute("SELECT * FROM Pedidos ORDER BY Id_pedido DESC")
    pedidos = cur.fetchall()
    cur.execute("SELECT * FROM Platos")
    platos = cur.fetchall()
    db.close()
    return render_template('detalle_form.html', accion='Nuevo', detalle=None, pedidos=pedidos, platos=platos)

@app.route('/detalles/editar/<int:id>', methods=['GET', 'POST'])
def editar_detalle(id):
    db = get_db()
    cur = db.cursor()
    if request.method == 'POST':
        id_pedido = request.form['id_pedido']
        id_plato = request.form['id_plato']
        cantidad = request.form['cantidad']
        cur.execute("UPDATE Detalle_Pedidos SET Id_pedido=%s, Id_plato=%s, Cantidad=%s WHERE Id_detalle=%s",
                    (id_pedido, id_plato, cantidad, id))
        db.close()
        flash('Detalle actualizado correctamente', 'success')
        return redirect(url_for('detalles'))
    cur.execute("SELECT * FROM Detalle_Pedidos WHERE Id_detalle=%s", (id,))
    detalle = cur.fetchone()
    cur.execute("SELECT * FROM Pedidos ORDER BY Id_pedido DESC")
    pedidos = cur.fetchall()
    cur.execute("SELECT * FROM Platos")
    platos = cur.fetchall()
    db.close()
    return render_template('detalle_form.html', accion='Editar', detalle=detalle, pedidos=pedidos, platos=platos)

@app.route('/detalles/eliminar/<int:id>')
def eliminar_detalle(id):
    db = get_db()
    cur = db.cursor()
    cur.execute("DELETE FROM Detalle_Pedidos WHERE Id_detalle=%s", (id,))
    db.close()
    flash('Detalle eliminado', 'warning')
    return redirect(url_for('detalles'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False)
