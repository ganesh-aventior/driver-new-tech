const compression = require('compression')
const express = require('express')
const app = express()
app.use(compression())


app.use(express.static('WB-Driver'))

app.all('*', function (req, res) {
    res.status(200).sendFile(`/`, {root: 'WB-Driver'});
});

app.listen(5200)

