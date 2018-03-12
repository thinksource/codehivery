from flask import Blueprint, jsonify, request
from flask import current_app as app
import json

JSON_ERROR = {"error": "wrong format of json data received"}
NOTFINDPERSON = {
    "error": "can not find the person with the same data you input"}
JSON_NOPERSON = {
    "error": "can not find correct person with provided person's name"}
JSON_IDERROR = {
    "error": "the person id you input is out of the range of people.json's id"}
JSON_WRONGCOMP={"error": "wrong company name"}

def takeset(peoplelist):
    result = set()
    for i in peoplelist:
        result.add(i['index'])
    return result

def check_persondata(data):
    if('name' in data and 'age' in data and 'address' in data and 'phone' in data):
        if(data['age'] > 0):
            return True
        else:
            return False
    else:
        return False

api=Blueprint("api", __name__, url_prefix='/api')

@api.route("/",methods=['GET', 'POST'])
def hello():
    return "The service is working"

# Given 2 people, provide their information (Name, Age, Address, phone) and the list of their friends\
# in common which have brown eyes and are still alive.
@api.route("/common",  methods=['GET', 'POST'])
def getcommon():
    people = app.config["people"]
    if request.is_json:
        p_data = request.get_json()
        if(len(p_data) != 2):
            return jsonify(JSON_ERROR), 400
        if not (check_persondata(p_data[0]) and check_persondata(p_data[1])):
            return jsonify(JSON_ERROR), 400
        l = len(people)
        p1 = None
        p2 = None
        for i in range(l):
            if(people[i]['name'] == p_data[0]['name'] and people[i]['age'] == p_data[0]['age']
               and people[i]['address'] == p_data[0]['address'] and people[i]['phone'] == p_data[0]['phone']):
                p1 = people[i]
            if(people[i]['name'] == p_data[1]['name'] and people[i]['age'] == p_data[1]['age']
               and people[i]['address'] == p_data[1]['address'] and people[i]['phone'] == p_data[1]['phone']):
                p2 = people[i]
        if (p1 and p2):

            common_index = takeset(p1['friends']) & takeset(p2['friends'])
            result = []
            for i in range(l):
                if i in common_index:
                    if(people[i]["has_died"] == False and people[i]["eyeColor"] == "brown"):
                        result.append(people[i])
            return jsonify(result)
        else:
            return jsonify(NOTFINDPERSON), 400
    else:
        return jsonify(JSON_ERROR), 400


@api.route("/commonid/<strid1>/<strid2>")
def getidcommon(strid1, strid2):
    people = app.config["people"]
    l = len(people)
    id1 = int(strid1)
    id2 = int(strid2)
    if(id1 < l and id1 >= 0 and id2 < l and id2 >= 0):
        p1 = people[id1]
        p2 = people[id2]
        common_index = takeset(p1['friends']) & takeset(p2['friends'])
        result = []
        for i in range(l):
            if i in common_index:
                if(people[i]["has_died"] == False and people[i]["eyeColor"] == "brown"):
                    result.append(people[i]['name'])
        return jsonify(result)
    return jsonify(JSON_IDERROR), 400

# Given 1 people, provide a list of fruits and vegetables they like. This endpoint must respect this interface for the output:
# { "username": "Ahi", "age":"30", "fruits":["banana", "apple"], "vegetables":["beetroot", "lettuce"]}
@api.route("/user/<name>")
def person(name):
    fruits = set(['apple', 'orange', 'strawberry', 'banana'])
    vegetables = set(['celery', 'cucumber',  'carrot', 'beetroot'])
    people = app.config["people"]
    for i in people:
        if i['name'] == name:
            food = i["favouriteFood"]
            f = []
            v = []
            for j in food:
                if j in fruits:
                    f.append(j)
                elif j in vegetables:
                    v.append(j)
            return jsonify({'name': i['name'], 'age': i['age'],  "fruits": f, "vegetables": v})
    return jsonify(JSON_NOPERSON), 400


# Given a company, the API needs to return all their employees. Provide the appropriate solution if the company does not have any employees.
@api.route("/company/<name>")
def getcompany(name):
    people = app.config["people"]
    companies = app.config["companies"]
    index = -1
    l = len(companies)
    re = []
    for i in range(l):
        if(companies[i]['company'] == name):
            index = companies[i]['index']
            break
    if(index == -1):
        return jsonify(JSON_WRONGCOMP), 400
    else:
        for i in range(len(people)):
            if (people[i]['company_id'] == index):
                re.append(people[i])
        return jsonify(re)