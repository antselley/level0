def area_of_triangle(a,b,c):
    s = (a+b+c)/2 #The Semi Perimeter
    return (  s * (s-a) * (s-b) * (s-c)  )**0.5  #as per Heron's formula 

print(area_of_triangle(3,4,5))
print(area_of_triangle(6,8,10))