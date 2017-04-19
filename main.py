import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk
from subprocess import call

def main():
	builder = gtk.Builder()
	builder.add_from_file('main.ui')	

	main_win = builder.get_object('main')
	pidbox = builder.get_object('pidbox')
	term_button = builder.get_object('sigterm')
	kill_button = builder.get_object('sigkill')

	main_win.connect('destroy', gtk.main_quit)
	term_button.connect('clicked', end_proc, ('term', pidbox))
	kill_button.connect('clicked', end_proc, ('kill', pidbox))

	gtk.main()

def end_proc(widget, data):
	signal = data[0]
	pidbox = data[1]

	pid = pidbox.get_text()

	if signal == 'term':
		command = ('kill -SIGTERM ' + pid).split(' ')
		call(command)
	if signal == 'kill':
		command = ('kill -SIGKILL ' + pid).split(' ')
		call(command)

	gtk.main_quit()

if __name__ == '__main__':
	main()