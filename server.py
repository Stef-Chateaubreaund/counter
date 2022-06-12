from flask import Flask, request,redirect, url_for, session, render_template  # Import Flask to allow us to create our app and add the templates 
app = Flask(__name__) 
app.secret_key = 'counter' #used to hide data( but why where and how?!

@app.route('/')
def index():
    if 'views' not in session:
        session['views'] = 0
    else:
        session['views'] += 1
    return render_template("index.html")

@app.route('/addOne') 
def addOne():
    if 'views' not in session:
        session['views'] = 0# why plus zero to add 1?
    else: 
        session['views'] += 0
    return redirect('/')    

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

@app.route('/addTwo')#what does session means? #open a session once visiting the website, "youre on the website"
def addtwo():#also known as "cookies" wow 
    if 'views' not in session:
        session['views'] = 0
    else: 
        session['views'] += 1
    return redirect('/')

if __name__=="__main__":   # essa parte e obrigatoria em todas as pastas   
    app.run(debug=True)    