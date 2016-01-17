from flask import Blueprint, render_template


admin = Blueprint('admin',__name__)

@admin.route("/")
def home():
    return render_template('admin/index.html')