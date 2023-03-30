package main

import "fmt"

/*
Reference: https://refactoring.guru/design-patterns/strategy
Intent: lets you define a family of algorithms, put each of them into a separate class, and make their objects interchangeable.

Strategy is a behavioral design pattern that turns a set of behaviors into objects and makes them interchangeable
inside original context object.

Context delegates the creating different algorithm objects into different class and each class represents one algorithm.
Context class is class which keeps reference to the algorithm chosen by the client and this can be modified
at runtime to. It works with all strategies through the same generic interface, which only exposes a single method for
triggering the algorithm encapsulated within the selected strategy
*/
func main() {
	fmt.Println("Client: Strategy is set to normal sorting.")
	ctx := ContextFactory(StrategyFactoryA())
	ctx.doSomeBusinessLogic()

	fmt.Println("Client: Strategy is set to reverse sorting.")
	ctx.setStrategy(StrategyFactoryB())
	ctx.doSomeBusinessLogic()
}

type Strategy interface {
	doAlgorithm(data []int) []int
}

type ConcreteStrategyA struct {
}

type ConcreteStrategyB struct {
}

type Context struct {
	strategy Strategy
}

func ContextFactory(strategy Strategy) *Context {
	return &Context{
		strategy: strategy,
	}
}

func (c *Context) setStrategy(strategy Strategy) {
	c.strategy = strategy
}

func (c *Context) doSomeBusinessLogic() []int {
	return c.strategy.doAlgorithm([]int{7, 4, 3, 6, 9})
}

func StrategyFactoryA() Strategy {
	return &ConcreteStrategyA{}
}

func StrategyFactoryB() Strategy {
	return &ConcreteStrategyB{}
}

func (a *ConcreteStrategyA) doAlgorithm(data []int) []int {
	fmt.Println("Strategy A")

	return []int{}
}

func (b *ConcreteStrategyB) doAlgorithm(data []int) []int {
	fmt.Println("Strategy B")

	return []int{}
}
