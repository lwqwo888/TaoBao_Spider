# coding=utf-8
# 通过pvs直接找库存
# 优点：速度稍快
# 缺点：无货商品库存没有体现，需手动置0或置为＂无货＂
import re
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def skuid_num(id):
    url = 'https://rate.tmall.com/list_detail_rate.htm?itemId=557200845972&sellerId=645039969&order=3&currentPage=1&'
    headers = {

        "cookie": "ubn=p; ucn=unsz; t=28edc35882e1fcf06bfaa67008da2a8f; cna=XTyQEoI1uE4CAXBfh3IMFSpJ; thw=cn; miid=6347655561018672771; uc3=sg2=WqIrBf2WEDhnXgIg9lOgUXQnkoTeDo019W%2BL27EjCfQ%3D&nk2=rUs9FkCy6Zs6Ew%3D%3D&id2=VWeZAHoeqUWF&vt3=F8dBzLgoJIN4WC0X30I%3D&lg2=VFC%2FuZ9ayeYq2g%3D%3D; lgc=%5Cu6211%5Cu6210%5Cu4F60%5Cu5669%5Cu68A6; tracknick=%5Cu6211%5Cu6210%5Cu4F60%5Cu5669%5Cu68A6; _cc_=WqG3DMC9EA%3D%3D; tg=0; enc=GtOY%2B8mhUi7LXIrV9LqmUl0PYsVpr9BbSzEB9GL%2Fq3i6Czwxxh5mE60CMJjep9GIq4iV04PvQsAGhzOIdrf6iw%3D%3D; mt=ci=-1_0; UM_distinctid=160fe373fd7c89-0f04cad75d123e-393d5f0e-1fa400-160fe373fd8e5a; hng=CN%7Czh-CN%7CCNY%7C156; _m_h5_tk=081b6ec244bfd7ba155325c85a14056e_1516103738466; _m_h5_tk_enc=8531a9b39cfb4a076e45dfad1fba7525; cookie2=16e0f40738dc82c43c53992cb5a26ebb; _tb_token_=3daeebbb3768e; v=0; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; uc1=cookie14=UoTdfYT5TUo4kA%3D%3D; isg=BDo6USLQNOpL5rgFeJZzPiuWi2CcQ9uEDF5FrkQyJ02YN9lxLHiA1B8ng8PrpzZd",
        "referer": "https://item.taobao.com/item.htm?spm=a219r.lmn002.14.174.6f516358W81jq9&id=561495525977&ns=1&abbucket=16",
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",

    }
    html = requests.get(url, headers=headers).text
    print html
    # html = '''
    #     jsonp1306({"rateDetail":{"paginator":{"items":5004,"lastPage":99,"page":1},"rateCount":{"picNum":1136,"shop":0,"total":5397,"used":393},"rateDanceInfo":{"currentMilles":1517644064294,"intervalMilles":8844470880,"showChooseTopic":false,"storeType":4},"rateList":[{"aliMallSeller":false,"anony":true,"appendComment":"","attributes":"","attributesMap":"","aucNumId":"","auctionPicUrl":"","auctionPrice":"","auctionSku":"颜色分类:贝壳粉/S/M/预售1月20号发货;尺码:XL","auctionTitle":"","buyCount":0,"carServiceLocation":"","cmsSource":"天猫","displayRatePic":"","displayRateSum":0,"displayUserLink":"","displayUserNick":"叶***2","displayUserNumId":"","displayUserRateLink":"","dsr":0.0,"fromMall":true,"fromMemory":0,"gmtCreateTime":1517302208000,"goldUser":true,"headExtraPic":"","id":339463228680,"memberIcon":"","pics":["//img.alicdn.com/bao/uploaded/i4/0/TB21SRWpnnI8KJjy0FfXXcdoVXa_!!72115691-0-rate.jpg","//img.alicdn.com/bao/uploaded/i4/0/TB2hbQDo9_I8KJjy0FoXXaFnVXa_!!72115691-0-rate.jpg","//img.alicdn.com/bao/uploaded/i1/0/TB2zYQto_nI8KJjSszgXXc8ApXa_!!72115691-0-rate.jpg","//img.alicdn.com/bao/uploaded/i2/0/TB2GMBMpmfD8KJjSszhXXbIJFXa_!!72115691-0-rate.jpg"],"picsSmall":"","position":"522-11-74,79;522-11-139,145;1822-12-7,19;10120-12-151,161;620-11-0,6;1120-12-102,110;11220-11-197,223;522-11-197,223;620-11-197,223;322-11-146,150;620-11-7,19;1822-11-88,95;20520-11-224,236;620-11-29,38;1822-12-62,66;920-11-237,240;222-11-132,138;1822-11-80,87;1822-12-20,28;920-12-39,51;","rateContent":"衣服挺暖和的，和原来的羽绒服里面一样穿，车上穿一会就出汗，质量太好也会有烦恼，我直接买了件不加绒的毛衣，试试穿出去会不会冷。穿了几天，说说我的感受。版型特别好，上身效果特别好，衣服穿上人显瘦，是我喜欢的，朋友也打算买一件。给大家参考一下：我身高158体重52公斤，穿M码刚刚好，衣服特别好看，颜色很正，拍的时候没有咨询客服，喜欢就拍了，本来还害怕网上的东西会有色差或者质量不好，收到之后还不错，要不是衣服真的漂亮无色差质量好我还真不会评论这一大篇。感觉衣服性价比还是蛮高的，很喜欢~","rateDate":"2018-01-30 16:50:08","reply":"","sellerId":645039969,"serviceRateContent":"","structuredRateList":[],"tamllSweetLevel":0,"tmallSweetPic":"","tradeEndTime":1516591178000,"tradeId":"","useful":true,"userIdEncryption":"","userInfo":"","userVipLevel":0,"userVipPic":""},{"aliMallSeller":false,"anony":true,"appendComment":"","attributes":"","attributesMap":"","aucNumId":"","auctionPicUrl":"","auctionPrice":"","auctionSku":"颜色分类:黑色;尺码:M","auctionTitle":"","buyCount":0,"carServiceLocation":"","cmsSource":"天猫","displayRatePic":"","displayRateSum":0,"displayUserLink":"","displayUserNick":"比***呆","displayUserNumId":"","displayUserRateLink":"","dsr":0.0,"fromMall":true,"fromMemory":0,"gmtCreateTime":1516512141000,"goldUser":false,"headExtraPic":"","id":338526927943,"memberIcon":"","pics":["//img.alicdn.com/bao/uploaded/i2/0/TB2z1Ban0nJ8KJjSszdXXaxuFXa_!!0-rate.jpg","//img.alicdn.com/bao/uploaded/i3/0/TB2O4cZnPnD8KJjSspbXXbbEXXa_!!0-rate.jpg","//img.alicdn.com/bao/uploaded/i2/0/TB2sC_Re0HO8KJjSZFtXXchfXXa_!!0-rate.jpg"],"picsSmall":"","position":"522-12-47,54;920-12-126,128;122-12-90,96;620-12-112,119;1822-12-65,77;620-12-97,104;622-11-0,12;41022-12-133,140;1822-11-55,60;121022-12-105,111;920-11-172,180;220-13-13,25;520-11-181,188;","rateContent":"拿到衣服的第一感觉很厚重，拆开来觉得包装有点简陋了，建议以后换个纸盒的包装，毕竟牌子的东西哦?衣服是H版型的，穿上很显瘦，158.108产后三个月也能穿上，建议瘦小的妹子选小一码，面料是光面的，摸起来很有质感，大口袋是亮点，能装下很多东西。毛领是真的，够大！ 缺点，袖子的毛不够多，摸起来很薄，下半身如果走起路来稍紧，要把最下面的扣子解开才行。不过总体是满意的，算是物有所值的，最开心的是上身很好看?","rateDate":"2018-01-21 13:22:21","reply":"","sellerId":645039969,"serviceRateContent":"","structuredRateList":[],"tamllSweetLevel":0,"tmallSweetPic":"","tradeEndTime":1516511728000,"tradeId":"","useful":true,"userIdEncryption":"","userInfo":"","userVipLevel":0,"userVipPic":""},{"aliMallSeller":false,"anony":true,"appendComment":"","attributes":"","attributesMap":"","aucNumId":"","auctionPicUrl":"","auctionPrice":"","auctionSku":"颜色分类:黑色;尺码:L","auctionTitle":"","buyCount":0,"carServiceLocation":"","cmsSource":"天猫","displayRatePic":"","displayRateSum":0,"displayUserLink":"","displayUserNick":"s***1","displayUserNumId":"","displayUserRateLink":"","dsr":0.0,"fromMall":true,"fromMemory":0,"gmtCreateTime":1517483755000,"goldUser":false,"headExtraPic":"","id":339680888011,"memberIcon":"","pics":["//img.alicdn.com/bao/uploaded/i4/0/TB2eQTrXb9YBuNjy0FgXXcxcXXa_!!0-rate.jpg"],"picsSmall":"","position":"922-12-32,36;922-13-66,71;1822-13-14,21;222-11-9,13;1722-13-37,41;122-11-42,47;622-11-48,52;920-11-58,65;1822-12-22,31;26022-12-72,77;","rateContent":"本人166，61，大小合身，蚕茧型衣服显胖，敞开穿可解决此问题。做工优良，面料虽硬，但羽绒柔软，厚度适中，穿着舒适，适合南方的冬季。毛领稍粗糙，但手感尚可。","rateDate":"2018-02-01 19:15:55","reply":"","sellerId":645039969,"serviceRateContent":"","structuredRateList":[],"tamllSweetLevel":0,"tmallSweetPic":"","tradeEndTime":1517483402000,"tradeId":"","useful":true,"userIdEncryption":"","userInfo":"","userVipLevel":0,"userVipPic":""},{"aliMallSeller":false,"anony":false,"appendComment":{"commentId":"","commentTime":"2018-01-29 14:23:04","content":"忘说了 衣服很薄很薄 特别是袖子 还有衣服领子不是羽绒 是羽绒棉 以后洗过全部会坨在一起 毛领真的很丑 不想退了麻烦 有喜欢的送人了","days":5,"pics":"","reply":""},"attributes":"","attributesMap":"","aucNumId":"","auctionPicUrl":"","auctionPrice":"","auctionSku":"颜色分类:贝壳粉/S/M/预售1月20号发货;尺码:S","auctionTitle":"","buyCount":0,"carServiceLocation":"","cmsSource":"天猫","displayRatePic":"","displayRateSum":0,"displayUserLink":"","displayUserNick":"碧***杉","displayUserNumId":"","displayUserRateLink":"","dsr":0.0,"fromMall":true,"fromMemory":0,"gmtCreateTime":1517205920000,"goldUser":false,"headExtraPic":"","id":339363817546,"memberIcon":"","pics":["//img.alicdn.com/bao/uploaded/i1/0/TB20NuSo8DH8KJjy1zeXXXjepXa_!!0-rate.jpg","//img.alicdn.com/bao/uploaded/i3/0/TB2Oyx5o0fJ8KJjy0FeXXXKEXXa_!!0-rate.jpg","//img.alicdn.com/bao/uploaded/i3/0/TB291tZo_TI8KJjSsphXXcFppXa_!!0-rate.jpg","//img.alicdn.com/bao/uploaded/i4/0/TB2j0ukoZrI8KJjy0FhXXbfnpXa_!!0-rate.jpg","//img.alicdn.com/bao/uploaded/i3/0/TB2IcjxoYYI8KJjy0FaXXbAiVXa_!!0-rate.jpg"],"picsSmall":"","position":"322-12-49,55;920-11-130,137;920-12-126,129;720-11-9,17;822-13-56,61;11022-13-18,31;922-13-82,90;522-13-0,8;620-12-62,72;520-12-117,125;920-12-138,148;322-13-37,48;822-13-73,81;922-13-103,107;\u0001","rateContent":"衣服版型非常一般 和许多小伙伴一样 扣子都扣全下摆不怎么好走路 毛领很大 但是慢慢颜色是真的很丑 毛尖都是黑的 味道跟难闻 衣服都吹了有半月了吧 毛领味道还是很重 还有就是做工很差 最后一张图大家自己看吧 都是线头 这走针也是没谁了 最后价钱摆在这呢 四百多 也就值这样的吧 本人160高100斤 穿s码正好","rateDate":"2018-01-29 14:05:20","reply":"","sellerId":645039969,"serviceRateContent":"","structuredRateList":[],"tamllSweetLevel":0,"tmallSweetPic":"","tradeEndTime":1516698235000,"tradeId":"","useful":true,"userIdEncryption":"","userInfo":"","userVipLevel":0,"userVipPic":""},{"aliMallSeller":false,"anony":true,"appendComment":"","attributes":"","attributesMap":"","aucNumId":"","auctionPicUrl":"","auctionPrice":"","auctionSku":"颜色分类:黑色;尺码:L","auctionTitle":"","buyCount":0,"carServiceLocation":"","cmsSource":"天猫","displayRatePic":"","displayRateSum":0,"displayUserLink":"","displayUserNick":"z***5","displayUserNumId":"","displayUserRateLink":"","dsr":0.0,"fromMall":true,"fromMemory":0,"gmtCreateTime":1517101874000,"goldUser":true,"headExtraPic":"","id":339228628792,"memberIcon":"","pics":["//img.alicdn.com/bao/uploaded/i1/0/TB2bL6SoJrJ8KJjSspaXXXuKpXa_!!0-rate.jpg"],"picsSmall":"","position":"920-11-93,102;322-12-11,21;322-13-28,40;1822-11-28,40;620-12-0,10;222-12-51,56;620-12-79,89;920-11-57,60;920-12-41,50;522-11-22,27;622-13-71,78;","rateContent":"这件羽绒服关注很久了！同事也穿着一件粉色的，样子很好看，不过还是黑色百搭耐脏显瘦！身高163重120+买的L码的，很合适！确实像大家说的那样，不是特别的厚实，不过现在羽绒服都这样！哈哈～总之还是非常满意的！","rateDate":"2018-01-28 09:11:14","reply":"","sellerId":645039969,"serviceRateContent":"","structuredRateList":[],"tamllSweetLevel":0,"tmallSweetPic":"","tradeEndTime":1517101620000,"tradeId":"","useful":true,"userIdEncryption":"","userInfo":"","userVipLevel":0,"userVipPic":""},{"aliMallSeller":false,"anony":true,"appendComment":"","attributes":"","attributesMap":"","aucNumId":"","auctionPicUrl":"","auctionPrice":"","auctionSku":"颜色分类:黑色;尺码:XXL","auctionTitle":"","buyCount":0,"carServiceLocation":"","cmsSource":"天猫","displayRatePic":"","displayRateSum":0,"displayUserLink":"","displayUserNick":"t***3","displayUserNumId":"","displayUserRateLink":"","dsr":0.0,"fromMall":true,"fromMemory":0,"gmtCreateTime":1516507993000,"goldUser":false,"headExtraPic":"","id":338522753289,"memberIcon":"","pics":["//img.alicdn.com/bao/uploaded/i4/0/TB2DCA9nMDD8KJjy0FdXXcjvXXa_!!0-rate.jpg","//img.alicdn.com/bao/uploaded/i4/0/TB2YtAPnPnD8KJjSspbXXbbEXXa_!!0-rate.jpg","//img.alicdn.com/bao/uploaded/i4/0/TB25HkCnMvD8KJjy0FlXXagBFXa_!!0-rate.jpg"],"picsSmall":"","position":"520-11-80,89;920-13-62,69;10120-13-41,54;122-12-30,40;720-11-0,9;222-11-10,14;121022-12-15,22;","rateContent":"宝贝跟预想中的一样，大小刚好，喜欢它的大口袋，后收腰也不错，最大亮点还是大毛领了，虽然没卖家视频拍的那么蓬松，不过也可以了，毛毛上有点脏的，自己弄掉了并不影响，谁叫价位那么美丽呢，在另一电商平台看了许久都要569呢，值得推荐！！","rateDate":"2018-01-21 12:13:13","reply":"","sellerId":645039969,"serviceRateContent":"","structuredRateList":[],"tamllSweetLevel":2,"tmallSweetPic":"tmall-grade-t2-18.png","tradeEndTime":1516507326000,"tradeId":"","useful":true,"userIdEncryption":"","userInfo":"","userVipLevel":0,"userVipPic":""},{"aliMallSeller":false,"anony":true,"appendComment":"","attributes":"","attributesMap":"","aucNumId":"","auctionPicUrl":"","auctionPrice":"","auctionSku":"颜色分类:黑色;尺码:S","auctionTitle":"","buyCount":0,"carServiceLocation":"","cmsSource":"天猫","displayRatePic":"","displayRateSum":0,"displayUserLink":"","displayUserNick":"s***5","displayUserNumId":"","displayUserRateLink":"","dsr":0.0,"fromMall":true,"fromMemory":0,"gmtCreateTime":1517494421000,"goldUser":false,"headExtraPic":"","id":339754148067,"memberIcon":"","pics":["//img.alicdn.com/bao/uploaded/i1/0/TB2WfLHXXOWBuNjy0FiXXXFxVXa_!!0-rate.jpg","//img.alicdn.com/bao/uploaded/i2/0/TB2.SLGXbSYBuNjSspfXXcZCpXa_!!0-rate.jpg","//img.alicdn.com/bao/uploaded/i3/0/TB2Bf8nXdcnBKNjSZR0XXcFqFXa_!!0-rate.jpg"],"picsSmall":"","position":"1822-12-62,91;920-11-44,46;920-11-47,56;920-11-41,43;1822-11-0,7;920-11-38,40;","rateContent":"上身效果非常好，正好赶上下雪天，物流也特别的给力主要是正好赶上我参加会议穿，大爱！大爱！大爱！重要的是事情说三遍(亲亲)&hellip;&hellip;当我买这件衣服的时候我看评论发的图片没有人上身穿黑色的效果 所以我就秀一下，还会光临本店","rateDate":"2018-02-01 22:13:41","reply":"","sellerId":645039969,"serviceRateContent":"","structuredRateList":[],"tamllSweetLevel":0,"tmallSweetPic":"","tradeEndTime":1517494007000,"tradeId":"","useful":true,"userIdEncryption":"","userInfo":"","userVipLevel":0,"userVipPic":""},{"aliMallSeller":false,"anony":true,"appendComment":"","attributes":"","attributesMap":"","aucNumId":"","auctionPicUrl":"","auctionPrice":"","auctionSku":"颜色分类:黑色;尺码:XL","auctionTitle":"","buyCount":0,"carServiceLocation":"","cmsSource":"天猫","displayRatePic":"","displayRateSum":0,"displayUserLink":"","displayUserNick":"王***7","displayUserNumId":"","displayUserRateLink":"","dsr":0.0,"fromMall":true,"fromMemory":0,"gmtCreateTime":1517034887000,"goldUser":false,"headExtraPic":"","id":339175488737,"memberIcon":"","pics":["//img.alicdn.com/bao/uploaded/i2/0/TB2Voc0miqAXuNjy1XdXXaYcVXa_!!0-rate.jpg","//img.alicdn.com/bao/uploaded/i1/0/TB2loVxfpLM8KJjSZFBXXXJHVXa_!!0-rate.jpg","//img.alicdn.com/bao/uploaded/i2/0/TB2.iYYezgy_uJjSZSyXXbqvVXa_!!0-rate.jpg"],"picsSmall":"","position":"1822-11-6,12;622-11-24,26;1822-11-13,15;322-11-27,30;620-12-0,5;222-12-41,50;920-13-58,62;1822-11-31,40;922-11-19,23;122-12-16,18;","rateContent":"衣服收到了，整体效果不错，修身，面料，做工精良，厚实，颜色正，这次下雪穿着很暖和！就是拉链长度不到头，一走路就崩开，不太满意，其他都赞，好评！","rateDate":"2018-01-27 14:34:47","reply":"","sellerId":645039969,"serviceRateContent":"","structuredRateList":[],"tamllSweetLevel":0,"tmallSweetPic":"","tradeEndTime":1517034605000,"tradeId":"","useful":true,"userIdEncryption":"","userInfo":"","userVipLevel":0,"userVipPic":""},{"aliMallSeller":false,"anony":false,"appendComment":"","attributes":"","attributesMap":"","aucNumId":"","auctionPicUrl":"","auctionPrice":"","auctionSku":"颜色分类:黑色;尺码:M","auctionTitle":"","buyCount":0,"carServiceLocation":"","cmsSource":"天猫","displayRatePic":"","displayRateSum":0,"displayUserLink":"","displayUserNick":"w***1","displayUserNumId":"","displayUserRateLink":"","dsr":0.0,"fromMall":true,"fromMemory":0,"gmtCreateTime":1517453045000,"goldUser":false,"headExtraPic":"","id":339677187854,"memberIcon":"","pics":["//img.alicdn.com/bao/uploaded/i1/0/TB2g4KxXeySBuNjy1zdXXXPxFXa_!!0-rate.jpg","//img.alicdn.com/bao/uploaded/i1/0/TB2UuSwXf5TBuNjSspcXXbnGFXa_!!0-rate.jpg"],"picsSmall":"","position":"520-12-109,113;41022-11-41,50;122-12-51,56;920-13-123,128;522-13-104,108;520-12-10,20;722-12-0,9;420-12-114,122;1822-13-57,69;620-12-30,40;920-12-70,75;1822-12-85,91;41022-11-21,29;","rateContent":"这梵高也是大品牌了，做这样的衣服很掉价的，光看看袖子就好了，那家羽绒服会这样做啊，袖子随便一缝就好了，羽绒非常少，在西安这样的下雪天穿凑合，反正也不冷，家里公司都有暖气，就出去穿一下，但这样的衣服怎么穿出去，超级难看，超级掉价，要不是快递不收了，我坚决退货","rateDate":"2018-02-01 10:44:05","reply":"","sellerId":645039969,"serviceRateContent":"","structuredRateList":[],"tamllSweetLevel":0,"tmallSweetPic":"","tradeEndTime":1517372083000,"tradeId":"","useful":true,"userIdEncryption":"","userInfo":"","userVipLevel":0,"userVipPic":""},{"aliMallSeller":false,"anony":true,"appendComment":"","attributes":"","attributesMap":"","aucNumId":"","auctionPicUrl":"","auctionPrice":"","auctionSku":"颜色分类:贝壳粉;尺码:XL","auctionTitle":"","buyCount":0,"carServiceLocation":"","cmsSource":"天猫","displayRatePic":"","displayRateSum":0,"displayUserLink":"","displayUserNick":"婉***晶","displayUserNumId":"","displayUserRateLink":"","dsr":0.0,"fromMall":true,"fromMemory":0,"gmtCreateTime":1517366940000,"goldUser":false,"headExtraPic":"","id":339581005525,"memberIcon":"","pics":["//img.alicdn.com/bao/uploaded/i3/0/TB28BH7fazB9uJjSZFMXXXq4XXa_!!0-rate.jpg","//img.alicdn.com/bao/uploaded/i1/0/TB2jaiVphPI8KJjSspfXXcCFXXa_!!0-rate.jpg","//img.alicdn.com/bao/uploaded/i1/0/TB2bwFEXcpTBeNjSZFqXXa_nVXa_!!0-rate.jpg","//img.alicdn.com/bao/uploaded/i4/0/TB2G_VtpnTI8KJjSsphXXcFppXa_!!0-rate.jpg","//img.alicdn.com/bao/uploaded/i3/0/TB2iTSQeQfb_uJkHFNRXXc3vpXa_!!0-rate.jpg"],"picsSmall":"","position":"920-13-35,41;620-12-42,56;322-11-14,34;1822-11-7,13;722-11-57,65;522-11-0,6;122-11-14,34;","rateContent":"贝壳粉很漂亮，很显肤色白奥！里面的内衬是白色的感觉特干净说明羽绒很白，不钻毛放心买！去年给我闺女也买高梵的羽绒服，所以这个品牌放心，","rateDate":"2018-01-31 10:49:00","reply":"","sellerId":645039969,"serviceRateContent":"","structuredRateList":[],"tamllSweetLevel":0,"tmallSweetPic":"","tradeEndTime":1517366596000,"tradeId":"","useful":true,"userIdEncryption":"","userInfo":"","userVipLevel":0,"userVipPic":""},{"aliMallSeller":false,"anony":false,"appendComment":"","attributes":"","attributesMap":"","aucNumId":"","auctionPicUrl":"","auctionPrice":"","auctionSku":"颜色分类:海沫蓝;尺码:S","auctionTitle":"","buyCount":0,"carServiceLocation":"","cmsSource":"天猫","displayRatePic":"","displayRateSum":0,"displayUserLink":"","displayUserNick":"得***e","displayUserNumId":"","displayUserRateLink":"","dsr":0.0,"fromMall":true,"fromMemory":0,"gmtCreateTime":1517296093000,"goldUser":false,"headExtraPic":"","id":339482620795,"memberIcon":"","pics":["//img.alicdn.com/bao/uploaded/i3/0/TB2.HQio22H8KJjy0FcXXaDlFXa_!!2463290530-0-rate.jpg","//img.alicdn.com/bao/uploaded/i2/0/TB2kcsgo_nI8KJjSszbXXb4KFXa_!!2463290530-0-rate.jpg"],"picsSmall":"","position":"920-11-32,35;620-11-88,94;620-11-62,67;520-12-68,74;122-11-12,18;920-11-75,82;122-11-0,4;920-11-5,11;620-11-36,47;","rateContent":"面料不错，上身也刚刚好，大毛领特好看，同事们都在要链接呢，哈哈，很满意，高梵的衣服没让我失望过，以后我就是高梵的忠实粉丝了，质量杠杠的，价格也很亲民，喜欢就快下手吧，别犹豫了，好东西没的说","rateDate":"2018-01-30 15:08:13","reply":"","sellerId":645039969,"serviceRateContent":"","structuredRateList":[],"tamllSweetLevel":0,"tmallSweetPic":"","tradeEndTime":1517295888000,"tradeId":"","useful":true,"userIdEncryption":"","userInfo":"","userVipLevel":0,"userVipPic":""},{"aliMallSeller":false,"anony":true,"appendComment":"","attributes":"","attributesMap":"","aucNumId":"","auctionPicUrl":"","auctionPrice":"","auctionSku":"颜色分类:黑色;尺码:S","auctionTitle":"","buyCount":0,"carServiceLocation":"","cmsSource":"天猫","displayRatePic":"","displayRateSum":0,"displayUserLink":"","displayUserNick":"比***1","displayUserNumId":"","displayUserRateLink":"","dsr":0.0,"fromMall":true,"fromMemory":0,"gmtCreateTime":1517490311000,"goldUser":false,"headExtraPic":"","id":339804610598,"memberIcon":"","pics":["//img.alicdn.com/bao/uploaded/i4/0/TB2zTxrXljTBKNjSZFNXXasFXXa_!!0-rate.jpg"],"picsSmall":"","position":"522-11-90,94;522-11-13,23;10520-12-46,52;522-11-0,4;422-11-5,12;620-12-68,86;1822-11-115,126;10120-12-32,45;","rateContent":"挺好看的，款式是我喜欢的，毛领也特别特别的漂亮！之前没想到会买，只是抱着试试看的态度下的单，因为有运费险，如果穿着不好看我是打算退了的，但是收到衣服的时候迫不及待的试穿了下，哇撒，真的漂亮！亲们，我不是托噢，从来不评论那么多字的，真的穿着太多人说好看了！","rateDate":"2018-02-01 21:05:11","reply":"","sellerId":645039969,"serviceRateContent":"","structuredRateList":[],"tamllSweetLevel":0,"tmallSweetPic":"","tradeEndTime":1517203275000,"tradeId":"","useful":true,"userIdEncryption":"","userInfo":"","userVipLevel":0,"userVipPic":""},{"aliMallSeller":false,"anony":false,"appendComment":"","attributes":"","attributesMap":"","aucNumId":"","auctionPicUrl":"","auctionPrice":"","auctionSku":"颜色分类:贝壳粉;尺码:XL","auctionTitle":"","buyCount":0,"carServiceLocation":"","cmsSource":"天猫","displayRatePic":"","displayRateSum":0,"displayUserLink":"","displayUserNick":"飞***1","displayUserNumId":"","displayUserRateLink":"","dsr":0.0,"fromMall":true,"fromMemory":0,"gmtCreateTime":1517395037000,"goldUser":false,"headExtraPic":"","id":339626820976,"memberIcon":"","pics":["//img.alicdn.com/bao/uploaded/i1/0/TB2OPQ3fvjM8KJjSZFNXXbQjFXa_!!0-rate.jpg","//img.alicdn.com/bao/uploaded/i2/0/TB241rfXmtYBeNjSspaXXaOOFXa_!!0-rate.jpg","//img.alicdn.com/bao/uploaded/i1/0/TB2SU_bePgy_uJjSZSyXXbqvVXa_!!0-rate.jpg"],"picsSmall":"","position":"622-13-24,46;1822-12-24,46;1120-11-47,53;522-11-0,23;620-11-0,23;81022-11-54,66;","rateContent":"这羽绒服太值了光看毛领就显得很高档样式也很时尚！虽说不是特厚的那种但石家庄这温度穿着肯定不冷，媳妇说挺暖和，后面还能自己配个腰带不错。绝对给五星！","rateDate":"2018-01-31 18:37:17","reply":"","sellerId":645039969,"serviceRateContent":"","structuredRateList":[],"tamllSweetLevel":3,"tmallSweetPic":"tmall-grade-t3-18.png","tradeEndTime":1517394638000,"tradeId":"","useful":true,"userIdEncryption":"","userInfo":"","userVipLevel":0,"userVipPic":""},{"aliMallSeller":false,"anony":false,"appendComment":"","attributes":"","attributesMap":"","aucNumId":"","auctionPicUrl":"","auctionPrice":"","auctionSku":"颜色分类:黑色;尺码:L","auctionTitle":"","buyCount":0,"carServiceLocation":"","cmsSource":"天猫","displayRatePic":"","displayRateSum":0,"displayUserLink":"","displayUserNick":"百***7","displayUserNumId":"","displayUserRateLink":"","dsr":0.0,"fromMall":true,"fromMemory":0,"gmtCreateTime":1517215830000,"goldUser":false,"headExtraPic":"","id":339391728050,"memberIcon":"","pics":["//img.alicdn.com/bao/uploaded/i1/0/TB2wMtUeQfb_uJkSnhJXXbdDVXa_!!0-rate.jpg","//img.alicdn.com/bao/uploaded/i1/0/TB2sBHrftHO8KJjSZFHXXbWJFXa_!!0-rate.jpg","//img.alicdn.com/bao/uploaded/i3/0/TB2CMYNo9fD8KJjSszhXXbIJFXa_!!0-rate.jpg"],"picsSmall":"","position":"121022-12-30,37;920-11-45,55;920-12-45,55;1722-11-23,29;122-12-15,22;620-11-6,14;920-11-38,44;","rateContent":"年货节买的，收到宝贝后很惊喜，亮点就是大毛领，貉子毛柔柔的，还有两个大口袋，本人超级喜欢，喜欢的亲们不要犹豫了，赶快下手吧！！","rateDate":"2018-01-29 16:50:30","reply":"","sellerId":645039969,"serviceRateContent":"","structuredRateList":[],"tamllSweetLevel":0,"tmallSweetPic":"","tradeEndTime":1517215633000,"tradeId":"","useful":true,"userIdEncryption":"","userInfo":"","userVipLevel":0,"userVipPic":""},{"aliMallSeller":false,"anony":false,"appendComment":"","attributes":"","attributesMap":"","aucNumId":"","auctionPicUrl":"","auctionPrice":"","auctionSku":"颜色分类:黑色;尺码:S","auctionTitle":"","buyCount":0,"carServiceLocation":"","cmsSource":"天猫","displayRatePic":"","displayRateSum":0,"displayUserLink":"","displayUserNick":"t***2","displayUserNumId":"","displayUserRateLink":"","dsr":0.0,"fromMall":true,"fromMemory":0,"gmtCreateTime":1517303062000,"goldUser":false,"headExtraPic":"","id":339497855950,"memberIcon":"","pics":["//img.alicdn.com/bao/uploaded/i1/0/TB2_tpaXmBYBeNjy0FeXXbnmFXa_!!858129030-0-rate.jpg","//img.alicdn.com/bao/uploaded/i1/0/TB2pcs7o8DH8KJjSspnXXbNAVXa_!!858129030-0-rate.jpg","//img.alicdn.com/bao/uploaded/i4/0/TB2No74o4HI8KJjy1zbXXaxdpXa_!!858129030-0-rate.jpg","//img.alicdn.com/bao/uploaded/i2/0/TB2D1MUo3LD8KJjSszeXXaGRpXa_!!858129030-0-rate.jpg","//img.alicdn.com/bao/uploaded/i1/0/TB2Ps67fqLN8KJjSZFmXXcQ6XXa_!!858129030-0-rate.jpg"],"picsSmall":"","position":"920-11-92,99;622-11-13,16;620-12-134,137;520-12-138,142;122-12-0,4;920-12-82,83;16022-12-79,81;920-11-143,147;122-12-75,78;920-11-5,9;121022-12-33,37;131022-12-59,62;620-12-88,90;1822-11-50,57;1822-12-115,116;","rateContent":"衣服面料 超级满意 滑的 很厚实！  160身高 S 到膝盖下！ 兜子很大 ！ 160 体重90斤。穿着不肥也不瘦！ 帽子的 毛领.  很大. 但是 貉子毛 成分 少！刚打开 衣服  新毛领稍微掉点 伏毛！    收到货 还没有 穿 不知道 会不会跑绒！ 如果不跑绒 这衣服 这个价位、属于完美！！","rateDate":"2018-01-30 17:04:22","reply":"","sellerId":645039969,"serviceRateContent":"","structuredRateList":[],"tamllSweetLevel":0,"tmallSweetPic":"","tradeEndTime":1517302557000,"tradeId":"","useful":true,"userIdEncryption":"","userInfo":"","userVipLevel":0,"userVipPic":""},{"aliMallSeller":false,"anony":true,"appendComment":"","attributes":"","attributesMap":"","aucNumId":"","auctionPicUrl":"","auctionPrice":"","auctionSku":"颜色分类:黑色;尺码:M","auctionTitle":"","buyCount":0,"carServiceLocation":"","cmsSource":"天猫","displayRatePic":"","displayRateSum":0,"displayUserLink":"","displayUserNick":"l***o","displayUserNumId":"","displayUserRateLink":"","dsr":0.0,"fromMall":true,"fromMemory":0,"gmtCreateTime":1517478863000,"goldUser":false,"headExtraPic":"","id":339734019115,"memberIcon":"","pics":["//img.alicdn.com/bao/uploaded/i1/0/TB2kErjXb5YBuNjSspoXXbeNFXa_!!0-rate.jpg","//img.alicdn.com/bao/uploaded/i3/0/TB2wqJZXlmWBuNkSndVXXcsApXa_!!0-rate.jpg"],"picsSmall":"","position":"920-11-18,22;622-11-13,17;121022-12-7,12;1822-11-0,6;520-11-23,31;","rateContent":"上身效果很好，喜欢大口袋，面料厚实，值得够买，优惠卷下单很划算！","rateDate":"2018-02-01 17:54:23","reply":"","sellerId":645039969,"serviceRateContent":"","structuredRateList":[],"tamllSweetLevel":0,"tmallSweetPic":"","tradeEndTime":1517478250000,"tradeId":"","useful":true,"userIdEncryption":"","userInfo":"","userVipLevel":0,"userVipPic":""},{"aliMallSeller":false,"anony":false,"appendComment":"","attributes":"","attributesMap":"","aucNumId":"","auctionPicUrl":"","auctionPrice":"","auctionSku":"颜色分类:黑色;尺码:L","auctionTitle":"","buyCount":0,"carServiceLocation":"","cmsSource":"天猫","displayRatePic":"","displayRateSum":0,"displayUserLink":"","displayUserNick":"d***1","displayUserNumId":"","displayUserRateLink":"","dsr":0.0,"fromMall":true,"fromMemory":0,"gmtCreateTime":1517049692000,"goldUser":false,"headExtraPic":"","id":339138847690,"memberIcon":"","pics":"","picsSmall":"","position":"122-12-29,39;220-11-24,28;622-11-19,23;222-12-46,54;","rateContent":"Very good?,品牌就是有保证，衣服厚实，包装完美，大口袋和大毛领是最爱，身高162，特意选了个大码L，效果也不错?，今年过年就靠它了。近期有考虑入手羽绒服的可以放心购买哦???","rateDate":"2018-01-27 18:41:32","reply":"","sellerId":645039969,"serviceRateContent":"","structuredRateList":[],"tamllSweetLevel":2,"tmallSweetPic":"tmall-grade-t2-18.png","tradeEndTime":1516623114000,"tradeId":"","useful":true,"userIdEncryption":"","userInfo":"","userVipLevel":0,"userVipPic":""},{"aliMallSeller":false,"anony":true,"appendComment":"","attributes":"","attributesMap":"","aucNumId":"","auctionPicUrl":"","auctionPrice":"","auctionSku":"颜色分类:贝壳粉;尺码:S","auctionTitle":"","buyCount":0,"carServiceLocation":"","cmsSource":"天猫","displayRatePic":"","displayRateSum":0,"displayUserLink":"","displayUserNick":"冰***3","displayUserNumId":"","displayUserRateLink":"","dsr":0.0,"fromMall":true,"fromMemory":0,"gmtCreateTime":1517028630000,"goldUser":false,"headExtraPic":"","id":339151628892,"memberIcon":"","pics":["//img.alicdn.com/bao/uploaded/i1/0/TB2M20rftLO8KJjSZFxXXaGEVXa_!!0-rate.jpg"],"picsSmall":"","position":"920-11-65,74;222-11-81,84;920-11-32,40;620-12-41,55;622-13-75,80;1722-13-0,14;222-12-24,28;920-11-85,92;122-12-0,14;","rateContent":"面料是那种常见的有点硬的那种，163.100斤，买的s码。正好。很满意的一次购物，今年在淘宝上买了好几个羽绒服，都退了觉得不合适。但是这个真的很喜欢，不是特别厚，很合身。毛毛领也很好的。","rateDate":"2018-01-27 12:50:30","reply":"","sellerId":645039969,"serviceRateContent":"","structuredRateList":[],"tamllSweetLevel":0,"tmallSweetPic":"","tradeEndTime":1517028325000,"tradeId":"","useful":true,"userIdEncryption":"","userInfo":"","userVipLevel":0,"userVipPic":""},{"aliMallSeller":false,"anony":true,"appendComment":"","attributes":"","attributesMap":"","aucNumId":"","auctionPicUrl":"","auctionPrice":"","auctionSku":"颜色分类:黑色;尺码:S","auctionTitle":"","buyCount":0,"carServiceLocation":"","cmsSource":"天猫","displayRatePic":"","displayRateSum":0,"displayUserLink":"","displayUserNick":"t***7","displayUserNumId":"","displayUserRateLink":"","dsr":0.0,"fromMall":true,"fromMemory":0,"gmtCreateTime":1517453388000,"goldUser":false,"headExtraPic":"","id":339681516946,"memberIcon":"","pics":["//img.alicdn.com/bao/uploaded/i2/0/TB2ZOOiXndYBeNkSmLyXXXfnVXa_!!0-rate.jpg","//img.alicdn.com/bao/uploaded/i4/0/TB2svGvXXGWBuNjy0FbXXb4sXXa_!!0-rate.jpg","//img.alicdn.com/bao/uploaded/i2/0/TB2kI1vXkSWBuNjSszdXXbeSpXa_!!0-rate.jpg"],"picsSmall":"","position":"1822-12-39,46;41022-12-28,38;1822-12-6,13;422-11-14,21;622-13-22,27;","rateContent":"这几天下雪，穿了才来评价的，款式是我喜欢的，就是太薄了，尤其两袖子就是两层布，零下穿着有点冷，建议改进，再来光顾！","rateDate":"2018-02-01 10:49:48","reply":"","sellerId":645039969,"serviceRateContent":"","structuredRateList":[],"tamllSweetLevel":0,"tmallSweetPic":"","tradeEndTime":1517210176000,"tradeId":"","useful":true,"userIdEncryption":"","userInfo":"","userVipLevel":0,"userVipPic":""},{"aliMallSeller":false,"anony":true,"appendComment":"","attributes":"","attributesMap":"","aucNumId":"","auctionPicUrl":"","auctionPrice":"","auctionSku":"颜色分类:黑色;尺码:M","auctionTitle":"","buyCount":0,"carServiceLocation":"","cmsSource":"天猫","displayRatePic":"","displayRateSum":0,"displayUserLink":"","displayUserNick":"涵***9","displayUserNumId":"","displayUserRateLink":"","dsr":0.0,"fromMall":true,"fromMemory":0,"gmtCreateTime":1516862725000,"goldUser":false,"headExtraPic":"","id":338994098987,"memberIcon":"","pics":["//img.alicdn.com/bao/uploaded/i2/0/TB2b_XmoCYH8KJjSspdXXcRgVXa_!!0-rate.jpg"],"picsSmall":"","position":"1822-12-74,80;920-11-64,69;920-12-0,4;920-12-26,29;520-11-5,17;11022-12-42,48;920-11-88,92;1822-11-30,34;920-12-88,92;1822-12-35,41;920-11-49,57;920-12-81,87;620-13-18,25;322-12-70,73;","rateContent":"毛领很大，469这个价钱也差不多了，这款衣服中间肥，下面瘦，穿上保暖，在家也能常穿，下面扣子扣上，往上一翻就可以了，还不往下掉。而且还暖和。黑色的，能穿的就一些，宝宝刚1岁多，正淘气呢，经常要抱抱，也不怕","rateDate":"2018-01-25 14:45:25","reply":"","sellerId":645039969,"serviceRateContent":"","structuredRateList":[],"tamllSweetLevel":0,"tmallSweetPic":"","tradeEndTime":1516862207000,"tradeId":"","useful":true,"userIdEncryption":"","userInfo":"","userVipLevel":0,"userVipPic":""}],"searchinfo":"","tags":""}})
    # '''
    img_url_obj = re.compile(r'(//img.*?\.(jpg|png|SS2|gif|mp4))', re.S)
    img_url_list = img_url_obj.findall(html)
    list = []
    for i in img_url_list:
        print i[0]
        list.append(i[0])
    print len(list)
skuid_num(557200845972)



'''
https://rate.taobao.com/feedRateList.htm?auctionNumId=562441235623&userNumId=747719712&currentPageNum=1&pageSize=20&rateType=3&orderType=sort_weight&attribute=&sku=&hasSku=false&folded=0&ua=098%23E1hvK9vWvRhvUpCkvvvvvjiPPLSO0jrbP2dvtjYHPmPhsj3CRFsWsj3UPLSy0jlbPu6Cvvyv2nem1Gwv5jWCvpvVvmvvvhCvkphvC99vvOC0B4yCvv9vvUmQVgTfRqyCvm9vvvvvphvvvvvvC8ivpv3evvm2phCvhRvvvUnvphvppvvv96CvpCCvmphvLCCIqpvjNtjUwJh1e11yFaB1gBQfjVoxzjj35CIwXE5hkbmAdcwuYUkU%2Bb8ram56QbmxdB%2BaUWmQiNoOejnv%2BneYiLUpwhKn3w0xhE9PvpvhMMGvv2yCvvpvvvvviQhvCvvv9U8jvpvhvvpvvUhCvvsNqzrwlxdNzYY18aQtvpvhvvvvvv%3D%3D&_ksTS=1517660019415_1989&callback=jsonp_tbcrate_reviews_list
'''
'''
https://rate.tmall.com/list_detail_rate.htm?itemId=557200845972&spuId=869019630&sellerId=645039969&order=3&currentPage=1&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hvd9vEvbQvUvCkvvvvvjiPPLSO6jYPRFswQjEUPmPysjE8Rs5hQjEVR2dwQjnbRphvCvvvphvCvpvVvvBvpvvvkphvC9hvpyPOs8yCvv9vvhh94OiWhqyCvm9vvhCvvvvvvvvvBGwvvU2mvvCj1Qvvv3QvvhNjvvvmmvvvBGwvvvUUmphvLvvVajpa1EeKdigDNKBldf8rejOdafm653u4wZ4Q0fJ6W3CQog0HKfUpVcEUAXZTKFyzOvxrl8TJ%2Bull88AURdh6h7QHYWA4e3%2B7nDyPvpvhvv2MMTwCvvpvvhHh3QhvCvmvphv%3D&isg=BD8_wllXWQP0t10l7lYo6HtCzhMJjPaHkUngfdEMxe444F9i2fQjFr3yJrIeuGs-&needFold=0&_ksTS=1517644063554_1305&callback=jsonp1306
'''
'''

'''