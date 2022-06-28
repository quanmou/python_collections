#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from tqdm import tqdm


def download_file1(url, name):
    """
    方法1
    Termius.exe:  19%|█▊        | 28695/154342.1171875 [00:03<00:11, 10473.31k/s]
    """
    resp = requests.get(url=url, stream=True)  # stream=True的作用是仅让响应头被下载，连接保持打开状态
    content_size = int(resp.headers['Content-Length']) / 1024  # 确定整个安装包的大小
    with open(name, "wb") as f:
        print("安装包整个大小是：", content_size, 'k，开始下载...')
        for data in tqdm(iterable=resp.iter_content(1024), total=content_size, unit='k', desc=name):
            # 调用iter_content，一块一块的遍历要下载的内容，搭配stream=True，此时才开始真正的下载
            # iterable：可迭代的进度条 total：总的迭代次数 desc：进度条的前缀
            f.write(data)
        print(name + "已经下载完毕！")


def download_file2(url, name):
    """
    方法2（推荐）
    Termius.exe: 100%|██████████| 151M/151M [00:23<00:00, 6.78MiB/s]
    """
    resp = requests.get(url, stream=True)
    total = int(resp.headers.get('content-length', 0))  # 拿到文件的长度，并把total初始化为0
    # 初始化tqdm，传入总数，文件名等数据，接着就是写入，更新等操作了
    with open(name, 'wb') as file, tqdm(
        desc=name,
        total=total,
        unit='iB',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for data in resp.iter_content(chunk_size=1024):
            size = file.write(data)
            bar.update(size)


if __name__ == '__main__':
    url = "https://autoupdate.termius.com/windows/Termius.exe"
    name = url.split('/')[-1]  # 截取整个url最后一段即文件名
    download_file2(url, name)
