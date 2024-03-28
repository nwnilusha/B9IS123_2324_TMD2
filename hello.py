from flask import Flask
app = Flask(__name__)
@app.route("/")#URL leading to method
def hello(): # Name of the method
 current_date = datetime.now().strftime("%Y-%m-%d")  # Get current date in YYYY-MM-DD format
  return f"Hello Nilusha, It is a beautiful day! {current_date}"  # Include current date in the response
if __name__ == "__main__":
 app.run(host='0.0.0.0', port='8080') # indent this line