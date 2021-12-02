from flask import *

# i used it just for simple captcha system  + save ids on your host!

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route('/python-host/', methods=['GET'])
def thehostpythonbotpage():

    id = str(request.args.get('id'))

    with open('../public_html/botdata/data.txt', 'a') as the_bin_file:
        the_bin_file.writelines(f'{id}\n')

    data = {'stats': 'Done! you have been added to the bot database'}
    return data


if __name__ == "__main__":
    app.run()