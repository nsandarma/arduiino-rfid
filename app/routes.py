from app import app,render_template,request,db,Data_card,login,login_required,login_user,logout_user,redirect,session,cek_card,open_portal

@login.user_loader
def load_user(user_id):
    return Data_card.query.get(int(user_id))

@app.route('/',methods=['GET','POST'])
@login_required
def home():
    q = session.get('key')
    data = Data_card.query.filter_by(id_card=q).first()
    return render_template('dashboard.html',data=data.nim)


@app.route('/login',methods=['GET','POST'])
def login():
    session.clear()
    if request.method == 'POST':
        try :
            get = cek_card()
            if get == 'alat error':
                return "alat tidak terkoneksi"
            else:
                data = Data_card.query.filter_by(id_card=get).first()
                login_user(data)
                session['key'] = get
                return redirect('/')
                
        except Exception as e :
            session['key'] = get
            return redirect('/register')
            # return f'{e}'
    return render_template('index.html')
@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        id_card = session.get('key')
        nama = request.form['nama']
        nim = request.form['nim']
        email = request.form['email']
        password = request.form['password']

        if nama and nim and email and id_card and password:
            try:
                q = Data_card(nama=nama,id_card=id_card,nim=nim,email=email,password_portal=password)
                db.session.add(q)
                db.session.commit()
                session.clear()
                return redirect('/')
            except Exception as e:
                return f"error {e}"
    return render_template('Register.html')
@app.route('/portal/<nim>')
@login_required
def portal(nim):
    q = Data_card.query.filter_by(nim=str(nim)).first()
    try:
        open_portal(q.nim,q.password_portal)
        return redirect('/')
    except Exception as e:
        return redirect('/')


@app.route('/logout')
def logout():
    logout_user()
    session.clear()
    return redirect('/')
 
@app.route('/delete/<int:nim>')
def delete(nim):
    q = Data_card.query.filter_by(nim=nim).first()
    db.session.delete(q)
    db.session.commit()
    logout_user()
    return redirect('/')



        


