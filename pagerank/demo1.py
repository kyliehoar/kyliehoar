from flask import Flask, send_from_directory
from jinja2 import Template,Environment,FileSystemLoader
import pandas as pd

app= Flask(__name__,static_folder="static") # create an app for the website
file_loader = FileSystemLoader('.')
env = Environment(loader=file_loader)
t = env.get_template('index.html')
d = pd.read_csv('data_R1.csv')


@app.route("/")
def result():
    return t.render(data=d)
    

if __name__ == "__main__":
    app.run()
