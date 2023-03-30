package main

import "fmt"

func main() {
	account := CheckingAccountFactory("Shiva ")
	account.validateIdentity()
	account.createAccount()

	fmt.Println("")

	account = SavingsAccountFactory("Charan ")
	account.validateIdentity()
	account.createAccount()
}

type BankAccount interface {
	validateIdentity()
	createAccount()
}

type Person struct {
	name string
}

type CheckingAccount struct {
	Person
}

func CheckingAccountFactory(name string) BankAccount {
	return &CheckingAccount{
		Person{
			name: name,
		},
	}
}

func (c *CheckingAccount) validateIdentity() {
	fmt.Printf("validating identity of %s", c.name)
}

func (c *CheckingAccount) createAccount() {
	fmt.Printf("careating  checkin account for %s", c.name)
}

type SavingsAccount struct {
	Person
}

func SavingsAccountFactory(name string) BankAccount {
	return &SavingsAccount{
		Person{
			name: name,
		},
	}
}

func (s *SavingsAccount) validateIdentity() {
	fmt.Printf("validating identity of %s for creating savings account", s.name)
}

func (s *SavingsAccount) createAccount() {
	fmt.Printf("careating  savings account for %s", s.name)
}
