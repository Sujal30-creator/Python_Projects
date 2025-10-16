import os

class Config:
   SECRET_KEY= '01b385dd834398f503b0be5f5743d58f'#os.environ.get('SECRET_KEY')
   SQLALCHEMY_DATABASE_URI= 'sqlite:///site.db'#os.environ.get('SQLALCHEMY_DATABASE_URI')
    #FOR EMAIL _ SERVER
   MAIL_SERVER= 'smtp.googlemail.com'
   MAIL_PORT= 587
   MAIL_USE_TLS= True
   MAIL_USERNAME= 'sujalvaishnav30804@gmail.com'#os.environ.get('EMAIL_USER')
   MAIL_PASSWORD= 'xttd sngm sdfb jozt'#os.environ.get('EMAIL_PASS')
    # MAIL_DEFAULT_SENDER = 'sujal.235706101@vcet.edu.in'