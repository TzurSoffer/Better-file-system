# Better file system
it makes writing to files easy

#how to use

import simpleFiles

file = simpleFiles.MakeFile("fileName")

file.write("text") writes in the file "text"

file.changeLine(line, "new info") changes the line to "new info"

file.clear() deletes the content of the file

file.append("info") adds a new line with the text "info"

file.getLine(line) returns the content of the line
