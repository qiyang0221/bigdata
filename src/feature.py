#!/usr/bin/python
import bookFeature 

path = "../data"

book_class_path = path + "/book_class.txt"
book_path = path + "/train/book.txt"

bookFeature.getFeature(book_path,book_class_path)

