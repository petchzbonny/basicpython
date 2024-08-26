
from flask import Blueprint,render_template ,jsonify
from app.models import EMPLOYEE ,CER_REPORT

main = Blueprint('main', __name__)

@main.route('/')
def index():
    users = EMPLOYEE.query.all()  # ดึงข้อมูลผู้ใช้ทั้งหมด
    return render_template('index.html', users=users)
@main.route('/test')


def test2():
      records = CER_REPORT.query.filter_by(Sample='MANGO').all()
      if records:
        return jsonify([record.to_dict() for record in records])  # Assuming you have a to_dict method in your model
      else:
        return jsonify({'error': 'No record found'}), 404


