from flask import Flask,request,render_template,flash,redirect,url_for,session
from form import simpleform
app=Flask(__name__)
app.secret_key = 'private_key'
#home page
@app.route('/')
def defaultHome():
    return render_template('home.html')

#registration form
@app.route('/registrationform', methods=['POST','GET'])
def registrationform():
    s= simpleform()
    if request.method== 'POST':
        a,c=0,0
        session['Gender']=request.form['Gender']
        session['Married']=request.form['Married']
        session['Education']=request.form['Education']
        session['self_employed']=request.form['self_employed']
        session['Credit_History']=request.form['Credit_History']
        session['Property_Area']=request.form['Property_Area']
        if session['Gender']=='Male': c+=1
        if session['Married']=='Yes': c+=1
        if session['Education']=='Graduate': c+=1
        if session['self_employed']=='No': c+=1
        if session['Credit_History']=='1': c+=1
        if session['Property_Area']=='Semi Urban': c+=1
        if s.validate()=='False':
            flash('Please fill out this field')
            return render_template('register.html')
        elif c>=4:
            a=c
            return render_template('register.html',a=a,form=s)
        else: return redirect(url_for('successform'))
    elif request.method== 'GET':
        return render_template('register.html',form=s)

@app.route('/successform')
def successform():
    Gender=session.get('Gender', None)
    return render_template('successform.html')

if __name__ == '__main__':
    app.run(debug=True)