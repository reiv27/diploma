import sys
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Range
from std_msgs.msg import Int16MultiArray


data_file = open(f'/home/user/Projects/diploma/sim_ws/src/ultrasonic/data/{sys.argv[1]}.txt', 'w')


class UltrasonicData(Node):  # Class for sonars

    def __init__(self):
        self.node_name = "ultrasonic_node"
        super().__init__(self.node_name)

        self.results = Int16MultiArray()
        self.results.data = [0, 0, 0, 0, 0,  # Array of data in mm
                             0, 0, 0, 0, 0]

        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 1

        # Front sonars
        self.s1 = self.create_subscription(
            Range,
            '/front_sonars/s1',
            self.s1_callback,
            10
        )

        self.s10 = self.create_subscription(
            Range,
            '/front_sonars/s10',
            self.s10_callback,
            10
        )

        self.s2 = self.create_subscription(
            Range,
            '/front_sonars/s2',
            self.s2_callback,
            10
        )

        # Right sonars
        self.s4 = self.create_subscription(
            Range,
            '/right_sonars/s4',
            self.s4_callback,
            10
        )

        self.s3 = self.create_subscription(
            Range,
            '/right_sonars/s3',
            self.s3_callback,
            10
        )

        self.s5 = self.create_subscription(
            Range,
            '/right_sonars/s5',
            self.s5_callback,
            10
        )

        # Left sonars
        self.s8 = self.create_subscription(
            Range,
            '/left_sonars/s8',
            self.s8_callback,
            10
        )

        self.s7 = self.create_subscription(
            Range,
            '/left_sonars/s7',
            self.s7_callback,
            10
        )

        self.s9 = self.create_subscription(
            Range,
            '/left_sonars/s9',
            self.s9_callback,
            10
        )

        # Back sonars
        self.s6 = self.create_subscription(
            Range,
            '/back_sonar/s6',
            self.s6_callback,
            10
        )

        # Multiple publisher
        self.pub = self.create_publisher(
            Int16MultiArray,
            '/results',
            10
        )

    # Front group's callbacks
    def s1_callback(self, msg: Range):
        if msg.range < msg.min_range or msg.range > msg.max_range:
            self.results.data[0] = -1
        else:
            self.results.data[0] = int(round(msg.range*1000))

    def s10_callback(self, msg: Range):
        if msg.range < msg.min_range or msg.range > msg.max_range:
            self.results.data[9] = -1
        else:
            self.results.data[9] = int(round(msg.range*1000))

    def s2_callback(self, msg: Range):
        if msg.range < msg.min_range or msg.range > msg.max_range:
            self.results.data[1] = -1
        else:
            self.results.data[1] = int(round(msg.range*1000))

    # Right group's callbacks
    def s4_callback(self, msg: Range):
        if msg.range < msg.min_range or msg.range > msg.max_range:
            self.results.data[3] = -1
        else:
            self.results.data[3] = int(round(msg.range*1000))

    def s3_callback(self, msg: Range):
        if msg.range < msg.min_range or msg.range > msg.max_range:
            self.results.data[2] = -1
        else:
            self.results.data[2] = int(round(msg.range*1000))

    def s5_callback(self, msg: Range):
        if msg.range < msg.min_range or msg.range > msg.max_range:
            self.results.data[4] = -1
        else:
            self.results.data[4] = int(round(msg.range*1000))

    # Left group's callbacks
    def s8_callback(self, msg: Range):
        if msg.range < msg.min_range or msg.range > msg.max_range:
            self.results.data[7] = -1
        else:
            self.results.data[7] = int(round(msg.range*1000))

    def s7_callback(self, msg: Range):
        if msg.range < msg.min_range or msg.range > msg.max_range:
            self.results.data[6] = -1
        else:
            self.results.data[6] = int(round(msg.range*1000))

    def s9_callback(self, msg: Range):
        if msg.range < msg.min_range or msg.range > msg.max_range:
            self.results.data[8] = -1
        else:
            self.results.data[8] = int(round(msg.range*1000))

    # Back sonar's callback
    def s6_callback(self, msg: Range):
        if msg.range < msg.min_range or msg.range > msg.max_range:
            self.results.data[5] = -1
        else:
            self.results.data[5] = int(round(msg.range*1000))

    # Callback for publisher's timer
    def timer_callback(self):
        self.pub.publish(self.results)
        print(f'{self.i} {self.results.data}')
        data_file.write(f'{self.i} {self.results.data}\n')
        self.i += 1


def main(args=None):

    rclpy.init(args=args)

    data_taking = UltrasonicData()

    rclpy.spin(data_taking)

    data_taking.destroy_node()
    data_file.close()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
