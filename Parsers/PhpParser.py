import re

class PhpParser:

    commentPatter = r"/[\*]{1,2}[^(\*/)]*[\s\S]]*\*/|//[^\n]*$"
    linkPattern = r"(?:require_once|require|include_once|include)[^\n][\s|(]*['|\"]{1}([\s\w\-.()]*)['|\"]{1}"

    def removeComments(self, file):
        file = re.sub(self.commentPatter, '', file, 0, re.MULTILINE)
        return file

    def findDependencies(self, file):
        dependencies = re.findall(self.linkPattern, file, re.MULTILINE)
        return dependencies