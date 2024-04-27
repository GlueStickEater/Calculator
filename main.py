import sys
import os
import time

shape_file = open("Shapes List.txt" , "r")
shape_read = shape_file.readlines()

shape_file.close()

pa_file = open("P and A.txt", "r")
pa_read = pa_file.readlines()

pa_file.close()

vp_file = open("V and P.txt", "r")
vp_read = vp_file.readlines()

vp_file.close()

ca_file = open("C and A.txt", "r")
ca_read = ca_file.readlines()

ca_file.close()

time.sleep(.5)
welcome = "Welcome to the Calculator!"
for char in welcome:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.03)
print()

def intro():
    items = "Regular, Circle, Sphere, Rectangle, Rectangular Prism, Square, Cube, Triangle."
    for char in items:
      sys.stdout.write(char)
      sys.stdout.flush()
      time.sleep(0.03)
    print()
    global shape
    shape = input("What do you need calculated out of the list above? ")
    if shape.lower() not in items.lower():
      print("That is an invalid answer.")
      time.sleep(2.5)
      os.system("clear")
      intro()
    else:
      time.sleep(0.0)
intro()

print()

#Regular Calculator
if shape.lower() == "regular":
  def regular():
    validates = """The operations you may use are +, -, /, *, ., ()
    num**num == Powers
    Please put * inbetween () Ex: num * (num)
    You don't need to put spaces inbetween signs Ex: num*(num) <-- "Okay"
    """
    for char in validates:
      sys.stdout.write(char)
      sys.stdout.flush()
      time.sleep(0.03)
    print()    
    expression = input("What is your Mathmatical Expression (num and signs no equal)? ")
    answer_reg = eval(expression)
    answer_reg_r = f"The answer to {expression} is: {answer_reg}"
    for char in answer_reg_r:
      sys.stdout.write(char)
      sys.stdout.flush()
      time.sleep(0.03)
  regular()
# Circle
elif shape.lower() == "circle":
    def circle():
        which = input("Do you want Area or Circumference calculated? ")
        if which.lower() == "area":
            print()
            os.system("clear")
            radius_c_a = float(input("What is your Radius (num)? "))
            pi_c_a = float(input("What is your Pi approximate (num Ex:3.14)? "))
            unit_c_a = input("What is your unit of measure? ")
            radius2_c_a = radius_c_a ** 2
            circle_area = radius2_c_a * pi_c_a
            circle_area_rounded = round(circle_area, 2)
            print(f"Equation: {radius}^2 * {pi_c_a}")
            answer_c_a = f"The Area of the Circle is: {circle_area_rounded}{unit_c_a}^2"
            for char in answer_c_a:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.03)
        elif which.lower() == "circumference":
            print()
            os.system("clear")
            diameter = float(input("What is your Diameter (num)? "))
            pi_c_c = float(input("What is your Pi approximate (num Ex:3.14)? "))
            unit_c_c = input("What is your unit of measure? ")
            circle_circumference = pi_c_c * diameter
            circle_circumference_rounded = round(circle_circumference, 2)
            print(f"Equation: {pi_c_c} * {diameter}")
            answer_c_c = f"The Circumference of the Circle is: {circle_circumference_rounded}{unit_c_c}"
            for char in answer_c_c:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.03)
        else:
            if which.lower() not in [ca_file]:
               print("That is an invalid answer.")
               time.sleep(2.5)
               os.system("clear")
               circle()

    circle()

# Sphere
elif shape.lower() == "sphere":
    def sphere():
        which_s = input("Do you want to calculate Area, Volume, or Circumference? ")
        if which_s.lower() == "volume":
            print()
            os.system("clear")
            radius_s_v = float(input("What is your Radius (num)? "))
            pi_s_v = float(input("What is your Pi approximate (num Ex: 3.14)? "))
            unit_s_v = input("What is unit of measure? ")
            radius3_s_v = radius_s_v ** 3
            pi_radius_s_v = pi_s_v * radius3_s_v
            sphere_s_v_a = (4 / 3) * pi_radius_s_v
            sphere_s_v_r = round(sphere_s_v_a, 2)
            print(f"Equation: 4/3({radius_s_v}^3 * {pi_s_v})")
            answer_s_v = f"The Volume of the Sphere is: {sphere_s_v_r}{unit_s_v}^3"
            for char in answer_s_v:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.03)
        elif which_s.lower() == "circumference":
            print()
            os.system("clear")
            radius_s_c = float(input("What is your Radius (num)? "))
            pi_s_c = float(input("What is your Pi approximate (num Ex: 3.14)? "))
            unit_s_c = input("What is your unit of measure? ")
            radius2_s_c = radius_s_c * 2
            pi_radius2_s_c = radius2_s_c * pi_s_c
            sphere_s_c_r = round(pi_radius2_s_c, 2)
            print(f"Equation: {pi_s_c}({radius_s_c} * 2)")
            answer_s_c = f"The Circumference of the Sphere is: {sphere_s_c_r}{unit_s_c}"
            for char in answer_s_c:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.03)
        elif which_s.lower() == "area":
            print()
            os.system("clear")
            radius_s_a = float(input("What is your Radius (num)? "))
            pi_s_a = float(input("What is your Pi approximate (num Ex:3.14)? "))
            unit_s_a = input("What is your unit of measure?")
            radius2_s_a = radius_s_a ** 2
            pi_radius_s_a = pi_s_a * radius2_s_a
            pi_radius_s_a4 = pi_radius_s_a * 4
            sphere_s_a_r = round(pi_radius_s_a4, 2)
            print(f"Equation: 4({radius_s_a}^2 * {pi_s_a})")
            answer_s_a = f"The Area of the Sphere is: {sphere_s_a_r}{unit_s_a}^2"
            for char in answer_s_a:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.03)
        else:
            if which_s.lower() not in ["area", "volume", "circumference"]:
                print("That is an invalid answer.")
                time.sleep(2.5)
                os.system("clear")
                sphere()

    sphere()

# Rectangle
elif shape.lower() == "rectangle":
    def rectangle():
        print()
        os.system('clear')
        which_r = input("Do you want to want to calculate Area or Perimeter? ")
        if which_r.lower() == "area":
            width_r_a = float(input("What is your Width (num)? "))
            length_r_a = float(input("What is your Length (num)? "))
            unit_r_a = input("What is your unit of measure? ")
            area_r_a = width_r_a * length_r_a
            area_r_r_a = round(area_r_a, 2)
            print(f"Equation: {width_r_a} * {length_r_a}")
            answer_r_a = f"The Area of the Rectangle is {area_r_r_a}{unit_r_a}^2"
            for char in answer_r_a:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.03)
        elif which_r.lower() == "perimeter":
            width_r_p = float(input("What is your Width (num)? "))
            length_r_p = float(input("What is you Lenth (num)? "))
            unit_r_p = input("What is your unit of measure? ")
            perimeter_r_w = width_r_p * 2
            perimeter_r_l = length_r_p * 2
            perimeter_r_a = perimeter_r_l + perimeter_r_w
            perimeter_r_r_a = round(perimeter_r_a, 2)
            print(f"Equation: 2({width_r_p} + {length_r_p}")
            answer_r_p = f"The Perimeter of the Rectangle is: {perimeter_r_r_a}{unit_r_p}"
            for char in answer_r_p:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.03)
        else:
            if which_r.lower() not in [pa_file]:
                print("That is an invalid answer.")
                time.sleep(2.5)
                os.system("clear")
                rectangle()

    rectangle()
# Rectangular Prism 
elif shape.lower() == "rectangular prism":
    def RP():
        print()
        os.system('clear')
        which_rp = input("Do you want to calculate Volume or Perimeter? ")
        if which_rp.lower() == "volume":
          width_rp_v = float(input("What is your Width (num)? "))
          length_rp_v = float(input("What is your Length (num)? "))
          height_rp_v = float(input("What is your Height (num)? "))
          unit_rp_v = input("What is your unit of measure? ")
          volume_rp_v = (width_rp_v * length_rp_v) * height_rp_v
          volume_rp_v_r = round(volume_rp_v, 2)
          print(f"Equation: {height_rp_v}({width_rp_v} * {length_rp_v}")
          answer_rp_v = f"The Volume of the Rectangular Prism is: {volume_rp_v_r}{unit_rp_v}^3"
          for char in answer_rp_v:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.03)

        elif which_rp.lower() == "perimeter":
          width_rp_p = float(input("What is your Width (num)? "))
          length_rp_p = float(input("What is your Length (num)? "))
          height_rp_p = float(input("What is your Height (num)? "))
          unit_rp_p = input("What is your unit of measure? ")
          perimeter_rp_p = (width_rp_p + length_rp_p + height_rp_p) * 4
          perimeter_rp_p_r = round(perimeter_rp_p, 2)
          print(f"Eqution: 4({width_rp_p} + {length_rp_p} + {height_rp_p})")
          answer_rp_p = f"The Perimeter of the Rectangular Prism is: {perimeter_rp_p_r}{unit_rp_p}"
          for char in answer_rp_p:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.03)

        else:
          if which_rp.lower() not in [vp_file]:
            print("That is an invalid answer.")
            time.sleep(2.5)
            os.system('clear')
            RP()
    RP()  
#Square
elif shape.lower() == "square":
    def square():
      print()
      os.system('clear')
      which_square = input("Do you want to caculate Area or Perimeter? ")
      if which_square.lower() == "area":
        side_sq_a = float(input("What is your side length (num)? "))
        unit_sq_a = input("What is your unit of measure? ")
        area_sq_a = side_sq_a **2
        area_sq_r_a = round(area_sq_a, 2)
        print(f"Equation: {side_sq_a}^2")
        answer_sq_a = f"The Area of the Square is: {area_sq_r_a}{unit_sq_a}^2"
        for char in answer_sq_a:
          sys.stdout.write(char)
          sys.stdout.flush()
          time.sleep(0.03)

      elif which_square.lower() == "perimeter":
        width_sq_p = float(input("What is your Width (num)? "))
        length_sq_p = float(input("What is your Length (num)? "))
        unit_sq_p = input("What is your unit of measure? ")
        perimeter_sq_w = width_sq_p * 2
        perimeter_sq_l = length_sq_p * 2
        area_sq_p = perimeter_sq_w + perimeter_sq_l
        area_sq_r_p = round(area_sq_p, 2)
        print(f"Equation: 2({width_sq_p} + {length_sq_p})")
        answer_sq_p = f"The Perimeter of the Square is: {area_sq_r_p}{unit_sq_p}"
        for char in answer_sq_p:
          sys.stdout.write(char)
          sys.stdout.flush()
          time.sleep(0.03)

      else:
        if which_square.lower() not in [pa_file]:
          print("That is an invalid answer.")
          time.sleep(2.5)
          os.system("clear")
          square()
    square() 
#Cube Cube Cube
elif shape.lower() == "cube":
    def cube():
      which_cube = input("What do you want to calculate Volume or Perimeter? ")
      if which_cube.lower() == "volume":
        side_cube_v = float(input("What is your side length (num)? "))
        unit_cube_v = input("What is your unit of measure? ")
        volume_cube = side_cube_v ** 3
        volume_cube_r = round(volume_cube, 2)
        print(f"Equation: {side_cube_v}^3")
        answer_cube_volume = f"The Volume of the Cube is: {volume_cube_r}{unit_cube_v}^3"
        for char in answer_cube_volume:
          sys.stdout.write(char)
          sys.stdout.flush()
          time.sleep(0.03)

      elif which_cube.lower() == "perimeter":
        side_cube_p = float(input("What is your Side Length (num)? "))
        unit_cube_p = input("What is your unit of measure? ")
        perimeter_cube = (side_cube_p *3) * 4
        perimeter_cube_r = round(perimeter_cube, 2)
        print(f"Equation: 4({side_cube_p} * 3)")
        answer_cube_perimeter = f"The Perimeter of the Cube is: {perimeter_cube_r}{unit_cube_p}"
        for char in answer_cube_perimeter:
          sys.stdout.write(char)
          sys.stdout.flush()
          time.sleep(0.03)

      elif which_cube.lower() not in [vp_file]:
        print("That is an invalid answer.")
        time.sleep(2.5)
        os.system('clear')
        cube()
    cube()
#Triangle
elif shape.lower() == "triangle":
    def triangle():
      which_triangle = input("What do you want to caculate Area or Perimeter? ")
      if which_triangle.lower() == "area":
        base_t_a = float(input("What is your Base (num)? "))
        height_t_a = float(input("What is your Height (num)? "))
        unit_t_a = input("What is you unit of measure? ")
        area_t_a = (height_t_a * base_t_a)/2
        area_t_a_r = round(area_t_a, 2)
        print(f"Equation: ({base_t_a} * {height_t_a})/2")
        answer_t_area = f"The Area of the Triangle is: {area_t_a_r}{unit_t_a}^2 "
        for char in answer_t_area:
          sys.stdout.write(char)
          sys.stdout.flush()
          time.sleep(0.03)

      elif which_triangle.lower() == "perimeter":
        one_side_length_t_p = float(input("What is one Side Length (num)? "))
        second_side_length_t_p = float(input("What is another Side Length (num)? "))
        third_side_length_t_p = float(input("What is another Side Length (num)? "))
        unit_t_p = input("What is your unit of measure? ")
        perimeter_t_p = one_side_length_t_p + second_side_length_t_p + third_side_length_t_p
        perimeter_t_p_r = round(perimeter_t_p, 2)
        print(f"Equation: {one_side_length_t_p} + {second_side_length_t_p} + {third_side_length_t_p}")
        answer_t_perimeter = f"The Permeter of the Triangle is: {perimeter_t_p_r}{unit_t_p}"
        for char in answer_t_perimeter:
          sys.stdout.write(char)
          sys.stdout.flush()
          time.sleep(0.03)

      else:
        if which_triangle.lower() not in [pa_file]:
          print("That is an invalid answer.")
          time.sleep(2.5)
          os.system("clear")
          triangle()
    triangle()
#Not Valid Answer
else:
  if shape.lower() not in [shape_file]:
    print("That is an invalid answer.")
    time.sleep(2.5)
    os.system("clear")
    intro()