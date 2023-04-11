import shelve


class Batch(object):
    """ Batch of distillate class """

    def __init__(self):
        self._style = None
        self._date = None
        self._original_gravity = 1.000
        self.volume = volume
        self.name = style + '_' + date
        self.final_gravity = 0
        self.abv = 0
        self.run = []
		
	@setter
	def style(self, style: str):
		"""Set the Style of the Batch"""
		self._style = style
	
	@setter
	def date(self, date: str):
		self._date = date
	
	@setter
	def orgin(self, orginal_gravity: float):
		"""Set the orginal specific gravity"""
		self._orginal_gravity = orginal_gravity
		
	@setter
	def volume(self, volume):
		"""Set the volume in liters"""
		self._volume = volume

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

    def save_data(self, location):
        db = shelve.open(location)
        db[self.name] = self
        db.close()

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

    def update_run(self, run_info: tuple):
        """

        :return:
        """
        self.run.append(run_info)

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
        total_alc = round(self.volume * float(self.abv), 2)

        for i in range(len(self.run)):
            total_collected += self.run[i][0]
            total_alc_collected += self.run[i][0] * (self.run[i][1] / 100)

        return total_collected, total_alc_collected, total_alc

    def update_info(self, location, changes: dict = {}, ):
        for change in changes.keys():
            if change == 'style':
                self.style = changes[change]
            elif change == 'date':
                self.date = changes[change]
            elif change == 'og':
                self.original_gravity = changes[change]
            elif change == 'fg':
                self.final_gravity = changes[change]
            elif change == 'volume':
                self.volume = changes[change]

        self.calc_abv()

        self.save_data(location)

    def calc_cum_totals(self, ind):
        cum_collected = 0
        cum_alc_collected = 0
        total_alc = round(self.volume * float(self.abv), 2)

        for i in range(ind):
            cum_collected += self.run[i][0]
            cum_alc_collected += self.run[i][0] * (self.run[i][1] / 100)

        alc_remaining = round(total_alc - cum_alc_collected / 1000, 2)

        return (cum_collected, cum_alc_collected, alc_remaining)


