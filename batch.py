
class Batch(object):
    """ Batch of distillate class """

    def __init__(self, style: str, date: str, og: float, volume: float):
        self.style = style
        self.date = date
        self.original_gravity = og
        self.volume = volume
        self.final_gravity = 0
        self.abv = 0
        self.run = []

    def __str__(self):
        total_collected, total_alc_collected, total_alc = self.calc_collection_totals()
        return ('Style: {}\nDate Create: {}\nOG: {}; FG: {}; ABV: {}% \nTotals:\n\t\
Collected: {}ml; Total Alc Collected: {}ml\n\tTotal Alcohol: {}'
                .format(self.style,
                        self.date,
                        self.original_gravity,
                        self.final_gravity,
                        round(self.abv * 100, 2),
                        total_collected,
                        total_collected,
                        total_alc))

    def update_final_gravity(self):
        """
        Updates the final gravity
        :return:
        """
        fg = float(input("Enter Final Gravity: "))
        self.final_gravity = fg
        self.calc_abv()

    def calc_abv(self):
        """
        Calculates the the alcohol by volume and updates abv variable
        :return:
        """
        self.abv = round((self.original_gravity - self.final_gravity) * 1.3125, 2)

    def update_run(self):
        """

        :return:
        """
        while True:
            stop = input("Add run info (Y/N): ")
            if stop.lower() == 'n':
                break
            volume = int(input("Enter Collected Volume (ml): "))
            tralles = int(input("Enter Tralles: "))
            head_temp = float(input("Enter head temp: "))
            self.run.append((volume, tralles, head_temp))
            self.show_collected_info()

    def start_run(self):
        """

        :return:
        """
        if not self.final_gravity:
            self.update_final_gravity()
            self.calc_abv()
        elif not self.calc_abv():
            self.calc_abv()

        self.update_run()

    def show_collected_info(self):
        """

        :return:
        """
        total_collected, total_alc_collected, total_alc = self.calc_collection_totals()

        print('Total Collected: {} ml'.format(total_collected))
        print('Total Alcohol Collected: {} ml'.format(total_alc_collected))
        print('Remaining Alcohol: {} ml'.format((total_alc * 1000) - total_alc_collected))

    def calc_collection_totals(self):
        total_collected = 0
        total_alc_collected = 0
        total_alc = round(self.volume * self.abv, 2)

        for i in range(len(self.run)):
            total_collected += self.run[i][0]
            total_alc_collected += self.run[i][0] * (self.run[i][1] / 100)

        return total_collected, total_alc_collected, total_alc

