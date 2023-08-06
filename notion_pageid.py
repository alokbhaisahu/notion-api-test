import argparse

def convert(pageid):
    txt=pageid
    fragments=[8,4,4,4,12]
    clist=[]
    for length in fragments:
        fr=txt[:length]
        clist.append(fr)
        txt=txt[length:]
    ctxt="-".join(clist)
    return ctxt


# print(convert("fad5f51e75af46aeb23d56e8f9db761f"))

parser=argparse.ArgumentParser()

parser.add_argument("pageId",help="the 32 character long string at the end of the page url",type=str)
print()

args= parser.parse_args()
if len(args.pageId)!=32:
    print("Invalid argument, pageId must be 32 character long")
else:
    print(convert(args.pageId))
