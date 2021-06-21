from app import ath
from flask import render_template
@ath.route('/',methods=['GET'])
def index():
	return "'render_template('index.html')'"