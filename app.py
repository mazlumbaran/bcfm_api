from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/whoami/<string:firstname>")
def bcfm_api(firstname:str):
    #firstname=request.args.get("firstname")
    return jsonify(data=firstname), 200

if __name__=="__main__":
    app.run()