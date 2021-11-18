from rest_framework.permissions import *
from rest_framework import permissions
from rest_framework.generics import *
from .serializers import *
from dastur.models import *


class StandardListView(ListCreateAPIView):
    serializer_class = StandardSerializer
    queryset = Standard.objects.all()


class SubjectListView(ListCreateAPIView):
    serializer_class = SubjectdSerializer
    queryset = Subject.objects.all()
    


class LessonListView(ListCreateAPIView):
    serializer_class = LessondSerializer
    queryset = Lesson.objects.all()
    


class WorkingDaysListView(ListCreateAPIView):
    serializer_class = WorkingDaysSerializer
    queryset = WorkingDays.objects.all()
    

class TimeSlotsListView(ListCreateAPIView):
    serializer_class = TimeSlotsSerializer
    queryset = TimeSlots.objects.all()



class SlotSubjectListView(ListCreateAPIView):
    serializer_class = SlotSubjectSerializer
    queryset = SlotSubject.objects.all()
     

class CommentListView(ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
     

class ReplyListView(ListCreateAPIView):
    serializer_class = ReplySerializer
    queryset = Reply.objects.all()
     