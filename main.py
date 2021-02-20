
# tick.wav length: 0.007s
# On the accuracy of sleep timers:
# https://stackoverflow.com/questions/1133857/how-accurate-is-pythons-time-sleep
# https://www.freertos.org/a00104.html#getting-started 

from playsound import playsound
import time
import logging

logging.basicConfig(level=logging.DEBUG)

def playTickSound(bpm):

	bps = bpm / 60
	interval = 1 / bps 

	logging.debug('BPS: {}/s'.format(bps))
	logging.debug('Interval: {}s'.format(interval))

	while True:
		playsound('./tick.wav')
		time.sleep(interval - 0.007)
	

playTickSound(120)