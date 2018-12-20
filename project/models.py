from django.db import models

class Course(models.Model):
    """
        Курс, который изучает пользователь. Кроме того мы будем отображать все
        курсы, по которым после пользователь сможет переходить.
    """
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """Возвращает строковое представление модели."""
        return self.text
        
class Lesson(models.Model):
    """
        Доступные уроки курсов. Содержат ссылку на материалы урока.
    """
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """Возвращает строковое представление модели."""
        return self.text
        
class Topic(models.Model):
    """
        Урок курса, где укажется весь материал нужный для работы.
    """
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
     
    def __str__(self):
        """Возвращает строковое представление модели."""
        if len(self.text)>50:
            return self.text[:50] + "..."
        else:
            return self.text
