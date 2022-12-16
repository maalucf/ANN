from cmath import sin
import math

from numpy import mat


def heun(f, x0:float, y0:float, t):
    r = []
    for i in range(1,151):
        #realizar as iterações
        hk=t[i]-t[i-1]
        m1 = f(x0, y0)
        m2 = f(x0 + hk, y0 + hk*m1)
        y1 = y0 + hk * (m1+m2)/2
        #atualizando os valores
        x0 += hk
        y0 = y1
        #colocando valores na lista
        print(str(y0.real),",", end='')
        r.append((x0, y0))
    return r

if __name__ == "__main__":
    def f(x, y):
        k = -0.0766
        der1=-math.exp(k*math.pi*x)*(2*math.cos(2*x) + k*math.pi*math.sin(2*x))
        der2=-math.exp(k*math.pi*x)*(4*k*math.pi*math.cos(2*x) + (k**2*math.pi**2-4) *math.sin(2*x))
        e=math.exp(k*math.pi*x)*math.sin(2*x-math.pi)
        c = 0.2856
        r = 1.2174
        l = 1.7807
        return c*der2+(der1/r)+(e/l)

    x0 = 0
    y0 = 0
    t0 = 0
    t = [t0, 0.0755, 0.1266, 0.2895, 0.3541, 0.4517, 0.5734, 0.6516, 0.7877, 0.8757, 0.9523, 1.0142, 1.1151, 1.2209, 1.3752, 1.4866, 1.5877, 1.633, 1.7111, 1.8446, 1.9642, 2.0205, 2.1858, 2.2653, 2.3292, 2.411, 2.5235, 2.6202, 2.7584, 2.827, 2.9396, 3.0319, 3.1629, 3.2467, 3.3714, 3.4246, 3.5356, 3.6236, 3.7312, 3.8683, 3.96, 4.0232, 4.1626, 4.2819, 4.3792, 4.4867, 4.5628, 4.6275, 4.7297, 4.8143, 4.9745, 5.0163, 5.1596, 5.2527, 5.3789, 5.4305, 5.5221, 5.622, 5.724, 5.8191, 5.9823, 6.0413, 6.1354, 6.2456, 6.3243, 6.4736, 6.5796, 6.6815, 6.7399, 6.8497, 6.9777, 7.0526, 7.1748, 7.2633, 7.3123, 7.4335, 7.5636, 7.6251, 7.7279, 7.8882, 7.9299, 8.0289, 8.1828, 8.2187, 8.3524, 8.4137, 8.5494, 8.6515, 8.7607, 8.8759, 8.964, 9.0187, 9.1788, 9.2711, 9.3561, 9.4823, 9.5176, 9.682, 9.7803, 9.8608, 9.9612, 10.0258, 10.1267, 10.2597, 10.3589, 10.4868, 10.5684, 10.6293, 10.7707, 10.8586, 10.9759, 11.0198, 11.1834, 11.2672, 11.3146, 11.415, 11.5162, 11.6756, 11.7557, 11.8754, 11.9151, 12.0889, 12.1137, 12.2791, 12.3638, 12.4625, 12.5813, 12.6393, 12.7799, 12.8865, 12.9437, 13.0789, 13.1705, 13.2103, 13.3545, 13.4298, 13.5499, 13.6842, 13.7434, 13.8242, 13.9611, 14.0425, 14.1228, 14.2878, 14.3462, 14.4747, 14.567, 14.6858, 14.7819, 14.8554, 14.9122]
    r = heun(f, x0, y0, t)
    # print(r)