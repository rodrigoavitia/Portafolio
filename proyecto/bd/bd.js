// const mysql = require('mysql2');

// const db = mysql.createConnection({
//     host: 'localhost',
//     user: 'root',
//     password: '', 
//     database: 'tienda' 
// });

// db.connect(err => {
//     if (err) {
//         console.error('Error de conexión a la base de datos:', err);
//         return;
//     }
//     console.log('Conectado a la base de datos');
// });


// module.exports = db;

// ============================================================
//  bd.js - Conexión a la base de datos MySQL
//  Exporta el objeto `db` para usarlo en todo el proyecto
// ============================================================

const mysql = require('mysql2');

// Configuración de la conexión
const db = mysql.createConnection({
    host:     'localhost', // Servidor de la base de datos
    user:     'root',      // Usuario de MySQL
    password: '',          // Contraseña (vacía en XAMPP por defecto)
    database: 'tienda'     // Nombre de la base de datos
});

// Intentamos conectar y mostramos resultado en consola
db.connect(err => {
    if (err) {
        console.error(' Error al conectar con la base de datos:', err.message);
        return;
    }
    console.log(' Conectado a la base de datos');
});

// Exportamos la conexión para usar en index.js
module.exports = db;
