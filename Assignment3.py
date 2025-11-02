# John is trying to solve the arithmetic series(AP). He wants to find two things in the series
# 1. He wants to find nth terms in the series
# 2. He wants to find the sum up to the nth term.

def solve_arithmetic_series(a, d, n):
  """
  Calculates the nth term and the sum up to the nth term of an Arithmetic Series (AP).

  Parameters:
  a (float/int): The first term of the series.
  d (float/int): The common difference.
  n (int): The number of terms (or the position of the desired term).

  Returns:
  tuple: (nth_term, sum_up_to_nth_term)
  """
  nth_term = a + (n - 1) * d

  sum_up_to_nth_term = (n / 2) * (a + nth_term)

  return nth_term, sum_up_to_nth_term

first_term = 3
common_difference = 4
term_number = 5

a_n, S_n = solve_arithmetic_series(first_term, common_difference, term_number)

print(f"Series: {first_term}, {first_term + common_difference}, ...")
print(f"For n = {term_number}:")
print(f"1. The {term_number}th term (a_{term_number}) is: {a_n}")
print(f"2. The Sum up to the {term_number}th term (S_{term_number}) is: {S_n}")