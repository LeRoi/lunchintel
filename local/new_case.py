import os, sys, time
from shutil import copyfile

year = "1L"
term = "Spring Term"
classmap = {
    "civpro":"Civil Procedure",
    "crim":"Criminal Law",
    "lrw":"Legal Reading and Writing",
    "legreg":"Legislation and Regulation",
    "torts":"Torts",
    "k":"Contracts",
    "prop":"Property",
    "media":"Mass Media",
    "china":"China Law"
}

def get_class_name():
    for key in classmap:
        print "%s - %s" % (key, classmap[key])
    return classmap[raw_input("Key: ").lower()]

def main():
    casename = raw_input("Case: ") if len(sys.argv) < 2 \
               else sys.argv[1]
    classname = get_class_name() if len(sys.argv) < 3 \
                else classmap[sys.argv[2].lower()]
    target = "../../%s/%s/%s/Briefs/%s.docx" % (year, term, classname, casename)
    target_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), target)
    if not os.path.isfile(target_path):
        copyfile("../../Brief Template.docx", target)
        os.startfile(target_path)
    else:
        print "Error. File already exists."
    
if __name__ == "__main__":
    main()
