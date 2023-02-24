#!/usr/bin/python3.7
# Author : Abderrezzak YAHI 
# This script is used to connect into Huawei DSLAM MA5600 ==> MA5800
# the base referrence of this script in the link below: 
# https://ktbyers.github.io/netmiko/docs/netmiko/huawei/huawei_smartax.html

################################################################################
######### Library part 
from netmiko import ConnectHandler, NetMikoTimeoutException, NetMikoAuthenticationException
from netmiko.huawei import huawei_smartax as ho

print("""
        ***********************       WARNING      **************************
          You must have prior authorization to run this Script. All
          connections are logged and monitored.By running this Script you
          fully consent to all monitoring. Any failuere in the 
          access or use will prosecuted to the  full extent of the law. 
                      !!!!! You have been warned !!!!!!.
       """)

######## connection variables part
HUAWEI_DSLAM = {
    'device_type': 'huawei',
    'host' : 'Insert_your_dslam_Name' , ## in this section you can add input("insert your  Name dslam or IP address to connect in ")
    'username': 'username', ## In this Line add your username you configured to supervised your dslam
    'password': 'password', ## In this Line add the password you configured to supervised your dslam
    'verbose':True,  ## you can let verbose mode enable to see all the messages if there any probleme while connecting in to your dslam 
    'session_timeout' : 360.00,
    'conn_timeout': 150.00,
    'timeout': 300,
    'fast_cli':False,
}
connection=ho.HuaweiSmartAXSSH(**HUAWEI_DSLAM)

####### Sending command without entering the enable mode 
card_board = connection.send_command('display board 0\n')

######## if you want to enter into enable 
connection.enable(cmd='enable')  ## ! This mode should be enabled to enter into configuration mode
List_Port=['0','1']

for i in List_Port.splitlines():
    interface= connection.send_config_set('interface adsl 0/'+i, exit_config_mode=False)  ## Sending command in config mode but you need to enter into enable mode
    print(interface)
