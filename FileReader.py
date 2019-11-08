import os
from Parsers.PhpParser import PhpParser
from Parsers.CppParser import CppParser
from Parsers.PythonParser import PythonParser


class FileReader:

    dependencies = {}

    parsers = {
        '.php': PhpParser(),
        '.cpp': CppParser(),
        '.py': PythonParser()
    }

    def readFiles(self, files):
        for fileName in files:
            filepath, extension = os.path.splitext(fileName)

            parser = self.parsers.get(extension)

            file = open(fileName, 'r')
            file = parser.removeComments(file.read())
            self.dependencies[fileName] = parser.findDependencies(file)
            print(self.dependencies)