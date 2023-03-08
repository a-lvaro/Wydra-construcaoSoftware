const mysql = require('mysql');
const debug = require('debug')('wydra:db')

const connection = mysql.createConnection({
    host: 'localhost',
    user: 'wydra',
    password: 'wydra',
    database: 'WYDRA'
});

connection.connect((err) => {
    if (err) {
        throw err;
    } else {
        debug('Conexão ao banco de dados efetuada com sucesso!');
    }
});

module.exports = connection;
