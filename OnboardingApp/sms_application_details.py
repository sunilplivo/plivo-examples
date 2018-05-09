import requests
from flask import Flask, Response, request, abort, make_response, jsonify
import plivo

app = Flask(__name__)

# auth_id = "MAZDVINGE4NWE5MGI2MM"
# auth_token = "ZjNjOWRhOWJhYmQ4ZDQ0MGM1YTdlZDMwMTBkNjRm"

@app.route("/get_application_details")
def hello():
    try:
        auth_id = request.headers.get('auth_id')
        auth_token = request.headers.get('auth_token')
        dst_number = request.args.get('dst')
        client = plivo.RestClient(auth_id=auth_id, auth_token=auth_token)
    except:
        return abort(make_response(jsonify(message="Please make sure you send auth_id " \
            "and auth_token as headers and dst as parameter"), 400))

    r = requests.get("https://api.plivo.com/v1/Account/MAZDVINGE4NWE5MGI2MM/Application/", headers={"Authorization":"Basic TUFaRFZJTkdFNE5XRTVNR0kyTU06WmpOak9XUmhPV0poWW1RNFpEUTBNR00xWVRkbFpETXdNVEJrTmpSbQ=="})
    apps = r.json()['objects']
    
    msg_text = 'Your Plivo Applications:\n'
    i = 1
    for app in apps:
        msg_text += str(i) + '. ' + app['app_name'] + '\n'
        i += 1

    message_created = client.messages.create(
        src='919740288161',
        dst=dst_number,
        text=msg_text
    )

    return Response(str(message_created), mimetype='text/plaintext')