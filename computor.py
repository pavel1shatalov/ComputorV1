import sys

def get_degree(polynom):
    degree = int(polynom.strip().split(' ')[-1][-1])
    return degree

def get_coefs(polynom, degree):
    value = 0
    data = polynom.strip().split(' ')
    coeff = [0] * (degree + 1)
    for i, arg in enumerate(data):
        if (arg[0].isdigit()):
            if (i >= 1 and data[i - 1] == '-'):
                value = float(data[i]) * (-1)
            else:
                value = float(data[i])
            degree = int(data[i + 2][-1]) if ((i + 2) < len(data) and data[i + 2][0] == 'X') else 0
            coeff[degree] = value
    return (coeff)

def get_discriminant(eq):
    discr = eq[1] * eq[1] - 4 * eq[0] * eq[2]
    return (discr)

def format_polynom(coeffs):
    polynom = ""
    for i, val in enumerate(coeffs):
        if val < 0:
            polynom += " - "
            val *= -1
        elif val >= 0 and i > 0:
            polynom += " + "
            if val == 0:
                val = int(val)
        polynom += str(val) + " * X^" + str(i)
    return (polynom + " = 0")

def format_reduce(flt):
    if (flt - int(flt) == 0):
        flt = int(flt)
    else:
        flt = float("{0:.2f}".format(flt))
    return (flt)

def format_solution(flt):
    if (flt - int(flt) == 0):
        flt = int(flt)
    else:
        flt = float("{0:.6f}".format(flt))
    return (flt)

def merge(arr1, arr2):
    values = []
    for i, val in enumerate(arr1):
        values.append(val - arr2[i])
    return values

def reduce(eq):
    i = -1
    while (len(eq) > 1):
        if (eq[i] == 0):
            del eq[-1]
        else:
            break
    eq = list(map(format_reduce, eq))
    print("Reduced form:", format_polynom(eq))
    return(len(eq) - 1)

def solve(eq, degree):
    print("Polynomial degree: ", degree)
    
    # deg >= 3
    if (degree >= 3):
        print("The polynomial degree is stricly greater than 2, I can't solve.")
        return 1

    # deg = 0
    if degree == 0:
        if (eq[0] == 0):
            print("All real numbers are solutions")
            return 0
        else:
            print("This equation has no solution")
            return 1
    
    # deg = 1
    elif degree == 1:
        print("The solution is:\n", format_solution(-eq[0] / eq[1]))
        return 0
    
    # deg = 2
    discr = get_discriminant(eq)
    if discr >= 0:
        sqrt = discr ** 0.5
    else:
        sqrt = ((-1) * discr) ** 0.5
    ## D > 0
    if (discr > 0):
        print("Discriminant is strictly positive, the two solutions are:")
        print(format_solution((-eq[1] - sqrt) / (2 * eq[2])))
        print(format_solution((-eq[1] + sqrt) / (2 * eq[2])))
    ## D = 0
    elif (discr == 0):
        print("The solution is:")
        print((-eq[1] / (2 * eq[2])))
    ## D < 0
    else:
        print("Discriminant is strictly negative, the two solutions are:")  
        eq[1] = -eq[1] / (2 * eq[2])
        sqrt = sqrt / (2 * eq[2])
        b = str(format_solution(eq[1]))
        sol = " i * " + str(format_solution(sqrt))
        ### b != 0
        if (eq[1] != 0):
            sol1 = (b + " -" + sol)
            sol2 = (b + " +" + sol)
        ### b == 0
        else:
            sol1 = " -" + sol
            sol2 = sol
        print(sol1)
        print(sol2)

if __name__ == "__main__":
    # check for args
    if len(sys.argv) < 2:
        print("Not enough arguments")
        exit(1)
    if len(sys.argv) > 2:
        print("Too many arguments")
        exit(1)
    
    # equation in form of a string
    equation = sys.argv[1]
    
    # sides[0] -> left part of equation
    # sides[1] -> right part of equation
    sides = equation.strip().split('=')

    # find max degree in equation
    degree_left = get_degree(sides[0])
    degree_right = get_degree(sides[1])
    degree = max(degree_left, degree_right)
    
    # create list of coefficients
    coef_left = get_coefs(sides[0], degree)
    coef_right = get_coefs(sides[1], degree)
    eq = merge(coef_left, coef_right)
    
    # reduce degree and print Reduced form
    degree = reduce(eq)

    # solve equation and prind details
    exit(solve(eq, degree))