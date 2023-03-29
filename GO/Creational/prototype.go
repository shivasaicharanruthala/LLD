package main

import "fmt"

// INode is a prototype interface
type INode interface {
	print(string)
	clone() INode
}

// File is Concrete prototype
type File struct {
	name string
}

func (f *File) print(indentation string) {
	fmt.Println(indentation + f.name)
}

func (f *File) clone() INode {
	return &File{name: f.name + "_clone"}
}

// Folder is a concrete prototype
type Folder struct {
	children []INode
	name     string
}

func (f *Folder) print(indentation string) {
	fmt.Println(indentation + f.name)
	for _, i := range f.children {
		i.print(indentation + indentation)
	}
}

func (f *Folder) clone() INode {
	cloneFolder := &Folder{name: f.name + "_clone"}
	var tempChildren []INode

	for _, i := range f.children {
		childCopy := i.clone()
		tempChildren = append(tempChildren, childCopy)
	}

	cloneFolder.children = tempChildren

	return cloneFolder
}

func main() {
	file1 := &File{name: "File1"}
	file2 := &File{name: "File2"}
	file3 := &File{name: "File3"}

	folder1 := &Folder{
		children: []INode{file1},
		name:     "Folder1",
	}

	folder2 := &Folder{
		children: []INode{folder1, file2, file3},
		name:     "Folder2",
	}

	fmt.Println("\nPrinting hierarchy for Folder2")
	folder2.print("  ")

	cloneFolder := folder2.clone()
	fmt.Println("\nPrinting hierarchy for clone Folder")
	cloneFolder.print("  ")
}
