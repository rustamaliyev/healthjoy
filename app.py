from flask import Flask, render_template, redirect, url_for, request
from github import Github

app = Flask(__name__)
repo_user = Github("004a41e17b3cf604a571b98e990333f4a561ca2b")

@app.route('/',methods = ['GET'])
def index():
    forks = repo_user.get_user().get_repo('healthjoy').get_forks()
    repo = repo_user.get_user().get_repo('healthjoy')
    return render_template("index.html", repo=repo, forks=forks)

@app.route('/fork',methods=['GET', 'POST'])
def fork():
  if request.method == 'POST':
    repo = repo_user.get_user().get_repo('healthjoy')
    github_pat = request.form["github_pat"]
    #github_user = Github("1a8289e88dfbcd2d918357621feb972e05191ad0")
    github_user = Github(github_pat)
    user = github_user.get_user()
    myfork = user.create_fork(repo)
    return render_template("success.html", user=user,repo=repo)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)