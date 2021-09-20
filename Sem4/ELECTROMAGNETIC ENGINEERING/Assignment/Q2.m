syms a rho delta
J = exp(-(1+1i)*(a - rho)/delta);
I = int(J*rho, a-3*delta, a);