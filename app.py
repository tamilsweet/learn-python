from flask import Flask, request

app = Flask(__name__)

stores = [
    {
        "name": "My Store",
        "items": [
            {
                "name": "Chair",
                "price": 14.99
            }
        ]
    }
]


@app.get('/store')
def get_stores():
  return {"stores": stores}
