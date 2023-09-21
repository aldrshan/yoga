import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import threading
import time

class YogaTastic(toga.App):

    def startup(self):
        # Data structure for yoga poses
        self.yoga_poses = {
            'day1': [
                {'name': "Child's Pose", 'image': "resources/img/childs_pose.jpg"},
                {'name': "Cat-Cow Pose", 'image': "resources/img/cat_cow.jpg"},
                {'name': "Downward-Facing Dog", 'image': "resources/img/down_dog.jpg"},
                {'name': "Three-Legged Dog (Right)", 'image': "resources/img/three_leg_dog.jpg"},
                {'name': "Low Lunge (Right)", 'image': "resources/img/low_lunge.jpg"},
                {'name': "Three-Legged Dog (Left)", 'image': "resources/img/three_leg_dog.jpg"},
                {'name': "Low Lunge (Left)", 'image': "resources/img/low_lunge.jpg"},
                {'name': "Mountain Pose", 'image': "resources/img/mountain.jpg"},
                {'name': "Standing Forward Bend", 'image': "resources/img/standing_forward_bend.jpg"},
                {'name': "Halfway Lift", 'image': "resources/img/halfway_lift.jpg"},
            ],
            'day2': [
                {'name': "Easy Pose", 'image': "resources/img/easy_pose.jpg"},
                {'name': "Twist (Right)", 'image': "resources/img/seated_twist.jpg"},
                {'name': "Twist (Left)", 'image': "resources/img/seated_twist.jpg"},
                {'name': "Tabletop Pose", 'image': "resources/img/tabletop_pose.jpg"},
                {'name': "Thread the Needle (Right)", 'image': "resources/img/thread_the_needle.jpg"},
                {'name': "Thread the Needle (Left)", 'image': "resources/img/thread_the_needle.jpg"},
                {'name': "Puppy Pose", 'image': "resources/img/puppy_pose.jpg"},
                {'name': "Cobra Pose", 'image': "resources/img/cobra_pose.jpg"},
                {'name': "Child's Pose", 'image': "resources/img/childs.jpg"},
                {'name': "Corpse Pose", 'image': "resources/img/corpse_pose.jpg"},
            ],
                        'day3': [
                {'name': "Seated Forward Bend", 'image': "resources/img/seated_forward_bend.jpg"},
                {'name': "Seated Wide-Legged Forward Bend", 'image': "resources/img/seated_wide_forward_bend.jpg"},
                {'name': "Bound Angle Pose", 'image': "resources/img/bound_angle.jpg"},
                {'name': "Bridge Pose", 'image': "resources/img/bridge_pose.jpg"},
                {'name': "Happy Baby", 'image': "resources/img/happy_baby.jpg"},
                {'name': "Supine Twist (Right)", 'image': "resources/img/supine_twist.jpg"},
                {'name': "Supine Twist (Left)", 'image': "resources/img/supine_twist.jpg"},
                {'name': "Reclined Butterfly", 'image': "resources/img/reclined_butterfly.jpg"},
                {'name': "Corpse Pose", 'image': "resources/img/corpse_pose.jpg"},
            ],
            'day4': [
                {'name': "Mountain Pose", 'image': "resources/img/mountain.jpg"},
                {'name': "Chair Pose", 'image': "resources/img/chair_pose.jpg"},
                {'name': "Standing Forward Bend", 'image': "resources/img/standing_forward_bend.jpg"},
                {'name': "Halfway Lift", 'image': "resources/img/halfway_lift.jpg"},
                {'name': "High Plank", 'image': "resources/img/high_plank.jpg"},
                {'name': "Low Plank", 'image': "resources/img/low_plank.jpg"},
                {'name': "Upward-Facing Dog", 'image': "resources/img/up_dog.jpg"},
                {'name': "Downward-Facing Dog", 'image': "resources/img/down_dog.jpg"},
                {'name': "Warrior I (Right)", 'image': "resources/img/warrior_one.jpg"},
                {'name': "Warrior I (Left)", 'image': "resources/img/warrior_one.jpg"},
            ],
            'day5': [
                {'name': "Warrior II (Right)", 'image': "resources/img/warrior_two.jpg"},
                {'name': "Warrior II (Left)", 'image': "resources/img/warrior_two.jpg"},
                {'name': "Extended Side Angle (Right)", 'image': "resources/img/extended_side_angle.jpg"},
                {'name': "Extended Side Angle (Left)", 'image': "resources/img/extended_side_angle.jpg"},
                {'name': "Reverse Warrior (Right)", 'image': "resources/img/reverse_warrior.jpg"},
                {'name': "Reverse Warrior (Left)", 'image': "resources/img/reverse_warrior.jpg"},
                {'name': "Triangle Pose (Right)", 'image': "resources/img/triangle_pose.jpg"},
                {'name': "Triangle Pose (Left)", 'image': "resources/img/triangle_pose.jpg"},
                {'name': "Wide-Legged Forward Bend", 'image': "resources/img/wide_forward_bend.jpg"},
                {'name': "Pyramid Pose (Right)", 'image': "resources/img/pyramid_pose.jpg"},
                {'name': "Pyramid Pose (Left)", 'image': "resources/img/pyramid_pose.jpg"},
            ],
            'day6': [
                {'name': "Tree Pose (Right)", 'image': "resources/img/tree_pose.jpg"},
                {'name': "Tree Pose (Left)", 'image': "resources/img/tree_pose.jpg"},
                {'name': "Eagle Pose (Right)", 'image': "resources/img/eagle_pose.jpg"},
                {'name': "Eagle Pose (Left)", 'image': "resources/img/eagle_pose.jpg"},
                {'name': "Dancer Pose (Right)", 'image': "resources/img/dancer_pose.jpg"},
                {'name': "Dancer Pose (Left)", 'image': "resources/img/dancer_pose.jpg"},
                {'name': "Half Camel Pose (Right)", 'image': "resources/img/half_camel.jpg"},
                {'name': "Half Camel Pose (Left)", 'image': "resources/img/half_camel.jpg"},
                {'name': "Child's Pose", 'image': "resources/img/child.jpg"},
            ],
            'day7': [
                {'name': "Cat-Cow Pose", 'image': "resources/img/cat_cow.jpg"},
                {'name': "Downward-Facing Dog", 'image': "resources/img/down_dog.jpg"},
                {'name': "Pigeon Pose (Right)", 'image': "resources/img/pigeon_pose.jpg"},
                {'name': "Pigeon Pose (Left)", 'image': "resources/img/pigeon_pose.jpg"},
                {'name': "Seated Forward Bend", 'image': "resources/img/seated_forward_bend.jpg"},
                {'name': "Seated Twist (Right)", 'image': "resources/img/seated_twist.jpg"},
                {'name': "Seated Twist (Left)", 'image': "resources/img/seated_twist.jpg"},
                {'name': "Boat Pose", 'image': "resources/img/boat_pose.jpg"},
                {'name': "Plow Pose", 'image': "resources/img/plow_pose.jpg"},
                {'name': "Corpse Pose", 'image': "resources/img/corpse_pose.jpg"},
            ],
        }

        self.current_pose_index = 0
        self.selected_day = 'day1'
        self.current_time = 60  # 1 minute in seconds
        self.timer_running = False



        # UI Elements
        self.pose_image = toga.ImageView('resources/img/childs_pose.jpg')
        self.workout_select = toga.Selection(items=[f"Day {i}" for i in range(1, 8)], on_select=self.update_image)
        self.start_pause_button = toga.Button('Start', on_press=self.start_pause)
        self.timer_label = toga.Label('01:00')

        # Layout
        box = toga.Box(
            children=[
                self.pose_image,
                self.workout_select,
                self.start_pause_button,
                self.timer_label
            ],
            style=Pack(direction=COLUMN, padding=100)
        )

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = box
        self.main_window.show()

    def countdown(self):
        while self.current_time > 0 and self.timer_running:
            mins, secs = divmod(self.current_time, 60)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            self.timer_label.text = timeformat
            time.sleep(60)  # Sleep for 1 minute
            self.current_time -= 1

        if self.current_time == 0:
            self.start_pause(self.start_pause_button)

    def update_image(self, widget):
        selected_day = widget.value.lower().replace(" ", "")
        first_pose = self.yoga_poses[selected_day][0]
        self.pose_image.image = toga.Image(first_pose['image'])
        print(f"Selected day: {selected_day}, Image path: {first_pose['image']}")
        self.current_time = 60
        self.timer_label.text = '01:00'

    def start_pause(self, widget):
        if widget.text == "Start":
            self.timer_running = True
            self.timer_thread = threading.Thread(target=self.countdown)
            self.timer_thread.start()
            widget.text = "Pause"
        else:
            self.timer_running = False
            widget.text = "Start"


def main():
    return YogaTastic()
