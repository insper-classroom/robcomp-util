import rclpy
from rclpy.node import Node
from rclpy.qos import ReliabilityPolicy, QoSProfile
from geometry_msgs.msg import Twist
from robcomp_util.laser import Laser
from robcomp_util.odom import Odom
import numpy as np
# Adicione aqui os imports necessários


class BaseControlNode(Node, Laser, Odom): # Mude o nome da classe

    def __init__(self):
        Node.__init__(self,'base_control_node') # Mude o nome do nó
        Laser.__init__(self)
        Odom.__init__(self)

        print(self.x)
        self.timer = self.create_timer(0.25, self.control)

    
    def custom_laser(self):
        pass

    def control(self):
        print('Min. Front:', np.min(self.front))
        print('X: ', self.x)
        
            
def main(args=None):
    rclpy.init(args=args)
    ros_node = BaseControlNode() # Mude o nome da classe

    rclpy.spin(ros_node)

    ros_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()