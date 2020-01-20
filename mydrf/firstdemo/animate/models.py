from django.db import models


class CateGory(models.Model):
    id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        db_table = 'tb_category'

class Animate(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False, unique=True, db_index=True)
    category = models.ForeignKey(CateGory, db_constraint=False, null=True,blank=True,on_delete=models.SET_NULL)
    ## 状态手动设置为tinyInt 迁移时不再操作这个表
    ## alter table tb_animate add status tinyint(3) not null default 0;
    ## self._meta.get_field('status').flatchoices 获取choices
    ## self.get_status_display() 获取字段映射的中文值
    status = models.SmallIntegerField(choices=((0, '未知'),(1,'完结'),(2,'连载'),(3,'下架')), default=0)

    class Meta:
        db_table = 'tb_animate'
        verbose_name = '动画'
        verbose_name_plural = '动画'
        managed = False

class ImageBase(models.Model):

    id = models.AutoField(primary_key=True)
    relative_path = models.CharField(max_length=200, null=True, blank=True)
    chapter = models.PositiveSmallIntegerField(null=True,blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    animate = models.ForeignKey(Animate, db_constraint=False,null=False,blank=False,on_delete=models.CASCADE)

    class Meta:
        db_table = 'tb_imagebase'
        managed = False
        #index_together = ['chapter','name']
        # 这里索引手动创建 迁移时不再操作此表
        # alter table tb_imagebase add INDEX `chapter_name` (chapter,name(4));


