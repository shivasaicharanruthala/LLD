package main

import "fmt"

// example - https://betterprogramming.pub/the-command-design-pattern-2313909122b5

// Device is a Receiver interface
type Device interface {
	on()
	off()
}

// Tv is a concrete receiver
type Tv struct {
	isRunning bool
}

func (t *Tv) on() {
	t.isRunning = true
	fmt.Println("Turning tv on")
}

func (t *Tv) off() {
	t.isRunning = false
	fmt.Println("Turning tv off")
}

// Command interface
type Command interface {
	execute()
}

// OnCommand is a Concrete command
type OnCommand struct {
	device Device
}

func (c *OnCommand) execute() {
	c.device.on()
}

// OffCommand is a Concrete command
type OffCommand struct {
	device Device
}

func (c *OffCommand) execute() {
	c.device.off()
}

// Button is an Invoker
type Button struct {
	command Command
}

func (b *Button) press() {
	b.command.execute()
}

func main() {
	tv := &Tv{}

	onCommand := &OnCommand{
		device: tv,
	}

	offCommand := &OffCommand{
		device: tv,
	}

	onButton := &Button{
		command: onCommand,
	}
	onButton.press()

	offButton := &Button{
		command: offCommand,
	}
	offButton.press()
}
