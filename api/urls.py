from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('employees', views.EmployeeViewSet, basename='employee')

urlpatterns = [
    # Students Path
    path('students/', views.studentsView, name='students-list'),
    path('students/<int:pk>/', views.studentView, name='student-detail'),

    # Employees Path
    # path('employees/', views.Employees.as_view()),
    # path('employees/<int:pk>/', views.EmployeeDetails.as_view()),

    #
    path('', include(router.urls)),

    #
    path('comments/', views.CommentsView.as_view()),
    path('blogs/', views.BlogsView.as_view()),
    path('blogs/<int:pk>/', views.BlogDetailView.as_view()),
    path('comments/<int:pk>/', views.CommentDetailView.as_view())
]