import rclpy  # Python library for ROS 2
from rclpy.node import Node  # Handles the creation of nodes
from sensor_msgs.msg import Image  # Image is the message type
from cv_bridge import CvBridge  # Package to convert between ROS and OpenCV Images
import cv2  # OpenCV library


class ImageChange(Node):
    """
    Create an ImageSubscriber class, which is a subclass of the Node class.
    """
    def __init__(self, video_input, video_out):
        """
        Class constructor to set up the node
        """
        # Initiate the Node class's constructor and give it a name
        super().__init__('image_changer')
        self.video_input = video_input
        self.video_out = video_out

        # Create the subscriber. This subscriber will receive an Image
        # from the video_frames topic. The queue size is 10 messages.
        self.subscription = self.create_subscription(
            Image,
            self.video_input,
            self.image_callback,
            10)
        #self.subscription  # prevent unused variable warning

        # Create the puisher
        self.publisher = self.create_publisher(
            Image,
            self.video_out,
            10)

        # Used to convert between ROS and OpenCV images
        self.br = CvBridge()

    def image_callback(self, data):
        """
        Callback function.
        """
        # Display the message on the console
        #self.get_logger().info('Receiving video frame')
        # Convert ROS Image message to OpenCV image
        current_frame = self.br.imgmsg_to_cv2(data)

        # Changing video
        grayFrame = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)
        (thresh, b_and_w) = cv2.threshold(grayFrame, 127, 255, cv2.THRESH_BINARY)
        changed_image = b_and_w

        #cv2.imshow("changed_image", blackAndWhiteFrame)
        #cv2.waitKey(1)

        # Convert OpenCV image message to ROS Image and publish
        final_image = self.br.cv2_to_imgmsg(changed_image)
        self.publisher.publish(final_image)


def main(args=None):

    # Initialize the rclpy library
    rclpy.init(args=args)

    # Create the node
    image_change = ImageChange('/camera/image_raw', '/changed_video')

    # Spin the node so the callback function is called.
    rclpy.spin(image_change)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    image_change.destroy_node()

    # Shutdown the ROS client library for Python
    rclpy.shutdown()


if __name__ == '__main__':
    main()
