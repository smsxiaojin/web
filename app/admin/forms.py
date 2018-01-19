# coding:utf8
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField, TextAreaField, SelectField
from wtforms.validators import DataRequired, ValidationError
from app.models import Contact
class MovieForm(FlaskForm):
    title = StringField(
        label="片名",
        validators=[
            DataRequired("请输入片名!")
        ],
        description="标签",
        render_kw={

            "class ": "form-control",
            "id": "input_title",
            "placeholder": "请输入标签片名！",
        }
    )

    url = FileField(
        label="文件",
        validators=[
            DataRequired("请上传文件!")
        ],
        description="文件",
    )
    info = TextAreaField(
        label="内容",
        validators=[
            DataRequired("请输入内容!")
        ],
        description="内容",
        render_kw={

            "class ": "form-control",
            "row": 10
        }
    )







    release_time = StringField(
        label="时间",
        validators=[
            DataRequired("请选择时间!")
        ],
        description="时间",
        render_kw={

            "class ": "form-control",
            "placeholder": "请选择时间！",
            "id": "input_release_time"
        }
    )
    submit = SubmitField(
        '编辑',
        render_kw={
            "class ": "btn btn-primary"

        }
    )