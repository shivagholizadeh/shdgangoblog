from django.db import models


class TodoItem(models.Model):
    des_work_todoitem = models.CharField(max_length=100)
    flg_checked_todoitem = models.BooleanField(default=False)
    dat_do_todoitem = models.DateField()
    dat_planning_todoitem = models.DateTimeField(auto_now=True)


    def __str__(self):
         return self.des_work_todoitem
