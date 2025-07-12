# from flask import Flask, request, redirect

# app = Flask(__name__)

# nextid = 4
# topics = [
#     {'id': 1, 'title': 'html', 'body': 'html is ...'},
#     {'id': 2, 'title': 'css', 'body': 'css is ...'},
#     {'id': 3, 'title': 'javascript', 'body': 'javascript is ...'}
# ]

# def template(contents, content, id=None):
#     contextUI =''
#     if id!= None:
#         contextUI='''
#             <li><a href="/update/{id}/">update</a></li>
#             <li><form action="/delete/{id}/" method="POST"><input type="submit" value="delete"></form></li>
#         '''
#     return f'''
#     <!doctype html>
#     <html>
#         <body>
#             <h1> <a href = "/">WEB</a></h1>
#             <ol>
#                 {contents}
#             </ol>
#             {content}
#             <ul>
#                 <li><a = href='/create/'>create</a></li>
#                 {contextUI}
#             </ul>
#         </body>
#     </html> 
#     '''

# def getContents():
#     liTags = ''
#     for topic in topics:
#         liTags = liTags + f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>' 
#     return liTags


# @app.route('/')
# def index():  #return값은 기본적으로 문자열로 응답해야함
#     return template(getContents(), '<h2>Welcome</h2>Hello, Web')

# @app.route('/create/', methods=['GET', 'POST'])
# def create():
#     if request.method == 'GET':
#         content = '''
#             <form action="/create/" method="POST">
#                 <p><input type="text" name="title" placeholder = "title"></p>  <!-- 입력한 값을 서버로 보낼 때 이름이 필요: name 태그 -->
#                 <p><textarea name = "body" placeholder = "body"></textarea></p>
#                 <p><input type="submit" value="create"></p>
#             </form>
#         '''
#         return template(getContents(), content)
#     elif request.method == 'POST':
#         global nextid
#         title = request.form['title']
#         body = request.form['body']
#         newTopic = {'id': nextid, 'title': title, 'body': body}
#         topics.append(newTopic)
#         url = '/read/'+str(nextid)+'/'
#         nextid = nextid+1 ## nextid는 전역변수이기에 그전에 전역변수 설정을 해줘야 함
#         return redirect(url)

# @app.route('/read/<int:id>/') ## 가변적으로 바뀌는 변수를 route로 받아내기 위해선 어떻게해야하나
# def read(id):
#     title = ''
#     body = ''
#     for topic in topics:
#         if id == topic['id']: ## <id>의 부분은 무조건 str로 들어오기에 앞에서 int로 type변환필요
#             title = topic['title']
#             body = topic['body'] 
#             break
#     return template(getContents(), f'<h2>{title}</h2>{body}', id)

# @app.route('/update/<int:id>', methods=['GET', 'POST'])
# def update(id):
#     if request.method == 'GET':
#         title = ''
#         body = ''
#         for topic in topics:
#             if id == topic['id']: ## <id>의 부분은 무조건 str로 들어오기에 앞에서 int로 type변환필요
#                 title = topic['title']
#                 body = topic['body'] 
#                 break
#         content = f'''
#             <form action="/update/{id}/" method="POST">
#                 <p><input type="text" name="title" placeholder = "title" value="{title}"></p>  <!-- 입력한 값을 서버로 보낼 때 이름이 필요: name 태그 -->
#                 <p><textarea name = "body" placeholder = "body">{body}</textarea></p>
#                 <p><input type="submit" value="update"></p>
#             </form>
#         '''
#         return template(getContents(), content)
#     elif request.method == 'POST':
#         global nextid
#         title = request.form['title']
#         body = request.form['body']
#         for topic in topic['id']:
#             if id == topic['id']:
#                 topic['title'] = title
#                 topic['body'] = body
#                 break
#         url = '/read/'+str(id)+'/'
#         return redirect(url)
    
# @app.route('/delete/<int:id>/', methods=['POST']) 
# def delete(id):
#     for topic in topics:
#         if id == topic['id']:
#             topics.remove(topic)
#             break
#     return redirect('/')


# app.run(debug=True) ## debuging모드로 flask 실행가능 // 편의를 위한거라 실제할 땐 debugmode x