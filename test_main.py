from main import *
import tabulate
import math

def test_simple_work():

  assert simple_work_calc(10, 2, 2) == 20
  assert simple_work_calc(20, 3, 2) == 50
  assert simple_work_calc(30, 4, 2) == 90
  assert simple_work_calc(1, 2, 2) == 1
  assert simple_work_calc(4, 2, 2) == 8
  assert simple_work_calc(3, 3, 2) == 6
  

def test_work():
  assert work_calc(10, 2, 2,lambda n: 1) == 11
  assert work_calc(20, 1, 2, lambda n: n*n) == 410
  assert work_calc(30, 3, 2, lambda n: n) == 75
  assert work_calc(5, 2, 2, lambda n: n) == 9
  assert work_calc(15, 2, 3, lambda n: 1) == 11
  assert work_calc(25, 5, 2, lambda n: n * n) == 685



def test_compare_work():
  # curry work_calc to create multiple work
  # functions taht can be passed to compare_work
    
  # create work_fn1
  # create work_fn2
  
    def work_fn1(n):
      a = 3
      b = 3
      c = 1
      f = lambda n:math.pow(n,c)
      return work_calc(n, a, b, f)


    def work_fn2(n):
      a = 16
      b = 2
      c = 6
      f = lambda n:math.pow(n,c)
      return work_calc(n, a, b, f)
  
    res = compare_work(work_fn1, work_fn2)
    print(res)

	
def test_compare_span():
  def work_fn1(n):
    a = 3
    b = 3
    c = 1
    f = lambda n:math.pow(n,c)
    return work_calc(n, a, b, f)


  def work_fn2(n):
    a = 16
    b = 2
    c = 6
    f = lambda n:math.pow(n,c)
    return work_calc(n, a, b, f)


  res = compare_span(work_fn1, work_fn2)
  print("Span COMPARE \n")
  return print_results(res)
