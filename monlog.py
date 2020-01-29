import logging
import time


formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
file_h = logging.FileHandler('/var/log/mon.log', 'a')
file_h.setFormatter(formatter)
file_h.setLevel(logging.DEBUG)
logger = logging.getLogger('MONLOG')
logger.addHandler(file_h)
logger.setLevel(logging.DEBUG)


def monitor():

	# formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
	# file_h = logging.FileHandler('/var/log/mon.log', 'a')
	# file_h.setFormatter(formatter)
	# file_h.setLevel(logging.DEBUG)
	# logger = logging.getLogger('MONLOG')
	# logger.addHandler(file_h)
	# logger.setLevel(logging.DEBUG)

	while True:
		logger.debug('debug message')
		logger.warning('warning message')
		time.sleep(1)


def main():
	monitor()


if __name__ == '__main__':
	main()