class Television:
    global MIN_CHANNEL
    global MAX_CHANNEL
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel
    global MIN_VOLUME
    global MAX_VOLUME
    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self):
        """
        - Create a private variable to store the TV channel. It should be set to the minimum TV channel by default.
        - Create a private variable to store the TV volume. It should be set to the minimum TV volume by default.
        - Create a private variable to store the TV status. The TV should start when it is off.
        """
        self.channel = MIN_CHANNEL
        self.volume = MIN_VOLUME
        self.status = False
        pass

    def power(self):
        """
        - This method should be used to turn the TV on/off.
        - If called on a TV object that is off, the TV object should be turned on.
        - If called on a TV object that is on, the TV object should be turned off.
        """
        if self.status == False:
            self.status = True
        else:
            self.status = False
        pass

    def channel_up(self):
        """
        - This method should be used to adjust the TV channel by incrementing its value.
        - It should only work for a TV that is on.
        - If the method is called when one is on the MAX_CHANNEL, it should take the TV channel back to the MIN_CHANNEL.
        """
        if self.status == True:
            if self.channel == MAX_CHANNEL:
                self.channel = MIN_CHANNEL
            else:
                self.channel += 1

    def channel_down(self):
        """
        - This method should be used to adjust the TV channel by decrementing its value.
        - It should only work for a TV that is on.
        - If the method is called when one is on the MIN_CHANNEL, it should take the TV channel back to the MAX_CHANNEL.
        """
        if self.status == True:
            if self.channel == MIN_CHANNEL:
                self.channel = MAX_CHANNEL
            else:
                self.channel -= 1

    def volume_up(self):
        """
        - This method should be used to adjust the TV volume by incrementing its value.
        - It should only work for a TV that is on.
        - If the method is called when one is on the MAX_VOLUME, the volume should not be adjusted.
        """
        if self.status == True:
            if self.volume == MAX_VOLUME:
                pass
            else:
                self.volume += 1
        pass

    def volume_down(self):
        """
        - This method should be used to adjust the TV volume by decrementing its value.
        - It should only work for a TV that is on.
        - If the method is called when one is on the MIN_VOLUME, the volume should not be adjusted.
        """
        if self.status == True:
            if self.volume == MIN_VOLUME:
                pass
            else:
                self.volume -= 1
            pass


    def __str__(self):
        """
        - This method should be used to return the TV status using the format shown in the comments of main.py
        """
        return "TV status: Is on = {}, Channel = {}, Volume = {}".format(self.status,self.channel,self.volume)
        pass
