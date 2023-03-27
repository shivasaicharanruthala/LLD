package main

import "fmt"

type Patient struct {
	name              string
	registrationDone  bool
	doctorCheckupDone bool
	medicineDone      bool
	paymentDone       bool
}

type Department interface {
	setNext(department Department)
	execute(patient *Patient)
}

type Reception struct {
	next Department
}

func ReceptionFactory(next Department) Department {
	return &Reception{
		next: next,
	}
}

func (r *Reception) execute(p *Patient) {
	if p.registrationDone {
		fmt.Println("Patient registration already done")
		r.next.execute(p)
		return
	}

	fmt.Println("Reception registering patient")
	p.registrationDone = true
	r.next.execute(p)

}

func (r *Reception) setNext(next Department) {
	r.next = next
}

type Doctor struct {
	next Department
}

func DoctorFactory(next Department) Department {
	return &Doctor{
		next: next,
	}
}

func (d *Doctor) execute(p *Patient) {
	if p.registrationDone {
		fmt.Println("Patient registration already done")
		d.next.execute(p)
		return
	}

	fmt.Println("Reception registering patient")
	p.registrationDone = true
	d.next.execute(p)

}

func (d *Doctor) setNext(next Department) {
	d.next = next
}

type Medical struct {
	next Department
}

func MedicalFactory(next Department) Department {
	return &Medical{
		next: next,
	}
}

func (m *Medical) execute(p *Patient) {
	if p.medicineDone {
		fmt.Println("Medicine already given to patient")
		m.next.execute(p)
		return
	}
	fmt.Println("Medical giving medicine to patient")
	p.medicineDone = true
	m.next.execute(p)
}

func (m *Medical) setNext(next Department) {
	m.next = next
}

type Cashier struct {
	next Department
}

func CashierFactory(next Department) Department {
	return &Cashier{
		next: next,
	}
}

func (c *Cashier) execute(p *Patient) {
	if p.paymentDone {
		fmt.Println("Payment Done")
	}
	fmt.Println("Cashier getting money from patient patient")
}

func (c *Cashier) setNext(next Department) {
	c.next = next
}

func main() {
	cashier := CashierFactory(nil)

	//Set next for medical department
	medical := MedicalFactory(cashier)
	medical.setNext(cashier)

	//Set next for doctor department
	doctor := DoctorFactory(medical)
	doctor.setNext(medical)

	//Set next for reception department
	reception := ReceptionFactory(doctor)
	reception.setNext(doctor)

	patient := &Patient{name: "shiva"}
	//Patient visiting
	reception.execute(patient)
}
