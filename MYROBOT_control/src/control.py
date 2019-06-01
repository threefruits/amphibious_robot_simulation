import rospy
import time
from math import pi
from math import floor
from std_msgs.msg import Float64
from std_msgs.msg import Float64MultiArray
from std_msgs.msg import Int16
from geometry_msgs.msg import Twist
from sensor_msgs.msg import JointState
from gazebo_msgs.msg import ModelStates
from tf.transformations import euler_from_quaternion,quaternion_from_euler 

velocity=[0,0,0,0,0,0]
position=[0,0,0,0,0,0]
k_leg=[0,0,0,0,0,0]
v=Twist()
state=[0,0,0,0,0,0,0,0]
train_state=Float64MultiArray()

train_state.data=state
def callback(data):
       for i in range(6):
            velocity[i]=data.velocity[i]
            position[i]=data.position[i]
            k_leg[i]=(position[i]+pi)//(2*pi)

def callback2(data):
    v.linear=data.linear
    v.angular=data.angular
    
def callback3(data):
    state[0]=data.pose[1].position.x
    state[1]=data.pose[1].position.y
    state[2]=data.pose[1].orientation.x
    state[3]=data.pose[1].orientation.y
    state[4]=data.pose[1].orientation.z
    state[5]=data.pose[1].orientation.w
    # train_state.data.append(state)
    print(state)
    
def set(velocity_d,position_d):
    is_ok = [0,0,0,0,0,0]
    while(1):
        if(abs(position_d[0]-position[0])>pi/15):
                if(position_d[0]>position[0]):
                    pub1.publish(velocity_d[0])
                else:
                    pub1.publish(-velocity_d[0])
        elif(abs(position_d[0]-position[0])>pi/200):
                if(position_d[0]>position[0]):
                    pub1.publish(0.4)
                else:
                    pub1.publish(-0.4)
        else:    
            pub1.publish(0)
            is_ok[0]=1



        if(abs(position_d[1]-position[1])>pi/15):
                if(position_d[1]>position[1]):
                    pub2.publish(velocity_d[1])
                else:
                    pub2.publish(-velocity_d[1])
        elif(abs(position_d[1]-position[1])>pi/200):
                if(position_d[1]>position[1]):
                    pub2.publish(0.4)
                else:
                    pub2.publish(-0.4)                   
        else:
            pub2.publish(0)
            is_ok[1]=1

        if(abs(position_d[2]-position[2])>pi/15):
                if(position_d[2]>position[2]):
                    pub3.publish(velocity_d[2])
                else:
                    pub3.publish(-velocity_d[2])
        elif(abs(position_d[2]-position[2])>pi/200):
                if(position_d[2]>position[2]):
                    pub3.publish(0.4)
                else:
                    pub3.publish(-0.4)   
        else:
            pub3.publish(0)
            is_ok[2]=1

        if(abs(position_d[3]-position[3])>pi/15):
                if(position_d[3]>position[3]):
                    pub4.publish(velocity_d[3])
                else:
                    pub4.publish(-velocity_d[3])
        elif(abs(position_d[3]-position[3])>pi/200):
                if(position_d[3]>position[3]):
                    pub4.publish(0.4)
                else:
                    pub4.publish(-0.4)   
        else:
            pub4.publish(0)
            is_ok[3]=1

        if(abs(position_d[4]-position[4])>pi/15):
                if(position_d[4]>position[4]):
                    pub5.publish(velocity_d[4])
                else:
                    pub5.publish(-velocity_d[4])
        elif(abs(position_d[4]-position[4])>pi/200):
                if(position_d[4]>position[4]):
                    pub5.publish(0.4)
                else:
                    pub5.publish(-0.4)   
        else:
            pub5.publish(0)
            is_ok[4]=1

        if(abs(position_d[5]-position[5])>pi/15):
                if(position_d[5]>position[5]):
                    pub6.publish(velocity_d[5])
                else:
                    pub6.publish(-velocity_d[5])
        elif(abs(position_d[5]-position[5])>pi/200):
                if(position_d[5]>position[5]):
                    pub6.publish(0.4)
                else:
                    pub6.publish(-0.4)   
        else:
            pub6.publish(0)
            is_ok[5]=1

        if(is_ok==[1,1,1,1,1,1]):
            break

def move_forward():
    k=k_leg[:]
    v1=[pi*17/9,pi/9,pi*17/9,pi/9,pi*17/9,pi/9]
    p1=[pi*17/9+2*k[0]*pi,pi/9+2*k[1]*pi,pi*17/9+2*k[2]*pi,pi/9+2*k[3]*pi,pi*17/9+2*k[4]*pi,pi/9+2*k[5]*pi]
    time.sleep(0.02)
    set(v1,p1)
    time.sleep(0.02)
    for i in range(1):
    # while(v.linea.x==1):
        # v2=[pi/9,pi*8/9,pi/9,pi*8/9,pi/9,pi*8/9]
        v2=[pi*2/9,pi*16/9,pi*2/9,pi*16/9,pi*2/9,pi*16/9]
        p2=[pi*(19.0/9+2*k[0]),pi*(17.0/9+2*k[1]),pi*(19.0/9+2*k[2]),pi*(17.0/9+2*k[3]),pi*(19.0/9+2*k[4]),pi*(17.0/9+2*k[5])]
        set(v2,p2)
        time.sleep(0.02)
        # v2=[pi*8/9,pi/9,pi*8/9,pi/9,pi*8/9,pi/9]
        v2=[pi*16/9,pi*2/9,pi*16/9,pi*2/9,pi*16/9,pi*2/9]
        p2=[pi*(35.0/9+2*k[0]),pi*(19.0/9+2*k[1]),pi*(35.0/9+2*k[2]),pi*(19.0/9+2*k[3]),pi*(35.0/9+2*k[4]),pi*(19.0/9+2*k[5])]
        set(v2,p2)
        time.sleep(0.02)
        for i in range(6):
            k[i]=k[i]+1
    
    for i in range(6):
            k[i]=k[i]+1
    
    v1=[pi/9,pi*17/9,pi/9,pi*17/9,pi/9,pi*17/9]
    p1=[2*k[0]*pi,2*k[1]*pi,2*k[2]*pi,2*k[3]*pi,2*k[4]*pi,2*k[5]*pi]
    
    set(v1,p1)
    time.sleep(0.02)
    print(k)

def move_backward():
    k=k_leg[:]
    v1=[pi*17/9,pi/9,pi*17/9,pi/9,pi*17/9,pi/9]
    p1=[-pi*17/9+2*k[0]*pi,-pi/9+2*k[1]*pi,-pi*17/9+2*k[2]*pi,-pi/9+2*k[3]*pi,-pi*17/9+2*k[4]*pi,-pi/9+2*k[5]*pi]
    time.sleep(0.1)
    set(v1,p1)
    time.sleep(0.05)
    for i in range(1):
    # while(v.linea.x==1):
        # v2=[pi/9,pi*8/9,pi/9,pi*8/9,pi/9,pi*8/9]
        v2=[pi*2/9,pi*16/9,pi*2/9,pi*16/9,pi*2/9,pi*16/9]
        p2=[pi*(-19.0/9+2*k[0]),pi*(-17.0/9+2*k[1]),pi*(-19.0/9+2*k[2]),pi*(-17.0/9+2*k[3]),pi*(-19.0/9+2*k[4]),pi*(-17.0/9+2*k[5])]
        set(v2,p2)
        time.sleep(0.05)
        # v2=[pi*8/9,pi/9,pi*8/9,pi/9,pi*8/9,pi/9]
        v2=[pi*16/9,pi*2/9,pi*16/9,pi*2/9,pi*16/9,pi*2/9]
        p2=[pi*(-35.0/9+2*k[0]),pi*(-19.0/9+2*k[1]),pi*(-35.0/9+2*k[2]),pi*(-19.0/9+2*k[3]),pi*(-35.0/9+2*k[4]),pi*(-19.0/9+2*k[5])]
        set(v2,p2)
        time.sleep(0.05)
        for i in range(6):
            k[i]=k[i]-1
    v1=[pi*17/9,pi/9,pi*17/9,pi/9,pi*17/9,pi/9]
    p1=[2*k[0]*pi,2*k[1]*pi,2*k[2]*pi,2*k[3]*pi,2*k[4]*pi,2*k[5]*pi]
    
    set(v1,p1)
    time.sleep(0.05)
    print(k)


def six_forward():
    k=k_leg[:]
    time.sleep(0.1)
    v2=[5,5,5,5,5,5]
    p2=[pi*(4+2*k[0]),pi*(4+2*k[1]),pi*(4+2*k[2]),pi*(4+2*k[3]),pi*(4+2*k[4]),pi*(4+2*k[5])]
    for i in range(6):
            k[i]=k[i]+2
    set(v2,p2)
    time.sleep(0.05)
    print(k)

def move_forward_fast():
    k=k_leg[:]
    v1=[pi*17/12,pi/12,pi*17/12,pi/12,pi*17/12,pi/12]
    p1=[pi*17/9+2*k[0]*pi,pi/9+2*k[1]*pi,pi*17/9+2*k[2]*pi,pi/9+2*k[3]*pi,pi*17/9+2*k[4]*pi,pi/9+2*k[5]*pi]
    time.sleep(0.1)
    set(v1,p1)
    time.sleep(0.1)
    for i in range(2):
        # v2=[pi/9,pi*8/9,pi/9,pi*8/9,pi/9,pi*8/9]
        v2=[pi*4/12,pi*32/12,pi*4/12,pi*32/12,pi*4/12,pi*32/12]
        p2=[pi*(19.0/9+2*k[0]),pi*(17.0/9+2*k[1]),pi*(19.0/9+2*k[2]),pi*(17.0/9+2*k[3]),pi*(19.0/9+2*k[4]),pi*(17.0/9+2*k[5])]
        set(v2,p2)
        time.sleep(0.1)
        # v2=[pi*8/9,pi/9,pi*8/9,pi/9,pi*8/9,pi/9]
        v2=[pi*32/12,pi*4/12,pi*32/12,pi*4/12,pi*32/12,pi*4/12]
        p2=[pi*(35.0/9+2*k[0]),pi*(19.0/9+2*k[1]),pi*(35.0/9+2*k[2]),pi*(19.0/9+2*k[3]),pi*(35.0/9+2*k[4]),pi*(19.0/9+2*k[5])]
        set(v2,p2)
        time.sleep(0.1)
        for i in range(6):
            k[i]=k[i]+1
    v1=[pi*17/12,pi/12,pi*17/12,pi/12,pi*17/12,pi/12]
    p1=[2*k[0]*pi,2*k[1]*pi,2*k[2]*pi,2*k[3]*pi,2*k[4]*pi,2*k[5]*pi]
    
    set(v1,p1)
    time.sleep(0.05)
    print(k)

# def turn_left():
#     k=k_leg[:]
#     v1=[pi*17/9,pi/9,pi*17/9,pi/9,pi*17/9,pi/9]
#     p1=[pi*17/9+2*k[0]*pi,pi/9+2*k[1]*pi,pi*17/9+2*k[2]*pi,-pi/9+2*k[3]*pi,-pi*17/9+2*k[4]*pi,-pi/9+2*k[5]*pi]
#     time.sleep(0.1)
#     set(v1,p1)
#     time.sleep(0.1)
#     while(v.angular.z==-1):
#         # v2=[pi/9,pi*8/9,pi/9,pi*8/9,pi/9,pi*8/9]
#         v2=[pi*2/9,pi*16/9,pi*2/9,pi*16/9,pi*2/9,pi*16/9]
#         p2=[pi*(19.0/9+2*k[0]),pi*(17.0/9+2*k[1]),pi*(19.0/9+2*k[2]),pi*(-17.0/9+2*k[3]),pi*(-19.0/9+2*k[4]),pi*(-17.0/9+2*k[5])]
#         set(v2,p2)
#         time.sleep(0.1)
#         # v2=[pi*8/9,pi/9,pi*8/9,pi/9,pi*8/9,pi/9]
#         v2=[pi*16/9,pi*2/9,pi*16/9,pi*2/9,pi*16/9,pi*2/9]
#         p2=[pi*(35.0/9+2*k[0]),pi*(19.0/9+2*k[1]),pi*(35.0/9+2*k[2]),pi*(-19.0/9+2*k[3]),pi*(-35.0/9+2*k[4]),pi*(-19.0/9+2*k[5])]
#         set(v2,p2)
#         time.sleep(0.1)
#         for i in range(3):
#             k[i]=k[i]+1
#             k[i+3]=k[i+3]-1
#     v1=[pi*17/9,pi/9,pi*17/9,pi/9,pi*17/9,pi/9]
#     p1=[2*k[0]*pi,2*k[1]*pi,2*k[2]*pi,2*k[3]*pi,2*k[4]*pi,2*k[5]*pi]
#     time.sleep(0.1)
#     set(v1,p1)
#     time.sleep(0.1)
#     print(k)

def turn_left():
    k=k_leg[:]
    v1=[pi*17/12,pi/12,pi*17/12,pi/12,pi*17/12,pi/12]
    p1=[pi*17/9+2*k[0]*pi,pi/9+2*k[1]*pi,pi*17/9+2*k[2]*pi,-pi/9+2*k[3]*pi,-pi*17/9+2*k[4]*pi,-pi/9+2*k[5]*pi]
    time.sleep(0.05)
    set(v1,p1)
    
    # for i in range(1):
    #     # v2=[pi/9,pi*8/9,pi/9,pi*8/9,pi/9,pi*8/9]
    #     v2=[pi*2/9,pi*16/9,pi*2/9,pi*16/9,pi*2/9,pi*16/9]
    #     p2=[pi*(19.0/9+2*k[0]),pi*(17.0/9+2*k[1]),pi*(19.0/9+2*k[2]),pi*(-17.0/9+2*k[3]),pi*(-19.0/9+2*k[4]),pi*(-17.0/9+2*k[5])]
    #     set(v2,p2)
    #     time.sleep(0.1)
        # v2=[pi*8/9,pi/9,pi*8/9,pi/9,pi*8/9,pi/9]
        # v2=[pi*16/9,pi*2/9,pi*16/9,pi*2/9,pi*16/9,pi*2/9]
        # p2=[pi*(35.0/9+2*k[0]),pi*(19.0/9+2*k[1]),pi*(35.0/9+2*k[2]),pi*(-19.0/9+2*k[3]),pi*(-35.0/9+2*k[4]),pi*(-19.0/9+2*k[5])]
        # set(v2,p2)
        # time.sleep(0.1)
    k[0]=k[0]+1
    k[2]=k[2]+1
    k[4]=k[4]-1

    k[1]=k[1]+1
    k[3]=k[3]-1
    k[5]=k[5]-1
    # v1=[pi*17/9,pi/9,pi*17/9,pi/9,pi*17/9,pi/9]
    v1=[pi/12,pi*17/12,pi/12,pi*17/12,pi/12,pi*17/12]
    p1=[2*k[0]*pi,2*k[1]*pi,2*k[2]*pi,2*k[3]*pi,2*k[4]*pi,2*k[5]*pi]
    time.sleep(0.05)
    set(v1,p1)
    time.sleep(0.1)
    print(k)

def turn_right():
    k=k_leg[:]
    v1=[pi/12,pi*17/12,pi/12,pi*17/12,pi/12,pi*17/12]
    p1=[-pi/9+2*k[0]*pi,-pi*17/9+2*k[1]*pi,-pi/9+2*k[2]*pi,pi*17/9+2*k[3]*pi,pi/9+2*k[4]*pi,pi*17/9+2*k[5]*pi]
    time.sleep(0.01)
    set(v1,p1)
    time.sleep(0.01)
    # for i in range(1):
    #     # v2=[pi/9,pi*8/9,pi/9,pi*8/9,pi/9,pi*8/9]
    #     v2=[pi*16/9,pi*2/9,pi*16/9,pi*2/9,pi*16/9,pi*2/9]
    #     p2=[pi*(-17.0/9+2*k[0]),pi*(-19.0/9+2*k[1]),pi*(-17.0/9+2*k[2]),pi*(19.0/9+2*k[3]),pi*(17.0/9+2*k[4]),pi*(19.0/9+2*k[5])]
    #     set(v2,p2)
    #     time.sleep(0.1)
    #     # v2=[pi*8/9,pi/9,pi*8/9,pi/9,pi*8/9,pi/9]
    #     v2=[pi*2/9,pi*16/9,pi*2/9,pi*16/9,pi*2/9,pi*16/9]
    #     p2=[pi*(-19.0/9+2*k[0]),pi*(-35.0/9+2*k[1]),pi*(-19.0/9+2*k[2]),pi*(35.0/9+2*k[3]),pi*(19.0/9+2*k[4]),pi*(35.0/9+2*k[5])]
    #     set(v2,p2)
    #     time.sleep(0.1)
    k[1]=k[1]-1
    k[3]=k[3]+1
    k[5]=k[5]+1

    k[0]=k[0]-1
    k[2]=k[2]-1
    k[4]=k[4]+1
    v1=[pi*17/12,pi/12,pi*17/12,pi/12,pi*17/12,pi/12]
    p1=[2*k[0]*pi,2*k[1]*pi,2*k[2]*pi,2*k[3]*pi,2*k[4]*pi,2*k[5]*pi]
    time.sleep(0.01)
    set(v1,p1)
    time.sleep(0.01)
    print(k)


# def turn_right():
#     k=k_leg[:]
#     v1=[pi/9,pi*17/9,pi/9,pi*17/9,pi/9,pi*17/9]
#     p1=[-pi/9+2*k[0]*pi,-pi*17/9+2*k[1]*pi,-pi/9+2*k[2]*pi,pi*17/9+2*k[3]*pi,pi/9+2*k[4]*pi,pi*17/9+2*k[5]*pi]
#     time.sleep(0.1)
#     set(v1,p1)
#     time.sleep(0.1)
#     for i in range(1):
#         # v2=[pi/9,pi*8/9,pi/9,pi*8/9,pi/9,pi*8/9]
#         v2=[pi*16/9,pi*2/9,pi*16/9,pi*2/9,pi*16/9,pi*2/9]
#         p2=[pi*(-17.0/9+2*k[0]),pi*(-19.0/9+2*k[1]),pi*(-17.0/9+2*k[2]),pi*(19.0/9+2*k[3]),pi*(17.0/9+2*k[4]),pi*(19.0/9+2*k[5])]
#         set(v2,p2)
#         time.sleep(0.1)
#         # v2=[pi*8/9,pi/9,pi*8/9,pi/9,pi*8/9,pi/9]
#         v2=[pi*2/9,pi*16/9,pi*2/9,pi*16/9,pi*2/9,pi*16/9]
#         p2=[pi*(-19.0/9+2*k[0]),pi*(-35.0/9+2*k[1]),pi*(-19.0/9+2*k[2]),pi*(35.0/9+2*k[3]),pi*(19.0/9+2*k[4]),pi*(35.0/9+2*k[5])]
#         set(v2,p2)
#         time.sleep(0.1)
#         for i in range(3):
#             k[i]=k[i]-1
#             k[i+3]=k[i+3]+1
#     v1=[pi/9,pi*17/9,pi/9,pi*17/9,pi/9,pi*17/9]
#     p1=[2*k[0]*pi,2*k[1]*pi,2*k[2]*pi,2*k[3]*pi,2*k[4]*pi,2*k[5]*pi]
#     time.sleep(0.1)
#     set(v1,p1)
#     time.sleep(0.1)
#     print(k)

if __name__=="__main__":
    rospy.init_node('control')
    # rospy.Subscriber("/cmd_vel",Twist,callback)
    pub1 = rospy.Publisher('/two_robot/joint1_velocity_controller/command',Float64, queue_size=3)
    pub2 = rospy.Publisher('/two_robot/joint2_velocity_controller/command',Float64, queue_size=3)
    pub3 = rospy.Publisher('/two_robot/joint3_velocity_controller/command',Float64, queue_size=3)
    pub4 = rospy.Publisher('/two_robot/joint4_velocity_controller/command',Float64, queue_size=3)
    pub5 = rospy.Publisher('/two_robot/joint5_velocity_controller/command',Float64, queue_size=3)
    pub6 = rospy.Publisher('/two_robot/joint6_velocity_controller/command',Float64, queue_size=3)
    rospy.Subscriber("/two_robot/joint_states",JointState,callback)
    rospy.Subscriber("/cmd_vel",Twist,callback2)
    rospy.Subscriber("/gazebo/model_states",ModelStates,callback3)
    pub7 = rospy.Publisher('/is_done',Int16, queue_size=3)
    pub8 = rospy.Publisher('/data',Float64MultiArray,queue_size=3)

    time.sleep(0.1)
    while(1):
        
        if(v.linear.x==1.0):
            train_state.data[6]=1
            train_state.data[7]=0
            pub8.publish(train_state)
            move_forward()
            pub7.publish(1)
            v.linear.x=0
            v.angular.z=0
        if(v.angular.z==-1):
            train_state.data[6]=0
            train_state.data[7]=-1
            pub8.publish(train_state)
            turn_left()
            pub7.publish(1)
            v.linear.x=0
            v.angular.z=0
        if(v.angular.z==1):
            train_state.data[6]=0
            train_state.data[7]=1
            pub8.publish(train_state)
            turn_right()
            pub7.publish(1)
            v.linear.x=0
            v.angular.z=0
        if(v.linear.x==-1):
            
            move_backward()
            pub7.publish(1)
            v.linear.x=0
            v.angular.z=0
    	if(v.linear.x==2.0):
            
            six_forward()
            pub7.publish(1)
            v.linear.x=0
            v.angular.z=0

        pub7.publish(1)
        
   
    # print(k_leg)
    # v1=[pi*17/18,pi/18,pi*17/18,pi/18,pi*17/18,pi/18]
    # v1=[pi*17/9,pi/9,pi*17/9,pi/9,pi*17/9,pi/9]
    # p1=[pi*17/9+2*k*pi,pi/9+2*k*pi,pi*17/9+2*k*pi,pi/9+2*k*pi,pi*17/9+2*k*pi,pi/9+2*k*pi]
    # time.sleep(1)
    # set(v1,p1)
    # time.sleep(1)
    
    
    # while(1):
    #     # v2=[pi/9,pi*8/9,pi/9,pi*8/9,pi/9,pi*8/9]
    #     v2=[pi*2/9,pi*16/9,pi*2/9,pi*16/9,pi*2/9,pi*16/9]
    #     p2=[pi*(19.0/9+2*k),pi*(17.0/9+2*k),pi*(19.0/9+2*k),pi*(17.0/9+2*k),pi*(19.0/9+2*k),pi*(17.0/9+2*k)]
    #     set(v2,p2)
    #     time.sleep(0.1)
    #     # v2=[pi*8/9,pi/9,pi*8/9,pi/9,pi*8/9,pi/9]
    #     v2=[pi*16/9,pi*2/9,pi*16/9,pi*2/9,pi*16/9,pi*2/9]
    #     p2=[pi*(35.0/9+2*k),pi*(19.0/9+2*k),pi*(35.0/9+2*k),pi*(19.0/9+2*k),pi*(35.0/9+2*k),pi*(19.0/9+2*k)]
    #     set(v2,p2)
    #     time.sleep(0.1)
    #     k=k+1



    # time.sleep(2)
    # print("ssdssd")
    
