from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, Email


class FeedbackForm(FlaskForm):
    name = StringField('Name *', validators=[DataRequired(), Length(min=0, max=50)])
    email = StringField('Email *', validators=[DataRequired(), Email()])
    subject = SelectField('Subject *',
                          choices=[('Saying hello', 'hello'), ('Question', 'Question'), ('Support', 'Support'),
                                   ('Feedback', 'Feedback'), ('A joke', 'A joke'), ('Enhancement', 'Enhancement'),
                                   ('Something else', 'Something else')], validators=[DataRequired()])
    message = TextAreaField('Message *', validators=[DataRequired(), Length(min=0, max=500)])
    submit = SubmitField('Say Hello')

    def to_json(self):
        """
        converts the form to a JSON
        the csrt_token is not included in the response
        :return: JSON representing the contents of the form
        :rtype: JSON
        """
        feedback_dict = {'name': self.name.data, 'email': self.email.data, 'subject': self.subject.data,
                         'message': self.message.data}
        return feedback_dict
