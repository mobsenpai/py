# Default Arguments

def calculate_simple_interest(P,R,T=1):
    SI = (P*R*T)/100
    print(SI)

calculate_simple_interest(1000, 5, 10)
calculate_simple_interest(1000, 5)
