
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.animation import Animation
from kivy.uix.recycleview import RecycleView
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen


import webbrowser
import pandas as pd
import os


class MainPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Button(text='Back', on_press=self.go_back))

    def go_back(self, instance):
        self.manager.current = 'main'

class ImagePage(Screen):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.add_widget(Button(text='Back', on_press=self.go_back))

        def go_back(self, instance):
            self.manager.current = 'main'

class MyApp(App):
    def build(self):
        layout = FloatLayout()
        sm = ScreenManager()
        sm.add_widget(MainPage(name='main'))
        sm.add_widget(ImagePage(name='image'))

        sfondo = Image(source='cinema.jpg', size_hint=(1,1), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        label1 = Label(text='Welcome to the Netflix movie finder!', size_hint=(.5,.5), pos_hint={'center_x': 0.5, 'center_y': 0.92}, bold=True, font_size='32sp')
        button1 = Button(text="""TV Shows vs Movies - What's your pick?""", size_hint=(.4,.05), pos_hint={'center_x': 0.25, 'center_y': 0.2})
        button2 = Button(text="Year with the highest views!", size_hint=(.4,.05), pos_hint={'center_x': 0.75, 'center_y': 0.2})
        button3 = Button(text="""Most popular genre...can you guess?""", size_hint=(.4,.05), pos_hint={'center_x': 0.25, 'center_y': 0.13})
        button4 = Button(text="""Average time spent by film!""", size_hint=(.4,.05), pos_hint={'center_x': 0.75, 'center_y': 0.13})
        button5 = Button(text="""Most viewed TV Show & Film""", size_hint=(.4,.05), pos_hint={'center_x': 0.25, 'center_y': 0.06})
        button6 = Button(text="""Rank 1 for TV Show & Film""", size_hint=(.4,.05), pos_hint={'center_x': 0.75, 'center_y': 0.06})
        button1.bind(on_press=self.open_image1)
        button3.bind(on_press=self.open_image3)
        button2.bind(on_press=self.open_image2)
        button5.bind(on_press=self.open_image5)
        button4.bind(on_press=self.open_image4)
        button6.bind(on_press=self.open_image6)

        

        anim1 = Animation(color=(1,0,0,1)) + Animation(color=(1,1,1,1))
        anim1.repeat = True
        anim1.start(button1)

        anim2 = Animation(color=(1,0,0,1)) + Animation(color=(1,1,1,1))
        anim2.repeat = True
        anim2.start(button2)

        anim3 = Animation(color=(1,0,0,1)) + Animation(color=(1,1,1,1))
        anim3.repeat = True
        anim3.start(button3)

        anim5 = Animation(color=(1,0,0,1)) + Animation(color=(1,1,1,1))
        anim5.repeat = True
        anim5.start(button5)

        anim4 = Animation(color=(1,0,0,1)) + Animation(color=(1,1,1,1))
        anim4.repeat = True
        anim4.start(button4)

        anim6 = Animation(color=(1,0,0,1)) + Animation(color=(1,1,1,1))
        anim6.repeat = True
        anim6.start(button6)


        
        layout.add_widget(sfondo)
        layout.add_widget(label1)
        layout.add_widget(button1)
        layout.add_widget(button2)
        layout.add_widget(button3)
        layout.add_widget(button4)
        layout.add_widget(button5)
        layout.add_widget(button6)
        
        

        
        return layout
    
    def open_webpage(self, instance):
        webbrowser.open("https://www.netflix.com/browse")

    def open_image3(self, instance):
        popup = Popup(title='Most popular genre', content=Image(source='most_popular_genre.png'), size_hint=(.8, .8), size=(400, 400))
        popup.open()

    def open_image2(self, instance):
        popup = Popup(title='Most popular genre', content=Image(source='releases_per_year.png'), size_hint=(1, 1), size=(400, 400))
        popup.open()

    def open_image1(self, instance):
        popup = Popup(title='Most popular genre', content=Image(source='tvshowsvsmovies.png'), size_hint=(1, 1), size=(400, 400))
        popup.open()

    def open_image5(self, instance):
        popup = Popup(title='Most popular genre', content=Image(source='most_viewd_tv_show.png'), size_hint=(1, 1), size=(400, 400))
        popup.open()

    def open_image4(self, instance):
        popup = Popup(title='Most popular genre', content=Image(source='spent_by_film.png'), size_hint=(1, 1), size=(400, 400))
        popup.open()
    
    def open_image6(self, instance):
        popup = Popup(title='Most popular genre', content=Image(source='most_viewed.png'), size_hint=(1, 1), size=(400, 400))
        popup.open()


            
    

    

    
    
if __name__ == '__main__':
    
    MyApp().run()

    