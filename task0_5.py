def area_of_triangle(side_length1, side_length2,side_length3):
    semi_perimeter = (side_length1 + side_length2 + side_length3)/2 
    return (  semi_perimeter * (semi_perimeter-side_length1) * (semi_perimeter-side_length2) * (semi_perimeter-side_length3)  )**0.5  #as per Heron's formula 

print(area_of_triangle(3,4,5))
print(area_of_triangle(6,8,10))