#! /usr/bin/env python3

"""
Description:
This ROS2 node periodically publishes "I love TS" messages to a topic.

------
Publishing Topics:
The channel containing  the "I love TS" messages
/py_TS_topic - std_msgs/String

Subscription Topics:
None
------

Author: Satyesh Shanker Awasthi
Date: 02 july, 2026
"""

import rclpy #Import the ROS2 client library for python
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node # Import the Node class, used for creating nodes

from std_msgs.msg import String #Import String message type for ROS2


class MinimalPyPublisher(Node):
  """_summary_
  Create a minimal publisher node

  Args:
      Node (_type_): _description_
  """

  def __init__(self):
      """_summary_
      create a custom node class for publishing messages
      """

      #initialize the node with a name
      super().__init__('minimal_py_publisher')

      #create a publisher on the topic with a queue size of 10 messages
      self.publisher_ = self.create_publisher(String, 'py_TS_topic', 10)

      #create a timer with a period of 0.5 seconds to trigger publishing of message
      timer_period = 0.5  # seconds
      self.timer = self.create_timer(timer_period, self.timer_callback)

      #initialize a counter variable for message content
      self.i = 0

  def timer_callback(self):
      """Callback function executed periodically by the time
      """
      #create a new string object
      msg = String()
      #Set the message data with a counter
      msg.data = 'I love TS: %d' % self.i
      #publish the message data with a counter
      self.publisher_.publish(msg)
      #log a message  indicating that the message has been published
      self.get_logger().info('Publishing: "%s"' % msg.data)
      self.i += 1


def main(args=None):
  """main function  to start the ROS2 Node

  Args:
      args (List, optional): _Command line arguments. Defaults to None.
  """
  try:
        with rclpy.init(args=args):
            minimal_py_publisher = MinimalPyPublisher()

            rclpy.spin(minimal_py_publisher)
            minimal_py_publisher.destroy_node()
            rclpy.shutdown()
  except (KeyboardInterrupt, ExternalShutdownException):
        pass


if __name__ == '__main__':
    main()