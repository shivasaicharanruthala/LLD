package main

import "fmt"

func main() {
	client := &Client{}
	mac := &Mac{}

	client.InsertLightningConnectorIntoComputer(mac)
	fmt.Println("================================================================")

	windowsMachine := &Windows{}
	windowsMachineAdapter := &WindowsAdapter{
		windowsMachine: windowsMachine,
	}

	client.InsertLightningConnectorIntoComputer(windowsMachineAdapter)
}

type Client struct {
}

func (c *Client) InsertLightningConnectorIntoComputer(com Computer) {
	fmt.Println("Client inserts Lightning connector into computer.")
	com.InsertIntoLightingPort()
}

// Computer is a client interface
type Computer interface {
	InsertIntoLightingPort()
}

// Mac service
type Mac struct {
}

func (m *Mac) InsertIntoLightingPort() {
	fmt.Println("Lightning connector is plugged into mac machine.")
}

// Windows is an unknown service
type Windows struct {
}

func (w *Windows) insertIntoUSBPort() {
	fmt.Println("USB connector is plugged into windows machine.")
}

// WindowsAdapter is an adapter
type WindowsAdapter struct {
	windowsMachine *Windows
}

func (wa *WindowsAdapter) InsertIntoLightingPort() {
	fmt.Println("Adapter converts Lightning signal to USB.")
	wa.windowsMachine.insertIntoUSBPort()
}
