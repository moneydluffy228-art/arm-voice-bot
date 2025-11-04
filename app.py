from flask import Flask, request, Response
from twilio.twiml.voice_response import VoiceResponse
from datetime import datetime
import pytz

app = Flask(__name__)
TZ = pytz.timezone("Asia/Yerevan")

@app.route("/voice", methods=["POST"])
def voice():
    now = datetime.now(TZ)
    weekday = now.weekday()  # 0=Mon ... 6=Sun
    resp = VoiceResponse()

    if weekday in (5, 6):
        resp.say("Օպերատորը հանգստյան օրերին հասանելի չէ։ "
                 "Ձեր դիմումը կարող եմ գրանցել, և մասնագետը կզանգի երկուշաբթի։",
                 language="hy-AM", voice="woman")
        resp.hangup()
        return Response(str(resp), mimetype="text/xml")

    resp.say("Բարի օր։ Դուք զանգել եք Կիբերնետ։ Այս պահին սա փորձնական տարբերակ է։",
             language="hy-AM", voice="woman")
    resp.hangup()
    return Response(str(resp), mimetype="text/xml")

@app.route("/", methods=["GET"])
def health():
    return "OK", 200
