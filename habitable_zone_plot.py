import matplotlib.pyplot as plt

color_dict = {
        40000:"blue",
        20000:"#ADD8E6",
        8750:"#F6F6FF",
        6750:"#FFFFFF",
        5500:"#ffff00",
        4250:"#FFAE42",
        3000:"#ff4500",
        30000:"#FFFFFF",
        3500:"#FF0000"
}

def plot_habitability(habitable_zone,semi_major,st_radius,st_temp,pl_name='unnamed exoplanet'):
    fig,ax = plt.subplots(1,1,figsize=(8,8))
    ax.set_facecolor('black')
    circle1 = plt.Circle((0,0),habitable_zone[0],color='red')
    circle2 = plt.Circle((0,0),habitable_zone[1],color='green')
    if semi_major <= habitable_zone[1]*2:
        circle3 = plt.Circle((0,0),habitable_zone[1]*2,color='darkblue')
    else:
        circle3 = plt.Circle((0,0),semi_major*1.1,color='darkblue')
    ax.add_artist(circle3)
    ax.add_artist(circle2)
    ax.add_artist(circle1)
    ax.scatter(0,0,c=color_dict[st_temp],s=st_radius*50,marker='*')
    ax.scatter(semi_major,0,c='gray')
    plt.title(f'{pl_name} System')
    if semi_major <= habitable_zone[1]*2:
        plt.xlim(habitable_zone[1]*-2,habitable_zone[1]*2)
        plt.ylim(habitable_zone[1]*-2,habitable_zone[1]*2)
    else:
        plt.xlim(semi_major*-1.2,semi_major*1.2)
        plt.ylim(semi_major*-1.2,semi_major*1.2)
    return fig, ax