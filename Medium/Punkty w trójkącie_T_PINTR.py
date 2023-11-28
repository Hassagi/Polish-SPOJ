def wyznacznik(A, B, C):
	return A[0]*B[1] + B[0]*C[1] + C[0]*A[1] - B[0]*A[1] - C[0]*B[1] - C[1]*A[0]
 
while(True):
    punkty = input().split()
    if (punkty == ['0', '0', '0', '0', '0', '0', '0', '0']):
        break
    else:
        punkty = list(map(int, punkty))
 
        A = punkty[0:2]
        B = punkty[2:4]
        C = punkty[4:6]
        P = punkty[6:8]
 
        det = wyznacznik(A, B, C)
        det_a = wyznacznik(A, B, P)
        det_b = wyznacznik(B, C, P)
        det_c = wyznacznik(C, A, P) 
        if(det_a==0 and det_b==0 ) or (det_b==0 and det_c ==0) or (det_c==0 and det_a==0):
            print("E")
        elif det_a == 0 or det_b == 0 or det_c == 0:
            if det_a == 0: det_a = 1
            if det_b == 0: det_b = 1
            if det_c == 0: det_c = 1
            if det_a*det_b*det_c > 0:
                print("E")
            else:
                print("O")
        else:
            if det > 0:
                if det_a>0 and det_b>0 and det_c>0:
                    print("I")
                else:
                    print("O")
            else:
                if det_a<0 and det_b<0 and det_c<0:
                    print("I")
                else:
                    print("O") 
