from models import Authors, Quotes


authors = Authors.objects()


for author in authors:
    print("-------------------")
    print(type(author.id), author.fullname)