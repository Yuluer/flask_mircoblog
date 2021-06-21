from app import ath
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm

@ath.route('/index',methods=['GET'])
def index():
	user = {'username': 'Miguel'}
	posts = [  # 创建一个列表：帖子。里面元素是两个字典，每个字典里元素还是字典，分别作者、帖子内容。
		{
			'author': {'username': 'John'},
			'body': 'Beautiful day in Portland!'
		},
		{
			'author': {'username': 'Susan'},
			'body': 'The Avengers movie was so cool!'
		}
	]
	return render_template('index.html',  user=user,posts=posts)

@ath.route('/login',methods=['GET','POST'])
def login():
	form = LoginForm()#表单实例化对象
	if form.validate_on_submit():
		flash('Login requested for user {},remember_me={}'.format(form.username.data, form.remember_me.data))
		return redirect(url_for('index'))
	return render_template('login.html', title='Sign In', form=form)