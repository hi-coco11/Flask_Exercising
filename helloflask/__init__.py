from flask import Flask, g, request, Response, make_response

app = Flask(__name__)
app.debug = True

@app.route('/rp')
def rp():
    # q = request.args.get('q')
    q = request.args.get('q')
    return "q= %s" % str(q)

@app.route('/')
def index():
    return 'hi'

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
    