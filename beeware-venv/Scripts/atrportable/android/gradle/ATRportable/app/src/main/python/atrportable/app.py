"""
Project UE3.4 ATRportable
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import atrportable.RealTimeVideo as RealTimeVideo
import atrportable.Detection_and_Tracking as Detection_and_Tracking

class ATRportable(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box()
        button = toga.Button(
            'Face recognition',
            on_press=self.DetectionAndTracking,
            style=Pack(padding=5)
        )
        button2 = toga.Button(
            'People detection',
            on_press=self.RealTimeVideo,
            style=Pack(padding=5)
        )
        main_box.add(button)
        main_box.add(button2)
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def RealTimeVideo(self,widget):
        RealTimeVideo.main()
    def DetectionAndTracking(self, widget):
        Detection_and_Tracking.main()
def main():
    return ATRportable()
