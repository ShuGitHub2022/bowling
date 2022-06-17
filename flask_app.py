from flask import Flask, request

from bowling import total_score

app = Flask(__name__)
app.config["DEBUG"] = True

inputs = []

@app.route("/", methods=["GET", "POST"])
def bowlingscore_page():
    errors = ""
    strikes=0
    if request.method == "POST":
        try:
            pin=int(request.form["number"])
            if pin>10 or pin<0 or (len(inputs)>0 and (len(inputs)-strikes)%2==1 and inputs[-1]!=10 and pin+inputs[-1]>10):
                raise ValueError
            else:
                if (len(inputs)-strikes)%2==0 and pin==10:
                    strikes+=1
                inputs.append(pin)
        except ValueError:
                errors+="<p>Error: Please input a valid number between 0-10 and the total number of your last two inputs should no more than 10.<p>"

        if request.form["action"] == "Calculate total score":
            result = total_score(inputs)
            inputs.clear()
            return '''
                <html>
                    <body>
                        <p>{result}</p>
                        <p><a href="/">Click here to calculate again</a>
                    </body>
                </html>
            '''.format(result=result)

    if len(inputs)>=21:
        errors+="You have input too many scores. Please try again!"
        numbers_so_far = ""
        inputs.clear()
    elif len(inputs) == 0:
        numbers_so_far = ""
    else:
        numbers_so_far = "<p>You have input {} throws so far:</p>".format(len(inputs))
        for number in inputs:
            numbers_so_far += "<p>{}</p>".format(number)

    return '''
        <html>
        <head>
            <title>Bowling Exercise</title>
        </head>
            <body>
            <h1>Welcome to Bowling Exercise. Enjoy!</h1>
                <p>A bowling game has 10 frames. Each frame you can have no more than 2 throws except the 10th frame.<br>
                The 10th frame <br>
                If you roll a strike in the first shot of the 10th frame, you get 2 more shots.<br>
                If you roll a spare in the first two shots of the 10th frame, you get 1 more shot.<br>
                If you leave the 10th frame open after two shots, the game is over and you do not get an additional shot.</p>
                {numbers_so_far}
                {errors}
                <p>Enter your score (0-10) by frame, one at a time.Please Do NOT enter more than 21 score:</p>
                <form method="post" action=".">
                    <p><input name="number" /></p>
                    <p><input type="submit" name="action" value="Add score" /></p>
                    <p><input type="submit" name="action" value="Calculate total score" /></p>
                </form>
            </body>
        </html>
    '''.format(numbers_so_far=numbers_so_far, errors=errors)
                
