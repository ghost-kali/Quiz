from flask import Flask ,jsonify,render_template,request
from flask_cors import CORS
from main import get_ticket_response_pydantic

query = """
Provide me 5 Questions on Python based on beginner Level Understanding
"""

# --------------------------------------------------------------
# Providing a JSON Schema
# --------------------------------------------------------------




app = Flask( __name__) 
CORS(app)
#@app.get("/")
#def index_get():
 #   return render_template("base.html")

@app.get("/predict")
def predict():
    
    message = get_ticket_response_pydantic(query=query)


    return message


if   __name__ == "__main__" : 
    #predict()
    app.run(debug=True)
  
