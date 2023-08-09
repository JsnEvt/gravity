import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation

# time array
t0 = 0
t_end = 12
dt = 0.02
t = np.arange(t0, t_end+dt, dt)

# gravitational accelerations
g_Earth = -9.8  # [m/s^2]
g_Mars = -3.7  # [m/s^2]
g_Moon = -1.6  # [m/s^2]

# position y arrays
n = 2
y_i = 100  # [m]
# forca gravitacional 100+0.5*(-9.8)*t^2 // 1/2g*t^2
y_Earth = y_i+0.5*g_Earth*t**n
y_Mars = y_i+0.5*g_Mars*t**n
y_Moon = y_i+0.5*g_Moon*t**n
# np.set_printoptions(supress=True)
# print(y_Earth)

# velocity y arrays
y_Earth_velocity = n*0.5*g_Earth*t**(n-1)
y_Mars_velocity = n*0.5*g_Mars*t**(n-1)
y_Moon_velocity = n*0.5*g_Moon*t**(n-1)

# acceleration y arrays
y_Earth_acceleration = (n-1)*g_Earth*t**(n-2)
y_Mars_acceleration = (n-1)*g_Mars*t**(n-2)
y_Moon_acceleration = (n-1)*g_Moon*t**(n-2)

# Create circle


def create_circle(r):
    degress = np.arange(0, 361, 1)
    radians = degress*np.pi/180
    sphere_x = r*np.cos(radians)
    sephere_y = r*np.sin(radians)
    return sphere_x, sephere_y


radius = 5  # [meters]
sphere_x_Earth, sphere_y_Earth = create_circle(radius)
sphere_x_Mars, sphere_y_Mars = create_circle(radius)
sphere_x_Moon, sphere_y_Moon = create_circle(radius)

# np.set_printoptions(suppress=True)
# print(y_Earth_velocity)
# print(sphere_y_Earth)
# exit()
 

frame_amount = len(t)
width_ratio = 1.2
y_f = -10
dy = 10


def update_plot(num):
    if y_Earth[num] >= radius:  # para o circulo parar no solo.
        spehere_Earth.set_data(sphere_x_Earth, sphere_y_Earth+y_Earth[num])
        alt_E.set_data(t[0:num], y_Earth[0:num])
        vel_E.set_data(t[0:num], y_Earth_velocity[0:num])
        acc_E.set_data(t[0:num], y_Earth_acceleration[0:num])

    if y_Mars[num] >= radius:  # para o circulo parar no solo.
        spehere_Mars.set_data(sphere_x_Mars, sphere_y_Mars+y_Mars[num])
        alt_Ma.set_data(t[0:num], y_Mars[0:num])
        vel_Ma.set_data(t[0:num], y_Mars_velocity[0:num])
        acc_Ma.set_data(t[0:num], y_Mars_acceleration[0:num])

    if y_Moon[num] >= radius:  # para o circulo parar no solo.
        spehere_Moon.set_data(sphere_x_Moon, sphere_y_Moon+y_Moon[num])
        alt_Mo.set_data(t[0:num], y_Moon[0:num])
        vel_Mo.set_data(t[0:num], y_Moon_velocity[0:num])
        acc_Mo.set_data(t[0:num], y_Moon_acceleration[0:num])

    return spehere_Earth, alt_E, vel_E, acc_E, \
        spehere_Mars, alt_Ma, vel_Ma, acc_Ma, \
        spehere_Moon, alt_Mo, vel_Mo, acc_Mo


# figure properties
fig = plt.figure(figsize=(16, 9), dpi=120, facecolor=(0.8, 0.8, 0.8))
gs = gridspec.GridSpec(3, 4)

# Create object for Earth
ax0 = fig.add_subplot(gs[:, 0], facecolor=(0.9, 0.9, 0.9))
spehere_Earth, = ax0.plot([], [], 'k', linewidth=3)
land_Earth = ax0.plot([-radius*width_ratio, radius *
                       width_ratio], [-6, -6], linewidth=38)
plt.xlim(-radius*width_ratio, radius*width_ratio)
plt.ylim(y_f, y_i+dy)
plt.xticks(np.arange(-radius, radius+1, radius))
plt.yticks(np.arange(y_f, y_i+2*dy, dy))
plt.ylabel('altitude[m]')
plt.title('Earth')


# Create object for Mars
ax1 = fig.add_subplot(gs[:, 1], facecolor=(0.9, 0.9, 0.9))
spehere_Mars, = ax1.plot([], [], 'k', linewidth=3)
land_Mars = ax1.plot([-radius*width_ratio, radius *
                      width_ratio], [-6, -6], 'orangered', linewidth=38)
plt.xlim(-radius*width_ratio, radius*width_ratio)
plt.ylim(y_f, y_i+dy)
plt.xticks(np.arange(-radius, radius+1, radius))
plt.yticks(np.arange(y_f, y_i+2*dy, dy))
plt.ylabel('altitude[m]')
plt.title('Mars')


# Create object for Moon
ax2 = fig.add_subplot(gs[:, 2], facecolor=(0.9, 0.9, 0.9))
spehere_Moon, = ax2.plot([], [], 'k', linewidth=3)
land_Moon = ax2.plot([-radius*width_ratio, radius *
                      width_ratio], [-6, -6], 'gray', linewidth=38)
plt.xlim(-radius*width_ratio, radius*width_ratio)
plt.ylim(y_f, y_i+dy)
plt.xticks(np.arange(-radius, radius+1, radius))
plt.yticks(np.arange(y_f, y_i+2*dy, dy))
plt.ylabel('altitude[m]')
plt.title('Moon')


# Create position function
ax3 = fig.add_subplot(gs[0, 3], facecolor=(0.9, 0.9, 0.9))
alt_E, = ax3.plot([], [], '', linewidth=3, label='Alt_Earth= ' +
                  str(y_i)+' + ('+str(round(g_Earth/2, 1))+')t^'+str(n)+' [m]')
alt_Ma, = ax3.plot([], [], 'orangered', linewidth=3, label='Alt_Mars= ' +
                   str(y_i)+' + ('+str(round(g_Mars/2, 1))+')t^'+str(n)+' [m]')
alt_Mo, = ax3.plot([], [], 'gray', linewidth=3, label='Alt_Moon= ' +
                   str(y_i)+' + ('+str(round(g_Moon/2, 1))+')t^'+str(n)+' [m]')
plt.xlim(0, t_end)
plt.ylim(0, y_i)
plt.xticks(np.arange(0, 14, 2))
plt.yticks(np.arange(0, y_i+2*dy, 20))
plt.legend(loc=(0.6, 0.7), fontsize='x-small')


# Create velocity function
ax4 = fig.add_subplot(gs[1, 3], facecolor=(0.9, 0.9, 0.9))
vel_E, = ax4.plot([], [], '', linewidth=3,
                  label='Vel_Earth =' + str(g_Earth)+'t [m/s')
vel_Ma, = ax4.plot([], [], 'orangered', linewidth=3,
                   label='Vel_Mars =' + str(g_Mars)+'t [m/s')
vel_Mo, = ax4.plot([], [], 'gray', linewidth=3,
                   label='Vel_Moon =' + str(g_Moon)+'t [m/s')
plt.xlim(0, t_end)
plt.ylim(y_Earth_velocity[-1], 0)
plt.legend(loc='lower left', fontsize='x-small')

# Create aceleration function
ax5 = fig.add_subplot(gs[2, 3], facecolor=(0.9, 0.9, 0.9))
acc_E, = ax5.plot([], [], '', linewidth=3,
                  label='Acc_Earth =' + str(g_Earth)+' [(m/s)/s = m/s^2]')
acc_Ma, = ax5.plot([], [], 'orangered', linewidth=3,
                   label='Acc_Mars =' + str(g_Mars)+' [(m/s)/s = m/s^2]')
acc_Mo, = ax5.plot([], [], 'gray', linewidth=3,
                   label='Acc_Moon =' + str(g_Moon)+' [(m/s)/s = m/s^2]')
plt.xlim(0, t_end)
plt.ylim(g_Earth-1, 0)
plt.legend(loc=(0.02, 0.25), fontsize='x-small')


plani_ani = animation.FuncAnimation(
    fig, update_plot, frames=frame_amount, interval=20, repeat=True, blit=True)
plt.show()
