package main

import "fmt"

func main() {
	item := ItemFactory("Book1")

	person1 := PersonFactory("shiva", "shiva@gmail.com")
	item.Register(person1)
	person2 := PersonFactory("sai", "sai@gmail.com")
	item.Register(person2)

	item.SellItem()
	item.UnRegister(person2)
	item.SellItem()
}

type Items interface {
	Register(Persons)
	UnRegister(Persons)
	NotifyPerson()
	getName() string
	SellItem()
}

type Persons interface {
	Update(Items)
	getEmail() string
}

type Item struct {
	name              string
	interestedPersons []Persons
}

func ItemFactory(name string) Items {
	return &Item{
		name: name,
	}
}

func (item *Item) Register(person Persons) {
	item.interestedPersons = append(item.interestedPersons, person)
}

func (item *Item) UnRegister(person Persons) {
	item.interestedPersons = remove(item.interestedPersons, person)
}

func (item *Item) NotifyPerson() {
	for _, person := range item.interestedPersons {
		person.Update(item)
	}
}

func (item *Item) getName() string {
	return item.name
}

func (item *Item) SellItem() {
	item.NotifyPerson()
}

type Person struct {
	name  string
	email string
}

func PersonFactory(name, email string) Persons {
	return &Person{
		name:  name,
		email: email,
	}
}

func (person *Person) Update(item Items) {
	if item.getName() == "Book1" {
		fmt.Printf("Sending email to customer %s for item %s\n", item.getName(), person.email)
	}
}

func (person *Person) getEmail() string {
	return person.email
}

func remove(persons []Persons, personToRemove Persons) []Persons {
	personsLength := len(persons)
	for i, person := range persons {
		if personToRemove.getEmail() == person.getEmail() {
			persons[personsLength-1], persons[i] = persons[i], persons[personsLength-1]
			return persons[:personsLength-1]
		}
	}
	return persons
}
