package main

import "fmt"

// Computers is an Abstraction
type Computers interface {
	Print()
	SetPrinter(Printer)
}

// MacSystem is Redefined Abstraction
type MacSystem struct {
	printer Printer
}

func (m *MacSystem) Print() {
	fmt.Println("Print request for mac")
	m.printer.PrintFile()
}

func (m *MacSystem) SetPrinter(p Printer) {
	m.printer = p
}

// WindowsSystem is Redefined Abstraction
type WindowsSystem struct {
	printer Printer
}

func (w *WindowsSystem) Print() {
	fmt.Println("Print request for windows")
	w.printer.PrintFile()
}

func (w *WindowsSystem) SetPrinter(p Printer) {
	w.printer = p
}

// Printer is an Implementation
type Printer interface {
	PrintFile()
}

// Epson is a Concrete implementation of Printer interface
type Epson struct {
}

func (p *Epson) PrintFile() {
	fmt.Println("Printing by a EPSON Printer")
}

// Hp is a Concrete implementation of Printer interface
type Hp struct {
}

func (p *Hp) PrintFile() {
	fmt.Println("Printing by a HP Printer")
}

func main() {
	hpPrinter := &Hp{}
	epsonPrinter := &Epson{}

	macComputer := &MacSystem{}

	macComputer.SetPrinter(hpPrinter)
	macComputer.Print()
	fmt.Println()

	macComputer.SetPrinter(epsonPrinter)
	macComputer.Print()
	fmt.Println()

	winComputer := &WindowsSystem{}

	winComputer.SetPrinter(hpPrinter)
	winComputer.Print()
	fmt.Println()

	winComputer.SetPrinter(epsonPrinter)
	winComputer.Print()
	fmt.Println()
}
