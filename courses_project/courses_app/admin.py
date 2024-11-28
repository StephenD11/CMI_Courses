from django.contrib import admin
from .models import CustomUser, Course, Topic, Question,Answer,AssignmentSubmission


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')  # Указываем, какие поля курса отображать в админке


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'order', 'is_completed')  # Какие поля темы отображать
    list_filter = ('course',)  # Фильтр для отображения тем по курсам
    ordering = ('course', 'order',)  # Сортировка тем сначала по курсу, потом по полю order

@admin.register(AssignmentSubmission)
class AssignmentSubmissionAdmin(admin.ModelAdmin):
    list_display = ('user','assignment_url','submitted_at')
    list_filter = ('submitted_at',)
    ordering = ('submitted_at',)



@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'topic', 'get_course')  # Используем метод get_course для отображения курса
    list_filter = ('topic__course', 'topic')  # Фильтрация по курсу через тему
    search_fields = ('question_text',)

    def get_course(self, obj):
        return obj.topic.course  # Получаем курс через связь с темой

    get_course.admin_order_field = 'topic__course'  # Устанавливаем порядок сортировки
    get_course.short_description = 'Курс'  # Название столбца в админке

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('answer_text', 'question', 'is_correct', 'question__topic','question__topic__course')  # Используем напрямую 'question__topic'
    list_filter = ('question__topic__course', 'question__topic', 'question')  # Фильтрация по курсу через вопрос
    search_fields = ('answer_text',)  # Поиск по тексту ответа




admin.site.register(CustomUser)

