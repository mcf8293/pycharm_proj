url = 'https://video.fedbf.com/20231028/ZGU1ZGE3ZD/004213/720/hls/encrypt/index.m3u8'
"""
这段代码首先使用Python的rsplit()函数从右向左将网址分割成两部分，以最后一个/为分隔符。
然后，它选择分割后的第一部分，即不包括index.m3u8的部分，并将其存储在base_url变量中。
最后，代码打印出base_url的值。
"""
base_url = url.rsplit('/', 1)[0]

print(base_url)
