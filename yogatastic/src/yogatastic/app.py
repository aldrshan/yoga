import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

class YogaApp(toga.App):
    def startup(self):
        # Create the main box container
        main_box = toga.Box(style=Pack(direction=COLUMN, padding=10))

        # Image view for the yoga pose
        self.pose_image = toga.ImageView('path_to_initial_image.png')
        main_box.add(self.pose_image)

        # Dropdown for workout selection
        self.workout_dropdown = toga.Selection(items=['Workout 1', 'Workout 2', ...])
        main_box.add(self.workout_dropdown)

        # Start/Pause button
        self.start_button = toga.Button('Start', on_press=self.start_workout)
        main_box.add(self.start_button)

        # Countdown timer label
        self.timer_label = toga.Label('01:00')
        main_box.add(self.timer_label)

        # Set the main window content
        self.main_window = toga.MainWindow(title="Yoga App")
        self.main_window.content = main_box
        self.main_window.show()

    def start_workout(self, widget):
        # Logic to start the workout, update the timer, etc.
        pass

def main():
    return YogaApp()
