# P-2.26 Write a Python program that inputs a polynomial in standard algebraic notation and outputs the first derivative of that polynomial.
class Polynomial:
    def __init__(self, poly):
        self.poly = poly

    def parse(self):
        terms = self.poly.split("+")
        parsed = []
        for term in terms:
            coeff, exp = self.parse_term(term.strip())
            parsed.append((coeff, exp))
        return parsed

    def parse_term(self, term):
        if 'x' in term:
            if 'x^' in term:
                coeff, exp = term.split('x^')
                return float(coeff) if coeff else 1.0, int(exp)
            elif 'x' in term:
                coeff = term.replace('x', '')
                return float(coeff) if coeff else 1.0, 1
        else:
            return float(term), 0

    def derivative(self):
        parsed = self.parse()
        derivative_terms = []
        for coeff, exp in parsed:
            if exp != 0:
                derivative_terms.append((coeff * exp, exp - 1))
        return derivative_terms

    def format_derivative(self):
        deriv_terms = self.derivative()
        deriv_str = ""
        for coeff, exp in deriv_terms:
            if exp == 0:
                deriv_str += f"{coeff}"
            elif exp == 1:
                deriv_str += f"{coeff}x"
            else:
                deriv_str += f"{coeff}x^{exp}"
            deriv_str += " + "
        return deriv_str[:-3]

input_poly = input("Enter a polynomial in standard algebraic notation: ")
poly = Polynomial(input_poly)
derivative = poly.format_derivative()

print(f"The derivative of {input_poly} is: {derivative}")

