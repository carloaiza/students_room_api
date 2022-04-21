from flask import Blueprint, Response,json
from service.student_service import StudentService
from util.util import MyEncoder

app_student = Blueprint('app_student',__name__)
studentService= StudentService()

@app_student.route('/student')
def getAllStudents():
    return Response(response=json.dumps(studentService.getAllStudents(),
                                        cls=MyEncoder),
                    status=200,
                    mimetype='application/json')