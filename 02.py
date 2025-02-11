print('\n'.join
      ([''.join
        ([('Davron'[(x-y)%6 ]
           if((x*0.05)**2+(y*0.1)**2-1)
           **4(x*0.1)**2*(y*0.1)
           **3<=0 else' ')
          for x in range(-40,30)])
        for y in range(15,-15,-1)]))
