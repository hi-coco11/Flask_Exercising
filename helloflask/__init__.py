from flask import Flask, g, request, Response, make_response, session
from flask import render_template, Markup
from datetime import date, datetime, timedelta

app = Flask(__name__)
app.debug = True
# app.jinja_env.trim_blocks = True

app.config.update(
    SECRET_KEY='XDF1230D011moq1QA',
    SESSION_COOKIE_NAME='pyweb_flask_session',
    PERMANENT_SESSION_LIFETIME=timedelta(31) # 31 days
)


@app.route('/')
def idx():
    return render_template('app.html', ttt='testTTT')

@app.route('/app')
def app():
    return render_template('application.html', title="MAIN!")

@app.route('/top100')
def top100():
    return render_template('applcation.html', title="MAIN!!")

@app.route('/main')
def main():
    return render_template('main.html', Title = titt)

@app.route('/rp')
def rp():
    # q = request.args.get('q')
    q = request.args.get('q')
    return "q= %s" % str(q)

@app.route('/wc')
def wc():
    key = request.args.get('key')
    val = request.args.get('val')
    res = Response("set cookie")
    res.set_cookie(key, val)
    return make_response(res)

@app.route("/tmpl")
def t():
    tit = Markup("<strong>Title</strong>")
    mu = Markup("<h1>iii = <i>%s</i></h1>")
    h = mu % "Italic"
    print("h=", h)

    lst = [("만남1", "김건모"), ("만남2", "노사연")]

    return render_template('index.html', title = tit, mu=h, lst=lst)

@app.route('/tmp2')
def tmp2():
    a = (1, "만남1", "김건모", False, [])
    b = (2, "만남2", "노사연", True, [a])
    c = (3, "만남3", "김건모2", False, [a, b])
    d = (4, "만남4", "노사연2", True, [a, b, c])

    return render_template("index.html", lst2=[a, b, c, d])

@app.route('/rc')
def rc():
    key = request.args.get('key')
    val = request.cookies.get(key)
    return "cookie["+key+"] = " + val


@app.route('/reqenv')
def reqenv():
    return ('Request_METHOD: %(REQUEST_METHOD) s <br>'
            'SCRIPT_NAME: %(SCRIPT_NAME) s <br>'
            'QUERY_STRING: %(QUERY_STRING) s <br>') %request.environ

# WebServer Gateway Interface
@app.route('/test_wsgi')
def wsgi_test():
        def application(environ, start_response):
            body = 'The request method was %s' % environ['REQUEST_METHOD']
            headers = [('Content-Type', 'text/plain'),
                       ('Content-Length', str(len(body)))]
            start_response('200 OK', headers)
            return [body]
        return make_response(application)
    
@app.route('/res')
def res1():
      custom_res = Response("Custom Response", 201, {'test': 'ttt'})
      return make_response(custom_res)

# # request 처리용 함수
# def ymd(fmt):
#     def trans(date_str):
#         return datetime.strptime(date_str, fmt)
#     return trans

# @app.route('/dt')
# def dt():
#     datestr = request.values.get('date', date.today(), type=ymd('%Y-%m-%d'))
#     return "우리나라 시간 형식: " + str(datestr)

# # session에 관한 예제 코드
# @app.route('/setsess')
# def setsess():
#     session['Token'] = '12345'
#     return 'session이 설정되었습니다 !'

# @app.route('/getsess')
# def getsess():
#     return session.get('Token')

# @app.route('/delsess')
# def delsess():
#     if session.get('Token'):
#         del session['Token']
#     return "Session이 삭제되었습니다."