import connexion
import six
from swagger_server.service.student_service import *

from swagger_server.models.student import Student  # noqa: E501
from swagger_server import util


def add_student(body=None):  # noqa: E501
    """Add a new student

    Adds an item to the system # noqa: E501

    :param body: Student item to add
    :type body: dict | bytes

    :rtype: float
    """
    if connexion.request.is_json:
        body = Student.from_dict(connexion.request.get_json())  # noqa: E501
        return add(body)
    return 500, 'error!'

def delete_student(student_id):  # noqa: E501
    """deletes a student

    delete a single student   # noqa: E501

    :param student_id: the uid
    :type student_id: float

    :rtype: Student
    """
    return delete(student_id)


def get_student_by_id(student_id):  # noqa: E501
    """gets student

    Returns a single student  # noqa: E501

    :param student_id: the uid
    :type student_id: float

    :rtype: Student
    """
    return get_by_id(student_id)
