from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.button import Label
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
from kivy.properties import ObjectProperty, StringProperty
import pickle
from hmm import hmm
from smartdictionary import SmartDictionary

Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '200')


class GridLayout(GridLayout):
    label_wid = ObjectProperty()
    text_wid = ObjectProperty()
    with open('trained_test.pkl', 'rb') as finput:
        load_net = pickle.load(finput) 
    net = load_net
    sd = SmartDictionary(SmartDictionary.SMART_WORDSEN_BIGRAM)
    previous_len = 0
    def do_action(self):
        self.label_wid.text = self.text_wid.text

    def whitelist_chars(self,text):
        if len(text) > 0:
            if text[-1] == ' ':
                self.correct()

    def correct(self):
        inserted = self.text_wid.text.split()
        print(inserted)
        if len(inserted) == 1:
            correct, probability = self.net.build_viterbi(2,25,inserted[0], self.sd)
            self.previous_len = 1
        elif len(inserted) == self.previous_len + 1:
            correct, probability = self.net.add_viterbi_layer(2,25,inserted[-1])
            self.previous_len += 1
        else:
            return
        self.label_wid.text = ' '.join(correct)


class GridLayoutApp(App):
    def build(self):
        return GridLayout()

prova=GridLayoutApp()
prova.run()
