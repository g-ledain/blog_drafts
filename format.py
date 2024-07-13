import re
import os

thisDir = os.path.dirname(os.path.realpath(__file__))
for subdir, dirs, files in os.walk(os.path.join(thisDir,"unformatted")):
    for file in files:
        with open(os.path.join(thisDir,"unformatted",file),"r") as rawFile:
            rawFileText = rawFile.read()
        latexRegex = r"(?<!\\)\$\$|(?<!\\)\$"#matches text between single or double dollar signs, but doesn't match \$
        #see https://stackoverflow.com/questions/35004800/regex-match-a-dollar-without-a-backslash-before-it
        dollars=re.findall(latexRegex,rawFileText)
        body=re.split(latexRegex,rawFileText)
        parsed=""
        for i in range(len(dollars)):
            parsed+=body[i]
            if dollars[i]=="$$":
                tag="div"
            if dollars[i]=="$":
                tag="span"
            
            if i%2==0:
                parsed+="<"+tag+">"
                parsed+=dollars[i]
            if i%2!=0:
                parsed+=dollars[i]
                parsed+="</"+tag+">"
            
        parsed+=body[-1]
        with open(os.path.join(thisDir,"_posts",file),"w") as parsedFile:
            parsedFile.write(parsed)
            parsedFile.close()
