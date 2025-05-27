const express = require('express');
const app = express();
const port = 3001;

app.get('/produtos', (req, res) => {
  res.json({
    produtos: [
      { id: 1, name: 'Notebook', price: 3000 },
      { id: 2, name: 'Mouse', price: 100 }
    ]
  });
});

app.listen(port, () => {
  console.log(`Produtos API running on port ${port}`);
});
