from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template('gpred.html')
    else:
     try:
        req_data = request.form  # Retrieves submitted form data
        print(req_data)
        values_list = [value for key, value in request.form.items()]
        t=values_list
        print(t)
        def check_grade(value):
            if value > 100:
                return "Unachievable"
            elif value < 0:
                return "Already Achieved"
            else:
                return round(value, 2)
        
        if values_list[0]=='python':
            q1,pe1,pe2,ga,grpa,bonus=int(values_list[1]),int(values_list[2]),int(values_list[3]),int(values_list[4]),int(values_list[5]),int(values_list[6])
            s=(90-(0.1*ga+0.1*grpa+0.1*q1+0.25*max(pe1,pe2)+0.15*min(pe1,pe2)))/0.4-bonus
            a=(80-(0.1*ga+0.1*grpa+0.1*q1+0.25*max(pe1,pe2)+0.15*min(pe1,pe2)))/0.4-bonus
            b=(70-(0.1*ga+0.1*grpa+0.1*q1+0.25*max(pe1,pe2)+0.15*min(pe1,pe2)))/0.4-bonus
            c=(60-(0.1*ga+0.1*grpa+0.1*q1+0.25*max(pe1,pe2)+0.15*min(pe1,pe2)))/0.4-bonus
            d=(50-(0.1*ga+0.1*grpa+0.1*q1+0.25*max(pe1,pe2)+0.15*min(pe1,pe2)))/0.4-bonus
            e=(40-(0.1*ga+0.1*grpa+0.1*q1+0.25*max(pe1,pe2)+0.15*min(pe1,pe2)))/0.4-bonus
            s = check_grade(s)
            a = check_grade(a)
            b = check_grade(b)
            c = check_grade(c)
            d = check_grade(d)
            e = check_grade(e)
            return render_template("gpredtable.html",s=s,a=a,b=b,c=c,d=d,e=e,req_data=req_data)
        elif values_list[0]=='dbms':
            q1,q2,pe1,ga,bonus=int(t[1]),int(t[2]),int(t[3]),int(t[4]),int(t[5])
            s=min((90-(0.1*ga+0.2*pe1+0.15*max(q1,q2)))/0.45,(90-(0.1*ga+0.2*pe1+0.1*q1+0.20*q2))/0.40)-bonus
            a=min((80-(0.1*ga+0.2*pe1+0.15*max(q1,q2)))/0.45,(80-(0.1*ga+0.2*pe1+0.1*q1+0.20*q2))/0.40)-bonus
            b=min((70-(0.1*ga+0.2*pe1+0.15*max(q1,q2)))/0.45,(90-(0.1*ga+0.2*pe1+0.1*q1+0.20*q2))/0.40)-bonus
            c=min((60-(0.1*ga+0.2*pe1+0.15*max(q1,q2)))/0.45,(80-(0.1*ga+0.2*pe1+0.1*q1+0.20*q2))/0.40)-bonus
            d=min((50-(0.1*ga+0.2*pe1+0.15*max(q1,q2)))/0.45,(90-(0.1*ga+0.2*pe1+0.1*q1+0.20*q2))/0.40)-bonus
            e=min((40-(0.1*ga+0.2*pe1+0.15*max(q1,q2)))/0.45,(80-(0.1*ga+0.2*pe1+0.1*q1+0.20*q2))/0.40)-bonus
            s = check_grade(s)
            a = check_grade(a)
            b = check_grade(b)
            c = check_grade(c)
            d = check_grade(d)
            e = check_grade(e)
            return render_template("gpredtable.html",s=s,a=a,b=b,c=c,d=d,e=e,req_data=req_data)
        elif values_list[0]=="pdsa":
            q1,q2,pe1,ga,bonus=int(t[1]),int(t[2]),int(t[3]),int(t[4]),int(t[5])
            score=(0.1*ga+0.2*pe1 +max(0.2*max(q1,q2),0.15*q1+0.15*q2))
            s=(90-score)/0.4-bonus
            a=(80-score)/0.4-bonus
            b=(70-score)/0.4-bonus
            c=(60-score)/0.4-bonus
            d=(50-score)/0.4-bonus
            e=(40-score)/0.4-bonus
            s = check_grade(s)
            a = check_grade(a)
            b = check_grade(b)
            c = check_grade(c)
            d = check_grade(d)
            e = check_grade(e)
            return render_template("gpredtable.html",s=s,a=a,b=b,c=c,d=d,e=e,req_data=req_data)
        elif values_list[0]=="mad1":
            q1,q2,ga,gla,bonus=int(t[1]),int(t[2]),int(t[3]),int(t[4]),int(t[5])
            s=min((90-(0.15*gla+0.05*ga+0.2*q1+0.25*q2))/0.35,(90-(0.15*gla+0.05*ga+0.3*max(q1,q2)))/0.4)
            a=min((80-(0.15*gla+0.05*ga+0.2*q1+0.25*q2))/0.35,(80-(0.15*gla+0.05*ga+0.3*max(q1,q2)))/0.4)
            b=min((70-(0.15*gla+0.05*ga+0.2*q1+0.25*q2))/0.35,(70-(0.15*gla+0.05*ga+0.3*max(q1,q2)))/0.4)
            c=min((60-(0.15*gla+0.05*ga+0.2*q1+0.25*q2))/0.35,(60-(0.15*gla+0.05*ga+0.3*max(q1,q2)))/0.4)
            d=min((50-(0.15*gla+0.05*ga+0.2*q1+0.25*q2))/0.35,(50-(0.15*gla+0.05*ga+0.3*max(q1,q2)))/0.4)
            e=min((40-(0.15*gla+0.05*ga+0.2*q1+0.25*q2))/0.35,(40-(0.15*gla+0.05*ga+0.3*max(q1,q2)))/0.4)
            s = check_grade(s)
            a = check_grade(a)
            b = check_grade(b)
            c = check_grade(c)
            d = check_grade(d)
            e = check_grade(e)
            return render_template("gpredtable.html",s=s,a=a,b=b,c=c,d=d,e=e,req_data=req_data)


        elif values_list[0]=="java":
            q1,pe1,pe2,q2,ga,grpa,bonus=int(t[1]),int(t[2]),int(t[3]),int(t[4]),int(t[5]),int(t[6]),int(t[7])
            score=0.1*ga+0.2*max(pe1,pe2)+0.1*min(pe1,pe2)+max(0.25*max(q1,q2),0.15*q1+0.25*q2)
            s=(90-score-bonus)/0.3
            a=(80-score-bonus)/0.3
            b=(70-score-bonus)/0.3
            c=(60-score-bonus)/0.3
            d=(50-score-bonus)/0.3
            e=(40-score-bonus)/0.3
            s = check_grade(s)
            a = check_grade(a)
            b = check_grade(b)
            c = check_grade(c)
            d = check_grade(d)
            e = check_grade(e)
            return render_template("gpredtable.html",s=s,a=a,b=b,c=c,d=d,e=e,req_data=req_data)

        elif values_list[0]=="sc":
            q1,pe1,pe2,ga,bonus=int(t[1]),int(t[2]),int(t[3]),int(t[4]),int(t[5])
            score=(0.1*ga+0.2*q1+0.3*pe1+0.1*pe2+bonus)
            s=(90-score)/0.3
            a=(80-score)/0.3
            b=(70-score)/0.3
            c=(60-score)/0.3
            d=(50-score)/0.3
            e=(40-score)/0.3
            s = check_grade(s)
            a = check_grade(a)
            b = check_grade(b)
            c = check_grade(c)
            d = check_grade(d)
            e = check_grade(e)
            return render_template("gpredtable.html",s=s,a=a,b=b,c=c,d=d,e=e,req_data=req_data)
            
        elif values_list[0]=="mad2":
            q1,q2,ga,gla,bonus=int(t[1]),int(t[2]),int(t[3]),int(t[4]),int(t[5])
            s=min((90-(0.05*ga+0.05*gla+0.25*q1+0.3*q2))/0.35,(90-(0.05*ga+0.05*gla+0.3*max(q1,q2)))/0.5)
            a=min((80-(0.05*ga+0.05*gla+0.25*q1+0.3*q2))/0.35,(80-(0.05*ga+0.05*gla+0.3*max(q1,q2)))/0.5)
            b=min((70-(0.05*ga+0.05*gla+0.25*q1+0.3*q2))/0.35,(70-(0.05*ga+0.05*gla+0.3*max(q1,q2)))/0.5)
            c=min((60-(0.05*ga+0.05*gla+0.25*q1+0.3*q2))/0.35,(60-(0.05*ga+0.05*gla+0.3*max(q1,q2)))/0.5)
            d=min((50-(0.05*ga+0.05*gla+0.25*q1+0.3*q2))/0.35,(50-(0.05*ga+0.05*gla+0.3*max(q1,q2)))/0.5)
            e=min((40-(0.05*ga+0.05*gla+0.25*q1+0.3*q2))/0.35,(40-(0.05*ga+0.05*gla+0.3*max(q1,q2)))/0.5)
            s = check_grade(s)
            a = check_grade(a)
            b = check_grade(b)
            c = check_grade(c)
            d = check_grade(d)
            e = check_grade(e)
            return render_template("gpredtable.html",s=s,a=a,b=b,c=c,d=d,e=e,req_data=req_data)

        elif values_list[0]=="mlt":
            q1,q2,ga,bonus=int(t[1]),int(t[2]),int(t[3]),int(t[4])
            score=(0.1*ga+max(0.25*q1+0.25*q2,0.4*max(q1,q2))+bonus)
            s = (90 - score) / 0.4
            a = (80 - score) / 0.4
            b = (70 - score) / 0.4
            c = (60 - score) / 0.4
            d = (50 - score) / 0.4
            e = (40 - score) / 0.4
            s = check_grade(s)
            a = check_grade(a)
            b = check_grade(b)
            c = check_grade(c)
            d = check_grade(d)
            e = check_grade(e)
            return render_template("gpredtable.html",s=s,a=a,b=b,c=c,d=d,e=e,req_data=req_data)

        elif values_list[0]=="mlp":
            q1,pe1,pe2,ga,npe1,npe2,bonus=int(t[1]),int(t[2]),int(t[3]),int(t[4]),int(t[5]),int(t[6]),int(t[7])
            score=(0.1*ga+0.20*pe1+0.20*pe2+0.15*q1+bonus*0.025*npe1+bonus*0.025*npe2)
            s=(90-score)/0.35
            a=(80-score)/0.35
            b=(70-score)/0.35
            c=(60-score)/0.35
            d=(50-score)/0.35
            e=(40-score)/0.35
            s = check_grade(s)
            a = check_grade(a)
            b = check_grade(b)
            c = check_grade(c)
            d = check_grade(d)
            e = check_grade(e)
            return render_template("gpredtable.html",s=s,a=a,b=b,c=c,d=d,e=e,req_data=req_data)
        elif values_list[0]=="bdm":
            q2,roe,ga,bonus=int(t[1]),int(t[2]),int(t[3]),int(t[4])
            score=0.3*ga+0.20*q2+0.2*roe+bonus
            s=(90-score)/0.3
            a=(80-score)/0.3
            b=(70-score)/0.3
            c=(60-score)/0.3
            d=(50-score)/0.3
            e=(40-score)/0.3
            s = check_grade(s)
            a = check_grade(a)
            b = check_grade(b)
            c = check_grade(c)
            d = check_grade(d)
            e = check_grade(e)
            return render_template("gpredtable.html",s=s,a=a,b=b,c=c,d=d,e=e,req_data=req_data)

        elif values_list[0]=="tds":
            roe,p1,p2,ga,bonus=int(t[1]),int(t[2]),int(t[3]),int(t[4]),int(t[5])
            score=(0.15*ga+0.2*roe+0.2*p1+0.2*p2+bonus)
            s=(90-score)/0.25
            a=(80-score)/0.25
            b=(70-score)/0.25
            c=(60-score)/0.25
            d=(50-score)/0.25
            e=(40-score)/0.25
            return render_template("gpredtable.html",s=s,a=a,b=b,c=c,d=d,e=e,req_data=req_data)

        elif t[0]=='stat1' or t[0]=="stat2":
            q1,q2,ga,act,bonus=int(t[1]),int(t[2]),int(t[3]),int(t[4]),int(t[5])
            s=min((90-(0.1*ga+0.2*max(q1,q2)+bonus+act))/0.6,(90-(0.1*ga+0.2*q1+0.3*q2+act+bonus))/0.4)
            a=min((80-(0.1*ga+0.2*max(q1,q2)+bonus+act))/0.6,(80-(0.1*ga+0.2*q1+0.3*q2+act+bonus))/0.4)
            b=min((70-(0.1*ga+0.2*max(q1,q2)+bonus+act))/0.6,(70-(0.1*ga+0.2*q1+0.3*q2+act+bonus))/0.4)
            c=min((60-(0.1*ga+0.2*max(q1,q2)+bonus+act))/0.6,(60-(0.1*ga+0.2*q1+0.3*q2+act+bonus))/0.4)
            d=min((50-(0.1*ga+0.2*max(q1,q2)+bonus+act))/0.6,(50-(0.1*ga+0.2*q1+0.3*q2+act+bonus))/0.4)
            e=min((40-(0.1*ga+0.2*max(q1,q2)+bonus+act))/0.6,(40-(0.1*ga+0.2*q1+0.3*q2+act+bonus))/0.4)
            s = check_grade(s)
            a = check_grade(a)
            b = check_grade(b)
            c = check_grade(c)
            d = check_grade(d)
            e = check_grade(e)
            return render_template("gpredtable.html",s=s,a=a,b=b,c=c,d=d,e=e,req_data=req_data)

        else:
            q1,q2,ga,bonus=int(t[1]),int(t[2]),int(t[3]),int(t[4])
            s=min((90-(0.1*ga+0.2*max(q1,q2)+bonus))/0.6,(90-(0.1*ga+0.2*q1+0.3*q2+bonus))/0.4)
            a=min((80-(0.1*ga+0.2*max(q1,q2)+bonus))/0.6,(80-(0.1*ga+0.2*q1+0.3*q2+bonus))/0.4)
            b=min((70-(0.1*ga+0.2*max(q1,q2)+bonus))/0.6,(70-(0.1*ga+0.2*q1+0.3*q2+bonus))/0.4)
            c=min((60-(0.1*ga+0.2*max(q1,q2)+bonus))/0.6,(60-(0.1*ga+0.2*q1+0.3*q2+bonus))/0.4)
            d=min((50-(0.1*ga+0.2*max(q1,q2)+bonus))/0.6,(50-(0.1*ga+0.2*q1+0.3*q2+bonus))/0.4)
            e=min((40-(0.1*ga+0.2*max(q1,q2)+bonus))/0.6,(40-(0.1*ga+0.2*q1+0.3*q2+bonus))/0.4)
            s = check_grade(s)
            a = check_grade(a)
            b = check_grade(b)
            c = check_grade(c)
            d = check_grade(d)
            e = check_grade(e)
            return render_template("gpredtable.html",s=s,a=a,b=b,c=c,d=d,e=e,req_data=req_data)
     except:
         return "congrats! you messed up my backend logic"
@app.route("/return",methods=["POST"])
def return_home():
   return render_template("gpred.html")
            

    



if __name__ == "__main__":
    app.run(debug=True)
