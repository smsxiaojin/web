# coding:utf8
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField, TextAreaField, SelectField
from wtforms.validators import DataRequired, ValidationError
from app.models import Contact


class MovieForm(FlaskForm):
    title = StringField(
        label="名称",
        validators=[
            DataRequired("请输入名称!")
        ],
        description="名称",
        render_kw={

            "class":"form-control input-lg",
            "name":"name",
            "id":"name",
            "placeholder":"Enter name"
        }
    )

    email = FileField(
        label="email",
        validators=[
            DataRequired("请填写email!")
        ],
        description="email",
    )
    message = TextAreaField(
        label="内容",
        validators=[
            DataRequired("请输入内容!")
        ],
        description="内容",
        render_kw={

            "class":"form-control",
            "rows":"4",
            "cols":"25",
            "required":"required"
        }
    )


    submit = SubmitField(
        '编辑',
        render_kw={
            "class ":"btn btn-skin btn-block"

        }
    )