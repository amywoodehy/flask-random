from whois import whois
from whois.parser import PywhoisError, datetime_parse
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def main():
    return jsonify({'status': 'error', 'data': 'not implemented'})

@app.route('/whois', methods=['GET'])
def whois_api_v01():
    domain = request.args.get('domain')
    response = {}
    try:
        w = whois(domain)
        response['status'] = 'success'
        response['data'] = w
        response['data']['text'] = w.text
        try:
            response['data']['expire_stamp'] = int(w['expiration_date'].strftime("%s"))
        except:
            pass #fuck it
    except PywhoisError as e:
        response['status'] = 'whois error'
        response['data'] = str(e)
    except Exception as e:
        response['status'] = 'error'
        response['data'] = str(e)

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)