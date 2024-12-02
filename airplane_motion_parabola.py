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

# Array for x (km)
a = 800
n2 = 1
x = a * t ** n2

# Array for y (km)
altitude = 2 
y = np.ones(len(t)) * altitude

# Array for speed in the x direction
speed_x = n2 * a * t ** (n2-1)


################## Animation Screen #####################
frame_amount = len(t)

# step 1: window template: Creates screen, resolution, background and grid 2x2.
fig = plt.figure(figsize = (16, 9), dpi = 80, facecolor = (0.8, 0.8, 0.8))
gs = gridspec.GridSpec(2, 2)                                                                     #slices it in 2x2






# Subplot 1 ------------------------------------------------------------------------------------
dot = np.zeros(frame_amount)
n = 20
for i in range(0, frame_amount):
    if i ==n:
        dot[i] = x[i]
        n = n + 20
    else:
        dot[i] = x[n-20]

ax1 = fig.add_subplot(gs[0, :], facecolor = (0.9, 0.9, 0.9))
plane_trajectory, = ax1.plot([],[], 'r:o', linewidth = 2 )                                       #line object that we define  :o gives it points
plane_vertical, = ax1.plot([],[], 'k:o', linewidth = 2)

plane_1,= ax1.plot([],[], 'k', linewidth = 10)                                                   #plane base          
plane_2, = ax1.plot([],[], 'k', linewidth = 5 )                                                  #plane top wing
plane_3, = ax1.plot([],[], 'k', linewidth = 5 )                                                  #plane bottom wing
plane_4, = ax1.plot([],[], 'k', linewidth = 3 )                                                  #plane back top wing
plane_5, = ax1.plot([],[], 'k', linewidth = 3 )                                                  #plane back bottom wing

#Buildings
building_1, = ax1.plot([100,100], [0, 1.0], 'k', linewidth = 7 )
building_2, = ax1.plot([300,300], [0, 1.0], 'k', linewidth = 7 )
building_3, = ax1.plot([700,700], [0, 0.7], 'k', linewidth = 15 )
building_4, = ax1.plot([900,900], [0, 0.9], 'k', linewidth = 10 )
building_5, = ax1.plot([1300,1300], [0, 1.0], 'k', linewidth = 20 )

#plot info
plt.xlim(x[0], x[-1])                                                                            #starts at 0 to 1600 point on the plt line x
plt.ylim(0, y[0] + 1)                                                                            #starts at 0 to 3 on the plt line y
plt.xticks(np.arange(x[0] , x[-1] + 1, x[-1]/4), size = 15)
plt.yticks(np.arange(0, y[0]+2, y[0]/y[0]), size = 15)
plt.xlabel('x-distance', fontsize = 15)
plt.ylabel('y-distance', fontsize = 15)
plt.title('Airplane', fontsize = 15)
plt.grid(True)

box_object = dict(boxstyle = 'square', fc = (0.9,0.9,0.9), ec = 'g', lw = 1)                
stopwatch0 = ax1.text(1400, 0.75, '', size = 15, color = 'g', bbox = box_object)

box_object2 = dict(boxstyle = 'square', fc = (0.9,0.9,0.9), ec = 'r', lw = 1)
dist_counter0 = ax1.text(1400, 0.30, '', size = 15, color = 'r', bbox = box_object2)







# Subplot 2 -------------------------------------------------------------------------------------
ax2 = fig.add_subplot(gs[1,0], facecolor = (0.9, 0.9, 0.9))
x_dist, = ax2.plot([], [], 'b', linewidth=3, label = 'X = ' + str(a) + '*t^' + str(n2))

horizontal_line, = ax2.plot([],[], 'r:o', linewidth = 2, label = 'horizontal line')
vertical_line, = ax2.plot([],[], 'g:o', linewidth = 2, label = 'vertical_line' )

#plot info
plt.xlim(t[0], t[-1])
plt.ylim(x[0], x[-1])
plt.xticks(np.arange(t[0],t[-1]+dt,t[-1]/4))
plt.yticks(np.arange(x[0], x[-1]+1, x[-1]/4))
plt.xlabel('time [hrs]', fontsize = 15)
plt.ylabel('x-distance [km]', fontsize = 15)
plt.title('X-distance VS time')
plt.grid(True)
plt.legend(loc = 'upper left', fontsize = 'medium')






# Subplot 3 -------------------------------------------------------------------------------------
ax3 = fig.add_subplot(gs[1, 1], facecolor = (0.9, 0.9, 0.9))
rateofchange, = ax3.plot([], [], 'b', linewidth = 2, label = 'dX/dt = ' + str(n2*a) + '*t^(' + str(n2-1) + ')')
roc_vertical_line, = ax3.plot([],[], 'b:o', linewidth = 2, label = 'speed' )

division_speed = ax3.text(0.1, speed_x[-1] * 2 * 0.8, '', fontsize = 20, color = 'b')

#plot info
plt.xlim(t[0], t[-1])
plt.ylim(0, speed_x[-1] * 2)
plt.xticks(np.arange(t[0],t[-1]+dt,t[-1]/4))
plt.yticks(np.arange(0, speed_x[-1]*2 + 1, speed_x[-1]*2/4))
plt.xlabel('time [hrs]', fontsize = 15)
plt.ylabel('speed [km/hr]', fontsize = 15)
plt.title('Speed as a function of time')
plt.grid(True)
plt.legend(loc = 'upper right', fontsize = 'medium')






# Design -----------------------------------------------------------------------------------------

def update_plot(num):
    #subplot1
    plane_trajectory.set_data(dot[0:num], y[0:num])
    plane_vertical.set_data([x[num], x[num]], [0, y[num]])

    plane_1.set_data([x[num]-40, x[num]+20], [y[num], y[num]])
    plane_2.set_data([x[num]-20, x[num]], [y[num] + 0.3, y[num]])
    plane_3.set_data([x[num]-20, x[num]], [y[num] - 0.3, y[num]])
    plane_4.set_data([x[num]-40, x[num]-30], [y[num] + 0.15, y[num]])
    plane_5.set_data([x[num]-40, x[num]-30], [y[num] - 0.15, y[num]])

    stopwatch0.set_text(str(round(t[num], 1)) + 'hrs')
    dist_counter0.set_text(str(int(x[num])) + 'km')

    #subplot2
    x_dist.set_data([t[0:num], x[0:num]])
    horizontal_line.set_data([t[0], t[num]], [x[num], x[num]])
    vertical_line.set_data([t[num], t[num]], [x[0], x[num]])

    #subplot3
    rateofchange.set_data(t[0:num], speed_x[0:num])
    roc_vertical_line.set_data([t[num], t[num]], [0, speed_x[num]])
    division_speed.set_text('dX/dt = ' + str(int(speed_x[num])) + ' km/hr')



    return plane_trajectory, plane_vertical, plane_1, plane_2, plane_3, plane_4, plane_5, stopwatch0, dist_counter0, x_dist, \
           horizontal_line, vertical_line, rateofchange, roc_vertical_line, division_speed,

# Runs the code/animation
plane_ani = animation.FuncAnimation(fig, update_plot, frames = frame_amount, interval = 20, repeat = True, blit = True)
plt.show()
################## Animation #####################