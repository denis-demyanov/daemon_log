#!/usr/bin/env python
import signal
import daemon
import daemon.pidfile
import grp
import sys
import os
import monlog

PID_FILE = '/var/run/monlog.pid'


def shutdown(signum, frame):
    sys.exit(0)


def stop():
	pidfile = daemon.pidfile.PIDLockFile(path=PID_FILE)
	if pidfile.is_locked():
		try:
			os.kill(pidfile.read_pid(), signal.SIGTERM)
			if pidfile.is_locked():
				sys.exit(1)
		except:
			exit(1)
		return True
	return True


def start():
	pidfile = daemon.pidfile.PIDLockFile(path=PID_FILE)
	if pidfile.is_locked():
		print('daemon instance is running with PID = {}'.format(pidfile.read_pid()))
		print('try "restart" option')
		sys.exit(1)
	with context:
		monlog.monitor()


def restart():
	if stop():
		start()


context = daemon.DaemonContext(
    working_directory='/var/lib/monlog',
    umask=0o002,
    pidfile=daemon.pidfile.PIDLockFile(PID_FILE)
    )
context.signal_map = {
    signal.SIGTERM: shutdown,
    signal.SIGHUP: restart,
    signal.SIGUSR1: restart
    }
context.gid = grp.getgrnam('root').gr_gid


def main():
	if len(sys.argv) != 2:
		print('Only start|stop|restart argument is acceptable')
		exit(1)
	if 'start' == sys.argv[1]:
		start()
	elif 'stop' == sys.argv[1]:
		stop()
	elif 'restart' == sys.argv[1]:
		restart()
	else:
		print('Wrong argument "{0}". Try:\nmonlog_d start|stop|restart'.format(sys.argv[1]))
		exit(1)


if __name__ == '__main__':
	main()
