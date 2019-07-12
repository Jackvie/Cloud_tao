import imghdr, base64

def image_file(value):
    """
    检查是否是图片文件
    :param value:
    :return:
    """
    try:
        file_type = imghdr.what(value)
        print(file_type)
    except Exception:
        raise ValueError('Invalid image.')
    else:
        if not file_type:
            raise ValueError('Invalid image.')
        else:
            return value

with open('./cywl.jpg', 'rb') as f:
    s = imghdr.what(f)  # 'jpeg'


with open('./cywl.jpg', 'rb') as f:
    content = f.read()[:32]
    r = imghdr.what(None, content)  # 'jpeg