from flask import Flask

app = Flask(__name__)

print("Sales Followup - Jabcross")
print("This project is ready for development.")

@app.route("/")
def HelloWorld():
   return "Hello, World again!"

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000, debug=True)