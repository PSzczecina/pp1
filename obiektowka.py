#task8##############################
class Phone():
    def __init__(self, state = "disabled", wifi = False, battery=100, battery_saving = False):
        self.state = state
        self.wifi = wifi
        self.battery = battery
        self.battery_saving = battery_saving

    
    def uruchom_lub_wylacz(self):
        if self.state == "disabled":
            self.state = "active"
        else:
            self.state = "disabled"
    def zadzwon(self, telephone_number = 456244592):
        if telephone_number != int(1):
            print("numer poprawny, no to dzwoni się...")
        else:
            print("nieznany numer telefonu")
    def change_battery_saving(self):
        if self.battery_saving == True:
            self.battery_saving = False
        elif self.battery_saving == False:
            self.battery_saving = True
        print(f"tryb oszczedzania energii: {self.battery_saving}")
    def opowiedz_o_sobie(self):
        print(f"telefon jest {self.state}. Wifi: {self.wifi}. Bateria: {self.battery}%. Tryb oszczędzania energii: {self.battery_saving}")




'''huawei = Phone()
huawei.zadzwon()
huawei.change_battery_saving()
huawei.opowiedz_o_sobie()
huawei.battery = 70
print(huawei.battery,"%")'''



#task10##############################
class Song():
    def __init__(self, title, author, release_year, album):
        self.title = title
        self.author = author
        self.release_year = release_year
        self.album = album
    
    def __str__(self):
        return "Song: "+ self.title +"\nAuthor: "+self.author +"\nAlbum: "+self.album+"\nRelease Year: " +str(self.release_year) + "\n"

'''song1 = Song("Renegade", "Kavinsky", 2022, "Reborn")
song2 = Song("Dzieci Wybiegły", "Elektryczne Gitary", 1993, "A Ty Co")
print(song1)
print(song2)'''


#teraz będzie taka sekwencja zadań
#task11##############################

class TV():
    #11
    def __init__(self, channel_no=1):
        self.is_on = False
        self.channel_no = channel_no #12

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def show_status(self):
        if self.is_on:
            print(f"TV is functioning. channel {self.channel_no}")
        elif self.is_on == False:
            print("TV is not working")
        else:
            print("Something imploded")
    #13
    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no
    
tv1 = TV()
tv1.show_status()
tv1.turn_on()
tv1.show_status()
tv1.turn_off()
tv1.show_status()
        