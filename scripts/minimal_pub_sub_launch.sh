#!/bin/bash

#Launch publisher and subscriber nodes with cleanup handle
cleanup() {
  echo "Restarting ROS2 daemon to cleanup before shutting down"
  ros2 daemon stop
  sleep 1
  ros2 daemon start
  echo "Terminating all ROS2-related processes..."
  kill 0
  exit
}

trap 'cleanup' SIGINT

#Launch the publisher node
ros2 run ros2_fundamentals_examples py_minimal_publisher.py & # & for background process( log not displayed )

sleep 2

#Launch the subscriber node
ros2 run ros2_fundamentals_examples py_minimal_subscriber.py 