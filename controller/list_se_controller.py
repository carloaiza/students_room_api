from flask import Blueprint, Response,json, request
from service.list_se_service import ListSeService
from util.util import MyEncoder

app_listse = Blueprint("app_listse",__name__)
listse_service = ListSeService()

@app_listse.route("/listse/all")
def get_all_linked():
    return Response(status=200,
                    response=json.dumps(listse_service.get_all_linked(),cls=MyEncoder),
                    mimetype="application/json")


@app_listse.route("/listse/invert")
def invert_list():
    return Response(status=200,
                    response=json.dumps(listse_service.invert()),
                    mimetype="application/json")

@app_listse.route("/listse",methods=["POST"])
def create_pet():
    return Response(status=200,
                    response=json.dumps(listse_service.add(request.json)),
                    mimetype="application/json")

@app_listse.route("/listse/tostart",methods=["POST"])
def create_pet_to_start():
    return Response(status=200,
                    response=json.dumps(listse_service.add_to_start(request.json)),
                    mimetype="application/json")

@app_listse.route("/listse/toposition/<position>",methods=["POST"])
def create_pet_to_position(position):
    return Response(status=200,
                    response=json.dumps(listse_service.add_to_position(int(position),request.json)),
                    mimetype="application/json")