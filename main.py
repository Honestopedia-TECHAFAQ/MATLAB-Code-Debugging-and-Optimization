import rclpy
from std_msgs.msg import String

def robot_state_callback(msg):
    process_robot_state(msg)
    control_cmd = generate_control_command(msg)
    control_pub.publish(control_cmd)

def process_robot_state(robot_state_msg):
    print("Received robot state message:", robot_state_msg.data)

def generate_control_command(robot_state_msg):
    control_cmd = "Control command based on robot state: " + robot_state_msg.data
    return String(data=control_cmd)

def main():
    rclpy.init()
    node = rclpy.create_node('robot_control_node')
    robot_state_sub = node.create_subscription(
        String,
        '/robot_state',
        robot_state_callback,
        10
    )
    global control_pub
    control_pub = node.create_publisher(String, '/robot_control', 10)
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
