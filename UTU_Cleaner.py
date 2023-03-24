#!/usr/bin/env python3

import gi
import psutil
import math

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib, Gdk

class ServerCleanupWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Ubuntu Server Cleanup")
        self.set_border_width(10)

        # Create a vertical box container to hold the buttons and circle graph
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(vbox)

        # Create a status bar
        self.statusbar = Gtk.Statusbar()
        vbox.pack_end(self.statusbar, False, False, 0)

        # Create buttons for each option
        button_empty = Gtk.Button(label="Empty trash and temporary files")
        button_empty.connect("clicked", self.on_button_empty_clicked)
        vbox.pack_start(button_empty, True, True, 0)

        button_kernels = Gtk.Button(label="Remove old kernels")
        button_kernels.connect("clicked", self.on_button_kernels_clicked)
        vbox.pack_start(button_kernels, True, True, 0)

        button_packages = Gtk.Button(label="Remove unused packages")
        button_packages.connect("clicked", self.on_button_packages_clicked)
        vbox.pack_start(button_packages, True, True, 0)

        button_disk = Gtk.Button(label="Analyze disk usage")
        button_disk.connect("clicked", self.on_button_disk_clicked)
        vbox.pack_start(button_disk, True, True, 0)

        # Create a box to hold the circle graph
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        vbox.pack_start(hbox, False, False, 0)

        # Create a Gtk.DrawingArea() widget to hold the circle graph
        self.graph = Gtk.DrawingArea()
        self.graph.set_size_request(100, 100)
        self.graph.modify_bg(Gtk.StateType.NORMAL, Gdk.color_parse("white"))

        # Connect the draw_graph method to the draw signal of the Gtk.DrawingArea() widget
        self.graph.connect('draw', self.draw_graph)

        # Add the Gtk.DrawingArea() widget to the right side of the menu
        align = Gtk.Alignment(xalign=1.0)
        align.add(self.graph)
        hbox.pack_end(align, False, False, 0)

    def on_button_empty_clicked(self, widget):
        self.statusbar.push(0, "Emptying trash and temporary files...")
        # Run the Bash script code to empty trash and temporary files
        GLib.timeout_add_seconds(2, self.statusbar.pop, 0)

    def on_button_kernels_clicked(self, widget):
        self.statusbar.push(0, "Removing old kernels...")
        # Run the Bash script code to remove old kernels
        GLib.timeout_add_seconds(2, self.statusbar.pop, 0)

    def on_button_packages_clicked(self, widget):
        self.statusbar.push(0, "Removing unused packages...")
        # Run the Bash script code to remove unused packages
        GLib.timeout_add_seconds(2, self.statusbar.pop, 0)

    def on_button_disk_clicked(self, widget):
        self.statusbar.push(0, "Analyzing disk usage...")
        # Run the Bash script code to analyze disk usage
        GLib.timeout_add_seconds(2, self.statusbar.pop, 0)

    def draw_graph(self, widget, cr):
    # Initialize the Cairo context
        cr = widget.get_window().cairo_create()

    # Get the hard drive usage percentage
        usage = psutil.disk_usage('/').percent

    # Set the circle graph parameters
        cx, cy = widget.get_allocated_width() / 2, widget.get_allocated_height() / 2
        radius = min(cx, cy) - 10
        start_angle = -90
        end_angle = start_angle + (usage / 100) * 360

    # Draw the circle graph
        cr.set_line_width(10)
        cr.set_source_rgba(0, 0.8, 0, 0.8)
        cr.arc(cx, cy, radius, start_angle * (math.pi / 180), end_angle * (math.pi / 180))
        cr.stroke()


win = ServerCleanupWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
