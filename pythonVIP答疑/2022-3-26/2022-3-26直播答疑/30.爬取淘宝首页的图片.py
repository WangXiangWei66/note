# coding:utf-8
# author:杨淑娟
3
import requests
url='http://img.alicdn.com/bao/uploaded/i1/2058819884/O1CN01VDUzES2MsvLbIST0G_!!0-item_pic.jpg_400x400q90.jpg' # _.webp
headers={
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
'cookie': 'cna=04FlGmClw1kCAWovQsCxhgxS; tracknick=%5Cu6768%5Cu6DD1%5Cu5A1F19820926; enc=Ho0R7kY32pN%2FSCM5HxEbP34UPp7uy%2Bzlf7P0EjzwxdynyrIkLikfK6SVTizjWtCe8UodHpwtYKDC%2FTw3q4Dx%2FQ%3D%3D; thw=cn; cookie2=1484d1fc8b353c90345b2c14543c2bbf; t=b86a0f1aebaee004123771ad1834a554; _tb_token_=3eef13f7957eb; xlly_s=1; _samesite_flag_=true; sgcookie=E100PfjYDWEbGCoUAVVs5X9GTczaS9QxDEWFFCi66Cg%2FL4CeLSvHOZTagyqdI2oIG6EzArQWVu%2BH3KdlagEqSNkrOTLhbT5bGjQTPBuz35QGpMU%3D; unb=157009061; uc3=vt3=F8dCvCoovAKtjDzHC04%3D&nk2=suF1TCukb8UM4oF6B8g%3D&id2=UoTbnVhZ73sG&lg2=W5iHLLyFOGW7aA%3D%3D; csg=0e4c8175; lgc=%5Cu6768%5Cu6DD1%5Cu5A1F19820926; cancelledSubSites=empty; cookie17=UoTbnVhZ73sG; dnk=%5Cu6768%5Cu6DD1%5Cu5A1F19820926; skt=c75ac825c812af8a; existShop=MTY0ODI4ODQ0Mw%3D%3D; uc4=nk4=0%40sOkt5gUlWRkCGCmLn2NJ0xiZbkdUA1tz7Q%3D%3D&id4=0%40UOxxY5n5Curx%2B7bnlkEeAnst5iE%3D; _cc_=URm48syIZQ%3D%3D; _l_g_=Ug%3D%3D; sg=618; _nk_=%5Cu6768%5Cu6DD1%5Cu5A1F19820926; cookie1=U7KqVJazNZRejLezTG%2FN1PoIRweTrpNKZzURldtk8CY%3D; mt=ci=26_1; _m_h5_tk=2bba0fc5e00c752aff3969d4fb0987f7_1648310964348; _m_h5_tk_enc=095c510560dc2bf6d39c4e369ce513f4; uc1=cookie14=UoewCLKrNW3M5g%3D%3D&cookie15=WqG3DMC9VAQiUQ%3D%3D&cookie21=V32FPkk%2Fhodroid0QSjisQ%3D%3D&cookie16=UtASsssmPlP%2Ff1IHDsDaPRu%2BPw%3',

'if-none-match': 'W/"18846-v2Q8MUjuuzvuagZJS5n1db2ppS0"'

}
resp=requests.get(url,headers=headers)
with open('a.jpg','wb') as file :
    file.write(resp.content)