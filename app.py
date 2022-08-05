from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
import os


app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')

db = SQLAlchemy(app)
ma = Marshmallow(app)

CORS(app)

class Legends(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    real_name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    legend_class = db.Column(db.String, nullable=False)
    home_world = db.Column(db.String, nullable=False)
    tac_ability_name = db.Column(db.String, nullable=False)
    tac_ability_description = db.Column(db.String, nullable=False)
    passive_ability_name = db.Column(db.String, nullable=False)
    passive_ability_description = db.Column(db.String, nullable=False)
    ultimate = db.Column(db.String, nullable=False)
    ultimate_description = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    quote = db.Column(db.String, nullable=False)
    picture_url = db.Column(db.String, nullable=False)


    def __init__(self, name, real_name, age, legend_class, home_world, tac_ability_name, tac_ability_description, passive_ability_name, passive_ability_description,ultimate, ultimate_description, description, quote, picture_url):
        self.name = name
        self.real_name = real_name
        self.age = age
        self.legend_class = legend_class
        self.home_world = home_world
        self.tac_ability_name = tac_ability_name
        self.tac_ability_description = tac_ability_description
        self.passive_ability_name = passive_ability_name
        self.passive_ability_description = passive_ability_description
        self.ultimate = ultimate
        self.ultimate_description = ultimate_description
        self.description = description
        self.quote = quote
        self.picture_url = picture_url

class LegendSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "real_name", "age", "legend_class", "home_world", "tac_ability_name", "tac_ability_description", "passive_ability_name", "passive_ability_description", "ultimate", "ultimate_description", "description", "quote", "picture_url");
legend_schema = LegendSchema()
legends_schema = LegendSchema(many=True)

@app.route("/legend/add", methods=["POST"])
def add_legend():
    name = request.json.get("name")
    real_name = request.json.get("real_name")
    age = request.json.get("age")
    legend_class = request.json.get("legend_class")
    home_world = request.json.get("home_world")
    tac_ability_name = request.json.get("tac_ability_name")
    tac_ability_description = request.json.get("tac_ability_description")
    passive_ability_name = request.json.get("passive_ability_name")
    passive_ability_description = request.json.get("passive_ability_description")
    ultimate = request.json.get("ultimate")
    ultimate_description = request.json.get("ultimate_description")
    description = request.json.get("description")
    quote = request.json.get("quote")
    picture_url = request.json.get("picture_url")
 
    record = Legends(name, real_name, age, legend_class, home_world, tac_ability_name, tac_ability_description, passive_ability_name, passive_ability_description,ultimate, ultimate_description, description, quote, picture_url)
    db.session.add(record)
    db.session.commit()

    return jsonify(legend_schema.dump(record))

@app.route("/legend/get", methods=["GET"])
def get_all_legends():
    all_legends = Legends.query.all()
    return jsonify(legends_schema.dump(all_legends))

@app.route("/legend/<id>", methods=["GET"])
def get_legend(id):
    legend = Legends.query.get(id)
    return legend_schema.jsonify(legend)

@app.route("/legend/<id>", methods=["PUT"])
def legend_update(id):
    legend = Legends.query.get(id)
    name = request.json['name']
    real_name = request.json['real_name']
    age = request.json['age']
    legend_class = request.json['legend_class']
    home_world = request.json['home_world']
    tac_ability_name = request.json['tac_ability_name']
    tac_ability_description = request.json['tac_ability_description']
    passive_ability_name = request.json['passive_ability_name']
    passive_ability_description = request.json['passive_ability_description']
    ultimate = request.json['ultimate']
    ultimate_description = request.json['ultimate_description']
    description = request.json['description']
    quote = request.json['quote']
    picture_url = request.json['picture_url']

    legend.name = name
    legend.real_name = real_name
    legend.age = age
    legend.legend_class = legend_class
    legend.home_world = home_world
    legend.tac_ability_name = tac_ability_name
    legend.tac_ability_description = tac_ability_description
    legend.passive_ability_name = passive_ability_name
    legend.passive_ability_description = passive_ability_description
    legend.ultimate = ultimate
    legend.ultimate_description = ultimate_description
    legend.description = description
    legend.quote = quote
    picture_url = picture_url

    db.session.commit()
    return legend_schema.jsonify(legend) 


@app.route("/legend/<id>", methods=["DELETE"])
def legend_delete(id):
    legend = Legends.query.get(id)
    db.session.delete(legend)
    db.session.commit()

    return "Legend was successfully deleted"

if __name__ == "__main__":
    app.run(debug=True)