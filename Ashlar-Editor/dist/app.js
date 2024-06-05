const compression = require('compression')
const express = require('express')
const app = express()
app.use(compression())


app.use(express.static('web-driver-admin'))

app.all('*', function (req, res) {
    res.status(200).sendFile(`/`, {root: 'web-driver-admin'});
});

app.listen(5300)

