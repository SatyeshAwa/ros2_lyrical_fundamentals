#! /usr/bin/env python3

"""_summary_
This ros2 node subscribes to 'I love TS' messages
-----
Publishing Topics:
None
-----
Subscription Topics:
The channel containing the "I love TS" messages
/py_TS_topic - std_msgs/String
----
Author: Satyesh Shanker Awasthi
Date : 03/07/2026
"""
import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node

from std_msgs.msg import String


class MinimalPySubscriber(Node):

    def __init__(self):
        super().__init__('minimal_py_subscriber')
        self.subscription = self.create_subscription(
            String,
            'py_TS_topic',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)


def main(args=None):
    try:
        with rclpy.init(args=args):
            minimal_py_subscriber = MinimalPySubscriber()

            rclpy.spin(minimal_py_subscriber)

            minimal_py_subscriber.destroy_node()

            rclpy.shutdown()

    except (KeyboardInterrupt, ExternalShutdownException):
        pass


if __name__ == '__main__':
    main()