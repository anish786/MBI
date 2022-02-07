import json
import random
import string
from flask import Flask

#Instance of a class
app = Flask(__name__)

#endpoint /
@app.route('/')
def index():
    return "<h1>Welcome to MBI API !!</h1>"

#endpoint /generate
@app.route('/generate')
def generate():
    chars_allowed = 'ACDEFGHJKMNPQRTUVWXY' #only allowed characters
    mbi_number = [] #array to store the generated MBI
    mbi_number.append(random.randrange(1,10)) #appending first MBI digit between 1-9
    for i in range(0,11):
        #Make sure 2,5,8 and 9 characters are from chars_allowed
        if i == 1 or i == 4 or i == 7 or i == 8:
            mbi_number.append(random.choice(chars_allowed))
        #Make sure 3 and 6 are alpha numberic from chars_allowed or 0-9
        elif i == 2 or i == 5:
            mbi_number.append(random.choice(chars_allowed + string.digits))
        #Make sure 4,7,10 and 11 digits are digits 0-9
        elif i == 3 or i == 6 or i == 9 or i == 10:
            mbi_number.append(random.randrange(10))
    return {"mbinumber": mbi_number}

#end point /verify/<mbinumber>
@app.route('/verify/<string:mbi>')
def verify(mbi: str):
    chars_allowed = 'ACDEFGHJKMNPQRTUVWXY'
    if len(mbi) == 11: #Check if length is 11
        #check if first digit is not 0 and its a number from 1 to 9
        if mbi[0] != 0 and int(mbi[0]) > 0 and int(mbi[0]) < 10:
            #check if 2,5,8 and 9 characters exists in chars_allowed
            if mbi[1] in chars_allowed and mbi[4] in chars_allowed and mbi[7] in chars_allowed and mbi[8] in chars_allowed:
                #check if 3 and 6 are in chars_allowed or its a number between 0-9
                if mbi[2] in (chars_allowed + string.digits) and mbi[5] in (chars_allowed + string.digits):
                    #check if 4,7,10 and 11 are digits from 0-9
                    if mbi[3] in string.digits and mbi[6] in string.digits and mbi[9] in string.digits and mbi[10] in string.digits:
                        return json.dumps(True)
    return json.dumps(False)

if __name__ == "__main__":
    app.run(debug=True)