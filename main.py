import streamlit as sl
import json
import datetime
import pytz
cn = pytz.country_timezones("cn")[0]
tz = pytz.timezone(cn)
page = sl.sidebar.radio('2018级6班',["恩师寄语","同学感悟","留言板","照片墙","班级合照"])
def home_liuyan():
    sl.title("留言板")
    with open("lyb_json.json",'r') as f:
        mes_list = json.load(f)
    mes_str = '欢迎来到留言板模块！请注意使用文明用语\n\n'
    for i in mes_list:
        mes_str += i[0] + "：" + i[1] + "[" +i[2] + "]\n\n"
    sl.code(mes_str,language="python")
    inm = sl.text_input("I'm")
    sl.info(f"用户名：{inm}")
    new_mes = sl.text_input("想要说的话……")
    but = sl.button("发送✈️")
    if inm and new_mes and but:
        time = str(datetime.datetime.now(tz=tz))
        mes_list.append([inm,new_mes,time[:19]])
        with open("lyb_json.json",'w') as f:
            json.dump(mes_list,f)
        sl.success("发送成功！刷新网页以查看最新留言板")
    sl.image("prop/xcy.jpg")

def home_hezhao():
    sl.title("入学合照🌈")
    sl.image("prop/g1.jpg")
    sl.title("毕业合照🎓")
    #sl.image("g6.jpg")
    sl.info("暂未拍摄🙇敬请期待")
    sl.title("")
    sl.image("prop/xcy.jpg")

def home_classmate():
    tab1,tab2,tab3,tab4,tab5,tab6 = sl.tabs(["蔡柳洋","李修远","马麟轩","马明宇","巫京辉","吴铭清"])
    tab7,tab8,tab9,tab10,tab11,tab12 = sl.tabs(["伍元希","于儆同","于芃博","袁航","曹颂元","曹涵度"])
    tab13,tab14,tab15,tab16,tab17,tab18 = sl.tabs(["曾天娇","陈思成","陈紫云","胡楠浠","姜琇实","金广艺"])
    tab19,tab20,tab21,tab22,tab23,tab24 = sl.tabs(["李思慧","李昕桐","李彦玥","李姃悦","崔程澎","林嘉欣"])
    tab25,tab26,tab27,tab28,tab29,tab30 = sl.tabs(["秦梓桐","汤亦安","王将旗","吴浟然","张然","周兴彤"])
    tab31,tab32,tab33,tab34,tab35,tab36 = sl.tabs(["朱涵钰","朱墨尘","朱颜乐","房业翔","郑伍七七","盖怀宇"])
    tab37,tab38,tab39,tab40,tab41 = sl.tabs(["巩骏修","雷家铭","李伯犀","李慕","刘大可"])
    with tab1:
        sl.info("制作中<(＿　＿)>敬请期待")
        # sl.image(f"pict/{tab}.jpg")
    with tab2:
        sl.info("制作中<(＿　＿)>敬请期待")
        # sl.image(f"pict/{tab}.jpg")
    with tab3:
        sl.info("制作中<(＿　＿)>敬请期待")
        # sl.image(f"pict/{tab}.jpg")
    with tab4:
        sl.info("制作中<(＿　＿)>敬请期待")
        # sl.image(f"pict/{tab}.jpg")
    with tab5:
        sl.info("制作中<(＿　＿)>敬请期待")
        # sl.image(f"pict/{tab}.jpg")
    with tab6:
        sl.info("制作中<(＿　＿)>敬请期待")
        # sl.image(f"pict/{tab}.jpg")
    with tab7:
        sl.info("制作中<(＿　＿)>敬请期待")
        # sl.image(f"pict/{tab}.jpg")
    with tab8:
        sl.info("制作中<(＿　＿)>敬请期待")
        # sl.image(f"pict/{tab}.jpg")
    with tab9:
        sl.info("制作中<(＿　＿)>敬请期待")
        # sl.image(f"pict/{tab}.jpg")
    with tab10:
        sl.info("制作中<(＿　＿)>敬请期待")
        # sl.image(f"pict/{tab}.jpg")
    with tab11:
        sl.info("制作中<(＿　＿)>敬请期待")
        # sl.image(f"pict/{tab}.jpg")
    with tab12:
        sl.info("制作中<(＿　＿)>敬请期待")
        # sl.image(f"pict/{tab}.jpg")
    with tab13:
        sl.info("制作中<(＿　＿)>敬请期待")
        # sl.image(f"pict/{tab}.jpg")
    with tab14:
        sl.info("制作中<(＿　＿)>敬请期待")
        # sl.image(f"pict/{tab}.jpg")
    with tab15:
        sl.info("制作中<(＿　＿)>敬请期待")
        # sl.image(f"pict/{tab}.jpg")
    with tab16:
        sl.info("制作中<(＿　＿)>敬请期待")
        # sl.image(f"pict/{tab}.jpg")
    with tab17:
        sl.info("制作中<(＿　＿)>敬请期待")
        # sl.image(f"pict/{tab}.jpg")
    with tab18:
        sl.info("制作中<(＿　＿)>敬请期待")
        # sl.image(f"pict/{tab}.jpg")
    with tab19:
        sl.info("制作中<(＿　＿)>敬请期待")
        # sl.image(f"pict/{tab}.jpg")
    with tab20:
        sl.info("制作中<(＿　＿)>敬请期待")
        # sl.image(f"pict/{tab}.jpg")
    with tab21:
        sl.info("制作中<(＿　＿)>敬请期待")
        # sl.image(f"pict/{tab}.jpg")
    with tab22:
        sl.info("制作中<(＿　＿)>敬请期待")
        # sl.image(f"pict/{tab}.jpg")
    with tab23:
        sl.info("制作中<(＿　＿)>敬请期待")
        # sl.image(f"pict/{tab}.jpg")
    with tab24:
        sl.info("制作中<(＿　＿)>敬请期待")
        # sl.image(f"pict/{tab}.jpg")
    with tab25:
        sl.info("制作中<(＿　＿)>敬请期待")
        # sl.image(f"pict/{tab}.jpg")
    with tab26:
        sl.info("制作中<(＿　＿)>敬请期待")
        # sl.image(f"pict/{tab}.jpg")
    with tab27:
        sl.info("制作中<(＿　＿)>敬请期待")
        # sl.image(f"pict/{tab}.jpg")
    with tab28:
        sl.info("制作中<(＿　＿)>敬请期待")
        # sl.image(f"pict/{tab}.jpg")
    with tab29:
        sl.info("制作中<(＿　＿)>敬请期待")
        # sl.image(f"pict/{tab}.jpg")
    with tab30:
        sl.info("制作中<(＿　＿)>敬请期待")
        # sl.image(f"pict/{tab}.jpg")
    with tab31:
        sl.info("制作中<(＿　＿)>敬请期待")
        # sl.image(f"pict/{tab}.jpg")
    with tab32:
        sl.info("制作中<(＿　＿)>敬请期待")
        # sl.image(f"pict/{tab}.jpg")
    with tab33:
        sl.info("制作中<(＿　＿)>敬请期待")
        # sl.image(f"pict/{tab}.jpg")
    with tab34:
        sl.info("制作中<(＿　＿)>敬请期待")
        # sl.image(f"pict/{tab}.jpg")
    with tab35:
        sl.info("制作中<(＿　＿)>敬请期待")
        # sl.image(f"pict/{tab}.jpg")
    with tab36:
        sl.info("制作中<(＿　＿)>敬请期待")
        # sl.image(f"pict/{tab}.jpg")
    with tab37:
        sl.info("制作中<(＿　＿)>敬请期待")
        # sl.image(f"pict/{tab}.jpg")
    with tab38:
        sl.info("制作中<(＿　＿)>敬请期待")
        # sl.image(f"pict/{tab}.jpg")
    with tab39:
        sl.info("制作中<(＿　＿)>敬请期待")
        # sl.image(f"pict/{tab}.jpg")
    with tab40:
        sl.info("制作中<(＿　＿)>敬请期待")
        # sl.image(f"pict/{tab}.jpg")
    with tab41:
        sl.info("制作中<(＿　＿)>敬请期待")
        # sl.image(f"pict/{tab}.jpg")
    sl.image("prop/xcy.jpg")

def home_teacher():
    t1,t2,t3,t4 = sl.tabs(["一年级班主任\n孙莉莉老师","二~四年级班主任\n韩坤丽老师","五年级班主任\n巴文红老师","六年级班主任\n李心言老师"])
    t5,t6 = sl.tabs(["数学老师\n李爱民","英语老师\n石爱军"])
    with t1:
        sl.info("制作中<(＿　＿)>敬请期待")
        # sl.image(f"pict/{t}.jpg")
    with t2:
        sl.info("制作中<(＿　＿)>敬请期待")
        # sl.image(f"pict/{t}.jpg")
    with t3:
        sl.info("制作中<(＿　＿)>敬请期待")
        # sl.image(f"pict/{t}.jpg")
    with t4:
        sl.info("制作中<(＿　＿)>敬请期待")
        # sl.image(f"pict/{t}.jpg")
    with t5:
        sl.info("制作中<(＿　＿)>敬请期待")
        # sl.image(f"pict/{t}.jpg")
    with t6:
        sl.info("制作中<(＿　＿)>敬请期待")
        # sl.image(f"pict/{t}.jpg")
    sl.image("prop/xcy.jpg")

def home_pict():
    sl.info("制作中<(＿　＿)>敬请期待")
    #循环生成照片
    sl.image("prop/xcy.jpg")

if(page=="留言板"):
    home_liuyan()
elif(page=="班级合照"):
    home_hezhao()
elif(page=="同学感悟"):
    home_classmate()
elif(page=="恩师寄语"):
    home_teacher()
elif(page=="照片墙"):
    home_pict()