#!usr/bin/env python
#coding=utf-8

from Tkinter import  *
import time
from grad_pro.wave_data_core import energy_wave_data, file_wave_open
from grad_pro.wave_data_core import init_wave_data, abs_wave_data

from grad_pro.wave_data_core import wave_data_dispaly
from _ast import Pass

USERNAME = "1"
USERKEY  = "1"
#由于出了点问题。。在这里定义了全局变量。。
global value_left, value_right
wave_data = file_wave_open()
#实例化
root = Tk()
#主菜单
def menu_main_outer():
    global root
    menu_test = Menu(root)
    
    wenjian_test = Menu(menu_test)
    for item in ['新建', '保存', '打开', '最近']:
        wenjian_test.add_command(label = item)
    bianji_test = Menu(menu_test)
    for item in ['复制', '粘贴', '删除']:
        bianji_test.add_command(label= item)
    shitu_test = Menu(menu_test)
    for item in ['功能块1', '功能块2', '功能块3']:
        shitu_test.add_command(label = item)
    guanyu_test = Menu(menu_test)
    for item in ['功能块1', '功能块2', '功能块3']:
        guanyu_test.add_command(label = item)
    bangzhu_test = Menu(menu_test)
    for item in ['功能块1', '功能块2', '功能块3', '功能块4']:
        bangzhu_test.add_command(label = item)
    sousuo_test = Menu(menu_test)
    for item in ['功能块1', '功能块2', '功能块3']:
        sousuo_test.add_command(label= item)
    chuangkou_test = Menu(menu_test)
    for item in ['功能块1', '功能块2', '功能块3']:
        chuangkou_test.add_command(label = item)
    gongju_test = Menu(menu_test)
    for item in ['功能块1', '功能块2', '功能块3']:
        gongju_test.add_command(label = item)

    menu_test.add_cascade(label = "文件", menu = wenjian_test)
    menu_test.add_cascade(label = "编辑", menu = bianji_test)
    menu_test.add_cascade(label = "视图", menu = shitu_test)
    menu_test.add_cascade(label = "工具", menu = gongju_test)
    menu_test.add_cascade(label = "搜索", menu = sousuo_test)
    menu_test.add_cascade(label = "窗口", menu = chuangkou_test)
    menu_test.add_cascade(label = "关于", menu = guanyu_test)
    menu_test.add_cascade(label = "帮助", menu = bangzhu_test)
    
    return menu_test

#鼠标右键触发
def menu_right_test():
    global root
    Label(root, text= "").grid()
    
#鼠标右击事件触发 
def meun_right_outer():
    menubar = Menu(root)
    for item in ['复制', '粘贴', '剪贴']:
        menubar.add_command(label = item)
    
    menubar.add_command(label = "打开", command = menu_right_test)
    return menubar
#将右键菜单的句柄拿出来
MENUBAR = menu_main_outer()
def pop(event):
    global MENUBAR
    MENUBAR.post(event.x_root, event.y_root)  
#label   
def label_outer():
    
    label_a = Label(root, text='            ', font=('Arial', 20))  #设置标签字体的初始大小
    label_b = Label(root, text='智能语音识别系统', background="yellow", font=('Arial', 20))
    label_c = Label(root, text='     --中北大学--',background="yellow", font=('Arial', 15))
    label_a.grid(row = 0, column = 0)
    label_b.grid(row = 1, column = 1)
    label_c.grid(row = 2, column = 1)
#窗口大小
def size_outer():
    global root
    root.geometry("640x400")  
#标题   
def title_outer():
    global root
    root.title("智能语音识别系统")

#登陆认证
def reg_demo():
    
    global E1, E2, C
    s1 =  E1.get()
    s2 =  E2.get()
    t1 = len(s1)
    t2 = len(s2)
    if s1 == USERNAME and s2 == USERKEY :
        C["text"] = "登陆成功"
        loading_display()
        #这里才是新的开始，，，，！！！！让我们开始吧 ，，
        root.destroy()
        root_sys_outer()
        
    else:
        C["text"] = "登陆失败"
        E1.delete(0, t1)
        E2.delete(0, t2)
#登陆        
def reg_outer():
    first = Label(root, text="用户名：")
    first.grid(row = 3, column = 1, sticky = E)
    e1 = Entry(root)
    e1.grid(row = 3, column = 2, sticky = W)
    
    second = Label(root, text="密码：")
    second.grid(row = 4, column = 1, sticky = E)
    e2 = Entry(root)
    e2["show"] = "*"
    e2.grid(row = 4, column = 2, sticky = W)
    
    button_load = Button(root, text="登陆", command=reg_demo)
    button_load.grid(row = 5, column = 3)
    c = Label(root, text="")
    c.grid(row = 5, column = 1, sticky = E)
    #参数传递
    global E1, E2, C
    E1, E2, C = e1, e2, c
    return e1, e2, c

#进度条的加载
def loading_display():
    loading = " "
    for item in range(3) :
        label_d = Label(root, text=loading, background = "red", font=('Arial', 15))#设置标签字体的初始大
        label_d.grid(row = 7, column = 2)
        time.sleep(0.0)
        loading = loading + "*"

# listbox 
def listbox_outer(root_sys):
    
    listba  = Listbox(root_sys)          #  创建两个列表组件
    listbb = Listbox(root_sys)
    for item in message_listboxa:                 # 第一个小部件插入数据
        listba.insert(0,item)
    
    for item in message_listboxb:              # 第二个小部件插入数据
        listbb.insert(0,item)
    
    listba.grid(row = 0, column = 0)                    # 将小部件放置到主窗口中
    listbb.grid(row = 0, column = 1)
                
def return_root_sys(root_sys):
    return root_sys  
#按键  
def button_outer(root_sys):
    
    #框架的规划
    frm_shibie_button = Frame(root_sys)
    #frm_left = Frame(frm)
    #frm_right = Frame(frm)
    
    #与按键绑定的事件
    def button_label1():
        # s = Label(frm_right, text="显示成功")
        energy_wave_data(wave_data)
        # s.grid(row = 0, column = 0)
    def button_label2():
        # s = Label(frm_right, text="显示成功")
        abs_wave_data(wave_data)
        #s.grid(row = 1, column = 0) 
    def button_label3():
        #s = Label(frm_right, text="显示成功")
        init_wave_data(wave_data)
        #s.grid(row = 2, column = 0)   
    b3 = Button(frm_shibie_button, text="平均能量", command=button_label1)
    b2 = Button(frm_shibie_button, text="绝对能量", command=button_label2)
    b1 = Button(frm_shibie_button, text="原始信号", command=button_label3)
    #整体布局的控制：
    b1.grid(row = 0 , column =0)
    b2.grid(row = 1 , column =0)
    b3.grid(row = 2 , column =0)

frm_shibie_button.grid(row =1, column = 0)

#得到所需要的值$$   
def input_outer(root_sys):
    frm_shibie_label = Frame(root_sys)
    #frm_shibie_label.grid(row =0, column = 1)
    global value_left, value_right
    
    #frm_input = Frame(root_sys)
    label_a = Label(frm_shibie_label, text = "短时分析")
    entry_a = Entry(frm_shibie_label)
    entry_b = Entry(frm_shibie_label)
    button_load = Button(frm_shibie_label, text="波形显示", command = wave_display)
    frm_shibie_label.grid(row = 1, column = 1)
    label_a.grid(row = 0, column = 0)
    entry_a.grid(row = 1, column = 0)
    entry_b.grid(row = 2, column = 0)
    button_load.grid(row = 3, column = 0, sticky = S)
    value_left, value_right = entry_a.get(), entry_b.get()
    print value_left, value_right
    print type(value_left), type(value_right)
        #函数内部的函数，数据不能进行全局的定义 
    return wave_data, value_left, value_right
def baidu_api_title(root_sys):
    frm_baidu_api_titile = Frame(root_sys)
    label_a = Label(frm_baidu_api_titile, text = "在线识别模式", background="yellow", font=('Arial', 18))
    label_b = Label(frm_baidu_api_titile, text = "-----百度API", background="yellow", font=('Arial', 12))
    frm_baidu_api_titile.grid(row =0, column = 5, sticky = S+E+W)
    label_a.grid(row = 0, column = 0, sticky = S+E+W)
    label_b.grid(row = 1, column = 0, sticky = S+E+W)
def shibie_title(root_sys):
    frm_shibie_titile = Frame(root_sys)
    label_a = Label(frm_shibie_titile, text = "识别模式", background="yellow", font=('Arial', 18))
    frm_shibie_titile.grid(row =0, column = 1, sticky = S+E+W)
    label_a.grid(row = 0, column = 0, sticky = S+E+W)
#按键  
def button_xunlian_outer(root_sys)
    #框架的规划
    frm_xulian_button = Frame(root_sys)
    #frm_left = Frame(frm)
    #frm_right = Frame(frm)
    
    #与按键绑定的事件
    def button_label1():
        # s = Label(frm_right, text="显示成功")
        energy_wave_data(wave_data)
        # s.grid(row = 0, column = 0)
    def button_label2():
        # s = Label(frm_right, text="显示成功")
        abs_wave_data(wave_data)
        #s.grid(row = 1, column = 0) 
    def button_label3():
        #s = Label(frm_right, text="显示成功")
        init_wave_data(wave_data)
        #s.grid(row = 2, column = 0)   
 
    b3 = Button(frm_xulian_button, text="平均能量", command=button_label1)
    b2 = Button(frm_xulian_button, text="绝对能量", command=button_label2)
    b1 = Button(frm_xulian_button, text="原始信号", command=button_label3)
    #b4 = Button(frm_xulian_button, text="开始讲话", command=button_label3)
    # b5 = Button(frm_xulian_button, text="识别结果", command=button_label3)
    #整体布局的控制：
    b1.grid(row = 0 , column =0)
    b2.grid(row = 1 , column =0)
    b3.grid(row = 2 , column =0)
    ##b5.grid(row = 4 , column =0) 
    frm_xulian_button.grid(row =1, column = 2)
def kaishijianghua(root_sys):
    kaishi_frm = Frame(root_sys)
    button_load0 = Button(kaishi_frm, text="开始讲话", command = wave_display)  
    button_load1 = Button(kaishi_frm, text="结束讲话", command = wave_display) 
    button_load2 = Button(kaishi_frm, text="固定1秒讲话", command = wave_display) 
    button_load3 = Button(kaishi_frm, text="固定2秒讲话", command = wave_display) 
    button_load4 = Button(kaishi_frm, text="固定3秒讲话", command = wave_display) 
    label_KIONGGE1  = Label(kaishi_frm, text = "    ")
    label_KIONGGE  = Label(kaishi_frm, text = "    ")
    label_a = Label(kaishi_frm, text = "识别结果")
    entry_a = Entry(kaishi_frm)
    kaishi_frm.grid(row = 2, column = 1)
    button_load0.grid(row = 0, column = 0)
    button_load1.grid(row = 0, column = 1)
    label_KIONGGE.grid(row = 1, column = 0)
    button_load2.grid(row = 2, column = 1, sticky = W)
    button_load3.grid(row = 3, column = 1, sticky = W)
    button_load4.grid(row = 4, column = 1, sticky = W)
    label_KIONGGE1.grid(row = 5, column = 0)
    label_a.grid(row = 6, column = 0)
    entry_a.grid(row = 6, column = 1)
def kaishijianghua1(root_sys):
    kaishi_frm = Frame(root_sys)
    button_load0 = Button(kaishi_frm, text="开始讲话", command = wave_display)  
    button_load1 = Button(kaishi_frm, text="结束讲话", command = wave_display) 
    button_load2 = Button(kaishi_frm, text="固定1秒讲话", command = wave_display) 
    button_load3 = Button(kaishi_frm, text="固定2秒讲话", command = wave_display) 
    button_load4 = Button(kaishi_frm, text="固定3秒讲话", command = wave_display) 
    label_KIONGGE1  = Label(kaishi_frm, text = "    ")
    label_KIONGGE  = Label(kaishi_frm, text = "    ")
    label_a = Label(kaishi_frm, text = "识别结果")
    entry_a = Entry(kaishi_frm)
    kaishi_frm.grid(row = 2, column = 3)
    button_load0.grid(row = 0, column = 0)
    button_load1.grid(row = 0, column = 1)
    label_KIONGGE.grid(row = 1, column = 0)
    button_load2.grid(row = 2, column = 1, sticky = W)
    button_load3.grid(row = 3, column = 1, sticky = W)
    button_load4.grid(row = 4, column = 1, sticky = W)
    label_KIONGGE1.grid(row = 5, column = 0)
    label_a.grid(row = 6, column = 0)
    entry_a.grid(row = 6, column = 1)
def kaishijianghua2(root_sys):
    kaishi_frm = Frame(root_sys)
    zhongbei_frm = Frame(root_sys)
    button_load0 = Button(kaishi_frm, text="开始讲话", command = wave_display)  
    button_load1 = Button(kaishi_frm, text="结束讲话", command = wave_display) 
    button_load2 = Button(kaishi_frm, text="固定1秒讲话", command = wave_display) 
    button_load3 = Button(kaishi_frm, text="固定2秒讲话", command = wave_display) 
    button_load4 = Button(kaishi_frm, text="固定3秒讲话", command = wave_display) 
    label_zhongbei0 = Label(zhongbei_frm, text = "Made By：", background="yellow")
    label_zhongbei1 = Label(zhongbei_frm, text = "-----闫达帅", background="yellow")
    label_zhongbei2 = Label(zhongbei_frm, text = "-----中北大学", background="yellow")
    label_KIONGGE2  = Label(kaishi_frm, text = "    ")    label_KIONGGE1  = Label(kaishi_frm, text = "    ")
    label_KIONGGE  = Label(kaishi_frm, text = "    ")
    label_a = Label(kaishi_frm, text = "识别结果")
    entry_a = Entry(kaishi_frm)
    kaishi_frm.grid(row = 1, column = 5)
    zhongbei_frm.grid(row = 2, column = 5)
    label_KIONGGE2.grid(row = 0, column = 0)
    button_load0.grid(row = 1, column = 0)
    button_load1.grid(row = 1, column = 1)
    label_KIONGGE.grid(row = 2, column = 0)
    button_load2.grid(row = 3, column = 1, sticky = W)
    button_load3.grid(row = 4, column = 1, sticky = W)
    button_load4.grid(row = 5, column = 1, sticky = W)
    label_KIONGGE1.grid(row = 6, column = 0)
    label_a.grid(row = 7, column = 0)
    entry_a.grid(row = 7, column = 1)
    label_zhongbei0.grid(row = 0, column = 0, sticky = W)
    label_zhongbei1.grid(row = 1, column = 0)
    label_zhongbei2.grid(row = 2, column = 0)
#得到所需要的值$$   
def input_xunlian_outer(root_sys):
    frm_xunlian_label = Frame(root_sys)
    #frm_shibie_label.grid(row =0, column = 1)
    global value_left, value_right
    #frm_input = Frame(root_sys)
    label_a = Label(frm_xunlian_label, text = "短时分析")
    entry_a = Entry(frm_xunlian_label)
    entry_b = Entry(frm_xunlian_label)
button_load = Button(frm_xunlian_label, text="波形显示", command = wave_display)
frm_xunlian_label.grid(row = 1, column = 3)
    label_a.grid(row = 0, column = 0)
    entry_a.grid(row = 1, column = 0)
    entry_b.grid(row = 2, column = 0)
    button_load.grid(row = 3, column = 0, sticky = S)
    value_left, value_right = entry_a.get(), entry_b.get()
    print value_left, value_right
    print type(value_left), type(value_right)
    return wave_data, value_left, value_rightdef xunlian_title(root_sys):
    frm_xunlian_titile = Frame(root_sys)
    label_a = Label(frm_xunlian_titile, text = "训练模式", background="yellow", font=('Arial', 18))
    frm_xunlian_titile.grid(row =0, column = 3, sticky = S+E+W)
label_a.grid(row = 0, column = 0, sticky = S+E+W)
def wave_display(): 
    #进行波形的转换 短时分析。截取响应的值
    global value_left, value_right
    wave_data_dispaly(wave_data, value_left, value_right)
    pass 
        
          

#系统的主窗口
def root_sys_outer():
    root_sys = Tk()
    #main menu
    print "root_sys_outer had been called"
    root_sys.title("智能语音识别系统")
    root_sys.geometry("640x400") 
    root_sys['menu'] = menu_sys_main_outer(root_sys)
    #listbox_outer(root_sys)
    shibie_title(root_sys)
    button_outer(root_sys)
    input_outer(root_sys)    xunlian_title(root_sys)
    button_xunlian_outer(root_sys)
    input_xunlian_outer(root_sys)
    baidu_api_title(root_sys)
    kaishijianghua(root_sys)
    kaishijianghua1(root_sys)
    kaishijianghua2(root_sys)    
    root_sys.mainloop()
#root主控制
def root_outer():
    global root
    #main menu
    print "root_outer had been called"
    size_outer()
    title_outer()
    root['menu'] = menu_main_outer()
    label_outer()
    reg_outer()
    #right-menu
    root.bind("<Button-3>", pop)
    root.mainloop()if __name__ == "__main__" :
    root_outer()
    print  "main function had been called"
else :
    root_outer()
print "other module called "

#!usr/bin/env python
#coding=utf-8
import wave
import matplotlib.pyplot as plt
import numpy as np
from numpy.lib.shape_base import hsplit
from ctypes.wintypes import DOUBLE
from numpy.core.multiarray import dtype
def outer_none(fun):
    def wrapper():
        print "=" *50
        fun()
        print "=" *50      
    return wrapper

def outer_one(fun):
    def wrapper(arg):
        print "=" *50
        fun(arg)
        print "=" *50
    return wrapper

def outer_two(fun):
    def wrapper(arg, arg1):
        print "=" *50
        fun(arg, arg1)
        print "=" *50
    return wrapper
def inred(s):
    return"%s[31;2m%s%s[0m"%(chr(27), s, chr(27))
def read_wave_data(file_path):
    
    #open a wave file, and return a Wave_read object    
    f = wave.open(file_path,"rb")    
    #read the wave's format infomation,and return a tuple    
    params = f.getparams()    
    #get the info    
    nchannels, sampwidth, framerate, nframes = params[:4]  
    print nchannels,sampwidth  
    #Reads and returns nframes of audio, as a string of bytes.     
    str_data = f.readframes(nframes)    
    #close the stream    
    f.close()  
    #turn the wave's data to array    
    wave_data = np.fromstring(str_data, dtype = np.short)
    wave_data = deal_wave_data(wave_data)
    # wave_data = wave_date.shape(10,2000)  
    #calculate the time bar    
    time = np.arange(0, nframes) * (1.0/framerate) 
    len_time = len(time)/4  
    time = time[0:len_time] 
    #print time   
    time = np.arange(0, 20000)
    return wave_data, time
#将数组展平
@outer_none
def demo_test():
    print "正在测试 demo: "
@outer_one   
def flatten_wave_data(wave_data):
    print "展平之后的数据：\n\n"
    #global wave_data
    print "数组展平之后的维数：%d" %wave_data.flatten().ndim
    print wave_data
    print "展开之后的 数据如下"
    print wave_data.size
    print  "="*50
    print wave_data.flatten()
    print type(wave_data.flatten())
return wave_data.flatten()
def deal_wave_data(wave_data):
    #wave_data deal by this fuction 
    print wave_data.shape    
    #for the data is stereo,and format is LRLRLR...    
    #shape the array to n*2(-1 means fit the y coordinate)    
    wave_data.shape = -1, 2  
    #transpose the data    
    print wave_data.shape 
    wave_data = wave_data.T  
    hsplit(wave_data[0], 5)
return wave_data
@outer_two
def print_wave_data(time, wave_data):
    #print time and wave_data
    #没法使用全局变量的方法
    #global time, wave_data
    print '''
时间轴 (time)         : %d
波形数据(wave_data)   : %d %d
维数如下: %d    %d    %d    %d
       %d %d %d %d
    '''%(time.shape[0], wave_data.shape[0], wave_data.shape[1], time.ndim, wave_data[0].ndim, wave_data[1].ndim, wave_data.ndim, time.size, wave_data[0].size, wave_data[1].size, wave_data.size)
    #wave_data.shape[0]
    
    print "wave_data[0]数据如下:"
    print wave_data[0]
    print "wave_data[1]数据如下:"
    print wave_data[1]
    print "wave_data数据如下:"
    print wave_data
    print "time数据如下："
    print time
    print wave_data[0][0]
    print wave_data[0][1]
    print wave_data[1][0]    
def default_print():
    print '''
    
           名称：基于动态规整算法的特定人语音识别
           导师：姜三平
           制作人：闫达帅
 
    '''
def abs_wave_data(wave_data):
    time_xlocatiom = np.arange(0, 20000)
    
    plt.subplot(211)
    print type(wave_data.flatten())
    #此处有个问题
    print wave_data.size, time_xlocatiom.size
    plt.plot(time_xlocatiom, wave_data.flatten())
    #plt.plot(time, wave_data[0])
    #print testing 
    #plt.plot(time, time)
    plt.subplot(212)  
    #print testing
    #plt.plot(time, time)
    plt.plot(time_xlocatiom, abs(wave_data.flatten()), c = "r")
    #plt.plot(time, wave_data[1], c = "g")
    #plt.subplot(213)
    #plt.plot(time, wave_data_list1, c = "g")
    plt.show()
    
def energy_wave_data(wave_data):
    time_xlocatiom = np.arange(0, 20000)
    plt.subplot(211)
    print type(wave_data.flatten())
    #此处有个问题
    print wave_data.size, time_xlocatiom.size
    plt.plot(time_xlocatiom, wave_data.flatten())
    #plt.plot(time, wave_data[0])
    #print testing 
    #plt.plot(time, time)
    plt.subplot(212)  
    #print testing
    #plt.plot(time, time)
    #float_data = dtype['int32']
    float_data = ((wave_data.flatten()/181) * (wave_data.flatten()/181))
    #print float_data[0, :: 3]
    print "占用的字节数如下："
    print  float_data.itemsize
    
    print "数组的元素如下："
    print float_data
    print float(float_data[0])
    #print (wave_data.flatten() * wave_data.flatten())
    print float(3275)
    plt.plot(time_xlocatiom, float_data, c = "r")
    #plt.plot(time, wave_data[1], c = "g")
    #plt.subplot(213)
    #plt.plot(time, wave_data_list1, c = "g")
    plt.show()
    
def init_wave_data(wave_data):
    time_xlocation = np.arange(0, 20000)
    
    plt.subplot(111)
    print type(wave_data.flatten())
    #此处有个问题
    print wave_data.size, time_xlocation.size
    plt.plot(time_xlocation, wave_data.flatten())
    plt.show()
# 外部调用的接口
def wave_data_dispaly(wave_data, value_left, value_right):
    #截取一段波形进行显示
    value_left = int(value_left)
    value_right = int(value_right)
    time_xlocation = np.arange(0, value_right - value_left)
        
    plt.subplot(111)
    print type(wave_data.flatten())
    
    #wave_data = wave_data.flatten()
    #此处有个问题
    print wave_data.size, wave_data.flatten().size, time_xlocation.size
    wave_data_list = wave_data.flatten()[value_left:value_right]
    print wave_data_list.size, time_xlocation.size
plt.plot(time_xlocation, wave_data_list)
plt.show()
def file_wave_open():  
    print default_print()  
    wave_data, time = read_wave_data(r"f:\python_yds\f2.wav") 
    print_wave_data(time, wave_data) 
    flatten_wave_data(wave_data)
    print type(wave_data)
    demo_test()
    #wave_data_list0 = wave_data[0, ...][2000:2500]
    #wave_data_list1 = wave_data[0, ...][2500:3000]
    #draw the wave    
    #abs_wave_data(wave_data)
    #energy_wave_data(wave_data)
    return wave_data
wave_data = file_wave_open()

#encoding=utf-8            
import wave
import urllib2,pycurl
import base64
import json
import os
def get_token():  
    apiKey = "mg9oRTM77P1DcvY4LnQFNEQS"
    secretKey = "556ec7dd09331ee8146807ba71951a84"
    auth_url = "https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=" + apiKey + "&client_secret=" + secretKey;  
    res = urllib2.urlopen(auth_url)  
    json_data = res.read()  
    return json.loads(json_data)['access_token']  
def dump_res(buf):  
    print buf 
def use_cloud(token):
    os.system("sudo arecord -d 4 -D plughw:1,0 /home/pi/baidu_api_test.wav")
    fp = wave.open('/home/pi/baidu_api_test.wav', 'rb')
    nf = fp.getnframes()  
    f_len = nf * 2  
    audio_data = fp.readframes(nf)  
  
    cuid = "qq740595707" 
    srv_url = 'http://vop.baidu.com/server_api'+ '?cuid=' +cuid+ '&token='+ token  
    http_header = ['Content-Type: audio/wav; rate=8000','Content-Length: %d' % f_len]  #pcm
    c = pycurl.Curl()  
    c.setopt(pycurl.URL, str(srv_url))  
    #c.setopt(c.RETURNTRANSFER, 1)  
    c.setopt(c.HTTPHEADER, http_header)    
    c.setopt(c.POST, 1)  
    c.setopt(c.CONNECTTIMEOUT, 30)  
    c.setopt(c.TIMEOUT, 30)  
    c.setopt(c.WRITEFUNCTION, dump_res)  
    c.setopt(c.POSTFIELDS, audio_data)
    c.setopt(c.POSTFIELDSIZE, f_len)
    c.perform() 

if __name__ == "__main__":  
    token = get_token()  
    use_cloud(token)  
