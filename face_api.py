import urllib, urllib3
import json

def getFaceInfo(picurl):
    # http://apicn.faceplusplus.com/v2/detection/detect?
    url = "https://api-cn.faceplusplus.com/facepp/v3/detect?api_key=B3qtKcS9UqkW8zlvqxrt6w-I5KHvFN9q" \
          "&api_secret=qys06uKdTLVGJhOTyUP_XI4ozCpDuC8X&image_url=%s&attribute=glass,"\
         "pose,gender,age,race,smiling" %picurl
    data = "api_key=ZqEtIrxBeGzGvAnDSGYZ77wYEOA1-fS2&api_secret=EDgFfqaOZeLaLhLqJusHTFN8OHKDFNkJ&image_url=%s&"\
            "return_attributes=gender,age,smiling,headpose,eyestatus,ethnicity"% picurl
           # 'eyestatus,pose,gender,age,race,smiling' % picurl
    html = urllib3.urlopen('https://api-cn.faceplusplus.com/facepp/v3/detect', data=data).read()
    # html = urllib.urlopen(url).read()

    text = json.loads(html)
    print(text)

    # glass=佩戴眼镜
    # headpose=姿势
    # gender=性别
    # age=年龄
    # race=人种
    # smiling=微笑指数
    eyestatus = text['faces'][0]['attributes']['glass']['value']
    gender = text['faces'][0]['attributes']['gender']['value']
    age = text['faces'][0]['attributes']['age']['value']
    ethnicity = text['faces'][0]['attributes']['ethnicity']['value']
    smiling = text['faces'][0]['attributes']['smile']['value']
    headpose = text['faces'][0]['attributes']['headpose']['yaw_angle']
    print(u'人脸信息：\n年龄：%s\n性别：%s\n人种：%s\n微笑指数：%s\n头部姿势：%s' % (age, gender, ethnicity, smiling,headpose))
    return u'人脸信息：\n年龄：%s\n性别：%s\n人种：%s\n微笑指数：%s' %(age,gender,ethnicity,smiling)

def getPicInfo(url):
    data = 'api_key=ZqEtIrxBeGzGvAnDSGYZ77wYEOA1-fS2&api_secret=EDgFfqaOZeLaLhLqJusHTFN8OHKDFNkJ&image_url=%s' % url
    html = urllib3.urlopen('https://api-cn.faceplusplus.com/imagepp/beta/detectsceneandobject', data=data).read()
    text = json.loads(html)
    print(text)
    if text['scenes']:  # 场景
        scenes = text['scenes'][0]['value']
    else:
        scenes = None
    if text['objects']:  # 物品
        objects = text['objects'][0]['value']
    else:
        objects = None
    t_info = ""
    if scenes:
        t_info += u"图片场景可能是：%s\n" %scenes
    if objects:
        t_info += u"图片物品可能是：%s\n" %objects
    if not t_info:
        t_info = u'这是火星来的图片吧，什么都没发现！'
    print(t_info)
    return t_info

if __name__ == '__main__':
    # getFaceInfo("https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1527586359578&di=6664113230b71041c7727267c5e43e79&imgtype=0&src=http%3A%2F%2Fimgsrc.baidu.com%2Fimgad%2Fpic%2Fitem%2F6d81800a19d8bc3eb16291f6898ba61ea8d345a7.jpg")
      getFaceInfo("http://gb.cri.cn/mmsource/images/2005/07/20/el050720045.jpg")
      #
