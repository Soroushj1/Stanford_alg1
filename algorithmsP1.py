### This is really simple implementation of the grade school algorithm for calculating numbers


def calculator(first, second):
    array1 = [int(i) for i in str(first)]
    array2= [int(j) for j in str(second)]
    empty = []
    sum = 0
    for  x, item1 in enumerate(array1):
        for y, item2 in enumerate(array2):
            empty.append((10**(len(array1)-1-x))*item1*(10**(len(array2)-1-y))*item2)
            sum = sum + (10**(len(array1)-1-x))*item1*(10**(len(array2)-1-y))*item2
            
    
    print(sum)


calculator(314159265358979323846264338327941823749817234987123984719823479182734981723498172349871324987123984750288419716939937510582097494459254325434358927345987239845729834759823745982734598724359872493857298347598237459827345, 27182818284590452353602874713526624977572470936999595749664312987123948712983749182734891723498172349871234967627)

