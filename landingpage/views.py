from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from classroom.models import Classroom,Topic,ClassroomTeachers
from posts.models import Assignment,SubmittedAssignment,AssignmentFile, Attachment
# from classroom.forms import ClassroomCreationForm,JoinClassroomForm, PostForm, AssignmentFileForm, AssignmentCreateForm
from comments.forms import CommentCreateForm, PrivateCommentForm

# Create your views here.
def index(request):
    return render(request, 'land.html')
    

def join_classroom(request):
    if request.method == 'POST':
        return redirect('classroom:join_classroom')