M = int( input() )
Xld = int( input() )
Yld = int( input() )
W = int( input() )  ##Ширина
H = int( input() )  ##Висота

Xrd = Xld + W
Ylh = Yld + H


##Нижній рядок
dx1 = ((( Xld//M ) * M)+M)-Xld  ##неповний квадрат справа
P1 = Xld + dx1
dx2 = ( Xrd - P1 ) % M           ##неповний квадрат справа

W1 = ( Xrd - P1 ) // M
k1 = W1

if dx1 != 0:
    k1 += 1
if dx2 != 0:
    k1 += 1

##Лівий рядок
dy1 = ((( Yld//M ) * M) +M) - Yld
P2 = Yld + dy1
dy2 = ( Ylh - P2 ) % M

W2 = ( Ylh - P2 ) // M
k2 = W2

if dy1 != 0:
    k2 += 1
if dy2 != 0:
    k2 += 1

##print( "k1 =", k1 )
##print( "dx1 =", dx1 )
##print( "dx2 =", dx2 )
##
##print( "k2 =", k2 )
##print( "dy1 =", dy1 )
##print( "dy2 =", dy2 )

print( k1 * k2 )
