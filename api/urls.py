from django.contrib import admin
from django.urls import path
from api.views import *


urlpatterns = [
    path('standart/',StandardListView.as_view()),
    path('subject/',SubjectListView.as_view()),
    path('lesson/',LessonListView.as_view()),
    path('working-days/',WorkingDaysListView.as_view()),
    path('time-slots/',TimeSlotsListView.as_view()),
    path('slot-subject/',SlotSubjectListView.as_view()),
    path('comment/',CommentListView.as_view()),
    path('reply/',ReplyListView.as_view()),
]