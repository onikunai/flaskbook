from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length

# ユーザー新規作成とユーザー編集フォームクラス
class SignUpForm(FlaskForm):
    # ユーザーフォームのusername属性のラベルとバリデータを設定する
    username = StringField(
        "ユーザー名",
        validators=[
            DataRequired(message="ユーザー名は必須です。"),
            Length(min=1, max=30, message="30文字以内で入力してください。"),
        ],
    )
    
    # ユーザーフォームemail属性のラベルとバリデータを設定する
    email = StringField(
        "メールアドレス",
        validators=[
            DataRequired(message="メールアドレスは必須です。"),
            Email(message="メールアドレスの形式で入力してください。"),
        ],
    )
    
    # ユーザーフォームpassword属性のラベルとバリデータを設定する
    password = PasswordField(
        "パスワード",
        validators=[
            DataRequired(message="パスワードは必須です。")
        ]
    )
    
    # ユーザーフォームsubmitの文言を設定する
    submit = SubmitField("新規登録")
    
class LoginForm(FlaskForm):
    email = StringField(
        "メールアドレス",
        validators=[
            DataRequired("メールアドレスは必須です。"),
            Email("メールアドレスの形式で入力して下さい。"),
        ],
    )
    
    password = PasswordField(
        "パスワード",
        validators=[
            DataRequired("パスワードは必須です。"),
        ]
        )
    
    submit = SubmitField("ログイン")