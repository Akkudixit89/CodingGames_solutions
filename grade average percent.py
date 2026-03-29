marks1=float(input("enter first marks="))
marks2=float(input("enter first marks="))
marks3=float(input("enter first marks="))
marks4=float(input("enter first marks="))
marks_obtained=marks1+marks2+marks3+marks4
average=marks_obtained/4
print("average marks of student=",average)
percent=(marks_obtained/4)*100
if(percent>90):
    print("grade A")
elif(percent>70 and percent<90):
    print("grade B")
elif(percent>50 and percent<70):
    print("grade C")
else:
    print("grade D")
