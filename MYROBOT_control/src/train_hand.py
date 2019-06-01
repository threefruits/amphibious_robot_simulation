#coding=utf-8
import rospy
from std_msgs.msg import Int16
import time
from geometry_msgs.msg import Twist #导入需要的ros的package 
import numpy as np
is_done=Int16()
is_done.data=0
#定义发送数据的函数:只发一次（可以考虑发很多次，最终要看效果如何）
def data_publish(u):
    #初始化node
    

    #初始化publisher
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10) # topic和消息类型需要和肖岸星商量确定一下 
    
    #初始化twist
    twist = Twist()

    # 给twist赋值
    twist.linear.x = u[0] #线速度
    twist.linear.y = 0.0
    twist.linear.z = 0.0

    twist.angular.x = 0.0 #角速度
    twist.angular.y = 0.0
    twist.angular.z = u[1]

    #调试代码
    # print("twist")
    # print(twist)

    #发送twist
    pub.publish(twist) #将数据发送出去

#发送twist：一直发指令，直到一次运动结束之后就不发指令
def callback_2(data): 
    #接受数据
    is_done.data= data.data
    #print(finish)
    #判断状态
    # if (finish.data == 1):#完成转动
    #     is_done = 1
    #     # print("callback_2",is_done)
    # else:#没完成转动
    #     is_done = 0 
    #     print("moving")

if __name__ == '__main__':
    #初始化
    rospy.init_node('train_hand', anonymous=True)
    rospy.Subscriber("is_done", Int16, callback_2)
    start_flag = 1 #开始指令

    twist = Twist() #变量声明
    u = np.zeros(2) #控制量声明
   
    time.sleep(1)
    print(is_done.data)
    #控制说明
    print("前进：w 左拐：a 右拐:d 后退：s")
    time.sleep(0.1)
    #开始控制
    while start_flag == 1: #一直循环接受数据
        control_key = raw_input("raw_input：") #获得键盘输入

        if control_key == "w": #前进
            #显示控制量
            print("control is w")

            #设置频率
           

            #没收到结束信息一直发送控制量
            if(is_done.data==1):
                #赋值线速度
                u[0] = 1
                u[1] = 0
                
                #发布线速度消息
                data_publish(u)

               

                #以10HZ频率发送数据
              
            
        elif control_key == "a": #左转
            #显示控制量
            print("control is a")

            #设置频率
            rate = rospy.Rate(10) # 10hz

            #没收到结束信息一直发送控制量
            if(is_done.data==1):
                #赋值线速度
                u[0] = 0
                u[1] = -1
                
                #发布线速度消息
                data_publish(u)

                
                #如果接收到结束信息，is_done设为1,结束循环
               

                #以10HZ频率发送数据
                rate.sleep()

        elif control_key == "d": #右转
            #显示控制量
            print("control is d")

            #设置频率
            rate = rospy.Rate(10) # 10hz

            if(is_done.data==1):
                #赋值线速度
                u[0] = 0
                u[1] = 1
                
                #发布线速度消息
                data_publish(u)

                

                #如果接收到结束信息，is_done设为1,结束循环
                

                #以10HZ频率发送数据
                rate.sleep()

        elif control_key == "s": #后退
            #显示控制量
            print("control is s")

            #设置频率
            rate = rospy.Rate(10) # 10hz

            if(is_done.data==1):
                #赋值线速度
                u[0] = -1
                u[1] = 0
                
                #发布线速度消息
                data_publish(u)

        

                #如果接收到结束信息，is_done设为1,结束循环
          

                #以10HZ频率发送数据
                rate.sleep()
        
        elif control_key == "q": #六足步态
            #显示控制量
            print("control is s")

            #设置频率
            rate = rospy.Rate(10) # 10hz

            if(is_done.data==1):
                #赋值线速度
                u[0] = 2
                u[1] = 0
                
                #发布线速度消息
                data_publish(u)

        

                #如果接收到结束信息，is_done设为1,结束循环
          

                #以10HZ频率发送数据
                rate.sleep()
        #将is_down复位
        print("is_done已重置")
        is_done.data = 0


