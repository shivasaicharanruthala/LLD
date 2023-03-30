package main

import "fmt"

type IPizza interface {
	getPrice() int
}

// MargaritaPizza is Base class
type MargaritaPizza struct {
}

func BasePizzaFactory() IPizza {
	return &MargaritaPizza{}
}

func (b *MargaritaPizza) getPrice() int {
	return 7
}

// TomatoToppings is a additional wrapper to a base pizza and in total its a pizza
type TomatoToppings struct {
	basePizza IPizza
}

func TomatoToppingsFactory(basePizza IPizza) IPizza {
	return &TomatoToppings{
		basePizza: basePizza,
	}
}

func (tt *TomatoToppings) getPrice() int {
	return tt.basePizza.getPrice() + 7
}

// CheeseToppings is a additional wrapper to a base pizza and in total its a pizza
type CheeseToppings struct {
	basePizza IPizza
}

func CheeseToppingsFactory(basePizza IPizza) IPizza {
	return &CheeseToppings{
		basePizza: basePizza,
	}
}

func (ct *CheeseToppings) getPrice() int {
	return ct.basePizza.getPrice() + 7
}

func main() {
	pizza := BasePizzaFactory()
	pizzaWithTomatoToppings := TomatoToppingsFactory(pizza)
	pizzaWithTomatoAndCheeseToppings := CheeseToppingsFactory(pizzaWithTomatoToppings)

	fmt.Printf("Price of Margatita pizza with tomato and cheese toppings: %d", pizzaWithTomatoAndCheeseToppings.getPrice())

}
