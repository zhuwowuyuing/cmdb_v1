#coding=utf8
from django.db import models

# Create your models here.


class Status(models.Model):
    class Meta:
        verbose_name = '使用状态'
        verbose_name_plural = verbose_name

    status          = models.CharField('使用状态',max_length=60, primary_key=True)
    exclusive       = models.BooleanField('exclusive', default=False)

    def __unicode__(self):
        return u'%s' % (self.status)


class Devices(models.Model):
    class Meta:
        verbose_name = '设备信息'
        verbose_name_plural = verbose_name
        ordering = ['asset']

    asset           = models.CharField('资产编号', max_length=60, primary_key=True)
    asset_old       = models.CharField('旧资产编号', max_length=60, blank=True)
    district        = models.CharField('所在地区', max_length=60)
    company         = models.CharField('账上所属公司', max_length=60)
    status          = models.ForeignKey(Status)
    type            = models.CharField('类别', max_length=60)
    subtype         = models.CharField('子类别', max_length=60)
    manufacturer    = models.CharField('品牌', max_length=60, blank=True)
    model           = models.CharField('型号', max_length=100, blank=True)
    serialno    = models.CharField('序列号', max_length=100, blank=True)

    def __unicode__(self):
        return u'%s %s %s %s %s' % (self.asset, self.type, self.subtype, self.manufacturer, self.model)

class Server(models.Model):
    class Meta:
        verbose_name = '服务器信息'
        verbose_name_plural = verbose_name
        ordering = ['asset']

    asset           = models.CharField('资产编号', max_length=60, primary_key=True)
    size            = models.CharField('尺寸', max_length=60, blank=True)
    cpu             = models.CharField('CPU', max_length=200, blank=True)
    harddisk        = models.CharField('硬盘', max_length=200, blank=True)
    ram             = models.CharField('内存', max_length=200, blank=True)
    os              = models.CharField('操作系统',max_length=200, blank=True)
    building        = models.CharField('机房(所处位置)',max_length=60, blank=True)
    location        = models.CharField('机柜',max_length=60, blank=True)
    consignee       = models.CharField('托管编号',max_length=60, blank=True)
    hostname        = models.CharField('主机名',max_length=60, blank=True)
    dept            = models.CharField('使用部门',max_length=60, blank=True)
    business        = models.CharField('业务系统',max_length=60, blank=True)
    ownername       = models.CharField('领用人',max_length=60, blank=True)
    warehousedate   = models.DateField('入库时间', blank=True, null=True)
    receivedate     = models.DateField('领用时间', blank=True, null=True)
    warrantyexpirationdate = models.DateField('保修至', blank=True, null=True)
    scrapDate       = models.DateField('报废时间', blank=True, null=True)
    changeInfo      = models.TextField('变更信息',max_length=4000, blank=True)
    deviceno          = models.ForeignKey(Devices)

    def __unicode__(self):
        return u'%s' % (self.asset)
