import sympy as sp #for prime factors

def factorization_of_n (n) :
#returns a dictionary of proper prime factorization of n

	da = dict()
	prime_list = sp.primefactors(n)
	prime_list = [int(i) for i in prime_list]
	for i in prime_list :
		counter = 0
		while n % (i**counter) == 0 :
			counter +=1
		da[i] = counter-1

	return da

def phi_of_n (n):
#totient coefficient or Euiler's phi value calculation

	a=1
	if n==1 :
		pass
	elif sp.isprime(n) == True :
		a = n-1
	else :
		dnum = factorization_of_n(n)
		for key in dnum.keys() :
			a=a * (key**dnum[key] - key**(dnum[key]-1))
	print ("phi of {} = {}".format(n,a))

n = int(input("Enter the number for which phi has to be calclulated: "))
phi_of_n(n)
