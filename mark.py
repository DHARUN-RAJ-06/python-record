name=input("enter student name")
n=int(input("enter a number of subject:"))
total=0;
for i in range(1,n+1):
        mark=int(input(f"enter a mark of subject {i}:"))
        total=total+mark
percentage=total/n;
if percentage>=90:
    print(f"Grade: A+")
    print(f"performance=outstanding")
elif percentage>=80:
      print(f"grade=A")
      print(f"performance=Excellent")
elif percentage>=70:
      print(f"grade=B")
      print(f"performance=very good")
elif percentage>=40:
      print(f"grade=c")
      print(f"performance=good")
else:
      print(f"grade=fail")
      print(f"performance=very poor")