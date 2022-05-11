def area_triangle_calc(side_one, side_two, side_three):
    half_perimeter = (side_one + side_two + side_three) / 2
    area = (half_perimeter * (half_perimeter - side_one) * (half_perimeter - side_two) * (half_perimeter - side_three) ) ** 0.5
    return area 


print(area_triangle_calc(3,4,5))