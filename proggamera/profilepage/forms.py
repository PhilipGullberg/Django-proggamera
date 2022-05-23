from django import forms
from .models import Course
from .models import Student, Classroom, Teacher


class add_class_form(forms.Form):
    courses=Course.objects.all()
    course_list=courses.values_list()
    class_name=forms.CharField(label="Klassens namn ", max_length=50)
    courses = forms.MultipleChoiceField(required = True, label="Kurser " , widget=forms.CheckboxSelectMultiple, choices=course_list)

class add_student_form(forms.Form):
    student=forms.CharField(label="Elevens namn", max_length=100)
    student_email=forms.EmailField(label="Elevens mail", max_length=100)

class add_course_form(forms.Form):
    courses=Course.objects.all()
    course_list=courses.values_list()
    courses = forms.MultipleChoiceField(required = True, label="Kurser " , widget=forms.CheckboxSelectMultiple, choices=course_list)

class DateInput(forms.DateInput):
    input_type = 'date'

class add_excercise_form(forms.Form):
    Excercise_type=[('alla','Alla'),
     ('quiz','Quiz'),
     ('läs kapitlet','Läs kapitlet'),
     ('se video', 'Se video'),
     ('fill in blanks', 'Fill in blanks')]
    excercises=forms.MultipleChoiceField(
        required=False,
        label="Välj uppgifter",
        widget=forms.CheckboxSelectMultiple,
        choices=Excercise_type,
    )
    deadline = forms.DateField(widget=DateInput, label="Deadline")
   
   

        
