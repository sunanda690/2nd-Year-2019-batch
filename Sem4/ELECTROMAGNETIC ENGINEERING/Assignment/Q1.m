a = 88;
b = 2.5 * a;
h = (a + b) / 2;

syms theta
deno = sqrt(h*h + a*a + b*b -2*a*b*cos(theta));
num = [-sin(theta); cos(theta)];
expr = num ./ deno;
result = vpaintegral(expr, theta, 0, 2*pi);
disp(a*result);

syms phi1 phi2;
deno = h*h + a*a + b*b -2*a*b*cos(phi1 - phi2);
num = [cos(phi1); sin(phi1)];
expr = num ./ deno;
result = vpaintegral(expr, phi1, [0 2*pi], phi2, [0 2*pi]);
disp(result);

funx = @(phi1, phi2) -a*b*(a+b) * cos(phi1) ./ (h*h + a*a + b*b -2*a*b*cos(phi1 - phi2));
result = integral2(funx, 0, 2*pi, 0, 2*pi);
disp(result)
funy = @(phi1, phi2) -a*b*(a+b) * sin(phi1) ./ (h*h + a*a + b*b -2*a*b*cos(phi1 - phi2));
result = integral2(funy, 0, 2*pi, 0, 2*pi);
disp(result)
