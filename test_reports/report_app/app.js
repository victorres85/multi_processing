const express = require('express');
const fs = require('fs');
const path = require('path');

const app = express();
const PORT = 3000;

app.set('view engine', 'ejs');
app.use(express.static('public'));

app.get('/', (req, res) => {
    fs.readdir(path.join(__dirname, '..', '..', 'test_reports'), (err, files) => {
        if (err) {
            return res.status(500).send('Unable to scan directory'+err);
        }
        const htmlFiles = files.filter(file => file.endsWith('.html'));
        res.render('index', { files: htmlFiles });
    });
});


app.get('/report/:filename', (req, res) => {
    const { filename } = req.params;
    const filePath = path.join(__dirname, '..', '..', 'test_reports', filename);
    res.sendFile(filePath);
});
app.use(express.static(path.join(__dirname, '..', 'assets')));

// Serve CSS files with the correct content type
app.get('/style.css', (req, res) => {
    res.sendFile(path.join(__dirname, '..', 'assets', 'style.css'), {
        headers: {
            'Content-Type': 'text/css'
        }
    });
});

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});