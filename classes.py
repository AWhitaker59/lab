class Television:
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel
    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self) -> None:
        """

        """
        self.channel: int = Television.MIN_CHANNEL
        self.volume: int = Television.MIN_VOLUME
        self.status: bool = False
        pass

    def power(self) -> None:
        """
        This turns the selected television on if currently off
        and off if currently on
        """
        if self.status is False:
            self.status = True
        else:
            self.status = False
        pass

    def channel_up(self) -> None:
        """
        This raises the channel by 1 on the selected television
        or cycles the channel to the minimum if the current channel was the maximum
        """
        if self.status is True:
            if self.channel == Television.MAX_CHANNEL:
                self.channel = Television.MIN_CHANNEL
            else:
                self.channel += 1

    def channel_down(self) -> None:
        """
        This lowers the channel by 1 on the selected television
        or cycles the channel to the maximum of the current channel was the minimum
        """
        if self.status is True:
            if self.channel == Television.MIN_CHANNEL:
                self.channel = Television.MAX_CHANNEL
            else:
                self.channel -= 1

    def volume_up(self) -> None:
        """
        This raises the volume of the selected television by 1
        or does nothing if the volume is already at the maximum
        """
        if self.status is True:
            if self.volume == Television.MAX_VOLUME:
                pass
            else:
                self.volume += 1
        pass

    def volume_down(self) -> None:
        """
        This lowers the volume of the selected television by 1
        or does nothing if the volume is already at the minimum
        """
        if self.status is True:
            if self.volume == Television.MIN_VOLUME:
                pass
            else:
                self.volume -= 1
            pass

    def __str__(self):
        """
        This returns the current status of the Television
        """
        return "TV status: Is on = {}, Channel = {}, Volume = {}".format(self.status, self.channel, self.volume)
        pass
