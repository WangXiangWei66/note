# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from zcool import settings
import os
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request


class ZcoolPipeline(ImagesPipeline):  # 自定义的用于下载图片的pipeline
    def get_media_requests(self, item, info):
        image_requests = super().get_media_requests(item, info)  # 获取图片连接请求的列表

        for img_req in image_requests:
            img_req.item = item  # 对每一个图片连接的请求都添加一个item属性
        return image_requests

    # 重写这个方法的目的，改变存储路径
    def file_path(self, request, response=None, info=None):
        old_path = super().file_path(request, response, info)
        title = request.item['title']  # 获取到图片标题
        save_path = os.path.join(settings.IMAGES_STORE, title)
        # 原路径中提取文件名
        image_name = old_path.replace('full/', '')
        return os.path.join(save_path, image_name)
