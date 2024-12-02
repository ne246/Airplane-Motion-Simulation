#airplane foward motion
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation                                                           # FuncAnimation(name of the plot, function name, frame amount, time frames(ms), repeat, blit(true or false))
import numpy as np
 

# Set up the duration for the animation
t0 = 0       # [hrs]                    t = [0, 0.005, .......... 2]
t_end = 2    # [hrs]    
dt = 0.005   # [hrs]    


# Array for time (hrs)
t = np.arange(t0, t_end + dt, dt)                                                                  #creates the arary for time (begin, not included(where to stop), time interval)

#Airplane 1 ----------------------------------
# Array for x (km)
a1 = 800
n1 = 1
x1 = a1 * t ** n1

# Array for y (km)
altitude1 = 2.5 
y1 = np.ones(len(t)) * altitude1

# Array for speed in the x direction
if n1 < 1:
    t[0] = t[1]
speed_x1 = n1 * a1 * t ** (n1-1)

#Airplane 2 ----------------------------------
# Array for x (km)
a2 = 1600/2**0.5
n2 = 0.5
x2 = a2 * t ** n2

# Array for y (km)
altitude2 = 1.5 
y2 = np.ones(len(t)) * altitude2

# Array for speed in the x direction
if n2 < 1:
    t[0] = t[1]
speed_x2 = n2 * a2 * t ** (n2-1)

#Airplane 3 ----------------------------------
# Array for x (km)
a3 = 200
n3 = 3
x3 = a3 * t ** n3

# Array for y (km)
altitude3 = 0.5
y3 = np.ones(len(t)) * altitude3

# Array for speed in the x direction
if n3 < 1:
    t[0] = t[1]
speed_x3 = n3 * a3 * t ** (n3-1)



################## Animation Screen #####################
frame_amount = len(t)

# step 1: window template: Creates screen, resolution, background and grid 2x2.
fig = plt.figure(figsize = (16, 9), dpi = 65, facecolor = (0.8, 0.8, 0.8))
gs = gridspec.GridSpec(2, 2)                                                                     #slices it in 2x2




# Subplot 1 ------------------------------------------------------------------------------------

ax1 = fig.add_subplot(gs[0, :], facecolor = (0.9, 0.9, 0.9))

dot1 = np.zeros(frame_amount)
n = 20
for i in range(0, frame_amount):
    if i ==n:
        dot1[i] = x1[i]
        n = n + 20
    else:
        dot1[i] = x1[n-20]

dot2 = np.zeros(frame_amount)
n = 20
for i in range(0, frame_amount):
    if i ==n:
        dot2[i] = x2[i]
        n = n + 20
    else:
        dot2[i] = x2[n-20]

dot3 = np.zeros(frame_amount)
n = 20
for i in range(0, frame_amount):
    if i == n:
        dot3[i] = x3[i]
        n = n + 20
    else:
        dot3[i] = x3[n-20]

#Airplane 1 ------------------------------------------------------
plane1_1,= ax1.plot([],[], 'k', linewidth = 10)                                                   #plane base          
plane1_2, = ax1.plot([],[], 'k', linewidth = 5 )                                                  #plane top wing
plane1_3, = ax1.plot([],[], 'k', linewidth = 5 )                                                  #plane bottom wing
plane1_4, = ax1.plot([],[], 'k', linewidth = 3 )                                                  #plane back top wing
plane1_5, = ax1.plot([],[], 'k', linewidth = 3 )                                                  #plane back bottom wing

plane1_trajectory, = ax1.plot([],[], 'r:o', linewidth = 2 )                                      #line object that we define  :o gives it points

#Airplane 2 ------------------------------------------------------
plane2_1,= ax1.plot([],[], 'k', linewidth = 10)                                                   #plane base          
plane2_2, = ax1.plot([],[], 'k', linewidth = 5 )                                                  #plane top wing
plane2_3, = ax1.plot([],[], 'k', linewidth = 5 )                                                  #plane bottom wing
plane2_4, = ax1.plot([],[], 'k', linewidth = 3 )                                                  #plane back top wing
plane2_5, = ax1.plot([],[], 'k', linewidth = 3 )                                                  #plane back bottom wing

plane2_trajectory, = ax1.plot([],[], 'b:o', linewidth = 2 )                                      #line object that we define  :o gives it points

#Airplane 3 ------------------------------------------------------
plane3_1,= ax1.plot([],[], 'k', linewidth = 10)                                                   #plane base          
plane3_2, = ax1.plot([],[], 'k', linewidth = 5 )                                                  #plane top wing
plane3_3, = ax1.plot([],[], 'k', linewidth = 5 )                                                  #plane bottom wing
plane3_4, = ax1.plot([],[], 'k', linewidth = 3 )                                                  #plane back top wing
plane3_5, = ax1.plot([],[], 'k', linewidth = 3 )                                                  #plane back bottom wing

plane3_trajectory, = ax1.plot([],[], 'g:o', linewidth = 2 )                                      #line object that we define  :o gives it points

#plot info
plt.xlim(x1[0], x1[-1])                                                                            #starts at 0 to 1600 point on the plt line x
plt.ylim(0, y1[0] + 0.5)                                                                            #starts at 0 to 3 on the plt line y
plt.xticks(np.arange(x1[0] , x1[-1] + 1, x1[-1]/4), size = 15)
plt.yticks(np.arange(0, y1[0]+1, y1[0]/y1[0]), size = 15)
plt.xlabel('x-distance', fontsize = 15)
plt.ylabel('y-distance', fontsize = 15)
plt.title('Airplane', fontsize = 15)
plt.grid(True)


# Subplot 2 -------------------------------------------------------------------------------------
ax2 = fig.add_subplot(gs[1,0], facecolor = (0.9, 0.9, 0.9))
x_dist1, = ax2.plot([], [], 'r', linewidth=3, label = 'X = ' + str(int(a1)) + '*t^' + str(round(n1,1)))
x_dist2, = ax2.plot([], [], 'b', linewidth=3, label = 'X = ' + str(int(a2)) + '*t^' + str(round(n2,1)))
x_dist3, = ax2.plot([], [], 'g', linewidth=3, label = 'X = ' + str(int(a3)) + '*t^' + str(round(n3,1)))


#plot info
plt.xlim(t[0], t[-1])
plt.ylim(x1[0], x1[-1])
plt.xticks(np.arange(t[0],t[-1]+dt,t[-1]/4))
plt.yticks(np.arange(x1[0], x1[-1]+1, x1[-1]/4))
plt.xlabel('time [hrs]', fontsize = 15)
plt.ylabel('x-distance [km]', fontsize = 15)
plt.title('X-distance VS time')
plt.grid(True)
plt.legend(loc = 'upper left', fontsize = 'medium')


# Subplot 3 -------------------------------------------------------------------------------------
ax3 = fig.add_subplot(gs[1, 1], facecolor = (0.9, 0.9, 0.9))
speed1, = ax3.plot([], [], '-r', linewidth = 2, label = 'dX/dt = ' + str(int(n1*a1)) + '*t^(' + str(round((n1-1), 1)) + ')')
speed2, = ax3.plot([], [], '-b', linewidth = 2, label = 'dX/dt = ' + str(int(n2*a2)) + '*t^(' + str(round((n2-1), 1)) + ')')
speed3, = ax3.plot([], [], '-g', linewidth = 2, label = 'dX/dt = ' + str(int(n3*a3)) + '*t^(' + str(round((n3-1), 1)) + ')')

#plot info
plt.xlim(t[0], t[-1])
plt.ylim(0, speed_x1[-1] * 2)
plt.xticks(np.arange(t[0],t[-1]+dt,t[-1]/4))
plt.yticks(np.arange(0, speed_x1[-1]*2 + 1, speed_x1[-1]*2/4))
plt.xlabel('time [hrs]', fontsize = 15)
plt.ylabel('speed [km/hr]', fontsize = 15)
plt.title('Speed as a function of time')
plt.grid(True)
plt.legend(loc = 'upper right', fontsize = 'medium')



# Design -----------------------------------------------------------------------------------------

def update_plot(num):
    #subplot1
    plane1_trajectory.set_data(dot1[0:num], y1[0:num])

    plane1_1.set_data([x1[num]-40, x1[num]+20], [y1[num], y1[num]])
    plane1_2.set_data([x1[num]-20, x1[num]], [y1[num] + 0.3, y1[num]])
    plane1_3.set_data([x1[num]-20, x1[num]], [y1[num] - 0.3, y1[num]])
    plane1_4.set_data([x1[num]-40, x1[num]-30], [y1[num] + 0.15, y1[num]])
    plane1_5.set_data([x1[num]-40, x1[num]-30], [y1[num] - 0.15, y1[num]])

    plane2_trajectory.set_data(dot2[0:num], y2[0:num])

    plane2_1.set_data([x2[num]-40, x2[num]+20], [y2[num], y2[num]])
    plane2_2.set_data([x2[num]-20, x2[num]], [y2[num] + 0.3, y2[num]])
    plane2_3.set_data([x2[num]-20, x2[num]], [y2[num] - 0.3, y2[num]])
    plane2_4.set_data([x2[num]-40, x2[num]-30], [y2[num] + 0.15, y2[num]])
    plane2_5.set_data([x2[num]-40, x2[num]-30], [y2[num] - 0.15, y2[num]])

    plane3_trajectory.set_data(dot3[0:num], y3[0:num])

    plane3_1.set_data([x3[num]-40, x3[num]+20], [y3[num], y3[num]])
    plane3_2.set_data([x3[num]-20, x3[num]], [y3[num] + 0.3, y3[num]])
    plane3_3.set_data([x3[num]-20, x3[num]], [y3[num] - 0.3, y3[num]])
    plane3_4.set_data([x3[num]-40, x3[num]-30], [y3[num] + 0.15, y3[num]])
    plane3_5.set_data([x3[num]-40, x3[num]-30], [y3[num] - 0.15, y3[num]])
    

    #subplot2
    x_dist1.set_data([t[0:num], x1[0:num]])
    x_dist2.set_data([t[0:num], x2[0:num]])
    x_dist3.set_data([t[0:num], x3[0:num]])

    #subplot3
    speed1.set_data(t[0:num], speed_x1[0:num])
    speed2.set_data(t[0:num], speed_x2[0:num])
    speed3.set_data(t[0:num], speed_x3[0:num])


    return plane1_trajectory, plane1_1, plane1_2, plane1_3, plane1_4, plane1_5,  x_dist1, speed1, \
           plane2_trajectory, plane2_1, plane2_2, plane2_3, plane2_4, plane2_5,  x_dist2, speed2, \
           plane3_trajectory, plane3_1, plane3_2, plane3_3, plane3_4, plane3_5,  x_dist3, speed3, \
         

# Runs the code/animation
plane_ani = animation.FuncAnimation(fig, update_plot, frames = frame_amount, interval = 20, repeat = True, blit = True)
plt.show()
################## Animation #####################