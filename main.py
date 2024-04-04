import math


# d(R_k) to odległość anten w km
# ht(hb) to wysokość zawieszenia anteny stacji bazowej w metrach
# hr(rh) to wysokość zawieszenia anteny terminala ruchomego w metrach

def low(f_G: float , R_k: float, r_h: float, h_t: float, h_bd:float) -> float:
    d_h:float = h_t - h_bd
    path_loss = (139.01 + 42.59*math.log10(f_G))\
                -(14.97 + 4.99*math.log10(f_G))*abs(d_h)*math.log10(1+abs(d_h))\
                + (40.67 - 4.57*abs(d_h)*math.log10(1+abs(d_h)))*math.log10(R_k)\
                + 20*math.log10(d_h/7.8)+10*math.log10(20/r_h)
    return path_loss
def low_sideways(f_G: float , R_k: float, r_h: float, h_t: float, h_bd:float) -> float:
    d_h:float = h_t - h_bd
    path_loss = (127.39+31.63*math.log10(f_G))-(14.97+4.99*math.log10(f_G))*abs(d_h)*math.log10(1+abs(d_h))\
    + (40.67-4.57*abs(d_h)*math.log10(1+abs(d_h)))*math.log10(R_k)
    return path_loss

def high(f_G: float , R_k: float,  h_t: float) -> float:
    path_loss = 143.21+29.74*math.log10(f_G)\
                - 0.99*math.log10(h_t)+ (47.23+3.72*math.log10(h_t))*math.log10(R_k)
    return path_loss
def high_sideways(f_G: float , R_k: float, h_t: float) -> float:
    path_loss = 135.41+12.49*math.log10(f_G)\
        - 4.99*math.log10(h_t)+ (46.84-2.34*math.log10(h_t))*math.log10(R_k)
    return path_loss
def direct(f_G: float, R_k:float , r_h:float , h_t:float, l:float) -> float:
    R_bk = (4*h_t*r_h)/1000*l
    if R_k < R_bk:
        path_loss = 81.14+39.40*math.log10(f_G)\
        - 0.09*math.log10(h_t)+(15.80-5.73*math.log10(h_t))*math.log10(R_k)
        return path_loss
    if R_k > R_bk:
        path_loss = (48.38-32.10*math.log10(R_bk))+45.70*math.log10(f_G)\
        + (25.32-13.90*math.log10(R_bk))*math.log10(h_t)\
        + (32.10+13.90*math.log10(h_t))*math.log10(R_k)\
        +20*math.log10(1.6/r_h)
        return path_loss
    

print(f'{low(1.8, 0.8, 1.5, 15, 12):.2f} dB')
print(f'{low_sideways(1.8, 0.8, 1.5, 15, 12):.2f} dB')
print(f'{high(1.8, 0.8, 15):.2f} dB' )
print(f'{high_sideways(1.8, 0.8, 15):.2f} dB' )
print(f'{direct(1.8, 0.8, 1.5, 15, 2):.2f} dB')


