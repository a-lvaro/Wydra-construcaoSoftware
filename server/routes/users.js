var express = require('express');
var router = express.Router();

// Cadastro de Usuários
router.post('/signup', (req, res) => {
    if (!req.body.username || !req.body.password) {
        res.status('400');
        res.send('Cadastro inválido');
    } else {
        // verificar se usuário já existe
        // cadastrar usuário no db
        res.send('do stuff here');
    }
});

// Login 
router.post('/login', (req, res) => {
    if (!req.body.username || !req.body.password) {
        res.status('400');
        res.send('Login inválido');
    } else {
        // autenticar o usuário
        res.send('wow such security');
    }
});
 
module.exports = router;
