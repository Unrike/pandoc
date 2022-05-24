from panflute import Header, Strong, Str, run_filters, stringify

headings = []

def duplicateHeadings(element, _):
    if isinstance(element, Header):
        string = stringify(element)
        if string in headings:
            print("This header is present more than once:" + string)
        else:
            headings.append(string)

def capsHeadings(element, _):
    if isinstance(element, Header) and element.level > 2:
        return Header(Str(stringify(element).upper()), level=element.level)
    
def setBold(document):
    document.replace_keyword("BOLD", Strong(Str("BOLD")))


if __name__ == "__main__":
    run_filters([duplicateHeadings, capsHeadings], prepare=setBold)
