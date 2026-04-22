import rclpy
from rclpy.node import Node
from example_ros2_interface.msg import RobotStatus
from example_ros2_interface.srv import MoveRobot

class Exampleinterfacescontrol02(Node):
    def __init__(self,name):
        super().__init__(name)
        self.get_logger().info("节点启动 %s"%name)
        self.client = self.create_client(MoveRobot,"move_robot")
        self.robot_status_subscribe_ = self.create_subscription(RobotStatus,"robot_status",self.robot_status_callback,10)

    def robot_status_callback(self,msg):
        self.get_logger().info(f"收到状态数据位置：{msg.pose} 状态：{msg.status}")  

    def move_result_callback(self,result_future):
        response = result_future.result()
        self.get_logger().info(f"收到返回结果：{response.pose}")

    def move_robot(self, distance):
        while rclpy.ok() and self.client.wait_for_service(1)==False:
            self.get_logger().info(f"等待服务端上线....")
        request = MoveRobot.Request()
        request.distance = distance
        self.get_logger().info(f"请求服务让机器人移动{distance}")
        self.client_.call_async(request).add_done_callback(self.move_result_callback_)


def main(args=None):
    rclpy.init(args=args) 
    node = Exampleinterfacescontrol02("example_interfaces_control_02") 
    node.move_robot(5.0) 
    rclpy.spin(node) 
    rclpy.shutdown()     







