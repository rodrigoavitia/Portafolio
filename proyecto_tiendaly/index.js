
const express = require('express');
const session = require('express-session');
const bcrypt  = require('bcrypt');
const cors    = require('cors');
const db      = require('./bd/bd');

const app = express();
app.use(cors());
app.use(express.json());
app.use(express.static('public'));

app.use(session({
    secret: 'tiendaly_secret_2026',
    resave: false,
    saveUninitialized: false,
    cookie: { maxAge: 1000 * 60 * 60 }
}));

const requireAuth = (req, res, next) => {
    if (!req.session.usuario) return res.status(401).send();
    next();
};

// Autorización
app.post('/login', (req, res) => {
    const { email, password } = req.body;
    db.query('SELECT * FROM usuarios WHERE email = ?', [email], async (err, results) => {
        if (err || results.length === 0) return res.status(401).json({ error: 'Error' });
        const match = await bcrypt.compare(password, results[0].password);
        if (match) {
            req.session.usuario = { nombre: results[0].nombre };
            res.json({ nombre: results[0].nombre });
        } else res.status(401).json({ error: 'Error' });
    });
});

app.post('/register', requireAuth, async (req, res) => {
    const { nombre, email, password } = req.body;
    const hash = await bcrypt.hash(password, 10);
    db.query('INSERT INTO usuarios (nombre, email, password) VALUES (?, ?, ?)', [nombre, email, hash], () => {
        res.json({ ok: true });
    });
});

//Productos
app.get('/productos', requireAuth, (req, res) => {
    db.query('SELECT * FROM productos ORDER BY id DESC', (err, results) => res.json(results));
});

app.post('/productos', requireAuth, (req, res) => {
    const { nombre, cantidad, precio, categoria } = req.body;
    db.query('INSERT INTO productos (nombre, cantidad, precio, categoria) VALUES (?, ?, ?, ?)', [nombre, cantidad, precio, categoria], () => res.json({ ok: true }));
});

app.put('/productos/:id', requireAuth, (req, res) => {
    const { nombre, cantidad, precio, categoria } = req.body;
    db.query('UPDATE productos SET nombre=?, cantidad=?, precio=?, categoria=? WHERE id=?', 
    [nombre, cantidad, precio, categoria, req.params.id], () => res.json({ ok: true }));
});

app.delete('/productos/:id', requireAuth, (req, res) => {
    db.query('DELETE FROM productos WHERE id = ?', [req.params.id], () => res.json({ ok: true }));
});

app.get('/session', (req, res) => {
    if (req.session.usuario) res.json({ activa: true, nombre: req.session.usuario.nombre });
    else res.json({ activa: false });
});

app.get('/logout', (req, res) => {
    req.session.destroy(() => res.json({ ok: true }));
});

app.listen(3000, () => console.log('Tiendaly ejecutándose en http://localhost:3000'));
